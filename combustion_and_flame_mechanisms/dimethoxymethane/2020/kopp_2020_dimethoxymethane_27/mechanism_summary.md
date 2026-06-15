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
- Original mechanism source files: _processing/raw_downloads/S0010218025003827_mmc1.txt, _processing/raw_downloads/S0010218024000427_mmc4.txt, _processing/extracted/s0010218023003127_mmc3/mmc3.inp, _processing/extracted/s0010218023004327_mmc5/NC_Mechanism/NC_Mech_Paper.inp, _processing/extracted/s0010218023005527_mmc2/mmc2.inp, _processing/extracted/s0010218025004274_mmc2/mech.inp, _processing/extracted/s0010218024006278_mmc3/NH3_syngas mech.inp
- Original thermodynamic source files: _processing/raw_downloads/S0010218025003827_mmc7.txt, _processing/raw_downloads/S0010218024000427_mmc6.txt, _processing/extracted/s0010218024006278_mmc1/NH3_syngas thermo.dat, _processing/extracted/s0010218023003127_mmc1/mmc1.dat, _processing/extracted/s0010218023005527_mmc3/mmc3.dat, _processing/extracted/s0010218023004327_mmc5/NC_Mechanism/NC_Thermo_Paper.dat, _processing/extracted/s0010218025004274_mmc2/thermo.dat
- Original transport source files: _processing/extracted/s0010218024006278_mmc4/NH3_syngas trans.txt, _processing/extracted/s0010218023005527_mmc4/mmc4.dat, _processing/extracted/s0010218023003127_mmc2/mmc2.TRAN, _processing/extracted/s0010218025004274_mmc2/trans.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 33
- Reaction count: 228
- Message: InputError: No transport data for species 'Ar'. No transport data for species 'He'. No transport data for species 'C2H2O'. No transport data for species 'C2H2O2(7)'. No transport data for species 'C2H2O2(65)'. No transport data for species 'C2H3O2(59)'. No transport data for species 'C2H4O'. No transport data for species 'C2H3O'. No transport data for species 'C2H3O2(66)'. No transport data for species 'C2H2O4'. No transport data for species 'C3H4O2'. No transport data for species 'C4H5O3'. No transport data for species 'C4H6O3'. No transport data for species 'S(3)'. No transport data for species 'S(8)'. No transport data for species 'S(10)'. No transport data for species 'S(11)'. No transport data for species 'S(32)'. No transport data for species 'S(50)'. No transport data for species 'S ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: 33
- Reaction count: 228
- Message: InputError: Ignoring redundant declaration for species 'CH2(S)' Ignoring redundant declaration for species 'C' Ignoring redundant declaration for species 'CH3OH' Ignoring redundant declaration for species 'CH2OH' Ignoring redundant declaration for species 'CH3OOH' Suppressed 7 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Unparsable lines while reading thermo data in therm.dat starting on line 184: """ ! ******************************************************************************** ! ******************************************************************************** ! ***** H2 O2 O3 H O OH OH* HO2 H2O H2O2 ! ******************************************************************************** ! *********************** ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 3

- Status: cantera_failed
- Species count: 33
- Reaction count: 228
- Message: InputError: Ignoring redundant declaration for species 'CH3NCO' Ignoring redundant declaration for species 'OCNCHO' Error while reading section in chem.inp starting on line 141: """ REACTIONS MOLES CAL/MOLE MAXSP=8 """ Unrecognized token 'MAXSP=8' on REACTIONS line Error while reading reaction in chem.inp starting on line 880: """ H+CH3N(CO)CHO=(CHO)2NCH3 1E14 0.00E 0.00 """ could not convert string to float: '0.00E' Error while reading reaction in chem.inp starting on line 882: """ H+(CHO)2NCH2=(CHO)2NCH3 1E14 0.00E 0.00 """ could not convert string to float: '0.00E' Error while reading reaction in chem.inp starting on line 3984: """ CH2NCH2OOH=CH2NCHO+H2O +1.48E+016 -1.12E+000 +4.59493E+004 ! PLOG / +1.00E-2 +1.990+50 -1.270+01 +5.35319E+4 / PLOG / +1.00E-1 +4.720+47 -1.150+01 +5.43609E+ ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 4

- Status: cantera_failed
- Species count: 33
- Reaction count: 228
- Message: InputError: Ignoring redundant declaration for species 'CH3COH' Unparsable lines while reading thermo data in therm.dat starting on line 184: """ ! ******************************************************************************** ! ******************************************************************************** ! ***** H2 O2 O3 H O OH OH* HO2 H2O H2O2 ! ******************************************************************************** ! ******************************************************************************** ! ! H2 (g) ATcT ver. 1.122, DHf298 = 0.000 0.000 kJ/mol - fit JAN17 """ Lines could not be parsed as a NASA7 entry. No thermo data found for species 'OHV' No thermo data found for species 'CH3O2H' No thermo data found for species 'CH3O2' No thermo data found for species 'CH2O2H' N ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 5

- Status: ok
- Species count: 33
- Reaction count: 228
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
- extracted S0010218025002706_mmc1.zip
- extracted S0010218024000427_mmc5.docx
- extracted S0010218023003127_mmc7.docx
- extracted S0010218023005527_mmc4.zip
- extracted S001021802400227X_mmc1.zip
- extracted S0010218023003127_mmc1.zip
- extracted S0010218023005527_mmc3.zip
- extracted S0010218023004327_mmc5.zip
- extracted S0010218024000427_mmc2.xlsx
- extracted S0010218023003127_mmc4.xlsx
- extracted S0010218023004327_mmc1.docx
- extracted S0010218024006278_mmc4.zip
- extracted S0010218023003127_mmc2.zip
- extracted S0010218023003127_mmc3.zip
- extracted S0010218023004327_mmc3.docx
- extracted S0010218024006278_mmc3.zip
- extracted S0010218023002274_mmc1.docx
- extracted S0010218025004274_mmc2.zip
- extracted S0010218023004327_mmc4.docx
- extracted S0010218025003827_mmc4.xlsx
- extracted S0010218024000427_mmc1.xlsx
- extracted S0010218024006278_mmc1.zip
- extracted S0010218024000270_mmc2.xlsx
- extracted S0010218024000427_mmc3.xlsx
- extracted S0010218024000270_mmc3.xlsx
- extracted S0010218024000270_mmc1.zip
- extracted S0010218025003827_mmc2.xlsx
- extracted S0010218025003827_mmc3.xlsx
- extracted S0010218023003127_mmc5.xlsx
- extracted S0010218024002773_mmc1.docx
- extracted S0010218023005527_mmc1.xlsx
- extracted S0010218024006278_mmc2.docx
- extracted S0010218023004327_mmc2.docx
- extracted S0010218024006278_mmc5.xlsx
- extracted S0010218023005527_mmc2.zip
