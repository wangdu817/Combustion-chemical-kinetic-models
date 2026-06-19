# A kinetic and experimental analysis of the co-oxidation of ammonia and dimethoxymethane employing SVUV-PIMS

## Bibliography

Chunlan Qin, Bingzhi Liu, Weijie Xu, Canbin Lin, ... Lidong Zhang. A kinetic and experimental analysis of the co-oxidation of ammonia and dimethoxymethane employing SVUV-PIMS[J]. Combustion and Flame, 2026, 283: 114575. DOI: 10.1016/j.combustflame.2025.114575.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 283 / January
- Article number: 114575
- DOI: 10.1016/j.combustflame.2025.114575
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025006121
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ammonia_dimethoxymethane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: jet-stirred reactor, laminar flame speed, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing\extracted\s0010218025006121_mmc4\USTC-NH3_DMM.inp
- Original thermodynamic source files: _processing\extracted\s0010218025006121_mmc3\USTC-NH3_DMM.dat
- Original transport source files: _processing\extracted\s0010218025006121_mmc5\USTC-NH3_DMM_trans.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 227
- Reaction count: 1632
- Message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 4127 and 4136 of E:\mech_collection\combustion_and_flame_mechanisms\ammonia_dimethoxymethane\2026\qin_2026_ammonia_dimethoxymethane_114575\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 36: H + OH + M <=> H2O + M
Reaction 35: H2O + H2O <=> H + OH + H2O

|  Line |
|  4122 |   note: RAS/GLA08a HIP/TRO95
|  4123 | - equation: H2O2 + OH <=> H2O + HO2  # Reaction 34
|  4124 |   duplicate: true
|  4125 |   rate-constant: {A: 1.6e+18, b: 0.0, Ea: 2.941e+04}
|  4126 |   note: RAS/GLA08a HIP/TRO95
>  4127 > - equation: H + OH + M <=> H2O + M  # Reaction 35
            ^
|  4128 |   type: three-body
|  4129 |   rate-constant: {A: 8.62e+21, b: -2.0, Ea: 0.0}
|  4130 |   efficiencies: {H2O: 16.25, CO: 1.875, CO2: 3.75}
|  4131 |   note: |-
|  4132 |     r28
|  4133 |     OH+H+M=H2O+M                         4.5E22  -2.000       0 ! RAS/GLA08a CON/WES04
|  4134 |      AR/0.38/ H2/0.73/ H2O/12/ !HE/0.38/
|  4135 |     	BAULCH	76
>  4136 > - equation: 2 H2O <=> OH + H + H2O  # Reaction 36
            ^
|  4137 |   rate-constant: {A: 1.0e+26, b: -2.44, Ea: 1.2016e+05}
|  4138 | - equation: OH + H2 <=> H + H2O  # Reaction 37
|  4139 |   rate-constant: {A: 4.38e+13, b: 0.0, Ea: 6990.0}
*******************************************************************************

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

The carbon-neutral potential of ammonia is constrained by fundamental combustion barriers, driving the development of advanced bio-fuel blends as kinetic enhancement strategies. In this research, co-oxidation experiments of NH3 and dimethoxymethane (DMM, CH3OCH2OCH3) were executed in a jet-stirred reactor (JSR) under 1 atm and 730–1060 K. Through the use of state-of-the-art synchrotron radiation vacuum ultraviolet photoionization mass spectrometry (SVUV-PIMS) for online diagnostics, we achieved the first quantification of the species pool in the reaction system, covering C/H/O compounds and various key nitrogen-containing intermediates. The experimentally derived species profiles served as the foundation for refining a kinetic model to describe NH3 and DMM co-oxidation. The model was updated based on experimental and literature data, with key modifications to the rate constants for H-atom abstraction (DMM, NH3, intermediates) and the primary N2O consumption pathway. Ultimately, the improved model substantially improves the prediction of NH3/DMM co-oxidation species distribution (especially for DMM, NH3, CH3OCHO, CH2O, N2O, etc.), and it can also accurately reproduce ignition delay times and laminar flame speeds from previous studies. Additionally, the kinetic analysis further clarified the co-oxidation reaction pathways of NH3/DMM, especially highlighting the non-negligible influence of some key reaction pathways on their co-oxidation behaviour, such as CH3OCH2OCH3 + NH2 = CH3OCH2OCH2 (CH3OCHOCH3) + NH3, CO + N2O = N2 + CO2, etc. This research provides critical experimental data and a more reliable kinetic model, advancing our understanding of the chemical kinetics underlying NH3/DMM co-combustion.

## Processing Notes

- none
