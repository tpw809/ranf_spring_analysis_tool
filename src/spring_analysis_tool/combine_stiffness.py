"""Combine spring stiffness, series and parallel.

Reference: Mechanical Design and Systems Handbook, Rothbart, Section 33: Spring, William R Johnson. 
"""


def combined_stiffness_in_series(k1: float, k2: float) -> float:
    """
    
    Springs in series carry the same load, but have indepdendent deflections.
    
    P12 = P1 = P2
    
    delta_12 = delta_1 + delta_2
    """
    return 1.0 / (1.0 / k1 + 1.0 / k2)


def combined_stiffness_in_parallel(k1: float, k2: float) -> float:
    """
    Springs in parallel have the same displacement, but carry independent loads.
    
    P12 = P1 + P2
    
    delta_12 = delta_1 = delta_2
    """
    return k1 + k2


def main() -> None:
    # Test:
    k1 = 1.0
    k2 = 2.0
    
    k12_ser = combined_stiffness_in_series(k1, k2)
    print(f"k12_ser = {k12_ser}")
    
    k12_par = combined_stiffness_in_parallel(k1, k2)
    print(f"k12_par = {k12_par}")
    

if __name__ == "__main__":
    main()
    