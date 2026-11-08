import numpy as np
import matplotlib.pyplot as plt


def circle_plot(x:float, y:float, r:float, n:int, **kwargs):
    """
    x and y are the coordinates of the center of the circle
    r is the radius of the circle
    0.01 is the angle step, bigger values will draw the circle faster but
    you might notice imperfections (not very smooth)
    """
    
    xp = []
    yp = []
    
    t_range = np.linspace(0.0, 2.0 * np.pi, n)
    
    for t in t_range:
        #ang = 0:0.01:2 * np.pi
        xp.append(r * np.cos(t) + x)
        yp.append(r * np.sin(t) + y)
    
    plt.plot(xp, yp, **kwargs)
