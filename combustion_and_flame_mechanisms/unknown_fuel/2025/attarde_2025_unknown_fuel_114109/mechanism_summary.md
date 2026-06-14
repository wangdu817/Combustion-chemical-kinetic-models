# Modeling and validation: A comprehensive and robust surrogate kinetic model for oxidation of various biodiesels

## Bibliography

Lalit Y. Attarde, Krithika Narayanaswamy. Modeling and validation: A comprehensive and robust surrogate kinetic model for oxidation of various biodiesels[J]. Combustion and Flame, 2025, 276: 114109. DOI: 10.1016/j.combustflame.2025.114109.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 276 / June
- Article number: 114109
- DOI: 10.1016/j.combustflame.2025.114109
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025001476
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025001476/pdfft?md5=c01511bab4466fff560bf8b90db727f5&pid=1-s2.0-S0010218025001476-main.pdf
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218025001476_mmc1/Biodiesel_surrogates.inp, _processing/extracted/s0010218025001476_mmc2/dodecane.inp
- Original thermodynamic source files: _processing/extracted/s0010218025001476_mmc5/surrogate_therm.dat
- Original transport source files: _processing/extracted/s0010218025001476_mmc6/surrogate_trans.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 429: """ H+O2(+M)=HO2(+M) 4.66E12 0.44 0.0E0 HE/0.57/ N2/1.0/ AR/0.65/ O2/1.0/ H2/2.0/ CH4/2.0/ CO2/3.25/ H2O/17.6/ CO/4.0/ LOWMX/1.225E19 -1.2E0 0.0E0/ TROEMX/5.0E-1 1.0E0 1.0E10 1.0E30/ LOWSP/N2 4.5E20 -1.73E0 0.0E0/ TROESP/N2 5.0E-1 1.0E0 1.0E10 1.0E30/ """ could not convert string to float: 'N2' Please check https://cantera.org/stable/userguide/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files for the correct Chemkin syntax.; numeric cleanup retry failed: InputError: Error while reading reaction in chem_cantera_numeric_clean.inp starting on line 416: """ H+O2(+M)=HO2(+M) 4.66E12 0.44 0.0E0 HE/0.57/ N2/1.0/ AR/0.65/ O2/1.0/ H2/2.0/ CH4/2.0/ CO2/3.25/ H2O/17.6/ CO/4.0/ LOWMX/1.225E19 -1.2E0 0.0E0/ TROEMX/5.0E-1 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 378: """ H+O2(+M)=HO2(+M) 4.66E12 0.44 0.0E0 HE/0.57/ N2/1.0/ AR/0.65/ O2/1.0/ H2/2.0/ CH4/2.0/ CO2/3.25/ H2O/17.6/ CO/4.0/ LOWMX/1.225E19 -1.2E0 0.0E0/ TROEMX/5.0E-1 1.0E0 1.0E10 1.0E30/ LOWSP/N2 4.5E20 -1.73E0 0.0E0/ TROESP/N2 5.0E-1 1.0E0 1.0E10 1.0E30/ """ could not convert string to float: 'N2' Error while reading reaction in chem.inp starting on line 26428: """ C12H25-1+O2=C12H24-1+HO2 3.29E-13 7.45E+00 6.82E+03 ! Duan 2020 HR1+O2 PS13 PLOG/1.0E-2 4.95E+20 -2.09E+00 1.42E+04/ PLOG/1.0E-1 4.17E+07 1.93E+00 1.13E+04/ PLOG/1.0E 2.90E-05 5.55E+00 8.28E+03/ PLOG/1.0E1 3.17E-10 6.83E+00 7.34E+03/ PLOG/1.0E2 3.29E-13 7.45E+00 6.82E+03/ """ could not convert string to float: '1.0E' Error while reading reaction in chem.inp ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S0010218025001476_mmc4.zip
- extracted S0010218025001476_mmc2.zip
- extracted S0010218025001476_mmc1.zip
- extracted S0010218025001476_mmc6.zip
- extracted S0010218025001476_mmc5.zip
