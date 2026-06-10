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
- Fuel type: ammonia_methane_ethane_dimethoxymethane
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: extracted\s0010218025006121_mmc4\USTC-NH3_DMM.inp
- Original thermodynamic source files: extracted\s0010218025006121_mmc3\USTC-NH3_DMM.dat
- Original transport source files: extracted\s0010218025006121_mmc5\USTC-NH3_DMM_trans.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 4127 and 4136 of E:\mech_collection\combustion_and_flame_2026_mechanisms\ammonia_methane_ethane_dimethoxymethane\chunlan_qin_2026_114575_a_kinetic_and_experimental_analysis_of_the_co\mechanism.yaml:
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

not available

## Processing Notes

- extracted S0010218025006121_mmc3.zip
- extracted S0010218025006121_mmc4.zip
- extracted S0010218025006121_mmc5.zip
