# Corrigendum to ``Detailed kinetic modeling of dimethoxymethane. Part I: Ab initio thermochemistry and kinetics predictions for key reactions'' [Combust. Flame (189) 433-442]

## Bibliography

Wassja A. Kopp, Leif C. Kröger, Malte Döntgen, Sascha Jacobs, Ultan Burke, Henry J. Curran, et al.. Corrigendum to ``Detailed kinetic modeling of dimethoxymethane. Part I: Ab initio thermochemistry and kinetics predictions for key reactions'' [Combust. Flame (189) 433-442][J]. Combustion and Flame, 2020, 218: 27. DOI: 10.1016/j.combustflame.2020.03.020.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 218 / Aug
- Article number: 27
- DOI: 10.1016/j.combustflame.2020.03.020
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218020301231
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: dimethoxymethane
- Plasma-related mechanism: yes
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S0010218026002737_mmc2.txt, _processing/extracted/s0010218026000271_mmc3/kinetic.inp, _processing/extracted/s0010218015002734_mmc2/CSM_Master_PyrolysisMechanism.txt, _processing/extracted/s0010218010002774_mmc1/chem.inp
- Original thermodynamic source files: _processing/raw_downloads/S0010218026002737_mmc3.txt, _processing/extracted/s0010218026000271_mmc4/therm.dat, _processing/extracted/s0010218015002734_mmc2/CSM_Master_Thermo.txt, _processing/extracted/s0010218010002774_mmc1/therm.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 10
- Reaction count: 31
- Message: missing cantera result json
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 2

- Status: cantera_failed
- Species count: 10
- Reaction count: 31
- Message: InputError: Error while reading reaction in chem.inp starting on line 50: """ E + AR => E+ AR* f(E/N) ! BOLSIG AR -> AR* """ could not convert string to float: 'E+' Error while reading reaction in chem.inp starting on line 51: """ E + AR => E + E + AR^+ f(E/N) ! BOLSIG AR -> AR^+ """ could not convert string to float: '+' Error while reading reaction in chem.inp starting on line 54: """ E + NO => E + NO(V1) f(E/N) ! BOLSIG NO -> NO(V1) """ could not convert string to float: '+' Error while reading reaction in chem.inp starting on line 55: """ E + NO => E + NO(V2) f(E/N) ! BOLSIG NO -> NO(V2) """ could not convert string to float: '+' Error while reading reaction in chem.inp starting on line 56: """ E + NO => E + NO(V3) f(E/N) ! BOLSIG NO -> NO(V3) """ could not convert string to float: '+' ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 3

- Status: cantera_failed
- Species count: 10
- Reaction count: 31
- Message: InputError: Error while reading reaction in chem.inp starting on line 2: """ C2H5CN+CH2CN=NCCH2CN+C2H5 1.77E+09 0.805 24190.95 PLOG / 1.31E-04 2.35E+04 2.197 21164.95 / PLOG / 1.31E-03 3.31E+04 2.154 21245.83 / PLOG / 1.00E+00 1.77E+09 0.805 24190.95 / PLOG / 1.00E+01 1.94E+11 0.277 26551.64 / PLOG / 1.00E+02 1.14E+07 1.612 26774.06 / """ Unexpected token 'C2H5CN+CH2CN' in reaction expression 'C2H5CN+CH2CN=NCCH2CN+C2H5'. May be due to undeclared species 'C2H5CNCH2CN'. Error while reading reaction in chem.inp starting on line 9: """ C2H5CN+CH2CN=CH3CN+CH2CH2CN 1.34E-04 4.915 13067.54 """ Unexpected token 'C2H5CN+CH2CN' in reaction expression 'C2H5CN+CH2CN=CH3CN+CH2CH2CN'. May be due to undeclared species 'C2H5CNCH2CN'. Error while reading reaction in chem.inp starting on line 10: """ C2H5CN ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 4

- Status: cantera_failed
- Species count: 10
- Reaction count: 31
- Message: InputError: Error while reading reaction in chem.inp starting on line 2: """ C2H5CN+CH2CN=NCCH2CN+C2H5 1.77E+09 0.805 24190.95 PLOG / 1.31E-04 2.35E+04 2.197 21164.95 / PLOG / 1.31E-03 3.31E+04 2.154 21245.83 / PLOG / 1.00E+00 1.77E+09 0.805 24190.95 / PLOG / 1.00E+01 1.94E+11 0.277 26551.64 / PLOG / 1.00E+02 1.14E+07 1.612 26774.06 / """ Unexpected token 'C2H5CN+CH2CN' in reaction expression 'C2H5CN+CH2CN=NCCH2CN+C2H5'. May be due to undeclared species 'C2H5CNCH2CN'. Error while reading reaction in chem.inp starting on line 9: """ C2H5CN+CH2CN=CH3CN+CH2CH2CN 1.34E-04 4.915 13067.54 """ Unexpected token 'C2H5CN+CH2CN' in reaction expression 'C2H5CN+CH2CN=CH3CN+CH2CH2CN'. May be due to undeclared species 'C2H5CNCH2CN'. Error while reading reaction in chem.inp starting on line 10: """ C2H5CN ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S0010218014002776_mmc1.docx
- extracted S0010218026003275_mmc2.xlsx
- extracted S0010218018305273_mmc1.docx
- extracted S0010218019302767_mmc1.docx
- extracted S0010218015002734_mmc2.zip
- extracted S0010218026002749_mmc1.docx
- extracted S0010218012001927_mmc1.docx
- extracted S0010218026003275_mmc3.zip
- extracted S0010218026000271_mmc2.zip
- extracted S0010218026000271_mmc4.zip
- extracted S0010218026003275_mmc1.docx
- extracted S0010218026000271_mmc1.docx
- extracted S0010218026000271_mmc3.zip
- extracted S0010218010002774_mmc1.zip
