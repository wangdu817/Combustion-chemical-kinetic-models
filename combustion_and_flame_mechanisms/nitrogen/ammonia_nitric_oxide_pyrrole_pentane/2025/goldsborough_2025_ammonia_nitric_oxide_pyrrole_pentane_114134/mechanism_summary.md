# Experimental and modeling study of the autoignition behavior of a saturated heterocycle: Pyrrolidine

## Bibliography

S. Scott Goldsborough, Mads C. Jespersen, Jeffrey S. Santner, Raghu Sivaramakrishnan, ... William J. Pitz. Experimental and modeling study of the autoignition behavior of a saturated heterocycle: Pyrrolidine[J]. Combustion and Flame, 2025, 277: 114134. DOI: 10.1016/j.combustflame.2025.114134.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 277 / July
- Article number: 114134
- DOI: 10.1016/j.combustflame.2025.114134
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025001725
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025001725/pdfft?md5=57106f61431922861d66fd7d53f34ff4&pid=1-s2.0-S0010218025001725-main.pdf
- Fuel type: ammonia_nitric_oxide_pyrrole_pentane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S0010218025001725_mmc3.txt
- Original thermodynamic source files: _processing/extracted/s0010218025001725_mmc4/SM5 - thermo.CYC5H10_C4H9N_CHEMKIN_2025.CKT
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 140
- Reaction count: 1974
- Message: CanteraError: ******************************************************************************* InputFileError thrown by Kinetics::checkDuplicates: Error on line 3814 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ammonia_nitric_oxide_pyrrole_pentane/2025/goldsborough_2025_ammonia_nitric_oxide_pyrrole_pentane_114134/mechanism.yaml: No duplicate found for declared duplicate reaction number 661 (C5H5O + OH => C4H4 + CO + H2O) | Line | | 3809 | type: pressure-dependent-Arrhenius | 3810 | rate-constants: | 3811 | - {P: 0.1 atm, A: 4.91e+25, b: -3.12, Ea: 1.772673e+04} | 3812 | - {P: 1.0 atm, A: 3.06e+29, b: -4.07, Ea: 2.37896e+04} | 3813 | - {P: 10.0 atm, A: 8.13e+24, b: -2.67, Ea: 2.502564e+04} > 3814 > - equation: OH + C5H5O => H2O + CO + C4H4 # Reaction 662 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Experiments are conducted in both rapid compression machine (RCM) and shock tube (ST) to better quantify autoignition behavior (e.g., ignition delay, heat release) and understand heteroatomic effects in heterocyclic compounds, which are important reference components for the combustion of biomass-derived liquid fuels. These tests focus on the nitrogen-containing, five-membered saturated ring, pyrrolidine, at diluted conditions covering pressures of 20 and 50 bar, temperatures of 720–1450 K and a range of stoichiometries (ϕ = 0.5–2). A chemical kinetic model is developed and coupled to an existing combustion kinetics framework describing key nitrogen containing intermediates (e.g. pyrrole, ammonia and NOx). H-abstraction reactions by OH, H, CH3 and HO2, are determined using ab-initio transition state theory methods, while analogies to cyclopentane are adopted for many other reactions, such as ring-opening. The autoignition measurements reveal the lack of negative temperature coefficient (NTC) behavior and low-temperature chemistry for pyrrolidine, as opposed to its saturated hydrocarbon analogue, cyclopentane. Interestingly, at the lowest temperatures (T 70 %, are predicted to move through 1- or 2-pyrroline (C4H7N) and then the cyclic C4H6N radical, at both lower and higher temperatures, to form either CH2CHCHCHNH via ring-opening or pyrrole via β-scission. It appears that the ring opens more easily at lower temperature whereas the C–H β-scission dominates at higher temperature and lower pressure, such that the reaction of the fuel radical intermediate carrying an unpaired electron on the nitrogen atom with HO2 is the next most notable in promoting oxidation. When comparing pyrrolidine and cyclopentane, which exhibits distinct pathways in different temperature regimes, the pyrrolidine pathways and sensitivity analysis align more closely to the high temperature case of cyclopentane where the important role of HO2 radicals is seen to provide chain branching through HO2 reaction with the fuel, accompanied by H2O2 formation and decomposition to OH. The formation of 5-membered diene rings and ring opening reactions are also found to be highly relevant. Of particular note, it is found that there is little influence of small molecule nitrogen-chemistry, e.g., NH2, HCN, NO/NO2 on the reactivity of the pyrrolidine mixtures investigated here where no recirculated combustion gases are included.

## Processing Notes

- extracted S0010218025001725_mmc1.xlsx
- extracted S0010218025001725_mmc5.docx
- extracted S0010218025001725_mmc6.docx
- extracted S0010218025001725_mmc2.xlsx
- extracted S0010218025001725_mmc4.zip
