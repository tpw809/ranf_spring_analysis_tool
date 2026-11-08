"""Shigley Mechanical Engineering Design 6th Ed.

pg 600

S_ut = A / (d^m)
"""

import numpy as np


# A228 Music Wire:
m_a228 = 0.145
A_a228_MPa_mm = 2211.0
A_a228_ksi_in = 201.0

# A229 Oil Quench & Tempered Wire:
m_a229 = 0.187
A_a229_MPa_mm = 1855.0
A_a229_ksi_in = 147.0




# A313 Cr-Ni Stainless:
# if 0.013 <= d_in <= 0.10:
m_a313 = 0.146
A_a313_MPa_mm = 1867.0
A_a313_ksi_in = 169.0


# B159 Phosphore Bronze Wire:
# 0.004 < d < 0.022:
m_b159 = 0.0
A_b159_MPa_mm = 1000.0
A_b159_ksi_in = 145.0

# 0.022 < d < 0.075:
m_b159 = 0.028
A_b159_MPa_mm = 913.0
A_b159_ksi_in = 121.0

# 0.075 < d < 0.3:
m_b159 = 0.064
A_b159_MPa_mm = 932.0
A_b159_ksi_in = 110.0


def estimated_mts(d: float, A: float, m: float) -> float:
    """Estimated minimum ultimate tensile strength.
    
    Args:
        d: wire diameter
        A: coefficent
        m: exponent
    """
    return A / (d**m)


def main() -> None:
    # wire diameter:
    d = 0.3
    
    # coefficients:
    A = 2211.0
    m = 0.145
    
    mts = estimated_mts(d, A, m)
    print(f"mts = {mts}")



if __name__ == "__main__":
    main()
    