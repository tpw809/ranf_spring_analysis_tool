"""Spring Surge & Critical Frequency

Shigley Mechanical Engineering Design 6th Ed. pg. 620

J. C. Wolford & G. M. Smith, Surge of Helical Springs, 1976.

omega = 2*pi*f

omega => rad/sec

f => cycles/sec

f should be > 15-20X loading frequency, 
if not, increase k or decrease W
"""
import numpy as np

# harmonic number, 1, 2, ... :
m = 1

# [m/s^2], acceleration due to gravity:
g = 9.8

# specific weight of spring material:
gamma = 1.0

# weight of active part of the spring:
W = np.pi**2 * d**2 * D * N_a * gamma / 4.0

# natural frequency in rad/sec:
omega = m * np.pi * np.sqrt(k * g / W)

# fundamental frequency:
# 0.5 or 0.25 ???
f = 0.25 * np.sqrt(k * g / W)
