# Combustion kinetics of the e-fuels methyl formate and dimethyl carbonate: A modeling and experimental study

## Bibliography

Jianfei Yang, Sascha Jacobs, Chaimae Bariki, Joachim Beeckmann, ... Liming Cai. Combustion kinetics of the e-fuels methyl formate and dimethyl carbonate: A modeling and experimental study[J]. Combustion and Flame, 2025, 276: 114112. DOI: 10.1016/j.combustflame.2025.114112.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 276 / June
- Article number: 114112
- DOI: 10.1016/j.combustflame.2025.114112
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025001506
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025001506/pdfft?md5=0b6c3d115766aee132444f1bbdd655b3&pid=1-s2.0-S0010218025001506-main.pdf
- Fuel type: methyl_formate_ethyl_formate_dimethyl_carbonate
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/kinetic_model/Chemkin_format/Chemkin_mech.inp.txt
- Original thermodynamic source files: _processing/extracted/kinetic_model/FlameMaster_format/DMC_model.thermo.txt, _processing/extracted/kinetic_model/Chemkin_format/Chemkin_thermo.txt
- Original transport source files: _processing/extracted/kinetic_model/FlameMaster_format/DMC_model.trans.txt, _processing/extracted/kinetic_model/Chemkin_format/Chemkin.trans.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 185
- Reaction count: 1174
- Message: CanteraError: ******************************************************************************* CanteraError thrown by GasTransportData::validate: invalid geometry for species 'C8H2'. 'atom' specified, but species contains multiple atoms. *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

The Oxygenated hydrocarbons methyl formate (MeFo) and dimethyl carbonate (DMC) are regarded as promising e-fuel candidates. Their blends were investigated in engine experiments, showing satisfactory performance. In this work, the reaction kinetics of MeFo, DMC, and their blends are thus investigated for a deep understanding of their fundamental combustion characteristics. A chemical mechanism is proposed based on a newly developed MeFo model, which was revised by including missing reaction channels, incorporating rate and thermochemical data calculated theoretically at a high level, and modifying rate constants of sensitive reactions. In a comprehensive comparison of literature models with all available experimental data, the DMC mechanism of Sun et al. (Sun et al., 2016) shows the best performance, and its DMC-specific chemistry is thus added to the MeFo mechanism. The DMC submechanism is further revised in terms of reaction pathways and rate coefficients for improved prediction accuracy, where the rate coefficients of DMC reactions are updated analogously to the corresponding reactions in the MeFo submechanism if applicable, according to the similar C-H bond dissociation energies of DMC and MeFo. The mechanism is validated based on both experimental literature data for neat MeFo and DMC as well as new ignition delay times and laminar burning velocities measured as part of this study for their blends. Good agreement is observed between model predictions and experiments over a wide range of conditions. Finally, the underlying reaction pathways of neat MeFo and DMC as well as their blends are explored by means of reaction flux analysis, and implications are discussed in terms of their engine application potentials. It is revealed that the blending has a very minor impact on the underlying relative reaction fluxes of the two components. Novelty and Significance Statement The reaction kinetics of the promising e-fuel candidates MeFo, DMC, and their blends are investigated experimentally and numerically in this work. New experimental data of ignition delay times and laminar burning velocities are reported for the blends of MeFo and DMC, which are missing in the literature. A new kinetic model is proposed, which is validated successfully against all available literature data for neat MeFo and DMC as well as the new experimental results obtained as part of this study. The reaction pathways of MeFo, DMC, and their blends are explored. It is revealed that the blending has a very minor impact on the underlying relative reaction fluxes of the two components.

## Processing Notes

- extracted S0010218025001506_mmc1.zip
- extracted Experimental data.zip
- extracted Kinetic model.zip
- extracted Volume profile.zip
