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
- Fuel type: n_dodecane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, rapid compression machine, jet-stirred reactor, flow reactor, laminar flame speed, stirred reactor

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

In recent years, there has been a notable surge in experimental and kinetic modeling efforts concerning various biodiesels, their surrogates, and relevant molecules. This work culminates these research efforts to construct a comprehensive and robust surrogate kinetic model for various biodiesel fuels. This model has incorporated accurate chemistry and undergone extensive validation against a broad range of experimental data available for biodiesel. In order to accurately reproduce the combustion characteristics of biodiesel, methyl butanoate, methyl crotonate, 3-hexene, and n-dodecane are chosen as surrogate components. These molecules have been chosen to replicate the functional groups found in biodiesel methyl esters. Each surrogate component is firstly validated thoroughly against a wide array of experimental studies. The kinetics of each component are improved through careful rate assignments derived from various theoretical investigations. Subsequently, a surrogate mixture comprising these selected components is formulated by matching the functional groups of target fuels. This surrogate mechanism is used to validate the experimental data associated with various biodiesel fuels, their constituents, and methyl esters exhibiting similar functional groups to those present in actual biodiesel. The current kinetic model has demonstrated good agreement for various biodiesel fuels and their commonly used surrogates for a range of experimental studies, encompassing ignition delay times measured in shock tubes and rapid compression machines, laminar flame speeds, as well as species mole fractions measured in jet stirred reactors and laminar flow reactors. Novelty and significance statement This study introduces novel surrogate mixtures consisting of methyl butanoate, methyl crotonate, 3-hexene, and n-dodecane, formulated to predict the combustion characteristics of biodiesel. While several surrogate formulations for biodiesel exist in the literature, the novelty of this work lies in its extensive validation and reliable kinetic of the surrogate mixtures, which is leveraged from well-validated chemistry of each of these individual components. The study investigates whether selected small methyl esters and alkene can sufficiently capture combustion characteristics of molecules with similar functional groups. Currently, there are only two comprehensive biodiesel kinetic models in the literature, both developed over a decade ago, which have been widely used in subsequent studies for optimization and reduction. The new model presented in this study offers a more reliable chemistry while being relatively more compact, owing to its use of well validated small molecule surrogate components.

## Processing Notes

- extracted S0010218025001476_mmc4.zip
- extracted S0010218025001476_mmc2.zip
- extracted S0010218025001476_mmc1.zip
- extracted S0010218025001476_mmc6.zip
- extracted S0010218025001476_mmc5.zip
