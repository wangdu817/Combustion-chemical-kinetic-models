# An experimental and kinetic modeling study of the pyrolysis and oxidation of n-C3C5 aldehydes in shock tubes

## Bibliography

Matteo Pelucchi, Kieran P. Somers, Kenji Yasunaga, Ultan Burke, Alessio Frassoldati, Eliseo Ranzi, et al.. An experimental and kinetic modeling study of the pyrolysis and oxidation of n-C3C5 aldehydes in shock tubes[J]. Combustion and Flame, 2015, 162: 265-286. DOI: 10.1016/j.combustflame.2014.07.027.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 162 / Feb
- Article number: 265-286
- DOI: 10.1016/j.combustflame.2014.07.027
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218014002314
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: iron_biofuel
- Plasma-related mechanism: possible
- Validation reactor/type from abstract: shock tube

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218014002314_mmc4/4_a_POLIMI_aldehydes_kinetics.CKI, _processing/extracted/s0010218014002314_mmc3/3_a_NUIG_aldehydes_kinetics.MECH
- Original thermodynamic source files: _processing/extracted/s0010218014002314_mmc4/4_b_POLIMI_aldehydes_thermo.CKT, _processing/extracted/s0010218014002314_mmc3/3_b_NUIG_aldehydes_LT_HT.therm
- Original transport source files: _processing/extracted/s0010218014002314_mmc4/4_c_POLIMI_transport.TRC, _processing/extracted/s0010218014002314_mmc3/3_c_NUIG_aldehydes.tran

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant thermo data for species 'HOCH2O2H' starting on line 107 of therm.dat. Ignoring redundant thermo data for species 'HOCH2O2' starting on line 111 of therm.dat. Ignoring redundant thermo data for species 'OCH2O2H' starting on line 115 of therm.dat. Error while reading thermo entry in therm.dat starting on line 485: """ CHOCOCH2OOH THERMC 3H 4O 4 0 300.000 5000.000 1387.000 41 1.88513241E+01 9.20926912E-03-3.31625639E-06 5.32903065E-10-3.16697392E-14 2 -4.88407829E+04-6.72981510E+01 1.14193480E+00 5.43367117E-02-4.78232702E-05 3 2.06439596E-08-3.52353283E-12-4.31220565E+04 2.63898462E+01 4 """ could not convert string to float: '0 5000.00' Error while reading thermo entry in therm.dat starting on line 489: """ CHOCOOHCHO THERMC 3H 4O 4 0 300.000 5000.000 1387.000 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: No transport data for species 'ETC3H4O2'. No transport data for species 'KEA3G2'. No transport data for species 'KEA3B3'. No transport data for species 'RALD3B'. No transport data for species 'RALD3G'. No transport data for species 'CH2OOHCHCHO'. No transport data for species 'CH3CHOOCHO'. No transport data for species 'CH2OOCH2CHO'. No transport data for species 'CH2CHOOHCHO'. No transport data for species 'CH2OOHCHOOCHO'. No transport data for species 'CH2OOCHOOHCHO'. No transport data for species 'RALD4B'. No transport data for species 'RALD4G'. No transport data for species 'RALD4D'. Please check https://cantera.org/stable/userguide/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files for the correct Chemkin syntax.
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Due to the increasing interest in the use of biofuels for energy production, it is of great importance to better understand the combustion and thermal decomposition characteristics of species such as aldehydes. These are known to be key intermediate products of transport fossil and bio-fuels combustion and are also dangerous pollutants emitted from combustion in internal combustion engines and from gasification of biomasses. In this study, an experimental and kinetic modeling investigation of propanal, n-butanal and n-pentanal pyrolysis and oxidation in two shock tube facilities was carried out. Experiments were performed in a single pulse shock tube to determine the speciation profiles of the fuels and intermediate species under pyrolysis conditions for mixture of pure propanal/n-butanal/n-pentanal (3%)–Ar (97%), at averaged reflected pressure of 1.9atm and at reflected shock temperatures of 972–1372K. Additionally, ignition delay times for mixtures of pure propanal/n-butanal/n-pentanal (1%)–O2/Ar were measured in the temperature range 1136–1847K, at pressures of 1 and 3atm, and at equivalence ratios of 0.5, 1.0 and 2.0. A comprehensive sub-mechanism for the high temperature kinetics of the three aldehydes was developed. This scheme was then coupled with NUIG (National University of Ireland, Galway) and POLIMI (Politecnico di Milano) C0 C4 kinetic schemes. The inclusion of the aldehydes sub-mechanism in two different kinetic environments, required modifications for the H-abstraction reactions, due to different rate rules in use in the two kinetic environments, and due to differences in the C0 C4 kinetic schemes. Both of the models were validated and showed good agreement with the new experimental data. The mechanisms are also satisfactorily compared with ignition delay times, speciation profiles and laminar burning velocities previously published in literature. Reaction pathways and sensitivity analyses were also performed to highlight the important reaction steps involved in the pyrolysis and oxidation processes. The major differences between the models and the experiments have to be attributed to the chemistry of the smaller species, more than to aldehyde specific reactions. This work further highlights the relevant role of the C0 C4 sub-mechanism, mainly in terms of a unification process that needs to start from the smaller species chemistry in order to obtain an unambiguous description of any fuel investigated.

## Processing Notes

- extracted S0010218014002314_mmc1.docx
- extracted S0010218014002314_mmc4.zip
- extracted S0010218014002314_mmc2.docx
- extracted S0010218014002314_mmc3.zip
