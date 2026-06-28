# An experimental and kinetic modeling study of ethyl tert-butyl ether. Part I: High-temperature pyrolysis and oxidation chemistry

## Bibliography

Jiaxin Liu, Jin-Tao Chen, Maryam Khan-Ghauri, Joseph E. Jacobs, ... Henry J. Curran. An experimental and kinetic modeling study of ethyl tert-butyl ether. Part I: High-temperature pyrolysis and oxidation chemistry[J]. Combustion and Flame, 2025, 281: 114394. DOI: 10.1016/j.combustflame.2025.114394.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 281 / November
- Article number: 114394
- DOI: 10.1016/j.combustflame.2025.114394
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025004316
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025004316/pdfft?md5=27a2bcf33a9350c8db685b80e3c3969a&pid=1-s2.0-S0010218025004316-main.pdf
- Fuel type: etbe
- Plasma-related mechanism: no
- Validation reactor/type from abstract: laminar flame speed

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218025004316_mmc4/SM6_HT.MECH, _processing/extracted/s0010218025004316_mmc4/SM4.MECH
- Original thermodynamic source files: _processing/extracted/s0010218025004316_mmc4/SM7_HT.THERM, _processing/extracted/s0010218025004316_mmc4/SM5.THERM
- Original transport source files: _processing/extracted/s0010218025004316_mmc4/SM8_HT.TRAN

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 308: """ H+O2(+M)=HO2(+M) 4.66E12 0.44 0.0E0 !\Author: SP !\Ref: TROE, PROCI Volume 28, Issue 2, 2000, 1463-1469 / PCCP FERNANDES 2008 HE/1.0/ AR/0.0/ N2/1.0/ O2/1.0/ H2/2.0/ CH4/2.0/ CO2/3.25/ H2O/17.6/ CO/4.0/ LOWMX / 4.0662E19 -1.4E0 -1.80537E2 / TROEMX / 5.0E-1 1.0E0 1.0E10 1.0E30 / LOWSP / N2 1.91E+20 -1.5568 253.86 / !Yuki Murakami 28 July 2023 H2 project recommended TROESP / N2 5.0E-1 1.0E0 1.0E10 1.0E30 / LOWSP / HE 1.216E+19 -1.23 +0.00 / !Yuki Murakami 17 May 2024, From AramcoMech3.0 He 0.64 -> 0.70 TROESP / HE 6.70E-1 1.0E-30 1.0E30 1.0E30 / """ could not convert string to float: 'N2' Please check https://cantera.org/stable/userguide/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files for the correct Che ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 308: """ H+O2(+M)=HO2(+M) 4.66E12 0.44 0.0E0 !\Author: SP !\Ref: TROE, PROCI Volume 28, Issue 2, 2000, 1463-1469 / PCCP FERNANDES 2008 HE/1.0/ AR/0.0/ N2/1.0/ O2/1.0/ H2/2.0/ CH4/2.0/ CO2/3.25/ H2O/17.6/ CO/4.0/ LOWMX / 4.0662E19 -1.4E0 -1.80537E2 / TROEMX / 5.0E-1 1.0E0 1.0E10 1.0E30 / LOWSP / N2 1.91E+20 -1.5568 253.86 / !Yuki Murakami 28 July 2023 H2 project recommended TROESP / N2 5.0E-1 1.0E0 1.0E10 1.0E30 / LOWSP / HE 1.216E+19 -1.23 +0.00 / !Yuki Murakami 17 May 2024, From AramcoMech3.0 He 0.64 -> 0.70 TROESP / HE 6.70E-1 1.0E-30 1.0E30 1.0E30 / """ could not convert string to float: 'N2' Please check https://cantera.org/stable/userguide/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files for the correct Che ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

A comprehensive experimental and kinetic modeling study of the combustion of ethyl tert-butyl ether (ETBE) is conducted over a wide range of engine-relevant conditions. Part I focuses exclusively on the high-temperature chemistry including relevant experimental pyrolysis and high-temperature oxidative validation targets. Part II focuses on the low- to intermediate temperature chemistry of ETBE and uses ignition delay times to validate the mechanism. CO time-history profiles from highly-diluted ETBE pyrolysis are measured behind reflected shock waves with a spectroscopic laser diagnostic in the 1235–1528 K temperature range near atmospheric pressure. Laminar flame speed (LFS) measurements of ETBE oxidation in air are conducted at 1 and 3 atm in the equivalence ratio range of 0.7–1.6. Reaction classes involving unimolecular decomposition, hydrogen atom abstraction, fuel radical β-scission and isomerization reactions are included to describe the high-temperature chemistry using the GalwayMech1.0 core C0–C4 chemistry. Sensitivity analyses reveal that the rate constant of the elimination reaction ETBE ⇌ IC4H8 + C2H5OH is very important to species profile predictions, followed by the two C–O bond breaking channels. Hence, pressure- and temperature-dependent rate constants for the two alcohol elimination channels: (a) ETBE ⇌ IC4H8 + C2H5OH and (b) ETBE ⇌ TC4H9OH + C2H4 were calculated using quantum chemistry. Similarly, the C–O bond β-scission reaction of ETBE radical, ETBE-S ⇌ TĊ4H9 + CH3CHO was also calculated in this study. The LFS predictions are dominated by the C0–C2 core chemistry with the fuel chemistry not appearing to be sensitive.

## Processing Notes

- extracted S0010218025004316_mmc3.docx
- extracted S0010218025004316_mmc1.docx
- extracted S0010218025004316_mmc4.zip
- extracted S0010218025004316_mmc2.docx
