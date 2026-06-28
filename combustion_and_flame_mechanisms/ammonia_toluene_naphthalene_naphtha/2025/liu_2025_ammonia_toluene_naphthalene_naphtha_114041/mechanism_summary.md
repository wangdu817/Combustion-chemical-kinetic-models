# Experimental investigation and kinetic analysis of ammonia addition on the laminar flame speed of toluene and α-methylnaphthalene

## Bibliography

Zechang Liu, Guangyuan Feng, Xu He, Chengyuan Zhao, ... Qingchu Chen. Experimental investigation and kinetic analysis of ammonia addition on the laminar flame speed of toluene and α-methylnaphthalene[J]. Combustion and Flame, 2025, 274: 114041. DOI: 10.1016/j.combustflame.2025.114041.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 274 / April
- Article number: 114041
- DOI: 10.1016/j.combustflame.2025.114041
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025000793
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025000793/pdfft?md5=de780cfead16afe6792bfedf76b09444&pid=1-s2.0-S0010218025000793-main.pdf
- Fuel type: ammonia_toluene_naphthalene_naphtha
- Plasma-related mechanism: possible
- Validation reactor/type from abstract: laminar flame speed

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218025000793_mmc5/Toluene_NH3_mech.inp, _processing/extracted/s0010218025000793_mmc2/AMN_NH3_Mech.inp
- Original thermodynamic source files: _processing/extracted/s0010218025000793_mmc3/AMN_NH3_Therm.dat, _processing/extracted/s0010218025000793_mmc6/Toluene_NH3_therml.thermo
- Original transport source files: _processing/extracted/s0010218025000793_mmc1/AMN_NH3.TRAN, _processing/extracted/s0010218025000793_mmc7/Toluene_NH3_tran.TRAN

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading section in chem.inp starting on line 147: """ REACTIONS MAXSP=9 """ Unrecognized token 'MAXSP=9' on REACTIONS line Ignoring redundant thermo data for species 'HCN' starting on line 1666 of therm.dat. Ignoring redundant thermo data for species 'HNC' starting on line 1686 of therm.dat. Ignoring duplicate transport data for species "AR" on line 501 of "tran.dat". Ignoring duplicate transport data for species "N2" on line 502 of "tran.dat". Ignoring duplicate transport data for species "HE" on line 503 of "tran.dat". Ignoring duplicate transport data for species "H2" on line 504 of "tran.dat". Ignoring duplicate transport data for species "H" on line 505 of "tran.dat". Suppressed 184 additional warnings about duplicate transport data. Run ck2yaml again with the ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'AR' Ignoring redundant declaration for species 'HE' Ignoring redundant declaration for species 'N2' Ignoring redundant declaration for species 'HOCO' Ignoring redundant declaration for species 'CH2(S)' Suppressed 31 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Error while reading section in chem.inp starting on line 195: """ REACTIONS MAXSP=8 """ Unrecognized token 'MAXSP=8' on REACTIONS line Ignoring redundant thermo data for species 'HCN' starting on line 1666 of therm.dat. Ignoring redundant thermo data for species 'HNC' starting on line 1686 of therm.dat. No thermo data found for species 'C5H5CH3' No thermo data found for species 'C5H5OH' No thermo dat ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

This study explores the effects of ammonia (NH3) on the laminar flame speed ( S L ) and kinetic interactions with toluene (C7H8) and α-methylnaphthalene (AMN), two predominant aromatic hydrocarbons in transportation fuels. Utilizing the spherical flame technique, we measured the S L of both C7H8/NH3 and AMN/NH3 mixtures at an initial temperature (Ti) of 484 K, NH3 concentrations (XNH3) up to 70%, and equivalence ratios ( ϕ ) ranging from 0.8 to 1.3 under atmospheric pressure and elevated pressures. A chemical kinetic model was developed to integrate NH3 with these hydrocarbons, based on the advanced CRECK model, and includes cross C-N reaction pathways involving amine (NH2) with C7H8, AMN, and benzene (C6H6). The model effectively replicated the experimental S L and ignition delay time data for AMN/NH3 mixtures. Through sensitivity and reaction pathway analyses, the study identified critical reaction types: such as small molecule chain branching reactions (e.g., H+O2=O+OH and CO+OH=CO2+H) and H-abstraction from both the methyl and ring sides, as pivotal in influencing SL . Furthermore, the study examines the formation of NOx and soot, revealing that NH3 addition both increased the mole fraction of NO in C7H8/NH3 and AMN/NH3 mixtures, but the mole fraction of NO in C7H8/NH3 mixture is higher than AMN/NH3 mixture, attributed to the higher HNO/NH2/N radicals in C7H8/NH3 mixture, and finally leading to the promoted effect on the reaction pathways of NO production. The addition of NH3 also inhibits soot formation by reducing the production of soot precursors and C2H2, while increasing the production of HCN and blocking the formation of larger PAHs.

## Processing Notes

- extracted S0010218025000793_mmc4.docx
- extracted S0010218025000793_mmc5.zip
- extracted S0010218025000793_mmc3.zip
- extracted S0010218025000793_mmc7.zip
- extracted S0010218025000793_mmc1.zip
- extracted S0010218025000793_mmc2.zip
- extracted S0010218025000793_mmc6.zip
