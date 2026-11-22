"""Helical Compression Spring Design Optimization using pymoo

At time of writing, pymoo only supported to python version 3.14

created conda environment 'pymoo' with python3.12, numpy, and scipy

Possible Design Variables:

- d, wire diameter
- D, coil mean diameter
- Na or Nt or Ls, active coils, total coils, or solid length
- L0 or p, free length or pitch

a prior selections:

- material (G, E, rho, S_s, S_t)
- safety factors (yield and ultimate) = (1.1, 1.25)
- wire shape [round, square, rectangular]
- end type [open, closed, closed and ground, ground]

Performance Parmeters (objectives) or Constraints:

- load
- deflection (stroke)
- mass
- stored potential energy
- fundamental frequency

Constraints:

- L0 > Ls
- 5 < C < 15

Assume:

- margin = 0 => tau_max * SF = S_s
"""
import json
import numpy as np
import matplotlib.pyplot as plt
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.problem import ElementwiseProblem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter

import spring_analysis_tool as spanto


# a prior parameters:

# Safety Factors:
SFy = 1.1
SFu = 1.25

# material properties:
shear_tensile_ratio = 0.577

# tensile strength:
S_tu = 180.0e3
S_ty = 160.0e3
# shear strength:
S_su = shear_tensile_ratio*S_tu
S_sy = shear_tensile_ratio*S_ty

# elastic modulus:
E = 14.0e6

# torsion modulus:
G = 5.6e6

# density:
rho = 0.174

# Material Properties:
material_props = {
    "name": "TiBetaC",
    "spec": "AMS4957",
    "units": "lb_in_F",
    "elastic_modulus": E,  # [psi]
    "torsion_modulus": G,  # [psi]
    "ultimate_tensile_strength": S_tu,  # [psi]
    "yield_tensile_strength": S_ty,  # [psi]
    "ultimate_shear_strength": S_su, # [psi]
    "yield_shear_strength": S_sy, # [psi]
    "density": rho,  # [lb/in^3]
    "description": "",
}


# Baseline Design:
input_dict = {
    "type": "helical_compression_spring",
    "name": "optimize_test",
    "units": "lb_in_F",
    "wire_shape": "round",
    "end_type": "closed_end_ground",
    "wire_diameter": 0.419,  # [in]
    "coil_mean_diameter": 2.689,  # [in]
    "free_length": 10.0,  # [in]
    "service": "light",
    # "spring_rate": 0.0,  # [lb/in]
    "active_coils": 7.0,  # N
    "total_coils": 9.0,  # TC
    "yield_safety_factor": SFy,
    "ultimate_safety_factor": SFu,
    "material": material_props,
    "axial_load": 750.0,  # [lb]
    "buckling_info": {},
}

# run analysis:
try:
    input_dict = spanto.process_helical_compression_spring_json_input(
        input_dict, 
        verbose=False,
    )
    
except:
    # null result?
    pass
    print("analysis failed...")


# baseline F_max:
F_max_baseline = np.min([input_dict["load_at_0_yield_margin"],input_dict["load_at_0_ult_margin"]])
print(f"F_max_baseline = {F_max_baseline}")

delta_max_baseline = F_max_baseline / input_dict["spring_rate"]

baseline_energy = 0.4 * F_max_baseline * delta_max_baseline
# baseline_energy = 1.0*input_dict["design_load_case"]["stored_energy"]

m_baseline = input_dict['estimated_mass']
L0_baseline = input_dict['free_length']

print(f"energy_required = {baseline_energy}")
print(json.dumps(input_dict, indent=4))


# Define the optimization problem
class MyConstrainedProblem(ElementwiseProblem):

  def __init__(self):
    super().__init__(
        n_var=2,  # Number of decision variables
        n_obj=2,  # Number of objectives
        n_ieq_constr=3,  # Number of inequality constraints
        xl=np.array([0.01, 0.01]),  # Lower bounds
        xu=np.array([1.5, 8.0]),  # Upper bounds
    )

  def _evaluate(self, x, out, *args, **kwargs):
    
    # design variables:
    d = x[0] # wire diameter
    Dm = x[1] # coil mean diameter
    
    # need to set any of: Na or Nt or Ls
    
    # For closed & ground end & round wire:
    # p = (L0 - 2*d) / Na
    # L0 = p*Na + s*d
    # SH = d * Nt
    # Nt = Na + 2
    # C = Dm/d
    
    # spring index constraint: [5-15]:
    C = Dm / d
    
    # wahl correction factor:
    k_wahl = (4.0*C-1.0)/(4.0*C-4.0) + 0.615/C
    
    # max torsion stress:
    tau_max_y = S_sy / SFy
    tau_max_u = S_su / SFu
    tau_max = np.min([tau_max_y, tau_max_u])
    
    # max allowable force:
    F_max = tau_max * np.pi * d**3 / (k_wahl * 8.0 * Dm)
    
    # assumed design loads:
    F1 = 0.1 * F_max
    F2 = 0.9 * F_max
    
    # Choose Na, Nt, or Ls to meet deflection, stiffness, or energy
    # Na = 10.0
    # k = (G*d**4) / (8.0*Dm**3*Na)
    
    # if spring rate, k:
    # delta2 = F2 / k_desired
    # Na = G * d**4 / (k_desired * 8.0 * Dm**3)
    
    # if deflection:
    # k = F2 / delta2_desired
    # Na = G * d**4 / (k * 8.0 * Dm**3)
    
    # if energy, PE:
    delta_max = baseline_energy / (0.4 * F_max)
    k = F_max / delta_max
    Na = G * d**4 / (k * 8.0 * Dm**3)
    
    delta_max = F_max / k
    
    # L or p: choose to avoid bottoming at max load
    Nt = Na + 2
    
    # solid length:
    Ls = d * Nt
    
    # free length:
    L0 = Ls + delta_max
    
    # pitch at free length:
    p0 = (L0 - 2.0*d) / Na
    
    # mass:
    m = np.pi**2 * d**2 * Dm * Nt * rho / 4.0
    
    # Objectives (pymoo always minimizes)
    # mass:
    f1 = m
    # length:  
    f2 = L0
    
    # Constraints (formulated as g(x) <= 0)
    g1 = 5.0 - C  # C must be more than 5
    g2 = C - 15.0  # C must be less than 15
    g3 = L0 - 15.0  # L0 must be less than 15

    out["F"] = [f1, f2] # objectives
    out["G"] = [g1, g2, g3] # constraints


# Instantiate the problem and algorithm
problem = MyConstrainedProblem()
algorithm = NSGA2(pop_size=100)

# Run the optimization
res = minimize(
    problem, 
    algorithm, 
    termination=("n_gen", 40), 
    seed=1, 
    verbose=True
)

# Inspect and plot results
print("Best design variables (X):\n", res.X[:5])
print("Best objective values (F):\n", res.F[:5])

plot = Scatter(title="Pareto Front")
plot.add(res.F)
plot.add(np.array([m_baseline,L0_baseline]), color='r', marker='*')

plot2 = Scatter(title="Design Variables")
plot2.add(res.X)
plot2.add(np.array([0.419,2.689]), color='r', marker='*')

plot.show()
plot2.show()
