"""Involute Spiral for flexure plate bearings

Timothy Woodard
June 18, 2021
"""
import numpy as np
import matplotlib.pyplot as plt
from rot_z import rot_z
from circle_plot import circle_plot
from involute_spiral_cartesian import involute_spiral_cartesian

# [#], figure counter:
fcnt = 1


# base circle radius:
rb = 5.0    

# sets start location around the circle:
a = 0.0

# starting radius:
r1 = 7.5

# ending radius:
r2 = 85.0

# difference in radius:
dr = r2 - r1
print("dr = ", dr)

ang0 = np.pi
ang = 560.0 * np.pi / 180.0


x, y = involute_spiral_cartesian(0.0, a=0.0, r=r1, sc=1.0)
r = np.sqrt(x**2 + y**2)
print("t = 0, r = ", r)

x, y = involute_spiral_cartesian(ang0, a=0.0, r=r1, sc=1.0)
r0 = np.sqrt(x**2 + y**2)
dr0 = r0-r1
print("t = 180, r = ", r0, "dr0 = ", dr0)

print("ang0 / ang = ", (ang0 / ang))
print("ang / ang0 = ", (ang / ang0))
sc1 = (ang0 / ang)
#sc = 1.0
print("scaling factor 1 = ", sc1)

sc2 = dr / dr0
print("scaling factor 2 = ", sc2)

x, y = involute_spiral_cartesian(ang, a=0.0, r=r1, sc=sc1, sc2=sc2)
r = np.sqrt(x**2 + y**2)
print("t = 560, r = ", r)

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

for phi in np.arange(0.0, ang, 0.01):
#for phi in np.arange(0.0, 2.0 * np.pi, 0.001):
    phil.append(phi)
    
    x, y = involute_spiral_cartesian(
        phi, 
        a=0.0, 
        r=r1, 
        sc=sc1, 
        sc2=sc2,
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
    

p1 = [r1, 0.0]    
p2 = [r2, 0.0]
p1r = np.dot(rot_z(ang), p1)
p2r = np.dot(rot_z(ang), p2)

plt.figure(fcnt)
plt.title('involute spiral')
plt.plot(xl, yl)
plt.plot(xl2, yl2)
plt.plot(xl3, yl3)
circle_plot(0, 0, r1, 100, 'r')
circle_plot(0, 0, r2, 100, 'r')
plt.plot([r1, r2], [0.0, 0.0], ':')
plt.plot([p1r[0], p2r[0]], [p1r[1], p2r[1]], ':')
plt.axis('equal')
plt.savefig('involute_spiral_3_arm_560_deg')
fcnt += 1
'''
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
'''
plt.show()
