# Elucidating norbornane auto-ignition behavior via RCM experiments and kinetic modelling

## Bibliography

Hang Xiao, Zhaohan Chu, Chenyue Tao, Xiao Liu, Bin Yang. Elucidating norbornane auto-ignition behavior via RCM experiments and kinetic modelling[J]. Combustion and Flame, 2026, 284: 114656. DOI: 10.1016/j.combustflame.2025.114656.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 284 / February
- Article number: 114656
- DOI: 10.1016/j.combustflame.2025.114656
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025006911
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: norbornane
- Validation reactor/type from abstract: rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: extracted\s0010218025006911_mmc4\Nor_O2-Xiao25-Mech.inp
- Original thermodynamic source files: extracted\s0010218025006911_mmc5\Nor_O2-Xiao25-thermo.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 16067 and 16094 of E:\mech_collection\combustion_and_flame_2026_mechanisms\norbornane\hang_xiao_2026_114656_elucidating_norbornane_auto_ignition_behavior\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 989: H2 + M <=> 2 H + M
Reaction 985: 2 H + O2 <=> H2 + O2

|  Line |
|  16062 |   note: Added in v6
|  16063 | - equation: cCHC6H10-7-OO + cCHC6H10-7-OO <=> cCHC6H10-7-O + cCHC6H10-7-O
|  16064 |     + O2  # Reaction 984
|  16065 |   rate-constant: {A: 1.4e+16, b: -1.61, Ea: 1860.0}
|  16066 |   note: Added in v6
>  16067 > - equation: H2 + M <=> H + H + M  # Reaction 985
            ^
|  16068 |   type: three-body
|  16069 |   rate-constant: {A: 4.577e+19, b: -1.4, Ea: 1.044e+05}
|  16070 |   efficiencies: {HE: 0.83, CO: 1.9, CH4: 2.0, H2: 2.5, C2H6: 3.0, CO2: 3.8,
...
|  16089 |     CHEM REF DATA 2005, 34, 757-1397. !\Comment: WARNING'
|  16090 | - equation: H2 + OH <=> H + H2O  # Reaction 988
|  16091 |   rate-constant: {A: 2.2e+08, b: 1.51, Ea: 3430.0}
|  16092 |   note: '\Author: UB !\Ref: J.V.MICHAEL SUTHERLAND, J.PHYS.CHEM. 92(1988)
|  16093 |     3853 !\Comment: WARNING'
>  16094 > - equation: H + O2 + H <=> H2 + O2  # Reaction 989
            ^
|  16095 |   rate-constant: {A: 8.8e+22, b: -1.835, Ea: 800.0}
|  16096 |   note: '\Author: WARNING !\Ref: WARNING !\Comment: WARNING'
|  16097 | - equation: H + O2 + H <=> OH + OH  # Reaction 990
*******************************************************************************

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S0010218025006911_mmc1.docx
- extracted S0010218025006911_mmc2.docx
- extracted S0010218025006911_mmc3.zip
- extracted S0010218025006911_mmc4.zip
- extracted S0010218025006911_mmc5.zip
- extracted S0010218025006911_mmc6.zip
