"""Process helical torsion spring inout data.


References:
- Mechanical Design and Systems Handbook, Rothbart, 1964; Section 33: Springs, William R Johnson.


"""
import numpy as np


def process_helical_torsion_spring(input_dict, verbose: bool=False):
    """
    
    """
    # Get Unix timestamp (seconds since January 1, 1970)
    timestamp = time.time()
    
    now = datetime.now()
    
    # metadata:
    metadata_dict = {}
    metadata_dict['datetime'] = now.isoformat()
    metadata_dict['version'] = pkg_version
    metadata_dict['run_notes'] = ""
    metadata_dict['generated_by'] = "roads_are_no_fun.spring_analysis_tool.process_helical_torsion_spring_json_input"
    
    ###########################################
    # check input validity:
    ###########################################
    
    # check type:
    assert input_dict['type'] == 'helical_torsion_spring'
    
    # get name:
    assert input_dict.get('name') is not None
    
    name = input_dict.get('name')
    
    if name == "": # generate unique name...
        name = 'helical_torsion_spring_analysis' + timestamp
        print("generating name...")
    
    
    
    # number of turns (deflection)
    T = theta / (2.0 * np.pi)
    
    
    
    
    
    # round wire:
    
    # moment:
    M = theta * E * d**4 / (64.0 * N * D)
    
    # stress:
    sigma = 32.0 * K_B * M / (np.pi * d**3)
    
    
    # rectangular wire:
    
    # moment:
    M = theta * E * b * t**3 / (12.0 * np.pi * N * D)
    
    # stress:
    sigma = 6.0 * K_C * M / (b * t**2)
    
    
    
    
    
    
    
    ###########################################
    # return dictionary with new data:
    ###########################################
    input_dict['metadata'] = metadata_dict
    
    return input_dict



def main() -> None:
    # Test:
    
    input_dict = {
        "type": "helical_torsion_spring",
        
        "material": {
            "name": "Music Wire",
            "spec": "ASTM A228",
            "units": "lb_in_F",
            "elastic_modulus": 30.0e6,  # [psi]
            "torsion_modulus": 11.5e6,  # [psi]
            "elastic_limit_ratio": 0.6,
            "ultimate_tensile_strength": 250.0e3,  # [psi]
            "yield_shear_strength": None, # [psi]
            "design_stress_ratio": 0.45, # % of min tensile
            "max_operating_temperature": 250.0,  # [F]
            "density": 0.28,  # [lb/in^3]
            "description": "",
        },
        
    }
    
    output_dict = process_helical_torsion_spring_json_input(
        input_dict, 
        verbose=False,
    )
    
    print(json.dumps(output_dict, indent=4))
    

if __name__ == "__main__":
    main()
    