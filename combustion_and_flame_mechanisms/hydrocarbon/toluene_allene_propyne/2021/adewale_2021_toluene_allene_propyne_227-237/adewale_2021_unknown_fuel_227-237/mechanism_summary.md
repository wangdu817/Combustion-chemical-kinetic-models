# Kinetics of C5H4 isomer + H reactions and incorporation of C5H  (x = 3 – 5) chemistry into a detailed chemical kinetic model

## Bibliography

Rasheed Adewale, Gabriel da Silva. Kinetics of C5H4 isomer + H reactions and incorporation of C5H  (x = 3 – 5) chemistry into a detailed chemical kinetic model[J]. Combustion and Flame, 2021, 227: 227-237. DOI: 10.1016/j.combustflame.2020.12.046.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 227 / May
- Article number: 227-237
- DOI: 10.1016/j.combustflame.2020.12.046
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218020306015
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S0010218020306015_mmc1.txt
- Original thermodynamic source files: _processing/raw_downloads/S0010218020306015_mmc3.txt
- Original transport source files: _processing/raw_downloads/S0010218020306015_mmc4.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'C4H6' Error while reading thermo entry in therm.dat starting on line 1438: """ A1(C2H3)2 C 10H 10 G 300.000 5000.000 5000.00 1 5.60848905E+01 0.00000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00 2 -1.44640324E+04-3.08906342E+02 3.54769133E+00 6.32681160E-02-2.97482733E-05 3 6.21023998E-09-4.74202473E-13 2.29084499E+04 9.41010680E+00 4 """ Only one temperature range defined but two distinct sets of coefficients given in species thermo entry. Error while reading thermo entry in therm.dat starting on line 1446: """ C9H8CH3 C 10H 11 G 300.000 5000.000 5000.00 1 5.89344512E+01 0.00000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00 2 -2.21709548E+04-3.29232464E+02 1.57041459E+00 6.95644403E-02-3.28229474E-05 3 6.86333912E-09-5.2 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Although C5H4 isomers are detected in flames, they are not thoroughly incorporated into detailed chemical kinetics models (DCKMs). Here we use RRKM/ME modelling to simulate C5H4 + H reactions on a C5H5 potential energy surface. Kinetic studies indicate that C3H3 + C2H2 is the main fate but fall-off from the initial adduct isomer back to C5H4 + H cannot be ignored at relevant combustion temperatures of 900 to 2000 K. Calculated rate coefficient expressions were incorporated into a DCKM for a toluene flame, along with updates to other relevant reactions from the recent literature, particularly the open-chain 1-vinylpropargyl radical, l-C5H5. Obtained species mole fractions were found to be in good agreement with published experimental data for a low-pressure toluene flame, with a significant improvement in predicted concentration of the cyclopentadienyl radical. The presented DCKM will allow for further reactions of C5H x species such as 1-vinylpropargyl to be included in combustion simulations.

## Processing Notes

- extracted S0010218020306015_mmc2.docx
