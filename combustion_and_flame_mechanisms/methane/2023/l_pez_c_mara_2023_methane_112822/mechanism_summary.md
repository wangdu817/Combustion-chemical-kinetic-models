# Reduced chemical kinetic model for CH4-air non-premixed flames including excited and charged species

## Bibliography

Claudia-F. López-Cámara, Chiara Saggese, William J. Pitz, Xiao Shao, Hong G. Im, Derek Dunn-Rankin. Reduced chemical kinetic model for CH4-air non-premixed flames including excited and charged species[J]. Combustion and Flame, 2023, 253: 112822. DOI: 10.1016/j.combustflame.2023.112822.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 253 / July
- Article number: 112822
- DOI: 10.1016/j.combustflame.2023.112822
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023002031
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: methane
- Plasma-related mechanism: possible
- Validation reactor/type from abstract: burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S0010218023002031_mmc5.txt, _processing/extracted/s0010218023002031_mmc2/LUCI-Model1.inp
- Original thermodynamic source files: _processing/raw_downloads/S0010218023002031_mmc3.txt, _processing/raw_downloads/S0010218023002031_mmc6.txt
- Original transport source files: _processing/raw_downloads/S0010218023002031_mmc7.txt, _processing/extracted/s0010218023002031_mmc4/transport_LUCI_Model1.inp

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 45
- Reaction count: 216
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Electric fields can impact small laminar flames by changing their shape and overall behavior by acting on charged species produced in combustion. However, no reduced chemical kinetic model has been developed considering both major species and minor species related to flame characterization and flame behavior in the presence of an electric field. This study presents a reduced chemical kinetic model for methane-air combustion which includes minor excited species ( CH * and OH * ) and charged species ( H 3 O + , HCO + , C 2 H 3 O + , CH 5 O + , O 2 − , OH − , e − , CO 3 − , CHO 2 − , O − , CHO 3 − ). The results employing the reduced chemistry model have been validated for a two-dimensional flame geometry by comparison with (i) detailed chemistry simulation results for species location and peak values, and (ii) experimental CH * chemiluminescence location, considering the self-repulsion of charges yet without externally applied electric field to the flame. This reduced chemical kinetic model, with 45 species and 216 reactions, shows a computational demand one-third that of employing its equivalent detailed chemistry (83 species and 394 reactions). The reduction is modest but significant considering that high fidelity is needed to capture the behavior of the chemi-ion and chemiluminescent species. Future works will involve the use of this model for simulations predicting flame behavior with applied electric field (i.e., field strength ≠ 0 kV/cm).

## Processing Notes

- extracted S0010218023002031_mmc2.zip
- extracted S0010218023002031_mmc4.zip
