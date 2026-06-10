# Assessment of conditional source-term estimation (CSE) with direct chemistry integration including detailed and reduced kinetics for the simulation of a turbulent DME flame

## Bibliography

Amir H. Mahdipour, Fekadu Mosisa Wako, Cécile Devaud, W. Kendal Bushe. Assessment of conditional source-term estimation (CSE) with direct chemistry integration including detailed and reduced kinetics for the simulation of a turbulent DME flame[J]. Combustion and Flame, 2026, 285: 114714. DOI: 10.1016/j.combustflame.2025.114714.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 285 / March
- Article number: 114714
- DOI: 10.1016/j.combustflame.2025.114714
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025007497
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025007497/pdfft?md5=458f4982b7e1b849dd602a39c7cbf75c&pid=1-s2.0-S0010218025007497-main.pdf
- Fuel type: dimethyl_ether
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: extracted\s0010218025007497_mmc1\DME_reduced_CK_input
- Original thermodynamic source files: extracted\s0010218025007497_mmc1\DME_reduced_CK_input
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 241 and 398 of E:\mech_collection\combustion_and_flame_2026_mechanisms\dimethyl_ether\amir_h_mahdipour_2026_114714_assessment_of_conditional_source_term_estimat\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 64: H + O2 <=> O + OH
Reaction 1: H + O2 <=> O + OH

|  Line |
|   236 |       -1.123918e+04, 14.43229]
|   237 |     - [4.825938, 0.01384043, -4.557259e-06, 6.724967e-10, -3.598161e-14,
|   238 |       -1.271779e+04, -5.239507]
|   239 | 
|   240 | reactions:
>   241 > - equation: H + O2 <=> O + OH  # Reaction 1
            ^
|   242 |   rate-constant: {A: 3.5470000000000005e+15, b: -0.406, Ea: 1.6599e+04}
|   243 | - equation: H2 + O <=> H + OH  # Reaction 2
|   244 |   rate-constant: {A: 5.0800000000000015e+04, b: 2.67, Ea: 6290.0}
...
|   393 |   rate-constant: {A: 1.8550000000000003e-03, b: 5.29, Ea: -109.0}
|   394 | - equation: CH3OCH3 + HO2 <=> CH3OCH2 + H2O2  # Reaction 62
|   395 |   rate-constant: {A: 2.0000000000000004e+13, b: 0.0, Ea: 1.65e+04}
|   396 | - equation: CH3OCH2 <=> CH2O + CH3  # Reaction 63
|   397 |   rate-constant: {A: 1.2e+13, b: 0.0, Ea: 2.575e+04}
>   398 > - equation: H + O2 <=> O + OH  # Reaction 64
            ^
|   399 |   rate-constant: {A: 3.5470000000000005e+15, b: -0.406, Ea: 1.6599e+04}
|   400 | - equation: H2 + O <=> H + OH  # Reaction 65
|   401 |   rate-constant: {A: 5.0800000000000015e+04, b: 2.67, Ea: 6290.0}
*******************************************************************************

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S0010218025007497_mmc1.zip
