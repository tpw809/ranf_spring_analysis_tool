"""Spring Materials

Sources:

- Mechanical Design and Systems Handbook, Rothbart
- Machinery's Handbook, 29th Ed.
- https://www.leespring.com/spring-materials
- https://optimumspring.com/technical_resources/materials.aspx
"""
import json
import pandas as pd

####################################
# High Carbon Spring Steel Wire:
####################################

####################################
# Music Wire, ASTM A228
####################################
# C: 0.7-1.0%, Mn: 0.2-0.6%
# Alt names: 228 Music Wire, Piano wire, ASTM A228, ASTM A29, ASTM A682, AISI 1086, AMS 5112, QQ-W-470, UNS K08500, UNS G10860, SAE J403, SAE J412, SAE J414e, Japanese JIS G3522 SWP-A G3522 SWP-B, German DIN 1.1269, British BS 1408 5216 5201

####################################
# Oil-Tempered MB Grade, ASTM A229
####################################
E_astm_a229psi = 30.0e6
G_astm_a229_psi = 11.5e6
T_max_astm_a229_F = 300.0

# Oil-Tempered HB Grade, SAE 1080


####################################
# Hard-Drawn MB Grade, ASTM A227
####################################
# C: 0.45-0.85%, Mn: 0.6-1.3%
# Alt names: 227 Hard/Cold Drawn Carbon Galvanized hard-drawn ASTM A-764, HDMB, UNS K06501, ASTM A227, ASTM A764, AISI 1065, SAE J113, QQ-W-428 Type II, Japanese JIS G3521 SWB, German DIN 1.123, British BS 5216 NS 5216 HS
UTS_min_astm_a227_psi = 147.0
E_astm_a227_psi = 30.0e6
G_astm_a227_psi = 11.5e6
T_max_astm_a227_F = 250.0
design_stress_ratio_astm_a227 = 0.4  # % min tensile
rho_astm_a227_lb_in3 = 0.284
# Cold drawn. Average stress applications. Lower cost springs and wire forms. Hard Drawn is the most inexpensive general purpose spring steel and should be used only where life, accuracy, and deflection are not too important.


####################################
# Valve Spring, ASTM A230
####################################
E_astm_a230_psi = 30.0e6
G_astm_a230_psi = 11.5e6
T_max_astm_a230_F = 300.0


####################################
# High Carbon Spring Steel Strip:
####################################

# Cold-Rolled Spring Steel, Blue-Tempered or Annealed, SAE 1074, also 1064, and 1070


# Cold-Rolled Spring Steel, Blue-Tempered Clock Steel, SAE 1095


####################################
# Alloy Spring Steel:
####################################

####################################
# Chromium Vanadium, ASTM A231
####################################
# C: 0.48-0.53%, Cr: 0.8-1.1%, V: 0.15min%
# Alt names: Chrome-Vanadium, OTCV, OTVC, UNS G9254, ASTM A231, AISI 6150, AMS 6450, QQ-W-412 Comp, SAE 6150C
UTS_min_astm_a231_psi = 190.0
E_astm_a231_psi = 30.0e6
G_astm_a231_psi = 11.5e6
T_max_astm_a231_F = 400.0
design_stress_ratio_astm_a231 = 0.45  # % min tensile
rho_astm_a231_lb_in3 = 0.284
# Cold drawn and heat treated before fabrication. Used for shock loads and moderately elevated temperature.


####################################
# Silicon Manganese
####################################
T_max_silicon_manganese_F = 400.0


####################################
# Chromium Silicon, ASTM A401
####################################
# C: 0.51-0.59%, Cr: 0.6-0.8%, Si: 1.2-1.6%
UTS_min_astm_a401_psi = 235.0
E_astm_a401_psi = 30.0e6
G_astm_a401_psi = 11.5e6
T_max_astm_a401_F = 450.0
design_stress_ratio_astm_a401 = 0.45  # % min tensile
rho_astm_a401_lb_in3 = 0.284
# Cold drawn and heat treated before fabrication. Used for shock loads and moderately elevated temperature.


####################################
# Stainless Spring Steel:
####################################

# Austenitic AISI 301, 302
E_aisi_301_psi = 28e6
G_aisi_301_psi = 10e6
T_max_aisi_301_F = 600.0


# Stainless Type 302/304, ASTM A313
UTS_min_302_304_psi = 125.0
E_302_304_psi = 28.0e6
G_302_304_psi = 10.0e6
T_max_302_304_F = 550.0
rho_302_304_lb_in3 = 0.286


####################################
# Stainless Type 316, ASTM A313
####################################
UTS_min_316_psi = 110.0
E_316_psi = 28.0e6
G_316_psi = 10.0e6
T_max_316_F = 550.0
rho_316_lb_in3 = 0.286


####################################
# Stainless Type 17-7 PH ASTM A313, AMS 5678
####################################

# Stainless Type 414, SAE 51414

# Stainless Type 420, SAE 51420

####################################
# Stainless Chromium Type 431, SAE 51431
####################################
# (16% chromium, 2% nickel)
T_max_ss431_F = 600.0

####################################
# Stainless Steel 18-8
####################################
T_max_18_8_F = 550.0

####################################
# Martensitic AISI 410, 420
####################################
E_aisi_410_psi = 29e6
G_aisi_410_psi = 11e6
T_max_aisi_410_F = 500.0


####################################
# Copper-Base Spring Alloy:
####################################

# Spring Brass, ASTM B 134 (70% copper, 30% zinc)

# Phosphor Bronze, ASTM B 159 (95% copper, 5% tin)
T_max_astm_b159_F = 225.0

# Beryllium Copper, ASTM B 197 (98% copper, 2% beryllium)
T_max_astm_b197_F = 300.0

####################################
# Nickel-Base Spring Alloy:
####################################

# Monel
T_max_monel_F = 425.0

# K Monel
T_max_k_monel_F = 450.0

# Inconel
T_max_inconel_F = 700.0

# Inconel X (nickel, chromium, iron)
T_max_inconel_x_F = 850.0

# Duranickel (98% nickel)


####################################
# Nickel-Base Spring Alloy with
# Constant Moduli of Elasticity:
####################################

####################################
# Elinvar 
####################################
# (nickel, iron, chromium)


####################################
# Ni-Span C 
####################################
# (nickel, iron, chromium, titanium)


####################################
# Iso-Elastic 
####################################
# (nickel, iron, chromium, molybdenum)


####################################
# Elgiloy, AMS 5833
####################################
# (nickel: 15.5%, iron, chromium: 20%, cobalt: 40%, Mo: 7%) 
# Alt Names: Phynox, ASTM F1058, UNS R30003, AMS 5833


####################################
# Dynavar, Precipitation Hardened
####################################
# (nickel, iron, chromium, cobalt)


####################################
# Permanickel (Z-Nickel)
####################################
E_permanickel_psi = 0.0e6
G_permanickel_psi = 0.0e6
T_max_permanickel = 500.0


####################################
# Titanium Spring Materials:
####################################

# Grade 5 Ti6Al4V
# Grade 19 Ti3Al8V6Cr4Mo4Zr
# Grade 9 Ti3Al2.5V
# Nickel-Titanium (Nitinol)


####################################
# Better to have a .csv file with everything in rows or columns

template_constituents = {
    "C%": [0.0, 0.0],
    "Ni%": [0.0, 0.0],
    "Cr%": [0.0, 0.0],
    "Al%": [0.0, 0.0],
    "Co%": [0.0, 0.0],
    "Mo%": [0.0, 0.0],
    "V%": [0.0, 0.0],
}

template_material_dict = {
    "type": "material",
    "name": "",
    "spec": "",
    "units": "lb_in_F",
    "elastic_modulus": None, # psi or MPa
	"torsion_modulus": None, # psi or MPa
    "elastic_limit_ratio": None,
	"ultimate_tensile_strength": None, # min UTS, MTS
	"yield_shear_strength": None,
    "design_stress_ratio": None, # % of min tensile
	"max_operating_temperature": None, # F or C
	"density": None, # lb/in^3 or gcc
	"description": "",
    "constituents": template_constituents,
    "rockwell_hardness": "",
}
print(json.dumps(template_material_dict, indent=4))


####################################
# Music Wire, ASTM A228
####################################
# Alt names: 228 Music Wire, Piano wire, ASTM A228, ASTM A29, ASTM A682, AISI 1086, AMS 5112, QQ-W-470, UNS K08500, UNS G10860, SAE J403, SAE J412, SAE J414e, Japanese JIS G3522 SWP-A G3522 SWP-B, German DIN 1.1269, British BS 1408 5216 5201

music_wire_constituents = {
    "C%": [0.7, 1.0],
    "Mn%": [0.2, 0.6],
}

music_wire_material_dict = {
    "type": "material",
    "name": "Music Wire ASTM A228",
    "spec": "ASTM A228",
    "units": "lb_in_F",
    "elastic_modulus": 30.0e6, # psi or MPa
	"torsion_modulus": 11.5e6, # psi or MPa
    "elastic_limit_ratio": None,
	"ultimate_tensile_strength": 230.0e3, # min UTS, MTS
	"yield_shear_strength": None,
    "design_stress_ratio": 0.45, # % of min tensile
	"max_operating_temperature": 250.0, # F or C
	"density": 0.284, # lb/in^3 or gcc
	"description": "Music Wire is cold drawn, and it has a high and uniform tensile. Music Wire is the toughest and most widely used of all spring materials for small springs. It has the highest tensile strength and can withstand higher stresses under repeated loading than any other spring material.",
    "constituents": music_wire_constituents,
    "rockwell_hardness": "C41-60",
}
print(json.dumps(music_wire_material_dict, indent=4))


####################################
# Chromium Vanadium, ASTM A231
####################################
# Alt names: Chrome-Vanadium, OTCV, OTVC, UNS G9254, ASTM A231, AISI 6150, AMS 6450, QQ-W-412 Comp, SAE 6150C

chrome_vanadium_constituents = {
    "C%": [0.48, 0.53],
    #"Ni%": [0.0, 0.0],
    "Cr%": [0.8, 1.1],
    #"Al%": [0.0, 0.0],
    #"Co%": [0.0, 0.0],
    #"Mo%": [0.0, 0.0],
    "V%": [0.15, 0.15],
}

chrome_vanadium_material_dict = {
    "type": "material",
    "name": "Chrome-Vanadium ASTM A231",
    "spec": "ASTM A231",
    "units": "lb_in_F",
    "elastic_modulus": 30.0e6, # psi or MPa
	"torsion_modulus": 11.5e6, # psi or MPa
    "elastic_limit_ratio": None,
	"ultimate_tensile_strength": 190.0, # min UTS, MTS
	"yield_shear_strength": None,
    "design_stress_ratio": 0.45, # % of min tensile
	"max_operating_temperature": 400.0, # F or C
	"density": 0.284, # lb/in^3 or gcc
	"description": "Cold drawn and heat treated before fabrication. Used for shock loads and moderately elevated temperature.",
    "constituents": chrome_vanadium_constituents,
    "rockwell_hardness": "",
}
print(json.dumps(chrome_vanadium_material_dict, indent=4))


####################################
# Stainless Type 17-7 PH ASTM A313, AMS 5678
####################################
# Alt Names: 17-7 stainless steel, UNS S17700, ASTM A313, ASTM A613, AISI 631, AMS 5678, AMS 5529, SAE J217
# metric:
# E_17_7ph_mpa = 201.0e3
# G_17_7ph_mpa = 75.8e3
# T_max_17_7ph_C = 340.0
# rho_17_7ph_gcc = 7.8


SS17_7PH_constituents = {
    "Ni%": [6.5, 7.5],
    "Cr%": [16.0, 18.0],
    "Al%": [0.75, 1.5],
}

SS17_7PH_material_dict = {
    "type": "material",
    "name": "Stainless Steel 17-7PH CH900",
    "spec": "ASTM A313, AMS 5678",
    "units": "lb_in_F",
    "elastic_modulus": 29.5e6, # psi or MPa
	"torsion_modulus": 11.0e6, # psi or MPa
    "elastic_limit_ratio": None,
	"ultimate_tensile_strength": 235.0e3, # min UTS, MTS
	"yield_shear_strength": None,
    "design_stress_ratio": 0.45, # % of min tensile
	"max_operating_temperature": 650.0, # F or C
	"density": 0.286, # lb/in^3 or gcc
	"description": "Cold drawn & precipitation hardened after fabrication. High strength and general purpose corrosion resistance. Slightly magnetic in spring temper.",
    "constituents": SS17_7PH_constituents,
    "rockwell_hardness": "C38-57",
}
print(json.dumps(SS17_7PH_material_dict, indent=4))


####################################
# Elgiloy, AMS 5833
####################################
# Alt Names: Phynox, ASTM F1058, UNS R30003, AMS 5833

elgiloy_constituents = {
    "Ni%": [15.5, 15.5],
    "Co%": [40.0, 40.0],
    "Cr%": [20.0, 20.0],
    "Mo%": [7.0, 7.0],
}

elgiloy_material_dict = {
    "type": "material",
    "name": "elgiloy",
    "spec": "ASTM F1058, UNS R30003, AMS 5833",
    "units": "lb_in_F",
    "elastic_modulus": 29.5e6, # psi or MPa
	"torsion_modulus": 11.5e6, # psi or MPa
    "elastic_limit_ratio": 0.75,
	"ultimate_tensile_strength": 220.0e3, # min UTS, MTS
	"yield_shear_strength": None,
    "design_stress_ratio": 0.45, # % of min tensile
	"max_operating_temperature": 600.0, # F or C
	"density": 0.3, # lb/in^3 or gcc
	"description": "High strength, high ductility, and good mechanical properties. Applications range from freshwater to industrial and marine atmospheres, and mild chemical and oxidizing environments. Elgiloy shows a very good performance in high-temperature environments.",
    "constituents": elgiloy_constituents,
    "rockwell_hardness": "C38-55",
}
print(json.dumps(elgiloy_material_dict, indent=4))



materials_dict = {
    'music_wire': music_wire_material_dict,
    'ss17_7ph': SS17_7PH_material_dict,
    'elgiloy': elgiloy_material_dict,
}

# export to .cvs via pandas:



# TODO: functions that switch from lb_in_F to N_mm_C...
