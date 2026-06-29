# Experimental and kinetic modeling study of  α-methyl-naphthalene pyrolysis: Part II. PAH formation

## Bibliography

Hanfeng Jin, Junyu Hao, Jiuzhong Yang, Junjun Guo, Yan Zhang, ChuangChuang Cao, et al.. Experimental and kinetic modeling study of  α-methyl-naphthalene pyrolysis: Part II. PAH formation[J]. Combustion and Flame, 2021, 233: 111530. DOI: 10.1016/j.combustflame.2021.111530.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 233 / Nov
- Article number: 111530
- DOI: 10.1016/j.combustflame.2021.111530
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S001021802100273X
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: naphthalene_naphtha_pah
- Plasma-related mechanism: no
- Validation reactor/type from abstract: flow reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s001021802100273x_mmc4/SMM4. Kinetic Mechanism CHEMKIN.inp, _processing/extracted/s001021802100273x_mmc3/SMM3. Kinetic Mechanism Cantera.cti
- Original thermodynamic source files: _processing/extracted/s001021802100273x_mmc5/SMM5. Thermodynamic Data.dat, _processing/extracted/s001021802100273x_mmc3/SMM3. Kinetic Mechanism Cantera.cti
- Original transport source files: _processing/extracted/s001021802100273x_mmc6/SMM6. Transport Data.dat, _processing/extracted/s001021802100273x_mmc3/SMM3. Kinetic Mechanism Cantera.cti

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: CanteraError: ******************************************************************************* CanteraError thrown by newSolution: The CTI and XML formats are no longer supported. *******************************************************************************
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 10764: """ PERYCH3(+M)=PERY-+CH3(+M) 1.95E27 -3.16 1.07447E5 LOW/1.0E98 -2.2966E1 1.2208E5/ TROE/7.054562E-1 9.999989E9 4.59918E2 8.213938E9/ """ Unparsable line: '-----------------------------------------------------------'. Error while reading thermo entry in therm.dat starting on line 1451: """ A1(C2H3)2 C 10H 10 G 300.000 5000.000 5000.00 0 1 5.60848905E+01 0.00000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00 2 -1.44640324E+04-3.08906342E+02 3.54769133E+00 6.32681160E-02-2.97482733E-05 3 6.21023998E-09-4.74202473E-13 2.29084499E+04 9.41010680E+00 4 """ Only one temperature range defined but two distinct sets of coefficients given in species thermo entry. Ignoring redundant thermo data for species 'A1CHCH3' sta ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

α-Methyl-naphthalene plays an important role as a functional material in petrochemical industries and as a precursor of soot particles. The formation chemistry of polycyclic aromatic hydrocarbons (PAHs) from α-methyl-naphthalene, therefore, warrants detailed investigations. In this work, we studied PAH formation from its pyrolysis using experiments and kinetic models. Flow reactor pyrolytic experiments at low and atmospheric pressures (30 and 760 Torr) were performed using synchrotron vacuum ultraviolet photoionization molecular beam mass spectrometry (SVUV-PI-MBMS). A kinetic model was then developed to predict PAH formation from α-methyl-naphthalene. According to the kinetic analysis of the proposed model, naphth-1-yl-methyl, benzo-fulvenallene, and benzo-fulvenallenyl are three critical intermediates in the formation of large PAHs. Other than the traditional H-abstraction acetylene-/vinylacetylene-addition mechanisms, three prototypical PAH formation pathways are identified in α-methyl-naphthalene pyrolysis: 1) addition and cyclization reactions of naphth-1-yl-methyl and naphth-1-yl radicals; 2) recombination of resonance stabilized radicals (indenyl, benzo-fulvenallenyl, phenalenyl, etc.) and the subsequent ring expansion reactions; 3) sequential propargyl addition reactions.

## Processing Notes

- extracted S001021802100273X_mmc1.xlsx
- extracted S001021802100273X_mmc6.zip
- extracted S001021802100273X_mmc3.zip
- extracted S001021802100273X_mmc4.zip
- extracted S001021802100273X_mmc5.zip
