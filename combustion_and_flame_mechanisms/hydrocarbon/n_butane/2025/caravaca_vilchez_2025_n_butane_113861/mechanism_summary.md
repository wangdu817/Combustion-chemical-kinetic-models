# Advancing the C4 low-temperature oxidation chemistry through species measurements in a rapid compression machine. Part B: n-Butane

## Bibliography

Jesus Caravaca-Vilchez, Jiaxin Liu, Pengzhi Wang, Yuki Murakami, ... Karl Alexander Heufer. Advancing the C4 low-temperature oxidation chemistry through species measurements in a rapid compression machine. Part B: n-Butane[J]. Combustion and Flame, 2025, 272: 113861. DOI: 10.1016/j.combustflame.2024.113861.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 272 / February
- Article number: 113861
- DOI: 10.1016/j.combustflame.2024.113861
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024005704
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218024005704/pdfft?md5=085c928befd99d7835ea6ca32cb787d3&pid=1-s2.0-S0010218024005704-main.pdf
- Fuel type: n_butane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, rapid compression machine, flow reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218024005704_mmc7/NUIGMech1.3_C4_mod.inp, _processing/extracted/s0010218024005704_mmc5/NUIGMech1.3_C4_mod__Commented.cti
- Original thermodynamic source files: _processing/extracted/s0010218024005704_mmc5/NUIGMech1.3_C4_mod__Commented.cti, _processing/extracted/s0010218024005704_mmc6/NUIGMech1.3_C4_mod.dat
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

Studying the oxidation of n-butane, a major component of LNG, is critical to improve the efficiency of transportation engines. Furthermore, its negative temperature coefficient (NTC) behavior provides insights into the oxidation of larger hydrocarbons. Several studies have investigated n-butane oxidation at engine-operating pressures using various methods, including ignition delay time (IDT) measurements in rapid compression machines (RCMs) and shock tubes, flame velocities, and species concentrations in flow reactors. While these species measurements provide deeper insights into oxidation networks than IDTs, they are limited to either low-pressure or highly diluted conditions. To address this gap, this study measures species concentrations during n-butane oxidation at 30 bar in the NTC region (742 K and 855 K, respectively), at stoichiometric and moderate dilution levels in an RCM. A novel two-valve setup allowed gas sample extraction for off-line gas chromatography-mass spectrometry analysis. Complementary IDT data were obtained in the temperature range of 680 − 910 K, at pressures of 15 and 30 bar, and equivalence ratios of 0.5, 1.0, and 2.0. The results suggest that while current n-butane models reasonably predict its autoignition characteristics, they fall short in predicting the formation of key oxidation intermediates at engine-relevant conditions. In this context, the n-butane submechanism within the NUIGMech1.3 framework was updated. Modifications involve recently computed thermochemical data for critical intermediates and adjustments to rate constants, using analogies with structurally similar molecules such as n-propane and n-pentane. The present model reproduces reasonably well both the measured IDT and species concentrations documented herein and data from the literature. Nevertheless, the model slightly underestimates the reactivity within the NTC domain and the formation of some intermediates at the NTC peak. This study highlights the importance of integrating species concentration and IDT measurements at application-relevant conditions to refine kinetic mechanisms and significantly advances the understanding of C 4 hydrocarbon oxidation chemistry. Novelty and Significance Statement The novelty of this research lies in the measurement of species concentrations during the ignition delay of n-butane mixtures in an RCM at high pressures near the NTC minimum and maximum using a novel two-valve gas sampling setup. This, in combination with new thermochemical data and rate rules based on analogies with propane and n-pentane, allowed the refinement of the n-butane sub-mechanism within the NUIGMech1.3 framework. By combining species concentration measurements with ignition delay times in the RCM, this study examines the oxidation of n-butane, a major component of LPG, under conditions that closely mimic engine environments, overcoming the limitations of previous studies limited to highly dilute conditions. This research is part of a broader investigation of C 4 oxidation chemistry, along with our companion work on 1-butene. The resulting kinetic model is capable of reproducing most of the available n-butane and 1-butene validation targets.

## Processing Notes

- extracted S0010218024005704_mmc1.zip
- extracted S0010218024005704_mmc6.zip
- extracted S0010218024005704_mmc7.zip
- extracted S0010218024005704_mmc3.xlsx
- extracted S0010218024005704_mmc4.docx
- extracted S0010218024005704_mmc2.zip
- extracted S0010218024005704_mmc5.zip
- unsupported archive without 7z: ChromatographsGC1.7z
- unsupported archive without 7z: ChromatographsGC2.7z
