# Automatic generation of compact kinetic models for large alkane oxidation

## Bibliography

Sirio Brunialti, Xiaoyuan Zhang, Qi Wang, Tiziano Faravelli, S. Mani Sarathy. Automatic generation of compact kinetic models for large alkane oxidation[J]. Combustion and Flame, 2025, 280: 114355. DOI: 10.1016/j.combustflame.2025.114355.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 280 / October
- Article number: 114355
- DOI: 10.1016/j.combustflame.2025.114355
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S001021802500392X
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S001021802500392X/pdfft?md5=12af70667313d2c393421dcd0f00bc9e&pid=1-s2.0-S001021802500392X-main.pdf
- Fuel type: alkane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, rapid compression machine, jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s001021802500392x_mmc2/batch_lumped_mech_C30.yaml, _processing/extracted/s001021802500392x_mmc7/batch_lumped_mech_validation.inp, _processing/extracted/s001021802500392x_mmc4/batch_lumped_mech_PRF.yaml, _processing/extracted/s001021802500392x_mmc10/batch_lumped_mech_validation_ISOC16_highT.yaml, _processing/extracted/s001021802500392x_mmc5/batch_lumped_mech_PRF_highT.inp, _processing/extracted/s001021802500392x_mmc11/batch_lumped_mech_validation_NC12_highT.inp, _processing/extracted/s001021802500392x_mmc3/batch_lumped_mech_PRF.inp, _processing/extracted/s001021802500392x_mmc8/batch_lumped_mech_validation.yaml, _processing/extracted/s001021802500392x_mmc1/batch_lumped_mech_C30.inp, _processing/extracted/s001021802500392x_mmc9/batch_lumped_mech_validation_ISOC16_highT.inp, _processing/extracted/s001021802500392x_mmc6/batch_lumped_mech_PRF_highT.yaml, _processing/extracted/s001021802500392x_mmc12/batch_lumped_mech_validation_NC12_highT.yaml
- Original thermodynamic source files: _processing/extracted/s001021802500392x_mmc2/batch_lumped_mech_C30.yaml, _processing/extracted/s001021802500392x_mmc4/batch_lumped_mech_PRF.yaml, _processing/extracted/s001021802500392x_mmc10/batch_lumped_mech_validation_ISOC16_highT.yaml, _processing/extracted/s001021802500392x_mmc8/batch_lumped_mech_validation.yaml, _processing/extracted/s001021802500392x_mmc6/batch_lumped_mech_PRF_highT.yaml, _processing/extracted/s001021802500392x_mmc12/batch_lumped_mech_validation_NC12_highT.yaml
- Original transport source files: _processing/extracted/s001021802500392x_mmc4/batch_lumped_mech_PRF.yaml, _processing/extracted/s001021802500392x_mmc10/batch_lumped_mech_validation_ISOC16_highT.yaml, _processing/extracted/s001021802500392x_mmc8/batch_lumped_mech_validation.yaml, _processing/extracted/s001021802500392x_mmc6/batch_lumped_mech_PRF_highT.yaml, _processing/extracted/s001021802500392x_mmc12/batch_lumped_mech_validation_NC12_highT.yaml

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 850
- Reaction count: 3007
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: ok
- Species count: 336
- Reaction count: 1821
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 3

- Status: cantera_failed
- Species count: 850
- Reaction count: 3007
- Message: IndexError: index 1 is out of bounds for axis 0 with size 1
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 4

- Status: ok
- Species count: 597
- Reaction count: 2963
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 5

- Status: ok
- Species count: 343
- Reaction count: 1879
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 6

- Status: cantera_failed
- Species count: 850
- Reaction count: 3007
- Message: IndexError: index 1 is out of bounds for axis 0 with size 1
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 7

- Status: cantera_failed
- Species count: 597
- Reaction count: 2963
- Message: IndexError: index 1 is out of bounds for axis 0 with size 1
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 8

- Status: cantera_failed
- Species count: 881
- Reaction count: 3778
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by Reaction::checkBalance: Error on line 29451 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/alkane/2025/brunialti_2025_alkane_114355/mechanism.yaml: The following reaction is unbalanced: CETHE15OOH => 0.1585 C10O + 0.1572 C11O + 0.067 C12O + 0.001 C13O + 0.6724 C2H3 + 0.0257 C2H3CHO + 0.1772 C2H4 + 0.0187 C2H5 + 0.1717 C2H5CHO + 0.0666 C3H5-A + 0.0221 C3H6 + 0.0176 C4H71-4 + 0.018 C4H8-1 + 0.0054 C5H10-1 + 0.1525 C5O + 0.1553 C6O + 0.1541 C7O + 0.1515 C8O + 0.1529 C9O + 0.0078 CH2CHO + 0.0935 CH2O + 0.0062 CH3 + 0.0029 CH3C ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 9

- Status: cantera_failed
- Species count: 881
- Reaction count: 3778
- Message: IndexError: index 1 is out of bounds for axis 0 with size 1
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 10

- Status: cantera_failed
- Species count: 1504
- Reaction count: 5213
- Message: IndexError: index 1 is out of bounds for axis 0 with size 1
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 11

- Status: cantera_failed
- Species count: 1504
- Reaction count: 5213
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by Reaction::checkBalance: Error on line 43843 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/alkane/2025/brunialti_2025_alkane_114355/mechanism.yaml: The following reaction is unbalanced: CETHE15OOH => 0.1585 C10O + 0.1572 C11O + 0.067 C12O + 0.001 C13O + 0.6724 C2H3 + 0.0257 C2H3CHO + 0.1772 C2H4 + 0.0187 C2H5 + 0.1717 C2H5CHO + 0.0666 C3H5-A + 0.0221 C3H6 + 0.0176 C4H71-4 + 0.018 C4H8-1 + 0.0054 C5H10-1 + 0.1525 C5O + 0.1553 C6O + 0.1541 C7O + 0.1515 C8O + 0.1529 C9O + 0.0078 CH2CHO + 0.0935 CH2O + 0.0062 CH3 + 0.0029 CH3C ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 12

- Status: cantera_failed
- Species count: 1504
- Reaction count: 5213
- Message: IndexError: index 1 is out of bounds for axis 0 with size 1
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Large alkanes are principal chemical components in many petroleum and alternative renewable fuels. The development of oxidation models for large alkanes is often complex and time-consuming. A methodology for the automatic generation of detailed and lumped kinetic models of oxidation of large alkanes is presented herein. This procedure is built upon the authors’ previous work (Brunialti et al., 2023), wherein an automatic procedure for generating oxidation models of alkanes based on MAMOX++ software was developed. The procedure is based on a rate rule approach, and it can generate detailed and lumped reaction mechanisms. A new set of rate rules was developed to better describe the reactivity of large alkanes at high and low temperatures. The procedure also includes automatic thermochemical-property computation. The reaction mechanism generation procedure was reviewed to minimize the reaction mechanism size and required user inputs. Detailed reaction mechanism and lumped reaction mechanisms were generated for 40 alkanes with a carbon number of 5–16. The model predictions were compared with experimental data obtained from jet-stirred reactors, shock tubes, rapid compression machines, and laminar burning velocities. Validations were performed for 30 alkanes under a broad range of temperatures, pressures, and equivalence ratios. The predicted and measured values exhibited good agreement under all conditions for all fuels except for large, highly branched alkanes. The lumped models can reproduce the predictions of the detailed models with high fidelity under all explored conditions while considerably reducing the number of species and reactions involved in the reaction mechanism. Software capabilities for modeling the reactivity of extremely large alkanes were assessed in a comparative study for linear alkanes with up to 30 carbon atoms. Detailed and lumped models for gasoline primary reference fuel mixtures were generated and validated to demonstrate the procedure capabilities for generating compact, task-tailored models.

## Processing Notes

- extracted S001021802500392X_mmc8.zip
- extracted S001021802500392X_mmc9.zip
- extracted S001021802500392X_mmc3.zip
- extracted S001021802500392X_mmc6.zip
- extracted S001021802500392X_mmc4.zip
- extracted S001021802500392X_mmc2.zip
- extracted S001021802500392X_mmc1.zip
- extracted S001021802500392X_mmc5.zip
- extracted S001021802500392X_mmc7.zip
- extracted S001021802500392X_mmc10.zip
- extracted S001021802500392X_mmc12.zip
- extracted S001021802500392X_mmc11.zip
