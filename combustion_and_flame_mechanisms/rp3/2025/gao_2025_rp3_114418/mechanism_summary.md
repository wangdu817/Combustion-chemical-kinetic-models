# Experimental and kinetic modeling studies on high-pressure oxidation of RP-3 surrogate fuel. Part Ⅰ: Three-stage oxidation phenomenon of a three-component surrogate fuel

## Bibliography

Xiang Gao, Du Wang, Qian-Peng Wang, Xu-Peng Yu, ... Zhen-Yu Tian. Experimental and kinetic modeling studies on high-pressure oxidation of RP-3 surrogate fuel. Part Ⅰ: Three-stage oxidation phenomenon of a three-component surrogate fuel[J]. Combustion and Flame, 2025, 281: 114418. DOI: 10.1016/j.combustflame.2025.114418.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 281 / November
- Article number: 114418
- DOI: 10.1016/j.combustflame.2025.114418
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025004559
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025004559/pdfft?md5=e56ab208916ede4dfbf2d46e3a315201&pid=1-s2.0-S0010218025004559-main.pdf
- Fuel type: rp3
- Plasma-related mechanism: no
- Validation reactor/type from abstract: jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218025004559_mmc2/SM2_Mech_3C.inp
- Original thermodynamic source files: _processing/extracted/s0010218025004559_mmc3/SM3_Therm_3C.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'CH2OCH2O2H' Ignoring redundant declaration for species 'CH3CHCHCHO' Ignoring redundant declaration for species 'CH3CHOOCOCH3' Ignoring redundant declaration for species 'TC4H9O' Ignoring redundant declaration for species 'IC3H5O2HCHO' Suppressed 11 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Error while reading reaction in chem.inp starting on line 991: """ H+O2<=>O+OH 3.547E+15 -0.406 16599.0 """ list index out of range Ignoring redundant thermo data for species 'HO2CHO' starting on line 100 of therm.dat. Ignoring redundant thermo data for species 'O2CHO' starting on line 104 of therm.dat. Ignoring redundant thermo data for species 'HOCH2O2H' starting on ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Experimental and modeling studies were conducted on the oxidation of a three-component surrogate fuel for RP-3 kerosene in a jet-stirred reactor at pressure of 12.0 atm, temperatures of 525–1025 K, and equivalence ratios of 0.4 and 2.0. The surrogate fuel consists of 66.2 % n-dodecane, 18.0 % 1,3,5-trimethylcyclohexane, and 15.8 % n-propylbenzene (in mole fraction). A comprehensive kinetic model, incorporating 1527 species and 7781 reactions, was developed and validated against experimental data of high-pressure oxidation, atmospheric pressure oxidation, and ignition delay times. The model demonstrates a credible alignment with the experimental results. Unlike the strong NTC behavior observed at 1.0 atm, the three fuels exhibit a distinct three-stage oxidation phenomenon (weak NTC, WNTC) under high pressure. This process is characterized by an initial rapid decline in fuel concentration (Stage I), followed by a relatively stable phase (Stage II), and a final stage of gradual fuel consumption (Stage III). ROP analysis indicates that the dominant fuel consumption pathways involve H-abstraction by OH radicals, with the formation of aromatic products mainly originating from n-propylbenzene. In Stage I, fuel consumption is primarily driven by the rapid generation of OH via low-temperature chain-branching pathways. During Stage II, the competition for OH radicals among intermediates and fuels results in minimal changes in fuel concentration. In Stage III, the decomposition of H2O2 becomes the dominant source of OH radical, accelerating fuel oxidation. At Φ = 2.0, despite the overall reduction in OH radicals, the higher reactivity of NC12H26 enables it to compete more effectively for OH radicals, leading to a consumption profile similar to that at Φ = 0.4. In contrast, T135MCH and A1C3H7 exhibit lower consumption rates than those at Φ = 0.4. In comparing the kinetic results between 1.0 and 12.0 atm, it indicates that the differences in oxidation behaviors stem from pressure-dependent reactions, such as H2O2 decomposition and O2 addition. Sensitivity analysis reveals that reactions promoting fuel oxidation also enhance OH radical formation. The synergistic oxidation of the three fuels is reflected in sharing of radicals, with n-dodecane contributing most significantly to OH production.

## Processing Notes

- extracted S0010218025004559_mmc2.zip
- extracted S0010218025004559_mmc4.xlsx
- extracted S0010218025004559_mmc3.zip
