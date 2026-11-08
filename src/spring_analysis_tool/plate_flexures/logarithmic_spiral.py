"""Logarithmic Spiral for Centrifugal Compressors / Pumps

Timothy Woodard
Feb 16, 2020
"""
import numpy as np
import matplotlib.pyplot as plt
from rot_z import rot_z

# [#], figure counter:
fcnt = 1

a = 1.0
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

for phi in np.arange(0.0, np.pi, 0.01):
	phil.append(phi)
	x = a*np.e**(k * phi) * np.cos(phi)
	y = a*np.e**(k * phi) * np.sin(phi)
	xl.append(x)
	yl.append(y)

	x2, y2 = np.dot(rot_z(np.pi), [x, y])
	xl2.append(x2)
	yl2.append(y2)

	x3, y3 = np.dot(rot_z(np.pi/2.0), [x, y])
	xl3.append(x3)
	yl3.append(y3)

	x4, y4 = np.dot(rot_z(-np.pi/2.0), [x, y])
	xl4.append(x4)
	yl4.append(y4)

plt.figure(fcnt)
plt.title('log spiral')
plt.plot(xl, yl)
plt.plot(xl2, yl2)
plt.plot(xl3, yl3)
plt.plot(xl4, yl4)
plt.axis('equal')
plt.savefig('logspiral_a1_k1_4rotated')
fcnt += 1


xl = []
yl = []
xl2 = []
yl2 = []


for phi in np.arange(0.0, np.pi, 0.01):

	x = a*np.e**(k * phi) * np.cos(phi)
	y = a*np.e**(k * phi) * np.sin(phi)
	xl.append(x)
	yl.append(y)

	x2 = a/2.0*np.e**(k * phi) * np.cos(phi)
	y2 = a/2.0*np.e**(k * phi) * np.sin(phi)
	xl2.append(x2)
	yl2.append(y2)


plt.figure(fcnt)
plt.title('log spiral')
plt.plot(xl, yl)
plt.plot(xl2, yl2)
plt.axis('equal')
plt.savefig('logspiral_a1_a2_k1')
fcnt += 1


xl = []
yl = []
xl2 = []
yl2 = []

for phi in np.arange(0.0, np.pi, 0.01):

	x = a*np.e**(k * phi) * np.cos(phi)
	y = a*np.e**(k * phi) * np.sin(phi)
	xl.append(x)
	yl.append(y)

	x2 = a*np.e**(k/2.0 * phi) * np.cos(phi)
	y2 = a*np.e**(k/2.0 * phi) * np.sin(phi)
	xl2.append(x2)
	yl2.append(y2)

plt.figure(fcnt)
plt.title('log spiral')
plt.plot(xl, yl)
plt.plot(xl2, yl2)
plt.axis('equal')
plt.savefig('logspiral_a1_k1_k2')
fcnt += 1


'''
xl = []
yl = []
xl2 = []
yl2 = []

for phi in np.arange(0.0, np.pi, 0.01):

	x = np.cos(phi)
	y = np.sin(phi)
	xl.append(x)
	yl.append(y)

	x2 = a*np.e**(k/2.0 * phi) * np.cos(phi)
	y2 = a*np.e**(k/2.0 * phi) * np.sin(phi)
	xl2.append(x2)
	yl2.append(y2)

plt.figure(fcnt)
plt.plot(xl, yl)
plt.plot(xl2, yl2)
plt.axis('equal')
plt.savefig('logspiral_a1_k1_k2')
fcnt += 1
'''

plt.show()
