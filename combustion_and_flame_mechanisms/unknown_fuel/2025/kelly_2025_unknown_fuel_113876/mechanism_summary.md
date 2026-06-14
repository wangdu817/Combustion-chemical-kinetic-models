# Machine learned compact kinetic model for liquid fuel combustion

## Bibliography

Mark Kelly, G. Bourque, M. Hase, S. Dooley. Machine learned compact kinetic model for liquid fuel combustion[J]. Combustion and Flame, 2025, 272: 113876. DOI: 10.1016/j.combustflame.2024.113876.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 272 / February
- Article number: 113876
- DOI: 10.1016/j.combustflame.2024.113876
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024005856
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218024005856/pdfft?md5=38fca8642259e047b95fcd7bdcd4a436&pid=1-s2.0-S0010218024005856-main.pdf
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218024005856_mmc1/SupplementalMaterial/TCD_32s.yaml, _processing/extracted/s0010218024005856_mmc1/SupplementalMaterial/TCD_32s.cti
- Original thermodynamic source files: _processing/extracted/s0010218024005856_mmc1/SupplementalMaterial/TCD_32s.yaml, _processing/extracted/s0010218024005856_mmc1/SupplementalMaterial/TCD_32s.cti
- Original transport source files: _processing/extracted/s0010218024005856_mmc1/SupplementalMaterial/TCD_32s.yaml, _processing/extracted/s0010218024005856_mmc1/SupplementalMaterial/TCD_32s.cti

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 33
- Reaction count: 153
- Message: CanteraError: ******************************************************************************* CanteraError thrown by newSolution: The CTI and XML formats are no longer supported. *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: 33
- Reaction count: 153
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by Reaction::checkBalance: Error on line 575 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/unknown_fuel/2025/kelly_2025_unknown_fuel_113876/mechanism.yaml: The following reaction is unbalanced: nFuel => 2 C3H5 + 0.333 C3H6 Element Reactants Products C 7 6.9990000000000006 H 12 11.998000000000001 | Line | | 570 | type: pressure-dependent-Arrhenius | 571 | rate-constants: | 572 | - {P: 0.9999999 atm, A: 1.29e+15, b: -0.065781, Ea: 3634.963} | 573 | - {P: 5.0000001 atm, A: 1.29e+15, b: -0.065781, Ea: 3634.963} | 574 | - {P: 9.9 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S0010218024005856_mmc1.zip
