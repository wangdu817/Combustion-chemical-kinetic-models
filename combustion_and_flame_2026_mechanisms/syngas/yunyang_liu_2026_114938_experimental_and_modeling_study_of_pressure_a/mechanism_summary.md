# Experimental and modeling study of pressure and NOx addition effects on syngas oxidation in a flow reactor

## Bibliography

Yunyang Liu, Erjiang Hu, Jiajun You, Xiaoyang Guo, ... Zuohua Huang. Experimental and modeling study of pressure and NOx addition effects on syngas oxidation in a flow reactor[J]. Combustion and Flame, 2026, 287: 114938. DOI: 10.1016/j.combustflame.2026.114938.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 287 / May
- Article number: 114938
- DOI: 10.1016/j.combustflame.2026.114938
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026001744
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: syngas
- Validation reactor/type from abstract: flow reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: extracted\s0010218026001744_mmc2\Supplementary Material 2_chem.inp
- Original thermodynamic source files: extracted\s0010218026001744_mmc3\Supplementary Material 3_thermo.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 39
- Reaction count: 203
- Message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 451 and 676 of E:\mech_collection\combustion_and_flame_2026_mechanisms\syngas\yunyang_liu_2026_114938_experimental_and_modeling_study_of_pressure_a\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 41: H2 + M <=> 2 H + M
Reaction 1: 2 H + O2 <=> H2 + O2

|  Line |
|   446 |     - [4.04483566, 7.31130186e-03, -2.47625799e-06, 3.83733021e-10, -2.23107573e-14,
|   447 |       2.5324142e+04, 2.88423392]
|   448 |     note: T 7/11
|   449 | 
|   450 | reactions:
>   451 > - equation: H2 + M <=> H + H + M  # Reaction 1
            ^
|   452 |   type: three-body
|   453 |   rate-constant: {A: 4.577e+19, b: -1.4, Ea: 1.044e+05}
|   454 |   efficiencies: {H2: 2.5, H2O: 12.0, CO: 1.9, CO2: 3.8, HE: 0.83, CH4: 2.0,
...
|   671 |   rate-constant: {A: 3.93e+13, b: 0.0, Ea: 0.0}
|   672 |   note: '\Author: SP !\Ref: YU ET AL., JCP, 2008, 129(21) !\Comment: WARNING'
|   673 | - equation: CO + H2O <=> CO2 + H2  # Reaction 40
|   674 |   rate-constant: {A: 2.0e+11, b: 0.0, Ea: 3.8e+04}
|   675 |   note: POLIMI Mech
>   676 > - equation: H + O2 + H <=> H2 + O2  # Reaction 41
            ^
|   677 |   rate-constant: {A: 8.8e+22, b: -1.835, Ea: 800.0}
|   678 |   note: |-
|   679 |     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
*******************************************************************************

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S0010218026001744_mmc1.docx
- extracted S0010218026001744_mmc2.zip
- extracted S0010218026001744_mmc3.zip
- extracted S0010218026001744_mmc4.zip
