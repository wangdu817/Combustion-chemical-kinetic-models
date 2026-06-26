# Carbon dioxide-driven dual effects on ignition delay and preignition behavior in plasma-assisted methanol ignition

## Bibliography

Nan Liu, Bolin Li, Qi Chen. Carbon dioxide-driven dual effects on ignition delay and preignition behavior in plasma-assisted methanol ignition[J]. Combustion and Flame, 2026, 287: 114882. DOI: 10.1016/j.combustflame.2026.114882.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 287 / May
- Article number: 114882
- DOI: 10.1016/j.combustflame.2026.114882
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026001185
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: methanol_ethanol
- Plasma-related mechanism: yes
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218026001185_mmc2/mmc2/SMM/Chem.inp, _processing/extracted/s0010218026001185_mmc2/mmc2/SMM/plasma kinetics.inp
- Original thermodynamic source files: _processing/extracted/s0010218026001185_mmc2/mmc2/SMM/Therm.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 6646: """ tHNNO + OH = H2O + N2O 9.2E13 -0.550 338.0d0 """ could not convert string to float: '338.0d0' Error while reading reaction in chem.inp starting on line 6647: """ tHNNO + OH = NH2 + NO2 2.2E16 -1.440 1238.0d0 """ could not convert string to float: '1238.0d0' Error while reading reaction in chem.inp starting on line 6649: """ cHNNO + OH = H2O + N2O 5.9E14 -0.910 668.0d0 """ could not convert string to float: '668.0d0' Error while reading reaction in chem.inp starting on line 6650: """ cHNNO + OH = NH2 + NO2 1.5E14 -0.650 626.0d0 """ could not convert string to float: '626.0d0' Error while reading reaction in chem.inp starting on line 6651: """ cHNNO + OH = tHNNO + OH 8.2E12 -0.300 1159.0d0 """ could not convert s ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading entry in chem.inp starting on line 60: """ BOLSIG """ Section starts with unrecognized keyword 'BOLSIG' Ignoring redundant declaration for species '#' Error while reading thermo entry in therm.dat starting on line 1148: """ C2H4O2 C 2H 4O 2 0G 300.000 5000.000 1391.000 01 1.00941573E+01 1.23879015E-02-3.73811683E-06 5.46874551E-10-3.09943951E-14 2 -2.37710522E+04-2.00956526E+01 4.44209543E+00 2.52880383E-02-1.51605275E-05 3 5.24921198E-09-7.91470852E-13-2.17507126E+04 1.04122371E+01 4 """ Error parsing elemental composition for species 'C2H4O2'. Ignoring redundant thermo data for species 'NH3' starting on line 1207 of therm.dat. Ignoring redundant thermo data for species 'NH2' starting on line 1213 of therm.dat. Ignoring redundant thermo data for species 'N2 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Carbon dioxide is the primary constituent of exhaust gas recirculation (EGR) and strongly influences ignition chemistry in advanced engines. This work investigates the roles of CO2 addition in plasma assisted methanol ignition. Gas chromatograph is employed to quantify the species concentrations and a detailed kinetic mechanism incorporating the electron impact reactions of CH3OH, CO2 and air is developed and validated against the measurements, showing good predictive performance. A nonlinear dependence ignition delay time on reduced electric field (E/N) is observed at low temperatures: the IDT initially decreases and then increases with increasing E/N, while at high temperatures a linear relationship is obtained. Electron impact dissociation reactions of CO2, the dominant consumption pathways, absorb the discharge energy and weaken the ignition by reducing the electron energy available to excite N2, O2 and CH3OH. Conversely, CO2 forming reaction such as CO + OH = CO2 + H enlarges the radical pool through H + O2 = OH + O, thereby accelerating chain reactions and promoting ignition. The effects of CO2 are further decoupled into dilution, thermal and chemical effects on plasma assisted ignition. The electron energy distribution function remains the same. Among them, the thermal effect proves most beneficial, whereas the chemical effect inhibited ignition. Finally, ignition Damköhler number with CO2 addition for plasma assisted methanol ignition is smaller than that without CO2 at low temperature, reducing thermal diffusivity, forming a more uniform temperature distribution and decreasing the probability of preignition. This work provides mechanistic insight into CO2 effects on plasma assisted methanol ignition with implication for advanced engines.

## Processing Notes

- extracted S0010218026001185_mmc1.docx
- extracted S0010218026001185_mmc2.zip
