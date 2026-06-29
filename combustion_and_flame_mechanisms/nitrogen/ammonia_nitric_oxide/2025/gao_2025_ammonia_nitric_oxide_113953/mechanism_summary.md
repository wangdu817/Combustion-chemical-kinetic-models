# Kinetic mechanism and NOx emission characteristics of the ammonia/alcohol co-combustion explored by reactive molecular dynamics calculation and kinetic numerical simulation

## Bibliography

Yanyan Gao, Ying Guo, Yongqian Xie, Huanhuan Qin, Yulei Guan. Kinetic mechanism and NOx emission characteristics of the ammonia/alcohol co-combustion explored by reactive molecular dynamics calculation and kinetic numerical simulation[J]. Combustion and Flame, 2025, 273: 113953. DOI: 10.1016/j.combustflame.2024.113953.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 273 / March
- Article number: 113953
- DOI: 10.1016/j.combustflame.2024.113953
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S001021802400662X
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S001021802400662X/pdfft?md5=18d10060e4336403a94b4ea6f14d065d&pid=1-s2.0-S001021802400662X-main.pdf
- Fuel type: ammonia_nitric_oxide
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s001021802400662x_mmc2/NH3&C2H5OH.yaml
- Original thermodynamic source files: _processing/extracted/s001021802400662x_mmc2/NH3&C2H5OH.yaml
- Original transport source files: _processing/extracted/s001021802400662x_mmc2/NH3&C2H5OH.yaml

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 96
- Reaction count: 1138
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by parseReactionEquation: Error on line 4480 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ammonia_nitric_oxide/2025/gao_2025_ammonia_nitric_oxide_113953/mechanism.yaml: Trouble processing string 'H2' | Line | | 4475 | type: three-body | 4476 | rate-constant: {A: 1.89e+18, b: -0.85, Ea: 224950.0 cal/mol} | 4477 | - equation: N + O + M <=> NO + M # Reaction 1137 | 4478 | type: three-body | 4479 | rate-constant: {A: 7.6e+14, b: -0.1, Ea: -1770.0 cal/mol} > 4480 > - equation: H2 +M <=> 2H + M # Reaction 1138 ^ | 4481 | type: th ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Renewable alcohol fuels have higher energy density and lower emissions of combustion pollutant, and their co-combustion with ammonia (NH3) can reduce carbon footprint and alleviate energy pressure, which is an effective way to achieve “ammonia economy”. The purpose of this work is to investigate the reaction mechanism of ammonia and alcohol-based fuel co-combustion, focusing on the effect of pyrolysis and oxidation of different alcohols on the combustion behavior of NH3 at various temperatures, and the formation and reduction characteristics of nitric oxide (NO). The ReaxFF molecular dynamics (RMD) simulations show that the C–OH bond dissociation in alcohol molecules can proceed at relatively lower temperatures compared to N–H bond cleavage of NH3 to provide a rich pool of reactive radicals to promote NH3 decomposition and oxidation, and that the addition of ethanol (C2H5OH) enhances the NH3 combustion more significantly than methanol (CH3OH). In addition, the rate for NO formation is lower than that for NO reduction at high temperatures, leading to the decrease of NO emissions. Based on our RMD simulation results and previous work, a chemical kinetic model of C2H5OH/NH3 co-combustion is constructed. The C2H5OH/NH3 co-combustion kinetic numerical simulations at different equivalence ratios and different C2H5OH concentrations show that mixing a small amount of C2H5OH is beneficial to controlling NOx emission in oxygen-rich environment and under different concentrations of C2H5OH mixing, lowering the oxygen content will result in the NH3 not being completely consumed and decreasing the NOx emissions.

## Processing Notes

- extracted S001021802400662X_mmc1.docx
- extracted S001021802400662X_mmc2.zip
