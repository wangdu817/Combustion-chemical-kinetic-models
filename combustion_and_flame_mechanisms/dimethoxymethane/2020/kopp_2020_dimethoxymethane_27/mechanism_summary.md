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
- Plasma-related mechanism: possible
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S0010218025003827_mmc1.txt, _processing/raw_downloads/S0010218024000427_mmc4.txt, _processing/extracted/s001021802100273x_mmc3/SMM3. Kinetic Mechanism Cantera.cti, _processing/extracted/s0010218021002777_mmc1/chem.inp, _processing/extracted/s0010218023003127_mmc3/mmc3.inp, _processing/extracted/s0010218021007227_mmc3/naphtha mechanism.inp, _processing/extracted/s001021802100273x_mmc4/SMM4. Kinetic Mechanism CHEMKIN.inp, _processing/extracted/s0010218023004327_mmc5/NC_Mechanism/NC_Mech_Paper.inp, _processing/extracted/s0010218023005527_mmc2/mmc2.inp, _processing/extracted/s0010218025004274_mmc2/mech.inp, _processing/extracted/s0010218024006278_mmc3/NH3_syngas mech.inp
- Original thermodynamic source files: _processing/raw_downloads/S0010218025003827_mmc7.txt, _processing/raw_downloads/S0010218024000427_mmc6.txt, _processing/extracted/s001021802100273x_mmc5/SMM5. Thermodynamic Data.dat, _processing/extracted/s0010218024006278_mmc1/NH3_syngas thermo.dat, _processing/extracted/s001021802100273x_mmc3/SMM3. Kinetic Mechanism Cantera.cti, _processing/extracted/s0010218023003127_mmc1/mmc1.dat, _processing/extracted/s0010218021002777_mmc1/therm.dat, _processing/extracted/s0010218021007227_mmc3/naphtha mechanism.inp, _processing/extracted/s0010218023005527_mmc3/mmc3.dat, _processing/extracted/s0010218023004327_mmc5/NC_Mechanism/NC_Thermo_Paper.dat, _processing/extracted/s0010218025004274_mmc2/thermo.dat
- Original transport source files: _processing/extracted/s001021802100273x_mmc6/SMM6. Transport Data.dat, _processing/extracted/s001021802100273x_mmc3/SMM3. Kinetic Mechanism Cantera.cti, _processing/extracted/s0010218024006278_mmc4/NH3_syngas trans.txt, _processing/extracted/s0010218023005527_mmc4/mmc4.dat, _processing/extracted/s0010218021002777_mmc1/tran.dat, _processing/extracted/s0010218023003127_mmc2/mmc2.TRAN, _processing/extracted/s0010218025004274_mmc2/trans.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 94
- Reaction count: 389
- Message: CanteraError: ******************************************************************************* CanteraError thrown by newSolution: The CTI and XML formats are no longer supported. *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: 94
- Reaction count: 389
- Message: InputError: Error while reading reaction in chem.inp starting on line 10764: """ PERYCH3(+M)=PERY-+CH3(+M) 1.95E27 -3.16 1.07447E5 LOW/1.0E98 -2.2966E1 1.2208E5/ TROE/7.054562E-1 9.999989E9 4.59918E2 8.213938E9/ """ Unparsable line: '-----------------------------------------------------------'. Unparsable lines while reading thermo data in therm.dat starting on line 184: """ ! ******************************************************************************** ! ******************************************************************************** ! ***** H2 O2 O3 H O OH OH* HO2 H2O H2O2 ! ******************************************************************************** ! ******************************************************************************** ! ! H2 (g) ATcT ver. 1.122, DHf298 = 0.000 0.000 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 3

- Status: cantera_failed
- Species count: 94
- Reaction count: 389
- Message: InputError: Ignoring redundant declaration for species 'NC12H26' Ignoring redundant declaration for species 'C12H25-1' Ignoring redundant declaration for species 'C12H25-2' Ignoring redundant declaration for species 'C12H25-3' Ignoring redundant declaration for species 'C12H25-4' Suppressed 2786 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Ignoring redundant thermo data for species 'NC12H26' starting on line 571 of therm.dat. Ignoring redundant thermo data for species 'C12H25-1' starting on line 575 of therm.dat. Ignoring redundant thermo data for species 'C12H25-2' starting on line 579 of therm.dat. Ignoring redundant thermo data for species 'C12H25-3' starting on line 583 of therm.dat. Ignoring redundant ther ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 4

- Status: cantera_failed
- Species count: 94
- Reaction count: 389
- Message: InputError: No transport data for species 'Ar'. No transport data for species 'He'. No transport data for species 'C2H2O'. No transport data for species 'C2H2O2(7)'. No transport data for species 'C2H2O2(65)'. No transport data for species 'C2H3O2(59)'. No transport data for species 'C2H4O'. No transport data for species 'C2H3O'. No transport data for species 'C2H3O2(66)'. No transport data for species 'C2H2O4'. No transport data for species 'C3H4O2'. No transport data for species 'C4H5O3'. No transport data for species 'C4H6O3'. No transport data for species 'S(3)'. No transport data for species 'S(8)'. No transport data for species 'S(10)'. No transport data for species 'S(11)'. No transport data for species 'S(32)'. No transport data for species 'S(50)'. No transport data for species 'S ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 5

- Status: cantera_failed
- Species count: 94
- Reaction count: 389
- Message: InputError: Ignoring redundant declaration for species 'CH2(S)' Ignoring redundant declaration for species 'C' Ignoring redundant declaration for species 'CH3OH' Ignoring redundant declaration for species 'CH2OH' Ignoring redundant declaration for species 'CH3OOH' Suppressed 7 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Unparsable lines while reading thermo data in therm.dat starting on line 184: """ ! ******************************************************************************** ! ******************************************************************************** ! ***** H2 O2 O3 H O OH OH* HO2 H2O H2O2 ! ******************************************************************************** ! *********************** ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 6

- Status: cantera_failed
- Species count: 94
- Reaction count: 389
- Message: InputError: Ignoring redundant declaration for species 'CH3NCO' Ignoring redundant declaration for species 'OCNCHO' Error while reading section in chem.inp starting on line 141: """ REACTIONS MOLES CAL/MOLE MAXSP=8 """ Unrecognized token 'MAXSP=8' on REACTIONS line Error while reading reaction in chem.inp starting on line 880: """ H+CH3N(CO)CHO=(CHO)2NCH3 1E14 0.00E 0.00 """ could not convert string to float: '0.00E' Error while reading reaction in chem.inp starting on line 882: """ H+(CHO)2NCH2=(CHO)2NCH3 1E14 0.00E 0.00 """ could not convert string to float: '0.00E' Error while reading reaction in chem.inp starting on line 3984: """ CH2NCH2OOH=CH2NCHO+H2O +1.48E+016 -1.12E+000 +4.59493E+004 ! PLOG / +1.00E-2 +1.990+50 -1.270+01 +5.35319E+4 / PLOG / +1.00E-1 +4.720+47 -1.150+01 +5.43609E+ ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 7

- Status: ok
- Species count: 94
- Reaction count: 389
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S0010218023003127_mmc6.xlsx
- extracted S0010218025003827_mmc5.xlsx
- extracted S0010218024000427_mmc5.docx
- extracted S0010218023003127_mmc7.docx
- extracted S0010218023005527_mmc4.zip
- extracted S0010218023003127_mmc1.zip
- extracted S0010218023005527_mmc3.zip
- extracted S0010218023004327_mmc5.zip
- extracted S001021802100273X_mmc4.zip
- extracted S0010218024000427_mmc2.xlsx
- extracted S001021802100273X_mmc3.zip
- extracted S0010218023003127_mmc4.xlsx
- extracted S0010218023004327_mmc1.docx
- extracted S0010218021007227_mmc2.xlsx
- extracted S0010218024006278_mmc4.zip
- extracted S0010218021007227_mmc1.docx
- extracted S0010218023003127_mmc2.zip
- extracted S0010218023003127_mmc3.zip
- extracted S0010218023004327_mmc3.docx
- extracted S0010218024006278_mmc3.zip
- extracted S0010218025004274_mmc2.zip
- extracted S0010218021007227_mmc3.zip
- extracted S0010218023004327_mmc4.docx
- extracted S001021802100273X_mmc6.zip
- extracted S0010218025003827_mmc4.xlsx
- extracted S0010218024000427_mmc1.xlsx
- extracted S0010218021002777_mmc1.zip
- extracted S0010218024006278_mmc1.zip
- extracted S001021802100273X_mmc5.zip
- extracted S0010218024000427_mmc3.xlsx
- extracted S0010218025003827_mmc2.xlsx
- extracted S0010218025003827_mmc3.xlsx
- extracted S0010218023003127_mmc5.xlsx
- extracted S001021802100273X_mmc1.xlsx
- extracted S0010218023005527_mmc1.xlsx
- extracted S0010218024006278_mmc2.docx
- extracted S0010218023004327_mmc2.docx
- extracted S0010218024006278_mmc5.xlsx
- extracted S0010218023005527_mmc2.zip
