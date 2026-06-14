# A novel object-oriented directed path screening method for reduction of detailed chemical kinetic mechanism

## Bibliography

Wei Li, Tiemin Xuan, Qian Wang, Liming Dai. A novel object-oriented directed path screening method for reduction of detailed chemical kinetic mechanism[J]. Combustion and Flame, 2023, 251: 112727. DOI: 10.1016/j.combustflame.2023.112727.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 251 / May
- Article number: 112727
- DOI: 10.1016/j.combustflame.2023.112727
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023001128
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: laminar flame speed, burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218023001128_mmc1/DEGEP-M3.inp, _processing/extracted/s0010218023001128_mmc1/DEGEP-M2.inp, _processing/extracted/s0010218023001128_mmc1/DEGEP-M4.inp, _processing/extracted/s0010218023001128_mmc1/OoDPS-M1.inp, _processing/extracted/s0010218023001128_mmc1/OoDPS-M3.inp, _processing/extracted/s0010218023001128_mmc1/Tian-Detail.inp, _processing/extracted/s0010218023001128_mmc1/OoDPS-M2.inp, _processing/extracted/s0010218023001128_mmc1/DEGEP-M1.inp, _processing/extracted/s0010218023001128_mmc1/OoDPS-M4.inp
- Original thermodynamic source files: _processing/extracted/s0010218023001128_mmc1/thermo.dat
- Original transport source files: _processing/extracted/s0010218023001128_mmc1/tran.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 46
- Reaction count: 308
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Numerical simulation is widely recognized as an efficient means of developing high-performance combustors. However, its efficiency is limited by the growing size of chemical kinetic mechanisms, which increases computation costs. To substantially reduce the size of mechanism while retaining the accuracy, an object-oriented directed path screening (OoDPS) method is proposed in this study. In this methodology, species are ranked according to the order in which they are generated in flame, then reactions are ranked according to the generation of the species in the left hand side of each reaction. A set of important species codetermining the accurate prediction of concerned combustion characteristics are predefined as the "Object". Calibration databases are extracted from laminar premixed flames simulated using the detailed mechanism with equivalence ratio varying from 0.7 to 1.5. The contributions of each reaction in the detailed mechanism to the production/consumption of each species in the Object are evaluated. The size of the reduced mechanism depends on the user-defined contribution coefficient threshold. In this study, a detailed mechanism for methane-ammonia oxidation, consisted of 84 species and 703 reactions, is applied to demonstrate the reliability of the OoDPS method. Several derived skeletal mechanisms are validated against the detailed mechanism. OoDPS method shows a better performance than DRGEP in predicting the laminar burning velocity and ignition delay time at the same level of reaction number. For diffusion flames, OoDPS remains superior to DRGEP in predicting the concentration profiles of H, O and OH, and this superiority becomes more significant for reduced mechanism with less reactions. Unfortunately, as the size of reaction decreases from 703 to 109, the accuracy of OoDPS-generated skeletal mechanism decreases as the increase of ammonia in the fuel, which can be restrained by extending the calibration databases.

## Processing Notes

- extracted S0010218023001128_mmc1.zip
