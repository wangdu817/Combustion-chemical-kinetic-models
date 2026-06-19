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
- Plasma-related mechanism: no
- Validation reactor/type from abstract: rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing\extracted\s0010218025006911_mmc4\Nor_O2-Xiao25-Mech.inp
- Original thermodynamic source files: _processing\extracted\s0010218025006911_mmc5\Nor_O2-Xiao25-thermo.dat
- Original transport source files: _processing\extracted\s0010218025006911_mmc6\Nor_O2-Xiao25-transport.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 939
- Reaction count: 4366
- Message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 22618 and 22645 of E:\mech_collection\combustion_and_flame_mechanisms\norbornane\2026\xiao_2026_norbornane_114656\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 989: H2 + M <=> 2 H + M
Reaction 985: 2 H + O2 <=> H2 + O2

|  Line |
|  22613 |   note: Added in v6
|  22614 | - equation: cCHC6H10-7-OO + cCHC6H10-7-OO <=> cCHC6H10-7-O + cCHC6H10-7-O
|  22615 |     + O2  # Reaction 984
|  22616 |   rate-constant: {A: 1.4e+16, b: -1.61, Ea: 1860.0}
|  22617 |   note: Added in v6
>  22618 > - equation: H2 + M <=> H + H + M  # Reaction 985
            ^
|  22619 |   type: three-body
|  22620 |   rate-constant: {A: 4.577e+19, b: -1.4, Ea: 1.044e+05}
|  22621 |   efficiencies: {HE: 0.83, CO: 1.9, CH4: 2.0, H2: 2.5, C2H6: 3.0, CO2: 3.8,
...
|  22640 |     CHEM REF DATA 2005, 34, 757-1397. !\Comment: WARNING'
|  22641 | - equation: H2 + OH <=> H + H2O  # Reaction 988
|  22642 |   rate-constant: {A: 2.2e+08, b: 1.51, Ea: 3430.0}
|  22643 |   note: '\Author: UB !\Ref: J.V.MICHAEL SUTHERLAND, J.PHYS.CHEM. 92(1988)
|  22644 |     3853 !\Comment: WARNING'
>  22645 > - equation: H + O2 + H <=> H2 + O2  # Reaction 989
            ^
|  22646 |   rate-constant: {A: 8.8e+22, b: -1.835, Ea: 800.0}
|  22647 |   note: '\Author: WARNING !\Ref: WARNING !\Comment: WARNING'
|  22648 | - equation: H + O2 + H <=> OH + OH  # Reaction 990
*******************************************************************************

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Norbornane (C7H12), a typical polycyclic alkane, is currently of interest as a backbone for next-staged aviation fuels in fuel design and as a potential additive in commercial fuel to improve combustion performance. The polycyclic geometry of norbornane poses challenges in the characterization of its kinetics, thus hindering future applications. In this work, a combined experimental and kinetic modeling approach was employed to study the auto-ignition behavior of norbornane. A set of norbornane auto-ignition experiments was conducted in a rapid compression machine, covering the equivalence ratios of 0.5 and 1.0 across the temperature range of 623 K to 923 K and pressures of 10, 15, and 20 bar. The auto-ignition process of norbornane exhibits the two-stage ignition behavior. Ignition delay times were recorded, showing the negative temperature coefficient (NTC) phenomenon. With the assistance of gas chromatography, several oxidation products were identified and their concentration profiles through the whole ignition process were obtained under a typical condition, also demonstrating obvious two-stage ignition behavior. The first detailed oxidation kinetic model of norbornane was built with 939 species and 4364 reactions. Simulation results exhibit consistent agreement with experimental data. Throughout the modeling analyses, the critical reactions governing the ignition process are uncovered to elucidate the 2-staged ignition behavior. The increase of the effective temperature (Teff) shifts the branching ratio of low-temperature oxidation pathways, accounting for the disappearance of first-stage ignition and inducing the emergence of the NTC phenomenon of global ignition. Also, the different pressure dependencies of the first-stage and the global ignition contribute to the pressure effect on the shift of the temperature region showing the NTC.

## Processing Notes

- none
