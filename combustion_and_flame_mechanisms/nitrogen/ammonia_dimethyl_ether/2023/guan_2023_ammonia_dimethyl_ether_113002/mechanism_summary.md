# A dedicated reduced kinetic model for ammonia/dimethyl-ether turbulent premixed flames

## Bibliography

Wei Guan, Abouelmagd Abdelsamie, Cheng Chi, Zhixia He, Dominique Thévenin. A dedicated reduced kinetic model for ammonia/dimethyl-ether turbulent premixed flames[J]. Combustion and Flame, 2023, 257: 113002. DOI: 10.1016/j.combustflame.2023.113002.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 257 / November
- Article number: 113002
- DOI: 10.1016/j.combustflame.2023.113002
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023003735
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ammonia_dimethyl_ether
- Plasma-related mechanism: no
- Validation reactor/type from abstract: laminar flame speed, burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218023003735_mmc1/mmc1.cti, _processing/extracted/s0010218023003735_mmc2/mmc2.mech
- Original thermodynamic source files: _processing/extracted/s0010218023003735_mmc3/mmc3.therm, _processing/extracted/s0010218023003735_mmc1/mmc1.cti
- Original transport source files: _processing/extracted/s0010218023003735_mmc4/mmc4.tran, _processing/extracted/s0010218023003735_mmc1/mmc1.cti

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 48
- Reaction count: not parsed
- Message: CanteraError: ******************************************************************************* CanteraError thrown by newSolution: The CTI and XML formats are no longer supported. *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: ok
- Species count: 48
- Reaction count: 294
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Ammonia ( NH 3 ) as a promising energy vector receives growing interest to reduce carbon emissions in combustion applications. Co-firing with dimethyl ether (DME) is an outstanding route to enhance the combustion properties of ammonia. In this study, a reduced model for NH 3 /DME blend fuels made up of 48 species and 294 reactions was developed starting from a detailed kinetic mechanism. The overall agreement of the reduced model compared with both experimental data and predictions from the original one are good, in terms of ignition delay times, laminar flame speeds, species mole fraction profiles, and S-curves for a variety of NH 3 /DME mixtures. Additionally, the fidelity of the reduced model has been further evaluated by comparing with other detailed kinetic models from the literature. Using this reduced mechanism, a parametric analysis of one-dimensional flames reveals a trade-off in terms of emissions ( NO x vs. CO 2 ), equivalence ratios, and flame propagation characteristics. The ultimate objective of this study is to investigate ignition and turbulent flame dynamics. As a first step in this direction, a turbulent premixed flame of a rich NH 3 /DME mixture with 25% DME content is investigated by direct numerical simulation (DNS) using the reduced mechanism, and conditional averages are analyzed. This work paves the way for future systematic studies of turbulent NH 3 /DME flames by DNS.

## Processing Notes

- extracted S0010218023003735_mmc1.zip
- extracted S0010218023003735_mmc2.zip
- extracted S0010218023003735_mmc4.zip
- extracted S0010218023003735_mmc3.zip
