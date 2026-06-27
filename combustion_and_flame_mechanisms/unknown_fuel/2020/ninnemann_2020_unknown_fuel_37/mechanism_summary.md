# Comment on “Simultaneous lateral and endwall high-speed visualization of ignition in a circular shock tube” [Combustion and Flame 214 (2020) 263–265]

## Bibliography

Erik Ninnemann, Subith Vasu. Comment on “Simultaneous lateral and endwall high-speed visualization of ignition in a circular shock tube” [Combustion and Flame 214 (2020) 263–265][J]. Combustion and Flame, 2020, 217: 37. DOI: 10.1016/j.combustflame.2020.02.009.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 217 / Jul
- Article number: 37
- DOI: 10.1016/j.combustflame.2020.02.009
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218020300663
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: possible
- Validation reactor/type from abstract: shock tube

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S0010218026002737_mmc2.txt, _processing/raw_downloads/S0010218021004375_mmc4.txt, _processing/extracted/s0010218025006376_mmc2/naphtha mechanism -FINAL.inp, _processing/extracted/s0010218010003767_mmc1/Supplemental 2-Furan Mech.txt, _processing/extracted/s001021801300237x_mmc1/mech.inp, _processing/extracted/s0010218017304637_mmc1/supplement/prf/prf-207sp.inp, _processing/extracted/s0010218017304637_mmc1/supplement/propane/propane-32sp.inp, _processing/extracted/s0010218017304637_mmc1/supplement/methane/methane-27sp.inp, _processing/extracted/s0010218017304637_mmc1/supplement/nheptane/nc7h16-126sp.inp
- Original thermodynamic source files: _processing/raw_downloads/S0010218026002737_mmc3.txt, _processing/raw_downloads/S0010218021004375_mmc3.txt, _processing/raw_downloads/S001021801300237X_mmc2.txt, _processing/extracted/s0010218025006376_mmc2/naphtha mechanism -FINAL.inp, _processing/extracted/s0010218010003767_mmc1/Supplemental 2-Furan Mech.txt, _processing/extracted/s0010218017304637_mmc1/supplement/prf/therm-prf.dat, _processing/extracted/s0010218017304637_mmc1/supplement/propane/thermo-propane.dat, _processing/extracted/s0010218017304637_mmc1/supplement/methane/therm_methane.dat, _processing/extracted/s0010218017304637_mmc1/supplement/nheptane/therm-nc7h16.dat
- Original transport source files: _processing/extracted/s0010218017304637_mmc1/supplement/prf/tran-prf.dat, _processing/extracted/s0010218017304637_mmc1/supplement/propane/tran-propane.dat, _processing/extracted/s0010218017304637_mmc1/supplement/methane/transport_methane.dat, _processing/extracted/s0010218017304637_mmc1/supplement/nheptane/tran-nc7h16.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 27
- Reaction count: 155
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: 27
- Reaction count: 155
- Message: InputError: No thermo data found for species 'AR' No thermo data found for species 'H' No thermo data found for species 'H2' No thermo data found for species 'N' No thermo data found for species 'N2' No thermo data found for species 'NH3' No thermo data found for species 'NH2' No thermo data found for species 'NH' No thermo data found for species 'NNH' No thermo data found for species 'N2H2' No thermo data found for species 'N2H3' No thermo data found for species 'N2H4' No thermo data found for species 'H2NN' No transport data for species 'N'. No transport data for species 'NH3'. No transport data for species 'NH2'. No transport data for species 'NH'. No transport data for species 'NNH'. No transport data for species 'N2H2'. No transport data for species 'N2H3'. No transport data for speci ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 3

- Status: cantera_failed
- Species count: 27
- Reaction count: 155
- Message: InputError: No thermo data found for species 'H2' No thermo data found for species 'H' No thermo data found for species 'O' No thermo data found for species 'O2' No thermo data found for species 'OH' No thermo data found for species 'H2O' No thermo data found for species 'HO2' No thermo data found for species 'H2O2' No thermo data found for species 'CH2' No thermo data found for species 'CH2*' No thermo data found for species 'CH3' No thermo data found for species 'CH4' No thermo data found for species 'CO' No thermo data found for species 'CO2' No thermo data found for species 'HCO' No thermo data found for species 'CH2O' No thermo data found for species 'CH3O' No thermo data found for species 'C2H2' No thermo data found for species 'C2H3' No thermo data found for species 'C2H4' No thermo ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 4

- Status: cantera_failed
- Species count: 27
- Reaction count: 155
- Message: missing cantera result json
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 5

- Status: cantera_failed
- Species count: 27
- Reaction count: 155
- Message: InputError: Error while reading reaction in chem.inp starting on line 162: """ CH3O(+M)<=>CH2O+H(+M) 6.8000E+13 0.000 2.6170E+04 ! 61 LOW/ 1.8670E+25 -3.000 2.4307E+04 / TROE/ 0.9000 2500. 1300. 0.1000+100 / H2/ 2.00/ H2O/ 6.00/ CO/ 1.50/ CO2/ 2.00/ CH4/ 2.00/ C2H6/ 3.00/ """ could not convert string to float: '0.1000+100' Ignoring redundant thermo data for species 'NC3H7COCH2' starting on line 3505 of therm.dat. Ignoring redundant thermo data for species 'C5H10-1' starting on line 3533 of therm.dat. Ignoring redundant thermo data for species 'C5H91-4' starting on line 3549 of therm.dat. Ignoring redundant thermo data for species 'NC4H9CHO' starting on line 3577 of therm.dat. Ignoring redundant thermo data for species 'NC4H9CO' starting on line 3581 of therm.dat. Suppressed 6 additional wa ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 6

- Status: cantera_failed
- Species count: 27
- Reaction count: 155
- Message: missing cantera result json
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 7

- Status: cantera_failed
- Species count: 27
- Reaction count: 155
- Message: InputError: No thermo data found for species 'H2' No thermo data found for species 'H' No thermo data found for species 'O' No thermo data found for species 'O2' No thermo data found for species 'OH' No thermo data found for species 'H2O' No thermo data found for species 'HO2' No thermo data found for species 'H2O2' No thermo data found for species 'CH2' No thermo data found for species 'CH2*' No thermo data found for species 'CH3' No thermo data found for species 'CH4' No thermo data found for species 'CO' No thermo data found for species 'CO2' No thermo data found for species 'HCO' No thermo data found for species 'CH2O' No thermo data found for species 'CH3O' No thermo data found for species 'C2H2' No thermo data found for species 'C2H3' No thermo data found for species 'C2H4' No thermo ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 8

- Status: cantera_failed
- Species count: 27
- Reaction count: 155
- Message: InputError: Ignoring redundant thermo data for species 'naphthalene' starting on line 1082 of chem.inp. Unparsable lines while reading thermo data in chem.inp starting on line 563: """ !coefficients de CHEMKIn a haute temperature et THERGAS a basse temperature! """ Lines could not be parsed as a NASA7 entry. Error while reading reaction in chem.inp starting on line 4265: """ iC4H8+R2OH=>iC4H7+H2O 6.0D+06 2.000 -298.0 ! MES 878<C.M.>!(idem RF) """ could not convert string to float: '6.0D+06' Error while reading reaction in chem.inp starting on line 4436: """ C5H9#=C5H9 2.0D+14 0.005 35600.0 !SIRJEAN05 """ could not convert string to float: '2.0D+14' Error while reading reaction in chem.inp starting on line 4437: """ C5H9=C3H5Y+C2H4Z 3.3D+13 0.000 22500.0 ! EXGAS """ could not convert string ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 9

- Status: cantera_failed
- Species count: 27
- Reaction count: 155
- Message: InputError: Error while reading reaction in chem.inp starting on line 2: """ C2H5CN+CH2CN=NCCH2CN+C2H5 1.77E+09 0.805 24190.95 PLOG / 1.31E-04 2.35E+04 2.197 21164.95 / PLOG / 1.31E-03 3.31E+04 2.154 21245.83 / PLOG / 1.00E+00 1.77E+09 0.805 24190.95 / PLOG / 1.00E+01 1.94E+11 0.277 26551.64 / PLOG / 1.00E+02 1.14E+07 1.612 26774.06 / """ Unexpected token 'C2H5CN+CH2CN' in reaction expression 'C2H5CN+CH2CN=NCCH2CN+C2H5'. May be due to undeclared species 'C2H5CNCH2CN'. Error while reading reaction in chem.inp starting on line 9: """ C2H5CN+CH2CN=CH3CN+CH2CH2CN 1.34E-04 4.915 13067.54 """ Unexpected token 'C2H5CN+CH2CN' in reaction expression 'C2H5CN+CH2CN=CH3CN+CH2CH2CN'. May be due to undeclared species 'C2H5CNCH2CN'. Error while reading reaction in chem.inp starting on line 10: """ C2H5CN ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S0010218021004375_mmc1.docx
- extracted S0010218018305376_mmc1.docx
- extracted S0010218025006376_mmc1.docx
- extracted S0010218026000374_mmc1.docx
- extracted S0010218025006637_mmc1.zip
- extracted S0010218025006376_mmc2.zip
- extracted S0010218018301937_mmc1.zip
- extracted S0010218021004375_mmc2.xlsx
- extracted S001021801300237X_mmc1.zip
- extracted S0010218017304637_mmc1.zip
- extracted S0010218010003767_mmc1.zip
