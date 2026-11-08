"""Calculate (potential) energy stored in a spring.

Assume linear spring rate.
"""

# [N/m], spring rate:
k = 10.0

# [m], displacements:
# initial displacement:
x1 = 0.5

# final displacement:
x2 = 0.2

# [J], energy:
E = 0.5 * k * (x2**2 - x1**2)
print(f"E = {E} [J]")
