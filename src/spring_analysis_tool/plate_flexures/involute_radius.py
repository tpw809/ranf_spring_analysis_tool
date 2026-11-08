"""Defines involute_radius function."""
import numpy as np


def involute_radius(rb: float, phi: float) -> float:
    """Radius to involute at given pressure angle.
    
    Args:
        rb (float): base circle radius
        phi (float): involute angle
    """
    r = rb / np.cos(phi)
    return r
