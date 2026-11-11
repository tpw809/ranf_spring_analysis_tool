import json
import spring_analysis_tool as spanto

shear_tensile_ratio = 0.577

# material strengths:
# tensile:
S_tu = 180.0e3
S_ty = 160.0e3
# shear:
S_su = shear_tensile_ratio*180.0e3
S_sy = shear_tensile_ratio*160.0e3

# Material Properties:
material_props = {
    "name": "TiBetaC",
    "spec": "AMS4957",
    "units": "lb_in_F",
    "elastic_modulus": 14.0e6,  # [psi]
    "torsion_modulus": 5.6e6,  # [psi]
    "ultimate_tensile_strength": S_tu,  # [psi]
    "yield_tensile_strength": S_ty,  # [psi]
    "ultimate_shear_strength": S_su, # [psi]
    "yield_shear_strength": S_sy, # [psi]
    "density": 0.174,  # [lb/in^3]
    "description": "",
}


# Spring Properties:
input_dict = {
    "type": "helical_compression_spring",
    "name": "TiBetaC_47thAMS",
    "units": "lb_in_F",
    "wire_shape": "round",
    "end_type": "closed_end_ground",
    "wire_diameter": 0.419,  # [in]
    "coil_mean_diameter": 3.108 - 0.419,  # [in]
    "free_length": 10.0,  # [in]
    "service": "light",
    # "spring_rate": 0.0,  # [lb/in]
    "active_coils": 7.0,  # N
    "total_coils": 8.0,  # TC
    "yield_safety_factor": 1.07,
    "ultimate_safety_factor": 1.2,
    "material": material_props,
    "axial_load": 750.0,  # [lb]
    "buckling_info": {},
}

# run analysis:
results_dict = spanto.process_helical_compression_spring_json_input(
    input_dict, 
    verbose=True,
)

# print results to terminal:
print(json.dumps(results_dict, indent=4))
