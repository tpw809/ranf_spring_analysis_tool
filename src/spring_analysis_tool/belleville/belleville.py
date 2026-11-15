"""Belleville (disc) spring.

High loads for small deflections.

Key ratio: 
- h/t
- Do/Di (1.8 is most efficient)(ranges from 1.2 to 3.0 is ordinary)



Symbols:
- E: elastic modulus
- mu: Poisson's ratio
- t: thickness
- Do: outer diameter
- Di: inner diameter
- h: conical height
- delta: deflection
- P: load
- sigma: stress

"""
import numpy as np


def process_belleville_input(input_dict):
    """
    
    """
    # load:
    P = (4.0 * E * delta / ((1.0 - mu**2)* K1 * Do**2)) * ((h - delta)*(h - delta/2.0)*t + t**3)
    
    # stress:
    sigma = 4.0 * E * delta / ((1.0 - mu**2)* K1 * Do**2)) * (K2*(h - delta/2.0) + K3*t)
    
    return input_dict


def main() -> None:
    # Test:
    pass


if __name__ == "__main__":
    main()
    