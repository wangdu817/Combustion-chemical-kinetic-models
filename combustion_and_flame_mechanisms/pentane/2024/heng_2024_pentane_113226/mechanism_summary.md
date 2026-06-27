# An experimental and chemical kinetic modeling study of octane isomer oxidation. Part 1: 2,3,4-trimethyl pentane

## Bibliography

Yijun Heng, Gavin Kenny, Pengzhi Wang, Shijun Dong, Manik Kumer Ghosh, Gesheng Li, et al.. An experimental and chemical kinetic modeling study of octane isomer oxidation. Part 1: 2,3,4-trimethyl pentane[J]. Combustion and Flame, 2024, 263: 113226. DOI: 10.1016/j.combustflame.2023.113226.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 263 / May
- Article number: 113226
- DOI: 10.1016/j.combustflame.2023.113226
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023006004
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: pentane
- Plasma-related mechanism: yes
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218023006004_mmc4/mmc4.MECH
- Original thermodynamic source files: _processing/extracted/s0010218023006004_mmc5/mmc5.THERM
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 38479: """ CH3C6H3CH3+O2=>O2CH3C6H3CH3 1.950E+11 0.420 -631.1 !WAGNON1@LLNL.GOV! AS P-C6H4CH3+O2=>P-O2C6H4CH3 DA SILVA JPCA 117 (2007) 8663-8676 PLOG/ 1.00E-01 6.51+107 -32.05 12220 / PLOG/ 1.00E+00 3.21+132 -38.08 33960 / PLOG/ 1.00E+01 2.35+160 -45.03 60240 / PLOG/ 1.00E+02 6.57+179 -49.68 81660 / """ could not convert string to float: '6.51+107' Ignoring redundant thermo data for species 'XC6OOH1-3O2' starting on line 9366 of therm.dat. Ignoring redundant thermo data for species 'XC6D13-1Q' starting on line 12410 of therm.dat. Ignoring redundant thermo data for species 'XC6D13-1OJ' starting on line 12414 of therm.dat. Ignoring redundant thermo data for species 'XC6D13-Y1' starting on line 12418 of therm.dat. Ignoring ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

2,3,4-trimethyl pentane (234-TMP) is an isomer of octane with the same number of methyl branching groups as 2,2,4-trimethyl pentane (iso-octane). However, there are very few studies of this fuel available in the literature. In this work, a detailed chemical kinetic model is developed to describe the oxidation of 234-TMP using NUIGMech1.3 as the core mechanism. The rate constants for some important reaction classes are updated following a review of literature rate constants. Additionally, the impact of each rate constant on simulated ignition delay times for 234-TMP compared to 2,2,3-trimethyl pentane and 2,2,4-trimethyl pentane (iso-octane) is discussed. The thermodynamic data of the alkanes (RH), alkyl (Ṙ), alkyl peroxy (RȮ2), hydroperoxy-alkyl Q ˙ OOH, and peroxy hydroperoxyalkyl (Ȯ2QOOH) radicals are newly estimated based on recently updated group values in the literature. Moreover, this study presents the first set of data available for the oxidation of 234-TMP at higher pressures (15 and 30 atm), in the temperature range 600–1600 K, and at fuel/‘air’ equivalence ratios (φ) of 0.5, 1.0 and 2.0. The chemical kinetic model shows general good agreement with the experimental measurements. In addition, flux and sensitivity analyses are conducted to identify the important pathways and reactions controlling fuel oxidation at different temperatures. Furthermore, the reactivity of 234-TMP is compared to that of iso-octane, indicating that 234-TMP is slower to react as it has more tertiary carbon sites compared to iso-octane.

## Processing Notes

- extracted S0010218023006004_mmc4.zip
- extracted S0010218023006004_mmc2.xlsx
- extracted S0010218023006004_mmc5.zip
- extracted S0010218023006004_mmc3.xlsx
- extracted S0010218023006004_mmc1.docx
