# Advancing the C4 low-temperature oxidation chemistry through species measurements in a rapid compression machine, Part A: 1-Butene

## Bibliography

Jesus Caravaca-Vilchez, Jiaxin Liu, Pengzhi Wang, Yuki Murakami, ... Karl Alexander Heufer. Advancing the C4 low-temperature oxidation chemistry through species measurements in a rapid compression machine, Part A: 1-Butene[J]. Combustion and Flame, 2025, 272: 113833. DOI: 10.1016/j.combustflame.2024.113833.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 272 / February
- Article number: 113833
- DOI: 10.1016/j.combustflame.2024.113833
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S001021802400542X
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S001021802400542X/pdfft?md5=895ba6f38c268ebe066a19fffbcb8c26&pid=1-s2.0-S001021802400542X-main.pdf
- Fuel type: 1_butene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, rapid compression machine, jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s001021802400542x_mmc4/NUIGMech1.3_C4_mod__Commented.cti, _processing/extracted/s001021802400542x_mmc6/NUIGMech1.3_C4_mod.inp
- Original thermodynamic source files: _processing/extracted/s001021802400542x_mmc5/NUIGMech1.3_C4_mod.dat, _processing/extracted/s001021802400542x_mmc4/NUIGMech1.3_C4_mod__Commented.cti
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 749
- Reaction count: 4094
- Message: CanteraError: ******************************************************************************* CanteraError thrown by newSolution: The CTI and XML formats are no longer supported. *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 2

- Status: ok
- Species count: 749
- Reaction count: 4094
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Alkene chemistry plays a crucial role in the autoignition and oxidation of larger hydrocarbons. Unlike its other isomers, 1-butene is characterized by a two-stage ignition process. Various previous studies of 1-butene oxidation have used experimental techniques, including the measurement of ignition delay times in rapid compression machines (RCM) and in shock tubes, the determination of flame velocities, and the measurement of species concentrations in flames and in jet-stirred reactors (JSR). JSR studies provide an important insight into intermediate species formation at low temperatures but are constrained to low pressures and/or highly diluted conditions. To bridge the gap between JSR and engine-relevant conditions, this study presents species concentration measurements during the oxidation of 1-butene at 733 K and 30 bar under stoichiometric ’air-like’ conditions in an RCM, complemented by IDT measurements in the temperature range of 680–910 K. We designed an innovative 2-valve sampling setup to reduce quantitative uncertainties and the time required for species measurements. Our results indicate that existing 1-butene models fail to accurately predict the IDTs and the formation of the key oxidation intermediates. In response, potential optimizations for an improved kinetic model based on NUIGMech1.3 are discussed. Rate parameters for predominantly fuel consumption pathways, along with other reactions and thermochemical properties in the Waddington mechanism, have been altered within expected uncertainty limits to reflect the experimentally observed IDTs and species concentrations of this study and other validation data from the literature. However, the refined model does not predict the formation of 2-ethenyloxirane and ethene, indicating a gap in our understanding of the chemistry of these components. Overall, this study demonstrates the importance of measuring intermediates under the same conditions as IDTs to accurately address deficiencies in current kinetic mechanisms, and represents the first phase of a comprehensive investigation advancing the understanding of C 4 oxidation chemistry. Novelty and significance statement The novelty of this research lies in the design of an innovative sampling system for RCM species measurements, lowering the time for experimental execution and the uncertainties of the measurements. This enabled first-time species measurements during the oxidation of butene isomers in an RCM at high pressure and low level of dilution, contributing to the refinement of the 1-butene sub-mechanism within the NUIGMech1.3 framework. This research contributes to the understanding of the oxidation of alkenes, an important class of intermediates in gasoline and biofuel combustion. It emphasizes the need to measure intermediate species at the same conditions as ignition delay times, which are essential for understanding oxidation pathways under engine-relevant conditions. This research is part of a broader investigation of C4 oxidation chemistry, along with our companion work on n -butane. The resulting kinetic model is capable of reproducing most of the available n -butane and 1-butene validation targets.

## Processing Notes

- extracted S001021802400542X_mmc6.zip
- extracted S001021802400542X_mmc5.zip
- extracted S001021802400542X_mmc4.zip
- extracted S001021802400542X_mmc2.xlsx
- extracted S001021802400542X_mmc3.docx
- extracted S001021802400542X_mmc1.zip
