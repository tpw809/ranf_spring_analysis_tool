"""Helical Compression Spring Analysis

References:

- MIL-STD-29A, SPRINGS, MECHANICAL; DRAWING REQUIREMENTS FOR
- AFFDL-TR-69-42, Stress Analysis Manual, section 1.5.4
- Shigley, Mechanical Engineering Design, 5th Ed.
- Machinery Handbook
- NASA-STD-5017B, Design and Development Requirements for Mechanisms


- ult = ultimate
- yld = yield
- d = diameter
- r = radius
- k = spring rate (stiffness)
"""
import numpy as np

# wire shape:
#wire_shape = 'square'
#wire_shape = 'rectangular'
wire_shape = 'round'

# End Type:
# end_type = 'open_not_ground'
# end_type = 'open_end_ground'
# end_type = 'closed_not_ground'
end_type = 'closed_end_ground'


# [mm], wire diameter:
d_wire = 1.0

# [mm], wire side length of square wire:
b = 1.0

# [mm], mean coil diameter at free length:
D_mean = 10.0

# [mm/turn], pitch at free length:
pitch = 1.0

# [mm], spring radius:
r = D_mean / 2.0

# Service:
# Light: static loads, small deflections, seldom used, 1e3 to 1e4 deflections
# Average: general use, 1e5 to 1e6 deflections
# Severe: rapid deflections, shock loading, valves, 1e6 to 1e7 deflections


# [-], Spring Index (C):
# Spring index should be from 5 to 15, 7 to 9 is ideal
# typically 6 to 12 (Shigley)
if wire_shape == 'round':
    C = D_mean / d_wire
elif shape == 'square':
    C = D_mean / b
print(f"Spring Index, C = D / d = {C}")
# called 'm' in stress analysis manual

# [mm], Outer diameter (at free length):
OD = D_mean + d_wire

# [mm], Inner diameter (at free length):
ID = D_mean - d_wire

# [N/mm], spring rate:
k = 1.0

# number of active coils:
N = 10.0


# Factor of Safety:
# Ratio of max load a spring can sustain without permanent set to the max applied load.

# For critical applications:
SF_yield = 1.65
SF_ultimate = 2.0


# Material:

# Modulus of Elasticity:
E = 200.0e3

# Modulus of Torsion:
G = 85.0e3

# Elastic Limit:
EL = 0.6


# [n], Axial Load:
P = 1.0

# [N-mm], torsional load:
T = P * r

############################################
# Solid Height:
############################################

# TC = total coils

if end_type == 'open_not_ground':
    SH = (TC + 1) * d_wire
elif end_type == 'open_end_ground':
    SH = TC * d_wire
elif end_type == 'closed_not_ground':
    SH = (TC + 1) * d_wire
elif end_type == 'closed_end_ground':
    SH = TC * d_wire
else:
    raise Exception('select valid end_type')


############################################
# MIL-STD-29A, section 21.1: Design Formulas
############################################

# Table II:

if wire_shape == 'round':
    # torsional stress:
    # S_t = (P * D) / (0.393 * d**2)
    S_t = 8.0 * P * D_mean / (np.pi * d_wire**3)
    # S_t = (G * d * F) / (np.pi * N *D**2)

    # deflection:
    F = (8.0 * P * N * D_mean**3) / (G * d_wire**4)
    # F = (w * S_t * N * D**3) / (G * d)
    
    # helical compression spring rate:
    k = (G * d_wire**4) / (8.0 * D_mean**3 * N)
    
    # spring rate (shigley):
    k_shigley = d_wire**4 * G / (8.0 * D_mean**3 * N)
    
    # max shear stress in the spring:
    # stress analysis manual, pg 1-95:
    # s_max = 16.0 * P * r / (np.pi * d**3) * (1.0 + d / (4.0 * r))
    s_max = 16.0 * P * r / (np.pi * d_wire**3)
    
    # max shear stress in wire (Shigley):
    tau_max = 8.0 * P * D_mean / (np.pi * d_wire**3)
    
    # deflection:
    # stress analysis manual, pg 1-95:
    delta = 64.0 * P*r**3*N / (G * d_wire**4)

elif wire_shape == 'square':
    # max shear stress in the spring:
    # stress analysis manual, pg 1-96:
    s_max = 4.80 * P * r / b**3
    
    # deflection:
    # stress analysis manual, pg 1-96:
    delta = 44.5 * P * r**3 * N / (G * b**4)
else:
    print("rectangular wire not yet implemented...")


# MIL-STD-29A Table III:

# position of max stress is at the inside of the wire

print(f"Spring Deflection:")
print(f"delta = {delta} [mm]")
print(f"F = {F} [mm]")

print(f"Spring Rate:") # F = k * x
print(f"k = {k} [mm]")

P_est = k * delta
print(f"P_est = {P_est}")

############################################
# MIL-STD-29A, section 21.3: Diameter Changes in Compression Springs
############################################

# Increase in outside diameter when compressed:

# OD_c = outside diameter at solid length:
OD_c = np.sqrt(D_mean**2 + (pitch**2 - d_wire**2)/np.pi**2) + d_wire


############################################
# MIL-STD-29A, section 21.4: Buckling
############################################

# Slenderness Ratio = Free Length / Mean Diameter
# Springs with slenderness ratio > 4 are critical in lateral stability (buckling)


############################################
# MIL-STD-29A, section 21.5: Direction of Helix
############################################

# use opposite hand coils for nested springs
# use opposite hand coils if spring must slide over threads

############################################
# MIL-STD-29A, section 21.6: Natural Frequency, Vibration, Surge
############################################

# natural frequency of the spring should be 13X the frequency of the applied load.

# W = weight of load = applied load
W = P

# slowly applied load:
F = W / r

# suddenly applied load:
F = 2.0 * W / r

# applied load dropped vertically:
# (spring initially compressed)
# F = (W - F1 + np.sqrt((w - F1)**2 + 2.0 * W * r)) / r

# applied load with striking velocity of V:
# (spring in horizontal plane)

# velocity of impact:
V = 1.0
# F = (-F1 + np.sqrt(F1**3 + (W*r*V**2) / 336)) / r

############################################
# MIL-STD-29A, section 21.11: Curvature Stress-Correction Factors
############################################

# Shear Stress Correction Factor:
k_shear = (2.0 * C + 1.0) / (2.0 * C)
print(f"k_shear = {k_shear}")

# Curvature Stress Correction Factor: K
# Wahl Stress Correction Factor, K_w
K_wahl = (4.0 * C - 1.0) / (4.0 * C - 4.0) + 0.615 / C
print(f"K_wahl = {K_wahl}")

# Bergstrasser Factor:
K_berg = (4.0 * C + 2.0) / (4.0 * C - 3.0)
print(f"K_berg = {K_berg}")

# Curvature stress correction factor:
k_curv = K_wahl / k_shear
print(f"k_curv = {k_curv}")

s_max = s_max * K_wahl
print(f"s_max = {s_max} [MPa]")

S_t_max = S_t * K_wahl
print(f"S_t_max = {S_t_max} [MPa]")

# max shear stress in wire (Shigley):
tau_max = tau_max * K_wahl
print(f"tau_max = {tau_max} [MPa]")

# as spring diameter increases, this approaches:
# (1.0 + d / (4.0 * r))


############################################
# MIL-STD-29A, section 21.12: Keystone Effect
############################################

# *For square and rectangular wire only*

# t = thickness before coiling
t = b

# t_prime = new thickness of inner edge after coiling

t_prime = 0.48 * t * (OD / D_mean + 1.0)
print(f"t_prime = {t_prime}")


############################################
# Buckling Stability
############################################

# alpha = end condition constant
alpha = 0.0

# lambda_eff = slenderness ratio
lambda_eff = alpha * L0 / D


y_cr = L0 * c1 * (1.0 - (1.0 - c2/lambda_eff**2)**(0.5))


############################################
# Material Strength Capability (Allowable)
############################################

# ultimate tensile strength:
S_ut = 1200.0

# yield tensile strength:
S_yt = 1000.0

# ultimate shear strength:
S_su = 0.45 * S_ut
print(f"S_su = {S_su}")

# yield shear strength:
S_sy = 0.45 * S_yt
print(f"S_sy = {S_sy}")


############################################
# Spring Strength Margin of Safety
############################################
print(f"\nMargins:")

MS_shear_ult = (S_su / (SF_ultimate * tau_max)) - 1.0
print(f"MS_shear_ult = {MS_shear_ult}")

MS_shear_yld = (S_sy / (SF_yield * tau_max)) - 1.0
print(f"MS_shear_yld = {MS_shear_yld}")
