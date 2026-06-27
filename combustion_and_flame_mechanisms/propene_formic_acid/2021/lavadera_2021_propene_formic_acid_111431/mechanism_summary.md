# Laminar burning velocities of propionic acid + air flames: Experimental, modeling and data consistency study

## Bibliography

Marco Lubrano Lavadera, Alexander A. Konnov. Laminar burning velocities of propionic acid + air flames: Experimental, modeling and data consistency study[J]. Combustion and Flame, 2021, 230: 111431. DOI: 10.1016/j.combustflame.2021.111431.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 230 / Aug
- Article number: 111431
- DOI: 10.1016/j.combustflame.2021.111431
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S001021802100170X
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: propene_formic_acid
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S001021802100170X_mmc3.txt
- Original thermodynamic source files: _processing/raw_downloads/S001021802100170X_mmc2.txt
- Original transport source files: _processing/raw_downloads/S001021802100170X_mmc1.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 255
- Reaction count: 3038
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by PlogRate::validate: Error on line 10852 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/propene_formic_acid/2021/lavadera_2021_propene_formic_acid_111431/mechanism.yaml: Invalid rate coefficient for reaction 'C2H3O2 <=> CH3 + CO2' at P = 1.0132e+07, T = 500.0 To fix this error, remove this reaction or contact the author of the reaction/mechanism in question, because the rate expression is mathematically unsound at the temperatures and pressures noted above. | Line | | 10847 | fit btw. 550 and 1650 K with MAE of 0.9%, 4.4% | ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Laminar burning velocities of propionic acid + air flames have been determined using the heat flux method at atmospheric pressure and initial gas mixture temperature of 348 K over the range of equivalence ratios 0.7–1.3. The detailed kinetic model of the authors was extended by the reactions of propionic acid and its intermediates. Attention has been paid to the proper description of the formation and consumption of 1,1-propenediol, methyl ketene, and acrylic acid. New experimental results have been compared with the modelling using this kinetic mechanism and the mechanism of Zhang et al. (2021). The comparison of the new and available from the literature measurements obtained at different initial temperatures with predictions of the two models allowed for analysis of the data consistency for the burning velocities of propionic acid, as well as for acetic and formic acids. Inconsistencies of some datasets for these short-chain carboxylic acids were identified and discussed.

## Processing Notes

- none
