"""Torsion bar spring analysis function.

Torsion bar ends need to be stronger than the body.

Shot peening increases fatigue resistance.

Pre-setting only helps if deflection is in a single direction.
"""
import numpy as np



def process_torsion_bar_spring(input_dict):
    """
    
    """
    
    # moment:
    M = np.pi * theta * G * (do**4 - di**4) / (32.0 * L)
    
    # shear stress:
    tau = 16.0 * M / (do*np.pi*(do**2 - di**2))
    
    
    
    return input_dict



def main() -> None:
    pass


if __name__ == "__main__":
    main()
    