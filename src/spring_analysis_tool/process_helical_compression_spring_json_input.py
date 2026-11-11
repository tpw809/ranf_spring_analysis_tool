"""Process helical compression spring json input file.

Unitless... must use consistent units:

- Metric: mm, N, MPa, C
- English: in, lb, psi, F

Parameters:

- name: descriptor
- ultimate_safety_factor
- yield_safety_factor
- material.name
- material.ultimate_strength
- material.yield_strength
- material.elastic_limit
- material.elastic_modulus
- end constraints for buckling ()
- handedness (left or right) (doesn't matter for analysis)
- end type (open_not_ground, open_end_ground, closed_not_ground, closed_end_ground)
- condition (peened, preset)
- wire shape (round, square, rectangular)
- wire diameter
- wire diameter tolerance
- minimum tensile strength 
- spring rate
- spring index
- natural frequency
- coil inner diameter
- coil mean diameter
- coil outer diameter
- number of active coils, N
- number of total coils, TC
- pitch
- pitch angle
- free length
- solid length
- load at solid length
- corrected stress at solid length
- corrected % of MTS at solid
- expanded coil outer diameter at solid
- length at buckling
- application: static or dynamic?
- service / life: light (10^3-10^4 cycles), average (10^5-10^6 cycles), severe (<10^6 cycles)?


Load Case Specific Parameters:

- load, P
- load tolerance
- length at load
- deflection at load
- % of max deflection
- corrected stress
- corrected stress % of MTS
- uncorrected stress
- uncorrected stress % of MTS
- expanded coil outer diameter
- margin of safety (yield, ultimate, buckling, fatigue)

Design Scenarios:

- two-load
- one-load
- rate
- dimensional
- minimum weight

References:

- MIL-STD-29A, 
- AFFDL-TR-69-42 Stress Analysis Manual, section 1.5.4
- Shigley, Mechanical Engineering Design, 5th Ed.
- Machinery Handbook
- NASA-STD-5017B, Design & Development of Mechanisms

"""
import time
import json
import numpy as np


def get_max_shear_stress(
        load:float,
        d:float,
        D:float,
        k:float=1.0,
        wire_shape:str='round',
    ) -> float:
    """Get max corrected shear stress in helical spring wire.
    
    Args:
    d = wire diameter or width (if square)
    D = coil mean diameter
    load = applied axial load
    k = correction factor (Wahl)
    
    Returns:
        float: max corrected shear stress in wire
    """
    assert d > 0.0
    assert D > d
    assert k >= 1.0
    
    if wire_shape == 'round':
        tau_max = 8.0 * load * D / (np.pi * d**3)
    elif wire_shape == 'square':
        tau_max = 4.80 * load * (D/2.0) / d**3
    else:
        raise Exception("wire_shape must be round or square")
    
    return k * tau_max


def get_margin(
        actual:float, 
        capability:float, 
        safety_factor:float,
    ) -> float:
    """Margin = (Capability / (Actual * Safety_Factor)) - 1"""
    assert capability >= 0.0
    assert actual >= 0.0
    assert safety_factor >= 1.0
    if actual * safety_factor == 0.0: return np.inf
    return (capability / (actual * safety_factor)) - 1


def get_zero_margin_load(
        d:float,
        D:float,
        Ss:float,
        FoS: float=1.1,
        k:float=1.0,
        wire_shape:str='round',
    ):
    """Get load at zero shear stress margin (yield or ultimate).
    
    Args:
        d = wire diameter or width (if square)
        D = coil mean diameter
        Ss = shear strength (yield or ultimate)
        FoS = factor or safety (yield or ultimate)
        k = correction factor (Wahl)
    Returns:
        float: load at zero shear stress margin (yield or ultimate).
    """
    assert d > 0.0
    assert D > d
    assert k >= 1.0
    assert FoS >= 1.0
    assert Ss >= 0.0
    return np.pi * d**3 * Ss / (FoS * k * 8.0 * D)


def process_helical_compression_spring_json_input(
        input_dict: dict, 
        verbose:bool=False,
    ):
    """Process input dictionary and compute missing parameters.
    
    type: helical_compression_spring
    
    Must supply:
    - name: descriptor
    - material: spring material information
    - yield_safety_factor
    - ultimate_safety_factor
    - wire_shape
    - end_type
    - wire_diameter
    - coil_mean_diameter
    - pitch
    
    Optional:
    - 
    """
    # Get Unix timestamp (seconds since January 1, 1970)
    timestamp = time.time()
    
    ###########################################
    # check input validity:
    ###########################################
    
    # check type:
    assert input_dict['type'] == 'helical_compression_spring'
    
    # get name:
    assert input_dict.get('name') is not None
    
    name = input_dict.get('name')
    
    if name == "": # generate unique name...
        name = 'helical_spring_analysis' + timestamp
        print("generating name...")
    
    ###########################################
    # check for inputs and compute missing data:
    ###########################################
    
    # applied axial load, P:
    if input_dict.get('axial_load') is None:
        # default axial load is 0:
        input_dict['axial_load'] = 0.0
        print("no 'axial_load' provided, default=0")
    else:
        assert input_dict['axial_load'] >= 0.0
    
    P = input_dict['axial_load']
    
    # Total Number of Coils, TC:
    TC = input_dict['total_coils']
    
    # Number of Active Coils, N:
    N = input_dict['active_coils']
    
    assert TC >= N, "total coils must be >= than active coils"
    
    if verbose:
        print(f"active coils (N): {N}")
        print(f"total coils (TC): {TC}")
        print(f"applied axial load (P): {P}")
    
    ###########################################
    # Material Properties:
    ###########################################
    material = input_dict.get('material')
    
    # elastic modulus, G:
    E = material['elastic_modulus']
    assert E > 0.0
    
    # torsional modulus, G:
    G = material['torsion_modulus']
    assert G > 0.0
    
    # ultimate tensile strength, S_tu:
    S_tu = material['ultimate_tensile_strength']
    assert S_tu > 0.0
    
    # yield shear strength, S_sy:
    S_sy = material.get('yield_shear_strength')
    
    # ultimate shear strength, S_su:
    S_su = material.get('ultimate_shear_strength')
    
    # if S_sy is not provided:
    design_stress_ratio = material.get('design_stress_ratio')
    
    if S_sy is None:
        assert 0.0 < design_stress_ratio < 1.0
        S_sy = design_stress_ratio * S_tu
        material['yield_shear_strength'] = S_sy
    
    if S_su is None:
        S_su = 0.577 * S_tu
        material['ultimate_shear_strength'] = S_su
    
    assert S_sy > 0.0
    assert S_su > S_sy
    
    # density:
    rho = material.get('density')
    
    if verbose:
        print(f"Material: {material['name']}")
        print(f"E: {E}")
        print(f"G: {G}")
        print(f"design_stress_ratio: {design_stress_ratio}")
        print(f"S_sy: {S_sy}")
        print(f"S_su: {S_su}")
        # print(f"S_ty: {S_ty}")
        print(f"S_tu: {S_tu}")
        print(f"rho: {rho}")
        
    ###########################################
    # Safety Factors (Factors of Safety):
    ###########################################
    
    yield_safety_factor = input_dict['yield_safety_factor']
    ultimate_safety_factor = input_dict['ultimate_safety_factor']
    
    # safety factor should always be greater than 1:
    assert yield_safety_factor >= 1.0
    assert ultimate_safety_factor >= 1.0
    
    if verbose:
        print(f"yield_safety_factor = {yield_safety_factor}")
        print(f"ultimate_safety_factor = {ultimate_safety_factor}")
    
    ###########################################
    # identify / alert any missing required data:
    ###########################################
    
    # wire shape: 'square','rectangular','round'
    if input_dict.get('wire_shape') is None:
        # default wire shape is round:
        wire_shape = 'round'
        input_dict['wire_shape'] = wire_shape
        print("no 'wire_shape' provided, default='round'")
    else:
        wire_shape = input_dict['wire_shape']
        assert wire_shape in ['round', 'square']
    
    if verbose:
        print(f"wire_shape = {wire_shape}")
    
    # Spring End Type:
    # end_type = 'open_not_ground' = plain
    # end_type = 'open_end_ground' = plain and ground
    # end_type = 'closed_not_ground' = squared or closed
    # end_type = 'closed_end_ground' = squared and ground
    end_type = input_dict['end_type']
    
    if verbose:
        print(f"end_type = {end_type}")
    
    # wire diameter or side length:
    if wire_shape == 'round':
        # wire diameter:
        wire_diameter = input_dict['wire_diameter']
        assert wire_diameter > 0.0
    elif wire_shape == 'square': # side length of square wire:
        b = input_dict['wire_width']
    else:
        print('rectangular not implemented')
    
    # mean coil diameter at free length:
    # coil_mean_diameter = 10.0
    coil_mean_diameter = input_dict['coil_mean_diameter']
    assert coil_mean_diameter > wire_diameter
    
    # spring coil mean radius:
    r = coil_mean_diameter / 2.0
    
    # spring free length (length unloaded):
    free_length = input_dict.get('free_length')
    
    # [length distance/turn], pitch at free length:
    # Reference Shigley 6th Ed. pg 595:
    if end_type == 'open_not_ground':
        # free length L0
        pitch = (free_length - wire_diameter) / N
    elif end_type == 'open_end_ground':
        pitch = free_length / (N + 1.0)
    elif end_type == 'closed_not_ground':
        pitch = (free_length - 3.0*wire_diameter) / N
    elif end_type == 'closed_end_ground':
        pitch = (free_length - 2.0*wire_diameter) / N
    else:
        raise Exception("provide valid end_type")
    
    if input_dict.get('free_length_pitch') is None:
        input_dict['free_length_pitch'] = pitch
    else:
        print(f"calculated pitch: {pitch}")
        print(f"provided pitch: {pitch}")
    
    # Service:
    # Light: static loads, small deflections, seldom used, 1e3 to 1e4 deflections
    # Average: general use, 1e5 to 1e6 deflections
    # Severe: rapid deflections, shock loading, valves, 1e6 to 1e7 deflections
    
    ###########################################
    # [-], Spring Index (C):
    ###########################################
    
    # Spring index should be from 5 to 15, 7 to 9 is ideal
    # typically 6 to 12 (Shigley)
    # called 'm' in stress analysis manual
    if input_dict.get('spring_index') is None:
        if wire_shape == 'round':
            C = coil_mean_diameter / wire_diameter
        elif wire_shape == 'square':
            C = coil_mean_diameter / b
        else:
            print("need to implement rectangular wire...")
        
        input_dict['spring_index'] = C
    else:
        C = input_dict['spring_index']
    
    if verbose:
        print(f"Spring Index, C = D / d = {C}")
    
    if C < 5.0 or C > 15.0:
        print("WARNING: spring index outside typical range (5-15).")
    
    ############################################
    # Other Diameters:
    ############################################
    
    # Coil Outer diameter (at free length):
    if input_dict.get('coil_outer_diameter') is None:
        coil_OD = coil_mean_diameter + wire_diameter
        input_dict['coil_outer_diameter'] = coil_OD
    else:
        assert input_dict['coil_outer_diameter'] > coil_mean_diameter

    # Coil Inner diameter (at free length):
    if input_dict.get('coil_inner_diameter') is None:
        coil_ID = coil_mean_diameter - wire_diameter
        input_dict['coil_inner_diameter'] = coil_ID
    else:
        assert input_dict['coil_inner_diameter'] < coil_mean_diameter
    
    if verbose:
        print(f"coil_ID = {coil_ID}")
        print(f"coil_OD = {coil_OD}")
    
    ############################################
    # Solid Height:
    ############################################
    
    # TC = total coils
    
    if input_dict.get('solid_height') is None:
        if end_type == 'open_not_ground':
            SH = (TC + 1) * wire_diameter
        elif end_type == 'open_end_ground':
            SH = TC * wire_diameter
        elif end_type == 'closed_not_ground':
            SH = (TC + 1) * wire_diameter
        elif end_type == 'closed_end_ground':
            SH = TC * wire_diameter
        else:
            raise Exception('select valid end_type')
        
        input_dict['solid_height'] = SH
        
    else:
        assert input_dict['solid_height'] < free_length
        SH = input_dict['solid_height']
    
    deflection_at_solid = free_length - SH
    
    if verbose:
        print(f"total coils (TC): {TC}")
        print(f"solid height (SH): {SH}")
    
    ############################################
    # MIL-STD-29A, section 21.3: Diameter Changes in Compression Springs
    ############################################
    
    # Increase in outside diameter when compressed:
    # OD_c = outside diameter at solid length:
    OD_c = np.sqrt(coil_mean_diameter**2 + (pitch**2 - wire_diameter**2)/np.pi**2) + wire_diameter

    # input_dict['coil_outer_diameter_at_solid'] = OD_c
    
    if verbose:
        print(f"coil_outer_diameter_at_solid = {OD_c}")
    
    ############################################
    # Stiffness:
    ############################################
    
    if wire_shape == 'round':
        # helical compression spring rate, k:
        # spring rate (shigley), pg 592 6th ed.:
        spring_rate = (G * wire_diameter**4) / (8.0 * coil_mean_diameter**3 * N)
    elif wire_shape == 'square':
        pass
        # TODO: Not yet implemented...
    else:
        raise Exception("wire_shape must be round or square")
    
    # spring_rate:
    input_dict['spring_rate'] = spring_rate
    
    if verbose:
        print(f"spring_rate = {spring_rate}")
    
    ############################################
    # Surge & Natural Frequency:
    ############################################
    
    # estimated mass:
    m_est = np.pi**2 * wire_diameter**2 * coil_mean_diameter * TC * rho / 4.0
    input_dict['estimated_mass'] = m_est
    
    # active mass (for surge & natural frequency):
    m_act = np.pi**2 * wire_diameter**2 * coil_mean_diameter * N * rho / 4.0
    input_dict['active_mass'] = m_act
    
    # estimated fundamental frequency:
    # 0.5 or 0.25 ???
    fun_freq = 0.25 * np.sqrt(spring_rate / m_act)
    input_dict['fundamental_frequency'] = fun_freq
    
    ############################################
    # MIL-STD-29A, section 21.11: Curvature Stress-Correction Factors
    ############################################
    
    # Shear Stress Correction Factor:
    #k_shear = (2.0 * C + 1.0) / (2.0 * C)
    #input_dict['shear_stress_correction_factor'] = k_shear
    #if verbose:
    #    print(f"k_shear = {k_shear}")
    
    # Curvature Stress Correction Factor: K
    # Wahl Stress Correction Factor, k_wahl
    k_wahl = (4.0 * C - 1.0) / (4.0 * C - 4.0) + 0.615 / C
    input_dict['wahl_stress_factor'] = k_wahl
    
    if verbose:
        print(f"k_wahl = {k_wahl}")
    
    # Bergstrasser Factor:
    #k_berg = (4.0 * C + 2.0) / (4.0 * C - 3.0)
    #input_dict['bergstrasser_factor'] = k_berg
    #if verbose:
    #    print(f"k_berg = {k_berg}")
    
    # Curvature stress correction factor:
    #k_curv = k_wahl / k_shear
    #input_dict['curvature_stress_factor'] = k_curv
    #if verbose:
    #    print(f"k_curv = {k_curv}")
    
    # as spring diameter increases, this approaches:
    # (1.0 + d / (4.0 * r))
    
    ############################################
    # MIL-STD-29A, section 21.1: Design Formulas
    ############################################
    
    # TODO: find load at 0 margin
    
    # Load cases:
    # free (no load)
    # solid
    # provided P
    # 0 yield margin
    # 0 ult margin
    # 0 buckling margin
    
    # No Load:
    # no_load_case = {}
    # no_load_case['length'] = free_length
    # no_load_case['load'] = 0.0
    # no_load_case['deflection'] = 0.0
    # no_load_case['uncorrected_shear_stress'] = 0.0
    # no_load_case['corrected_shear_stress'] = 0.0
    # input_dict['no_load_case'] = no_load_case
    
    # solid case:
    solid_case = {}
    solid_case['length'] = SH
    load_at_solid = deflection_at_solid * spring_rate
    solid_case['load'] = load_at_solid
    solid_case['deflection'] = deflection_at_solid
    
    if wire_shape == 'round':
        # max shear stress in wire (Shigley):
        tau_max_solid = 8.0 * load_at_solid * coil_mean_diameter / (np.pi * wire_diameter**3)
    elif wire_shape == 'square':
        # max shear stress in the spring:
        # stress analysis manual, pg 1-96:
        tau_max_solid = 4.80 * load_at_solid * r / b**3
    else:
        print("rectangular wire not implemented...")
    
    solid_case['uncorrected_shear_stress'] = tau_max_solid
    solid_case['corrected_shear_stress'] = tau_max_solid * k_wahl
    
    yield_shear_stress_margin = (S_sy / (yield_safety_factor * tau_max_solid * k_wahl)) - 1.0
    solid_case['yield_shear_stress_margin'] = yield_shear_stress_margin
    
    ultimate_shear_stress_margin = (S_su / (ultimate_safety_factor * tau_max_solid * k_wahl)) - 1.0
    solid_case['ultimate_shear_stress_margin'] = ultimate_shear_stress_margin
    
    solid_case['coil_outer_diameter'] = OD_c
    
    input_dict['solid_case'] = solid_case
    
    # design (provided) load case:
    design_load_case = {}
    design_load_case['load'] = P
    
    # Table II:
    
    if wire_shape == 'round':
        # torsional stress:
        # max shear stress in the spring:
        # stress analysis manual, pg 1-95:
        # max shear stress in wire (Shigley):
        tau_max = 8.0 * P * coil_mean_diameter / (np.pi * wire_diameter**3)
        
        # deflection:
        # stress analysis manual, pg 1-95:
        delta = 64.0 * P*r**3*N / (G * wire_diameter**4)
        
        # deflection, F:
        deflection_at_load = (8.0 * P * N * coil_mean_diameter**3) / (G * wire_diameter**4)
        # F = (w * S_t * N * D**3) / (G * d)
        
        # deflection (Shigley), pg 592 6th ed.:
        y_shigley = ((8.0 * P * coil_mean_diameter**3 * N) / (G*wire_diameter**4)) * (1.0 + 1.0 / (2.0 * C**2))
        
        print(delta, deflection_at_load, y_shigley)
    
    elif wire_shape == 'square':
        # max shear stress in the spring:
        # stress analysis manual, pg 1-96:
        tau_max = 4.80 * P * r / b**3
        
        # deflection, delta:
        # stress analysis manual, pg 1-96:
        deflection_at_load = 44.5 * P * r**3 * N / (G * b**4)
    else:
        raise Exception("wire_shape must be round or square")
    
    
    # deflection_at_load:
    design_load_case['deflection'] = deflection_at_load
    
    if verbose:
        print(f"deflection_at_load = {deflection_at_load}")
        print(f"delta = {delta}")
        print(f"y_shigley = {y_shigley}")
    
    # if input_dict.get('load_at_solid_height') is None:
    #     input_dict['load_at_solid_height'] = (free_length - SH) * spring_rate
    
    if deflection_at_load > deflection_at_solid:
        print("***Warning Solid Height Reached at Load***")
    
    design_load_case['length'] = free_length - deflection_at_load
    design_load_case['uncorrected_shear_stress'] = tau_max
    
    # Max shear stress:
    # max shear stress in wire (Shigley):
    print("using Wahl stress correction factor...")
    tau_max_correct = tau_max * k_wahl
    design_load_case['corrected_shear_stress'] = tau_max_correct
    
    if verbose:
        print(f"tau_max = {tau_max}")
        print(f"tau_max_correct = {tau_max_correct}")
    
    ############################################
    # Buckling Stability
    ############################################
    # Shigley 6th Ed. pg 596-597
    
    if input_dict.get('bukcling_info') is None:
        input_dict['buckling_info'] = {}
    
    buckling_dict = input_dict['buckling_info']
    
    # alpha = end condition constant:
    # alpha = 0.5 => supported between flat surfaces (fixed ends)
    # alpha = 0.707 => one end supported by flat, other end pivoted
    # alpha = 1.0 => both ends pivoted
    # alpha = 2.0 => one end clamped, other end free
    
    if buckling_dict.get('alpha') is None:
        alpha = 0.5
        buckling_dict['alpha'] = alpha
        print("setting default end condition...alpha=0.5")
    
    # lambda_eff = slenderness ratio:
    lambda_eff = alpha * free_length / coil_mean_diameter
    buckling_dict['slenderness_ratio'] = lambda_eff
    
    # elastic constants:
    C1_prime = E / (2.0 * (E - G))
    C2_prime = (2.0 * np.pi**2 * (E - G)) / (2.0 * G + E)
    buckling_dict['C1_prime'] = C1_prime
    buckling_dict['C2_prime'] = C2_prime
    
    if C2_prime > lambda_eff**2:
        print("warning: y_cr undefined (complex number)...")
    
    # critical:
    part1 = 1.0 - C2_prime/lambda_eff**2
    y_cr = free_length * C1_prime * (1.0 - (part1)**(0.5))
    
    # TODO: fix when this is complex... what does that mean?
    buckling_dict['y_cr'] = y_cr.real
    
    if verbose:
        print("Buckling Stability:")
        print(f"\talpha: {alpha}")
        print(f"\tlambda_eff: {lambda_eff}")
        print(f"\tC1_prime: {C1_prime}")
        print(f"\tC2_prime: {C2_prime}")
        print(f"\ty_cr: {y_cr}")
    
    input_dict['buckling_info'] = buckling_dict
    
    # TODO: find length at buckling...
    
    ############################################
    # Spring Strength Margin of Safety
    ############################################
    
    # Margin = Capability / (Actual * Safety_Factor) - 1
    
    # Material Strength (Capability):
    # tensile ultimate strength = S_tu
    # tensile yield strength = S_ty
    # shear ultimate strength = S_su
    # shear yield strength = S_sy = tau_allowable
    
    # Distortion energy (from tensile yield to shear yield):
    # S_sy = 0.577 * S_ty
    # S_su = 0.577 * S_tu
    
    # Ultimate vs Yield:
    # S_ty ~ 0.75 * S_tu
    
    # Combine => S_sy ~ 0.45 * S_tu
    # design_stress_ratio = 0.45
    
    yield_shear_stress_margin = (S_sy / (yield_safety_factor * tau_max_correct)) - 1.0
    design_load_case['yield_shear_stress_margin'] = yield_shear_stress_margin
    
    ultimate_shear_stress_margin = (S_su / (ultimate_safety_factor * tau_max_correct)) - 1.0
    design_load_case['ultimate_shear_stress_margin'] = ultimate_shear_stress_margin
    
    if verbose:
        print(f"yield_shear_stress_margin = {yield_shear_stress_margin}")
        print(f"ultimate_shear_stress_margin = {ultimate_shear_stress_margin}")
    
    input_dict['design_load_case'] = design_load_case
    
    ############################################
    # find loads at 0 margin:
    ############################################
    # find when corrected shear stress == S_sy and S_su
    P0_yield = get_zero_margin_load(
        d=wire_diameter,
        D=coil_mean_diameter,
        Ss=S_sy,
        FoS=yield_safety_factor,
        k=k_wahl,
        # wire_shape:str='round',
    )
    # print(f"P0_yield = {P0_yield}")
    input_dict['load_at_0_yield_margin'] = P0_yield
    
    P0_ult = get_zero_margin_load(
        d=wire_diameter,
        D=coil_mean_diameter,
        Ss=S_su,
        FoS=ultimate_safety_factor,
        k=k_wahl,
        # wire_shape:str='round',
    )
    # print(f"P0_ult = {P0_yield}")
    input_dict['load_at_0_ult_margin'] = P0_ult
    
    # inputs:
    # safety_factor = yield_safety_factor
    # 
    # tau_max_correct = get_max_shear_stress(
    #     load=P0_yield,
    #     d=wire_diameter,
    #     D=coil_mean_diameter,
    #     k=k_wahl,
    #     wire_shape=wire_shape,
    # )
    # print(f"tau_max_correct = {tau_max_correct}")
    # 
    # margin = get_margin(
    #     actual=tau_max_correct,
    #     capability=S_sy,
    #     safety_factor=yield_safety_factor,
    # )
    # print(f"margin = {margin}")
    
    ###########################################
    # return dictionary with new data:
    ###########################################
    return input_dict


def main() -> None:
    # Test:
    
    input_dict = {
        "type": "helical_compression_spring",
        "name": "LeeSpring_LHL_375B_04_Hefty_Die",
        "units": "lb_in_F",
        # "wire_shape": "round",
        "end_type": "closed_end_ground",
        "wire_diameter": 0.059,  # [in]
        "coil_mean_diameter": 0.33 - 0.059,  # [in]
        "free_length": 1.75,  # [in]
        "free_length_pitch": None,
        "service": "light",
        "spring_index": None,
        "spring_rate": 58.0,  # [lb/in]
        "active_coils": 15.75,  # N
        "total_coils": 17.75,  # TC
        "yield_safety_factor": 1.1,
        "ultimate_safety_factor": 1.25,
        "material": {
            "name": "Music Wire",
            "spec": "ASTM A228",
            "units": "lb_in_F",
            "elastic_modulus": 30.0e6,  # [psi]
            "torsion_modulus": 11.5e6,  # [psi]
            "elastic_limit_ratio": 0.6,
            "ultimate_tensile_strength": 250.0e3,  # [psi]
            "yield_shear_strength": None, # [psi]
            "design_stress_ratio": 0.45, # % of min tensile
            "max_operating_temperature": 250.0,  # [F]
            "density": 0.28,  # [lb/in^3]
            "description": "",
        },
        "axial_load": 25.5,  # [lb]
        "helix_direction": None,
        "wahl_stress_factor": None,
        "buckling_info": {},
    }
    # print(json.dumps(input_dict, indent=4))
    
    output_dict = process_helical_compression_spring_json_input(input_dict, verbose=True)
    print(json.dumps(output_dict, indent=4))
    
    
if __name__ == "__main__":
    main()
    