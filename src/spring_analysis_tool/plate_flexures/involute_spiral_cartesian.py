import numpy as np


def involute_spiral_cartesian(
        t, 
        a=0.0, 
        r=1.0, 
        sc=0.9, 
        sc2=2.0,
    ): 
    """
    Args:
        t = parametric variable
        a = 
        r = 
        sc = 
        sc2 = 
    """
    t = t * sc
    x = (np.cos(t) + (t-a)*np.sin(t))
    y = (np.sin(t) - (t-a)*np.cos(t))
    x = x * sc2 * r 
    y = y * sc2 * r
    return [x, y]


'''
def involute_spiral_cartesian(t, a=0.0, r=1.0, sc=0.9, sc2=2.0): 
    t = t * sc
    x = r*(np.cos(t) + (t-a)*np.sin(t))
    y = r*(np.sin(t) - (t-a)*np.cos(t))
    return [x, y]
 '''
