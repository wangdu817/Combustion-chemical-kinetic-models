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
- Original mechanism source files: _processing/raw_downloads/S0010218021004375_mmc4.txt, _processing/raw_downloads/S0010218024003237_mmc4.txt, _processing/extracted/s0010218019305371_mmc3/mmc3.inp, _processing/extracted/s0010218025003797_mmc5/SM_5_Kinetic.mech, _processing/extracted/s0010218020304375_mmc3/CPT-DME.inp, _processing/extracted/s0010218023003735_mmc1/mmc1.cti, _processing/extracted/s0010218023003437_mmc2/HUST-DMM_2.inp, _processing/extracted/s0010218023003760_mmc1/chem.inp, _processing/extracted/s0010218023003735_mmc2/mmc2.mech, _processing/extracted/s001021802200373x_mmc2/Chem.inp
- Original thermodynamic source files: _processing/raw_downloads/S0010218022003741_mmc2.txt, _processing/raw_downloads/S0010218024003237_mmc5.txt, _processing/raw_downloads/S0010218021004375_mmc3.txt, _processing/extracted/s0010218023003437_mmc3/HUST-DMM_therm.dat, _processing/extracted/s0010218020304375_mmc3/CPT-DME.dat, _processing/extracted/s0010218023003735_mmc1/mmc1.cti, _processing/extracted/s0010218023003760_mmc1/therm.dat, _processing/extracted/s0010218023003760_mmc1/chem.inp, _processing/extracted/s001021802200373x_mmc1/Therm.dat, _processing/extracted/s0010218025003797_mmc6/SM_6_Therm.dat, _processing/extracted/s0010218023003735_mmc3/mmc3.therm, _processing/extracted/s0010218019305371_mmc4/mmc4.dat
- Original transport source files: _processing/raw_downloads/S0010218024003237_mmc3.txt, _processing/extracted/s0010218023003437_mmc4/HUST-DMM_trans.dat, _processing/extracted/s0010218023003735_mmc4/mmc4.tran, _processing/extracted/s0010218020304375_mmc3/CPT-DME.tran.dat, _processing/extracted/s0010218025003797_mmc7/SM_7_Tran.dat, _processing/extracted/s0010218019305371_mmc5/mmc5.dat, _processing/extracted/s0010218023003735_mmc1/mmc1.cti, _processing/extracted/s0010218023003760_mmc1/tran.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 78
- Reaction count: 900
- Message: InputError: Issue while reading reaction in chem.inp starting on line 157: """ OHEX<=>OH+HV 1.450E+06 0.0000 0.00 """ Found a reversible reaction containing a product photon. Converting to an irreversible reaction with the photon removed. Unparsable lines while reading thermo data in therm.dat starting on line 7147: """ CYC5H9 H 9C 5 0 0g 300.00 5000.00 1000.00 1 9.32131576E+00 2.89863850E-02-1.13280072E-05 2.02719921E-09-1.36385473E-13 2 8.06562846E+03-2.81238834E+01-3.40380867E+00 5.34723969E-02-1.16451511E-05 3 C5H6-L H 6C 5 G 300.00 5000.00 1372.00 1 1.29600892E+01 1.48953758E-02-5.23622902E-06 8.27916389E-10-4.86464523E-14 2 2.38180800E+04-4.25312093E+01 3.58448213E+00 3.24459626E-02-1.70150991E-05 3 4.22715914E-09-4.18452556E-13 2.76514681E+04 9.60644208E+00 4 """ Lines could not be ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: 78
- Reaction count: 900
- Message: InputError: Unparsable lines while reading thermo data in therm.dat starting on line 7147: """ CYC5H9 H 9C 5 0 0g 300.00 5000.00 1000.00 1 9.32131576E+00 2.89863850E-02-1.13280072E-05 2.02719921E-09-1.36385473E-13 2 8.06562846E+03-2.81238834E+01-3.40380867E+00 5.34723969E-02-1.16451511E-05 3 C5H6-L H 6C 5 G 300.00 5000.00 1372.00 1 1.29600892E+01 1.48953758E-02-5.23622902E-06 8.27916389E-10-4.86464523E-14 2 2.38180800E+04-4.25312093E+01 3.58448213E+00 3.24459626E-02-1.70150991E-05 3 4.22715914E-09-4.18452556E-13 2.76514681E+04 9.60644208E+00 4 """ Lines could not be parsed as a NASA7 entry. No thermo data found for species 'CH2CH2O-2OOH' No thermo data found for species 'CY(CCO)OH' No thermo data found for species 'CH2CHOH-2OOH' No thermo data found for species 'CH3CHOH-1O2' No thermo data ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 3

- Status: cantera_failed
- Species count: 78
- Reaction count: 900
- Message: InputError: Unparsable lines while reading thermo data in therm.dat starting on line 7147: """ CYC5H9 H 9C 5 0 0g 300.00 5000.00 1000.00 1 9.32131576E+00 2.89863850E-02-1.13280072E-05 2.02719921E-09-1.36385473E-13 2 8.06562846E+03-2.81238834E+01-3.40380867E+00 5.34723969E-02-1.16451511E-05 3 C5H6-L H 6C 5 G 300.00 5000.00 1372.00 1 1.29600892E+01 1.48953758E-02-5.23622902E-06 8.27916389E-10-4.86464523E-14 2 2.38180800E+04-4.25312093E+01 3.58448213E+00 3.24459626E-02-1.70150991E-05 3 4.22715914E-09-4.18452556E-13 2.76514681E+04 9.60644208E+00 4 """ Lines could not be parsed as a NASA7 entry. No thermo data found for species 'CH2OHCHO' No thermo data found for species 'O2C2H4O2H' No thermo data found for species 'C3H6O' No thermo data found for species 'HOC3H6O2' No thermo data found for spe ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 4

- Status: cantera_failed
- Species count: 78
- Reaction count: 900
- Message: InputError: Unparsable lines while reading thermo data in therm.dat starting on line 7147: """ CYC5H9 H 9C 5 0 0g 300.00 5000.00 1000.00 1 9.32131576E+00 2.89863850E-02-1.13280072E-05 2.02719921E-09-1.36385473E-13 2 8.06562846E+03-2.81238834E+01-3.40380867E+00 5.34723969E-02-1.16451511E-05 3 C5H6-L H 6C 5 G 300.00 5000.00 1372.00 1 1.29600892E+01 1.48953758E-02-5.23622902E-06 8.27916389E-10-4.86464523E-14 2 2.38180800E+04-4.25312093E+01 3.58448213E+00 3.24459626E-02-1.70150991E-05 3 4.22715914E-09-4.18452556E-13 2.76514681E+04 9.60644208E+00 4 """ Lines could not be parsed as a NASA7 entry. No thermo data found for species 'OH*' No thermo data found for species 'CH*' No thermo data found for species 'C3H6OOH2-2' No thermo data found for species 'C3H6OH' No thermo data found for species 'HO ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 5

- Status: cantera_failed
- Species count: 78
- Reaction count: 900
- Message: CanteraError: ******************************************************************************* CanteraError thrown by newSolution: The CTI and XML formats are no longer supported. *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 6

- Status: cantera_failed
- Species count: 78
- Reaction count: 900
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 1430 and 3481 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/unknown_fuel/2020/ninnemann_2020_unknown_fuel_37/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 <=> O + OH Reaction 451: H + O2 <=> O + OH | Line | | 1425 | diameter: 3.63 | 1426 | rotational-relaxation: 1.0 | 1427 | note: OIS | 1428 | | 1429 | reactions: > 1430 > - equation: H + O2 <=> O + OH # Reaction 1 ^ | 1431 | rate-constant: {A: 3.547e+15, b: -0.406, Ea: 1.6599e+04} | 1432 | note: |2 | 1433 | H2/O2 mechanism of Li et al. IJCK 36:565 (2004) ... | 3476 | 1 atm | 3477 | - equation: CH2NH + O <=> CH2O + NH ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 7

- Status: cantera_failed
- Species count: 78
- Reaction count: 900
- Message: InputError: Unparsable lines while reading thermo data in therm.dat starting on line 7147: """ CYC5H9 H 9C 5 0 0g 300.00 5000.00 1000.00 1 9.32131576E+00 2.89863850E-02-1.13280072E-05 2.02719921E-09-1.36385473E-13 2 8.06562846E+03-2.81238834E+01-3.40380867E+00 5.34723969E-02-1.16451511E-05 3 C5H6-L H 6C 5 G 300.00 5000.00 1372.00 1 1.29600892E+01 1.48953758E-02-5.23622902E-06 8.27916389E-10-4.86464523E-14 2 2.38180800E+04-4.25312093E+01 3.58448213E+00 3.24459626E-02-1.70150991E-05 3 4.22715914E-09-4.18452556E-13 2.76514681E+04 9.60644208E+00 4 """ Lines could not be parsed as a NASA7 entry. No thermo data found for species 'N' No thermo data found for species 'NH3' No thermo data found for species 'NH2' No thermo data found for species 'NH' No thermo data found for species 'NNH' No thermo ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 8

- Status: cantera_failed
- Species count: 78
- Reaction count: 900
- Message: InputError: Unparsable lines while reading thermo data in therm.dat starting on line 7147: """ CYC5H9 H 9C 5 0 0g 300.00 5000.00 1000.00 1 9.32131576E+00 2.89863850E-02-1.13280072E-05 2.02719921E-09-1.36385473E-13 2 8.06562846E+03-2.81238834E+01-3.40380867E+00 5.34723969E-02-1.16451511E-05 3 C5H6-L H 6C 5 G 300.00 5000.00 1372.00 1 1.29600892E+01 1.48953758E-02-5.23622902E-06 8.27916389E-10-4.86464523E-14 2 2.38180800E+04-4.25312093E+01 3.58448213E+00 3.24459626E-02-1.70150991E-05 3 4.22715914E-09-4.18452556E-13 2.76514681E+04 9.60644208E+00 4 """ Lines could not be parsed as a NASA7 entry. No thermo data found for species 'MIPK' No thermo data found for species 'MIPKR4' No thermo data found for species 'MIPKR3' No thermo data found for species 'MIPKR1' No thermo data found for species 'MI ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 9

- Status: cantera_failed
- Species count: 78
- Reaction count: 900
- Message: InputError: Unparsable lines while reading thermo data in therm.dat starting on line 7147: """ CYC5H9 H 9C 5 0 0g 300.00 5000.00 1000.00 1 9.32131576E+00 2.89863850E-02-1.13280072E-05 2.02719921E-09-1.36385473E-13 2 8.06562846E+03-2.81238834E+01-3.40380867E+00 5.34723969E-02-1.16451511E-05 3 C5H6-L H 6C 5 G 300.00 5000.00 1372.00 1 1.29600892E+01 1.48953758E-02-5.23622902E-06 8.27916389E-10-4.86464523E-14 2 2.38180800E+04-4.25312093E+01 3.58448213E+00 3.24459626E-02-1.70150991E-05 3 4.22715914E-09-4.18452556E-13 2.76514681E+04 9.60644208E+00 4 """ Lines could not be parsed as a NASA7 entry. No thermo data found for species 'CH3OCH3-DME' No thermo data found for species 'N' No thermo data found for species 'NO' No thermo data found for species 'N2O' No thermo data found for species 'NO2' No ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 10

- Status: cantera_failed
- Species count: 78
- Reaction count: 900
- Message: InputError: Ignoring redundant declaration for species 'O2CHO' Ignoring redundant declaration for species 'C2H5O2' Ignoring redundant declaration for species 'C2H4O2H' Ignoring redundant declaration for species 'C2H3O1-2' Ignoring redundant declaration for species 'CH2OCHO' Suppressed 92 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Error while reading reaction in chem.inp starting on line 7618: """ H+O2(+M)=HO2(+M) 4.66E12 0.44 0.0E0 !\Author: SP !\Ref: TROE, PROCI Volume 28, Issue 2, 2000, 1463-1469 / PCCP FERNANDES 2008 HE/1.0/ AR/0.0/ N2/1.0/ O2/1.0/ H2/2.0/ CH4/2.0/ CO2/3.25/ H2O/17.6/ CO/4.0/ LOWMX / 4.0662E19 -1.4E0 -1.80537E2 / TROEMX / 5.0E-1 1.0E0 1.0E10 1.0E30 / LOWSP / N2 1.91E+20 -1.5568 253.86 / !Y ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S0010218021004375_mmc2.xlsx
- extracted S0010218025003797_mmc3.docx
- extracted S0010218025003797_mmc6.zip
- extracted S0010218023003735_mmc1.zip
- extracted S0010218024003237_mmc2.xlsx
- extracted S0010218025003797_mmc2.xlsx
- extracted S0010218023003437_mmc3.zip
- extracted S0010218020304375_mmc1.docx
- extracted S001021802200373X_mmc1.zip
- extracted S0010218021004375_mmc1.docx
- extracted S0010218023003437_mmc2.zip
- extracted S0010218020304375_mmc2.zip
- extracted S0010218025003797_mmc1.docx
- extracted S0010218023003437_mmc1.docx
- extracted S0010218020304375_mmc3.zip
- extracted S0010218019305371_mmc5.zip
- extracted S0010218025003797_mmc5.zip
- extracted S0010218019305371_mmc2.xlsx
- extracted S0010218024003237_mmc1.docx
- extracted S0010218023003735_mmc2.zip
- extracted S0010218019305371_mmc3.zip
- extracted S0010218025003797_mmc8.zip
- extracted S0010218023003760_mmc1.zip
- extracted S0010218022003741_mmc1.docx
- extracted S0010218019305371_mmc4.zip
- extracted S0010218025003797_mmc7.zip
- extracted S0010218023003735_mmc3.zip
- extracted S0010218023003437_mmc4.zip
- extracted S0010218023003735_mmc4.zip
- extracted S001021802200373X_mmc2.zip
- extracted S0010218025003797_mmc4.xlsx
