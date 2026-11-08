"""Flexure Plate Design Script."""
import numpy as np

fcnt = 1


# Performance:

# [mm], total desired stroke:
stroke = 1.0

# [mm], single direction displacement:
disp = stroke / 2.0

# [N/mm], desired axial stiffness, F = kx, k = F/x:
ka = 1.0

# [N/mm], desired radial stiffness, F = kx, k = F/x:
kr = 1.0

# [#], number of life stroke cycles:
ncycles = 10e10

# [MPa], max stress at max stroke:
sigma_max = 1000.0

# [mm], outer diameter clamped:
OD_clamp = 100.0

# [mm], inner diameter clamped:
ID_clamp = 10.0


# Material:

# [MPa], youngs modulus:
E = 200.0e6

# [-], Poisson's ratio:
nu = 0.3

# fatigure strength for infinite life (based on S-N curve):
sigma_fatigue = 1000.0


# Design:

# [mm], plate thickness:
t = 0.5

# [#], number of spiral arms:
n_arms = 3

# [mm], width of the cut:
w = 0.5

# [rad], spiral arm angle of traverse:
trav_angle = 560.0 * np.pi / 180.0


# Materials:
# beryllium copper BeCu17200
# stainless steel 304
# titanium ti6al4v
