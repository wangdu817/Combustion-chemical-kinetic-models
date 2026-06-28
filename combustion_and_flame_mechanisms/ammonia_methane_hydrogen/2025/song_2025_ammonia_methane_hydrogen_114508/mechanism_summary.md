# Shock tube and laser absorption study of C–N–Cl interactions relevant to ammonium perchlorate combustion

## Bibliography

Shubao Song, Lin Zhang, Meishuai Zou, Jiankun Shao. Shock tube and laser absorption study of C–N–Cl interactions relevant to ammonium perchlorate combustion[J]. Combustion and Flame, 2025, 282: 114508. DOI: 10.1016/j.combustflame.2025.114508.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 282 / December
- Article number: 114508
- DOI: 10.1016/j.combustflame.2025.114508
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025005450
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025005450/pdfft?md5=eba30d2a8e7260a112e705ff3a2359d6&pid=1-s2.0-S0010218025005450-main.pdf
- Fuel type: ammonia_methane_hydrogen
- Plasma-related mechanism: yes
- Validation reactor/type from abstract: shock tube

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218025005450_mmc3/NH3_CCL4_mech.inp
- Original thermodynamic source files: _processing/extracted/s0010218025005450_mmc4/NH3_CCL4_thermo.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'CH2NCH2' Error while reading reaction in chem.inp starting on line 4375: """ CH3NCH+O=>CH3+NCO+H 7.0E13 0.000 0 ! ! A Lucassen K Zhang J Warkentin K Moshammer P Glarborg P Marshall K Kohse-Höinghaus, CF 159 (2012) 2254-2279. """ Unparsable line: 'REACTIONS'. Ignoring redundant thermo data for species 'CL2' starting on line 210 of therm.dat. Error while reading thermo entry in therm.dat starting on line 247: """ NOCL ATCT3EN 1CL 1O 1 0G 200.00 4000.00 1000.00 1 3.2325533 0.011886435 -2.1070873E-05 1.9552938E-08 -6.992627E-12 2 6363.5546 10.277271 6.179919 2.8500775E-04 1.7276529E-07 3 -3.0166754E-11, 9.0192767E-16 5632.7606 -4.3234813 4 """ could not convert string to float: '-3.0166754e-11,' Ignoring redundant thermo data for species ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

High-temperature gas-phase interactions between chlorine- and nitrogen-bearing species relevant to ammonium-perchlorate (AP) propellant combustion were elucidated by coupling shock-tube laser-absorption measurements with a detailed kinetic model. Time-resolved HCl concentration profiles were obtained for four argon-diluted surrogates—0.3 % NH3/0.3 % CCl4, 0.5 % NH3/0.3 % CCl4, 0.2 % NH3/0.2 % CCl4/0.2 % CH4, and 0.2 % NH3/0.2 % CCl4/0.2 % H2—over 1158–1506 K at near-atmospheric pressure. A kinetic model consisting of 164 species and 1358 reactions, assembled from state-of-the-art CCl4, H–Cl–O, NH3/C0–C2, and N–Cl sub-models, reproduced the new HCl data alongside literature ignition-delay and speciation measurements with excellent accuracy. Sensitivity and rate-of-production analyses reveal a temperature-robust control structure in which HCl forms almost entirely through Cl-atom abstraction from NH3, with Cl supplied by rapid CCl4 dissociation; the barrierless Cl + H HCl path dominates in H2-containing mixtures, whereas competition from Cl + CH4 CH3 + HCl moderates HCl growth and channels carbon–nitrogen flux toward toxic HCN when CH4 is present. Elevated temperature chiefly amplifies Cl production and suppresses NH2 recombination, accelerating overall reactivity without altering the dominant pathways. The resulting benchmark HCl time-histories and rigorously validated model advance fundamental understanding of chlorine–nitrogen combustion chemistry and provide quantitative guidance for formulating halogenated energetic materials that maximise performance while limiting hazardous by-product formation. Importantly, the mechanism developed here may serve as a transferable gas-phase sub-model for future integration into comprehensive AP combustion frameworks, enabling more predictive simulations of real propellant systems.

## Processing Notes

- extracted S0010218025005450_mmc3.zip
- extracted S0010218025005450_mmc4.zip
- extracted S0010218025005450_mmc1.docx
- extracted S0010218025005450_mmc2.xlsx
