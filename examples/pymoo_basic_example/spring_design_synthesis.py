"""Spring Design Synthesis"""
import numpy as np

# assumptions:
# MS = 0 => tau_max * SF = Ss
# stroke from 0.1 to 0.9 delta_max
# delta_max = solid height

# a priori:
# closed and ground ends
# round wire

# material:
shear_tensile_ratio = 0.577

# tensile strength:
S_tu = 180.0e3
S_ty = 160.0e3
# shear strength:
S_su = shear_tensile_ratio*180.0e3
S_sy = shear_tensile_ratio*160.0e3

# elastic modulus:
E = 14.0e6

# torsion modulus:
G = 5.6e6

# density:
rho = 0.174

# Safety Factors:
SFy = 1.1
SFu = 1.25

# choose d and Dm:
# wire diameter:
d = 0.419

# coil mean diameter:
Dm = 2.689

# spring index constraint: [5-15]:
C = Dm / d

# wahl correction factor:
k_wahl = (4.0*C-1.0)/(4.0*C-4.0) + 0.615/C

# max torsion stress:
tau_max_y = S_sy / SFy
tau_max_u = S_su / SFu
tau_max = np.min([tau_max_y, tau_max_u])

# max allowable force:
F_max = tau_max * np.pi * d**3 / (k_wahl * 8.0 * Dm)

# assumed design loads:
F1 = 0.1 * F_max
F2 = 0.9 * F_max


# Choose Na, Nt, or Ls to meet deflection, stiffness, or energy
Na = 10.0
k = (G*d**4) / (8.0*Dm**3*Na)

# if spring rate, k:
# delta2 = F2 / k_desired
# Na = G * d**4 / (k_desired * 8.0 * Dm**3)

# if deflection:
# k = F2 / delta2_desired
# Na = G * d**4 / (k * 8.0 * Dm**3)

# if energy, PE:
# delta_max = PE_desired / (0.4 * F_max)
# k = F_max / delta_max
# Na = G * d**4 / (k * 8.0 * Dm**3)

delta_max = F_max / k

# L or p: choose to avoid bottoming at load
Nt = Na + 2

# solid length:
Ls = d * Nt

# free length:
L0 = Ls + delta_max

# pitch at free length:
p0 = (L0 - 2.0*d) / Na

# mass:
m = np.pi**2 * d**2 * Dm * Nt * rho / 4.0

# fundamental frequency:



print(f"wire diameter, d = {d}")
print(f"mean coil diameter, Dm = {Dm}")
print(f"spring index, C = {C}")
print(f"k_wahl = {k_wahl}")
print(f"tau_max_y = {tau_max_y}")
print(f"tau_max_u = {tau_max_u}")
print(f"tau_max = {tau_max}")
print(f"F_max = {F_max}")
print(f"F1 = {F1}")
print(f"F2 = {F2}")
print(f"delta_max = {delta_max}")
print(f"Na = {Na}")
print(f"Nt = {Nt}")
print(f"solid length, Ls = {Ls}")
print(f"free length, L0 = {L0}")
print(f"pitch, p0 = {p0}")
print(f"mass, m = {m}")
