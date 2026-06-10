# Combustion reaction mechanism of C0-C3/N2O flames: Experimental and kinetic modeling study of laminar burning velocity

## Bibliography

Yun Ge, Hong-Hao Ma, Yue Jiao, Shuo Yang, ... Lu-Qing Wang. Combustion reaction mechanism of C0-C3/N2O flames: Experimental and kinetic modeling study of laminar burning velocity[J]. Combustion and Flame, 2026, 288: 114948. DOI: 10.1016/j.combustflame.2026.114948.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 288 / June
- Article number: 114948
- DOI: 10.1016/j.combustflame.2026.114948
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026001847
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: n2o_c0_c3_fuel_blends
- Validation reactor/type from abstract: laminar flame speed

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: extracted\s0010218026001847_mmc2\Chem.txt
- Original thermodynamic source files: extracted\s0010218026001847_mmc3\Thermo.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 96
- Reaction count: 626
- Message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 2565 and 2751 of E:\mech_collection\combustion_and_flame_2026_mechanisms\n2o_c0_c3_fuel_blends\yun_ge_2026_114948_combustion_reaction_mechanism_of_c0_c3_n2o_fl\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 448: NNH + M <=> H + N2 + M
Reaction 400: NNH + O2 <=> H + N2 + O2

|  Line |
|  2560 |   note: GRI Mech 3.0
|  2561 | - equation: NH2 + H <=> NH + H2  # Reaction 399
|  2562 |   duplicate: true
|  2563 |   rate-constant: {A: 4.0e+13, b: 0.0, Ea: 3650.0}
|  2564 |   note: GRI Mech 3.0
>  2565 > - equation: NNH + M <=> N2 + H + M  # Reaction 400
            ^
|  2566 |   type: three-body
|  2567 |   rate-constant: {A: 1.3e+14, b: -0.11, Ea: 4980.0}
|  2568 |   efficiencies: {H2: 2.0, H2O: 6.0, CH4: 2.0, CO: 1.5, CO2: 2.0, C2H6: 3.0,
...
|  2746 |   note: J.W. Bozzelli, et al., International journal of chemical kinetics
|  2747 |     27 (1995) 1097-1109
|  2748 | - equation: NNH + O2 <=> N2 + HO2  # Reaction 447
|  2749 |   rate-constant: {A: 5.6e+14, b: -0.385, Ea: -13.0}
|  2750 |   note: S.J. Klippenstein, et al., Combustion and Flame 158 (2011) 774-789
>  2751 > - equation: NNH + O2 <=> N2 + H + O2  # Reaction 448
            ^
|  2752 |   rate-constant: {A: 5.0e+13, b: 0.0, Ea: 0.0}
|  2753 |   note: P. Glarborg, et al., Combustion and Flame 115 (1998) 1-27.
|  2754 | - equation: NNH + NO <=> N2 + HNO  # Reaction 449
*******************************************************************************

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S0010218026001847_mmc1.zip
- extracted S0010218026001847_mmc2.zip
- extracted S0010218026001847_mmc3.zip
- extracted S0010218026001847_mmc4.zip
- extracted S0010218026001847_mmc5.zip
