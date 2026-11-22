"""
At time of writing, pymoo only supported to python version 3.14

created conda environment 'pymoo' with python3.12, numpy, and scipy
"""
import numpy as np
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.problem import ElementwiseProblem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter


# 1. Define the optimization problem
class MyConstrainedProblem(ElementwiseProblem):

  def __init__(self):
    super().__init__(
        n_var=2,  # Number of decision variables
        n_obj=2,  # Number of objectives
        n_ieq_constr=2,  # Number of inequality constraints
        xl=np.array([-2, -2]),  # Lower bounds
        xu=np.array([2, 2]),  # Upper bounds
    )

  def _evaluate(self, x, out, *args, **kwargs):
    # Objectives (pymoo always minimizes)
    f1 = 100 * (x[0] ** 2 + x[1] ** 2)
    f2 = (x[0] - 1) ** 2 + x[1] ** 2

    # Constraints (formulated as g(x) <= 0)
    g1 = 2 * (x[0] - 0.1) * (x[0] - 0.9) / 0.18
    g2 = -20 * (x[0] - 0.4) * (x[0] - 0.6) / 4.8

    out["F"] = [f1, f2]
    out["G"] = [g1, g2]


# 2. Instantiate the problem and algorithm
problem = MyConstrainedProblem()
algorithm = NSGA2(pop_size=40)

# 3. Run the optimization
res = minimize(
    problem, algorithm, termination=("n_gen", 40), seed=1, verbose=False
)

# 4. Inspect and plot results
print("Best design variables (X):\n", res.X[:5])
print("Best objective values (F):\n", res.F[:5])

plot = Scatter(title="Pareto Front")
plot.add(res.F)
plot.show()
