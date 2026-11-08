"""Archimedean Spiral for flexure plate bearings
Timothy Woodard
June 16, 2021
"""
import numpy as np
import matplotlib.pyplot as plt
from rot_z import rot_z
from circle_plot import circle_plot

# [#], figure counter:
fcnt = 1

# [deg/rad], convert radians to degrees:
r2d = 180.0 / np.pi

# [rad/deg], convert degrees to radians:
d2r = np.pi / 180.0

# angular extent of each spiral:
ang = 560.0 * np.pi / 180.0

# spiral starting radius:
r1 = 10.0

# spiral ending radius:
r2 = 40.0

# inner radius:
ri = 2.5

# outer radius:
ro = 50.0

# radial extent of the spiral
dr = r2 - r1

tht_offset = arch_spiral_polar_inv(r1)

# spiral scaling factor (slope)
b = dr / ang

ang_check = arch_spiral_polar_inv(r2, b=b) - arch_spiral_polar_inv(r1, b=b)
print(ang, ang_check)

thtl = []
rl = []
xl = []
yl = []
xl2 = []
yl2 = []
xl3 = []
yl3 = []

for tht in np.arange(0.0, ang, 0.001):
    thtl.append(tht)
    
    r = arch_spiral_polar(
        tht, 
        a=r1, 
        b=b,
    )
    
    rl.append(r)
    x = r * np.cos(tht+tht_offset)
    y = r * np.sin(tht+tht_offset)
    xl.append(x)
    yl.append(y)
    
    x2 = r * np.cos(tht+tht_offset+2.0*np.pi/3.0)
    y2 = r * np.sin(tht+tht_offset+2.0*np.pi/3.0)
    xl2.append(x2)
    yl2.append(y2)
    
    x3 = r * np.cos(tht+tht_offset-2.0*np.pi/3.0)
    y3 = r * np.sin(tht+tht_offset-2.0*np.pi/3.0)
    xl3.append(x3)
    yl3.append(y3)

# List radii as a function of angle:
for tht in np.arange(0.0, ang * r2d, 45.0):
    tht *= d2r
    
    r = arch_spiral_polar(
        tht, 
        a=r1, 
        b=b,
    )
    
    print("theta = %3.4f [deg], r = %3.4f [mm]" % (tht * r2d, r))

r = arch_spiral_polar(
    560 * d2r, 
    a=r1, 
    b=b,
)

print("theta = %3.4f [deg], r = %3.4f [mm]" % (560.0, r))
   
plt.figure(fcnt)
plt.plot(xl, yl)
plt.plot(xl2, yl2)
plt.plot(xl3, yl3)
circle_plot(0, 0, r1, n=100, color='r')
circle_plot(0, 0, r2, n=100, color='r')
circle_plot(0, 0, ri, n=100, color='b')
circle_plot(0, 0, ro, n=100, color='b')
plt.axis('equal')
fcnt += 1 

plt.figure(fcnt)
plt.plot(np.dot(thtl, r2d), rl)
plt.xlabel('angle [deg]')
plt.ylabel('radius [mm]')
fcnt += 1

plt.show()
