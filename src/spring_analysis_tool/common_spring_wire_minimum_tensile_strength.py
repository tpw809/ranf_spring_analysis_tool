"""Shigley Mechanical Engineering Design 6th Ed.

pg 600

Ultimate Tensile Strength:
S_ut = A / (d^m)
"""
import numpy as np
from functools import partial


def estimated_mts(
        d: float, 
        A: float, 
        m: float,
        d_min: float=0.0,
        d_max: float=float('inf'),
    ) -> float:
    """Estimated minimum ultimate tensile strength (MTS).
    
    Args:
        d: wire diameter
        A: coefficent
        m: exponent
    Returns:
        float: Minimum Tensile Strength (MTS).
    """
    assert np.all(d_min <= d)
    assert np.all(d <= d_max)
    return A / (d**m)


# A228 Music Wire:
m_a228 = 0.145
A_a228_MPa_mm = 2211.0
A_a228_ksi_in = 201.0
d_min_a228_in = 0.004
d_max_a228_in = 0.256
d_min_a228_mm = 0.1
d_max_a228_mm = 6.5

estimated_mts_a228_metric = partial(
    estimated_mts, 
    A=A_a228_MPa_mm, 
    m=m_a228,
    d_min=d_min_a228_mm,
    d_max=d_max_a228_mm
)

estimated_mts_a228_english = partial(
    estimated_mts, 
    A=A_a228_ksi_in, 
    m=m_a228,
    d_min=d_min_a228_in,
    d_max=d_max_a228_in
)

# A229 Oil Quench & Tempered Wire:
m_a229 = 0.187
A_a229_MPa_mm = 1855.0
A_a229_ksi_in = 147.0
d_min_a229_in = 0.02
d_max_a229_in = 0.5
d_min_a229_mm = 0.5
d_max_a229_mm = 12.7

estimated_mts_a229_metric = partial(
    estimated_mts, 
    A=A_a229_MPa_mm, 
    m=m_a229,
    d_min=d_min_a229_mm,
    d_max=d_max_a229_mm
)

estimated_mts_a229_english = partial(
    estimated_mts, 
    A=A_a229_ksi_in, 
    m=m_a229,
    d_min=d_min_a229_in,
    d_max=d_max_a229_in
)

# A227 Hard-Drawn Wire:
m_a227 = 0.190
A_a227_MPa_mm = 1783.0
A_a227_ksi_in = 140.0
d_min_a227_in = 0.028
d_max_a227_in = 0.5
d_min_a227_mm = 0.7
d_max_a227_mm = 12.7

estimated_mts_a227_metric = partial(
    estimated_mts, 
    A=A_a227_MPa_mm, 
    m=m_a227,
    d_min=d_min_a227_mm,
    d_max=d_max_a227_mm
)

estimated_mts_a227_english = partial(
    estimated_mts, 
    A=A_a227_ksi_in, 
    m=m_a227,
    d_min=d_min_a227_in,
    d_max=d_max_a227_in
)

# A232 Chrome-Vanadium Wire:
m_a232 = 0.168
A_a232_MPa_mm = 2005.0
A_a232_ksi_in = 169.0
d_min_a232_in = 0.032
d_max_a232_in = 0.437
d_min_a232_mm = 0.8
d_max_a232_mm = 11.1

estimated_mts_a232_metric = partial(
    estimated_mts, 
    A=A_a232_MPa_mm, 
    m=m_a232,
    d_min=d_min_a232_mm,
    d_max=d_max_a232_mm
)

estimated_mts_a232_english = partial(
    estimated_mts, 
    A=A_a232_ksi_in, 
    m=m_a232,
    d_min=d_min_a232_in,
    d_max=d_max_a232_in
)

# A401 Chrome-Silicon Wire:
m_a401 = 0.108
A_a401_MPa_mm = 1974.0
A_a401_ksi_in = 202.0
d_min_a401_in = 0.063
d_max_a401_in = 0.375
d_min_a401_mm = 1.6
d_max_a401_mm = 9.5

estimated_mts_a401_metric = partial(
    estimated_mts, 
    A=A_a401_MPa_mm, 
    m=m_a401,
    d_min=d_min_a401_mm,
    d_max=d_max_a401_mm
)

estimated_mts_a401_english = partial(
    estimated_mts, 
    A=A_a401_ksi_in, 
    m=m_a401,
    d_min=d_min_a401_in,
    d_max=d_max_a401_in
)


# A313 Cr-Ni Stainless:
# if 0.013 <= d_in <= 0.10:
m_a313 = 0.146
A_a313_MPa_mm = 1867.0
A_a313_ksi_in = 169.0


# B159 Phosphore Bronze Wire:
# 0.004 < d < 0.022:
m_b159_1 = 0.0
A_b159_1_MPa_mm = 1000.0
A_b159_1_ksi_in = 145.0
d_min_1_b159_in = 0.004
d_max_1_b159_in = 0.022
d_min_1_b159_mm = 0.1
d_max_1_b159_mm = 0.6

# 0.022 < d < 0.075:
m_b159_2 = 0.028
A_b159_2_MPa_mm = 913.0
A_b159_2_ksi_in = 121.0
d_min_2_b159_in = 0.022
d_max_2_b159_in = 0.075
d_min_2_b159_mm = 0.6
d_max_2_b159_mm = 2.0

# 0.075 < d < 0.3:
m_b159_3 = 0.064
A_b159_3_MPa_mm = 932.0
A_b159_3_ksi_in = 110.0
d_min_3_b159_in = 0.075
d_max_3_b159_in = 0.3
d_min_3_b159_mm = 2.0
d_max_3_b159_mm = 7.5


def estimated_mts_b159_metric(
        d: float, 
    ) -> float:
    """Estimated minimum ultimate tensile strength (MTS).
    
    Args:
        d: wire diameter
    Returns:
        float: Minimum Tensile Strength (MTS).
    """
    d_min = d_min_1_b159_mm = 0.1
    d_max = d_max_3_b159_mm = 7.5
    
    assert np.all(d_min <= d)
    assert np.all(d <= d_max)
    
    if d <= d_max_1_b159_mm:
        A = A_b159_1_MPa_mm
        m = m_b159_1
    elif d_max_1_b159_mm < d < d_max_2_b159_mm:
        A = A_b159_2_MPa_mm
        m = m_b159_2
    else:
        A = A_b159_3_MPa_mm
        m = m_b159_3
    
    return A / (d**m)



def main() -> None:
    import matplotlib.pyplot as plt
    
    # wire diameter:
    d = 0.3
    
    # coefficients:
    A = A_a228_MPa_mm
    m = m_a228
    
    mts = estimated_mts(d, A, m)
    print(f"mts = {mts}")
    
    mts = estimated_mts_a229_english(d=0.059)
    print(f"mts = {mts} [ksi]")
    
    # A228 Music Wire:
    d_range_a228 = np.linspace(0.1, 6.5, 1000)
    mts_range_a228 = estimated_mts(d_range_a228, A, m)
    
    # A229 Oil Quench & Tempered Wire:
    d_range_a229 = np.linspace(0.5, 12.7, 1000)
    mts_range_a229 = estimated_mts_a229_metric(d_range_a229)
    
    # A227 Hard-Drawn Wire:
    d_range_a227 = np.linspace(0.7, 12.7, 1000)
    mts_range_a227 = estimated_mts_a227_metric(d_range_a227)
    
    # A232 Chrome-Vanadium Wire:
    d_range_a232 = np.linspace(0.8, 11.1, 1000)
    mts_range_a232 = estimated_mts_a232_metric(d_range_a232)
    
    # A401 Chrome-Silicon Wire:
    d_range_a401 = np.linspace(1.6, 9.5, 1000)
    mts_range_a401 = estimated_mts_a401_metric(d_range_a401)
    
    # A313 Cr-Ni Stainless:
    d_range_a313 = np.linspace(0.3, 10.0, 1000)
    mts_range_a313 = np.zeros(1000)
    
    
    
    # B159 Phosphore Bronze Wire:
    d_range_b159 = np.linspace(0.1, 7.5, 1000)
    mts_range_b159 = np.zeros(1000)
    
    for i, d in enumerate(d_range_b159):
        mts_range_b159[i] = estimated_mts_b159_metric(d)
    
    try:
        mts = estimated_mts_a228_metric(d=0.05)
    except:
        print("caught diameter out of bounds")
    
    plt.figure()
    plt.title('Spring Wire MTS')
    plt.plot(d_range_a228, mts_range_a228, label='A228 Music Wire')
    plt.plot(d_range_a229, mts_range_a229, label='A229 Oil Q&T')
    plt.plot(d_range_a227, mts_range_a227, label='A227 Hard Drawn')
    plt.plot(d_range_a232, mts_range_a232, label='A232 Chrome-Vanadium')
    plt.plot(d_range_a401, mts_range_a401, label='A401 Chrome-Silicon')
    plt.plot(d_range_b159, mts_range_b159, label='B159 Phosphor-Bronze')
    plt.xlabel('diameter [mm]')
    plt.ylabel('tensile strength [MPa]')
    plt.grid()
    plt.legend()
    plt.savefig('estimated_spring_wire_MTS')
    
    plt.show()



if __name__ == "__main__":
    main()
    