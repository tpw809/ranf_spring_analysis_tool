"""Archimedean Spiral for flexure plate bearings."""
import numpy as np
import matplotlib.pyplot as plt
from rot_z import rot_z
from circle_plot import circle_plot

# [#], figure counter:
fcnt = 1

# a = ???
a = 1.0

# k = ???
k = 1.0

xl = []
yl = []
xl2 = []
yl2 = []
xl3 = []
yl3 = []
xl4 = []
yl4 = []
phil = []
rl = []

for phi in np.arange(0.0, 560.0 * np.pi / 180.0, 0.01):
    phil.append(phi)
    
    x, y = arch_spiral_cartesian(
        phi, 
        v=4.0, 
        c=7.5, 
        omg=1.0,
    )
    
    xl.append(x)
    yl.append(y)
    r = np.sqrt(x**2 + y**2)
    rl.append(r)
    
    x2, y2 = np.dot(rot_z(2.0*np.pi/3.0), [x, y])
    
    xl2.append(x2)
    yl2.append(y2)
    
    x3, y3 = np.dot(rot_z(-2.0*np.pi/3.0), [x, y])
    
    xl3.append(x3)
    yl3.append(y3)

plt.figure(fcnt)
plt.title('Archimedes Spiral, 560 degrees')
plt.plot(xl, yl)
plt.plot(xl2, yl2)
plt.plot(xl3, yl3)
circle_plot(0, 0, 7.5, n=100, color='r')
circle_plot(0, 0, 45.0, n=100, color='r')
plt.axis('equal')
plt.savefig('archspiral_3_arm_560_deg')
fcnt += 1

plt.figure(fcnt)
plt.plot(phil, rl)
plt.xlabel('angle [rad]')
plt.ylabel('radius [mm]')
fcnt += 1

plt.figure(fcnt)
plt.plot(np.dot(180.0/np.pi,phil), rl)
plt.xlabel('angle [deg]')
plt.ylabel('radius [mm]')
fcnt += 1

plt.show()
