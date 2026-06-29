# An experimental and modeling study on norbornane pyrolysis aided by chemical information from neural network-assisted molecular dynamics

## Bibliography

Hang Xiao, Zhaohan Chu, Haodong Chen, Taichang Zhang, ... Bin Yang. An experimental and modeling study on norbornane pyrolysis aided by chemical information from neural network-assisted molecular dynamics[J]. Combustion and Flame, 2025, 274: 114039. DOI: 10.1016/j.combustflame.2025.114039.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 274 / April
- Article number: 114039
- DOI: 10.1016/j.combustflame.2025.114039
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S001021802500077X
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S001021802500077X/pdfft?md5=db69aa9e55cbc80434e4dcd9ed9fbfdb&pid=1-s2.0-S001021802500077X-main.pdf
- Fuel type: norbornane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s001021802500077x_mmc4/mech.inp
- Original thermodynamic source files: _processing/extracted/s001021802500077x_mmc6/thermo.dat
- Original transport source files: _processing/extracted/s001021802500077x_mmc7/transport.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading thermo entry in therm.dat starting on line 896: """ A1(C2H3)2 C 10H 10 G 300.000 5000.000 5000.00 1 5.60848905E+01 0.00000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00 2 -1.44640324E+04-3.08906342E+02 3.54769133E+00 6.32681160E-02-2.97482733E-05 3 6.21023998E-09-4.74202473E-13 2.29084499E+04 9.41010680E+00 4 """ Only one temperature range defined but two distinct sets of coefficients given in species thermo entry. Error while reading thermo entry in therm.dat starting on line 904: """ C9H8CH3 C 10H 11 G 300.000 5000.000 5000.00 1 5.89344512E+01 0.00000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00 2 -2.21709548E+04-3.29232464E+02 1.57041459E+00 6.95644403E-02-3.28229474E-05 3 6.86333912E-09-5.24482994E-13 1.81216645E+04 1.77907635E+01 4 """ Only ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Norbornane has been reported in recent years as a diesel additive that can improve soot characteristics or as the backbone of new jet fuels to increase fuel density and the net heat of combustion. However, there is still a lack of experimental and modeling studies on norbornane pyrolysis, which limits its further application. This work uses a flow tube reactor to conduct experiments at 30 torr, 923 K ∼ 1373 K, with a photoionization molecular-beam mass spectrometer to identify and quantify the pyrolysis species. At the same time, an attempt is made to apply high-precision deep potential molecular dynamics (DPMD) to assist in kinetic model construction. Species analysis on MD simulations provides additional chemical information on key pyrolysis species in the norbornane pyrolysis system, which agrees with experimental results. Therefore, the reactions appearing in MD simulations are supposed to play a nonnegligible role in the experimental system, so that high-frequency reactions of selected are added to the pyrolysis kinetic model. Further comparison of experimental and modeling results shows that the modeling results can accurately predict experimental concentrations for most species. By analyzing the rate of production of all species in the system, we highlight their primary production and consumption pathways, especially the pathways from norbornane to benzene in the system. When conducting sensitivity analysis, it is found that the initial decomposition reactions of the fuel have large sensitivity coefficients on the experimental results, especially the concentration of norbornane; it is also noteworthy that the reactions extracted in the MD results have an essential impact on the concentration of 1,3-cyclohexadiene.

## Processing Notes

- extracted S001021802500077X_mmc4.zip
- extracted S001021802500077X_mmc1.docx
- extracted S001021802500077X_mmc3.xlsx
- extracted S001021802500077X_mmc7.zip
- extracted S001021802500077X_mmc6.zip
- extracted S001021802500077X_mmc5.zip
- extracted S001021802500077X_mmc2.docx
