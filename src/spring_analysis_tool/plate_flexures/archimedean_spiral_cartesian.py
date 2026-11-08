import numpy as np


def arch_spiral_cartesian(
        t, 
        v=1.0, 
        c=0.0, 
        omg=1.0,
    ):
    """
    t = 
    v = 
    c = 
    omg = 
    """
    x = (v*t + c) * np.cos(omg*t)
    y = (v*t + c) * np.sin(omg*t)
    return [x, y]
