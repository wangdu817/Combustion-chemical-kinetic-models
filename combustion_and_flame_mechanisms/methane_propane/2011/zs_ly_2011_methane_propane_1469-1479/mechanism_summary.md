# Reduction of a detailed kinetic model for the ignition of methane/propane mixtures at gas turbine conditions using simulation error minimization methods

## Bibliography

I.Gy. Zsély, T. Nagy, J.M. Simmie, H.J. Curran. Reduction of a detailed kinetic model for the ignition of methane/propane mixtures at gas turbine conditions using simulation error minimization methods[J]. Combustion and Flame, 2011, 158: 1469-1479. DOI: 10.1016/j.combustflame.2010.12.011.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 158 / Aug
- Article number: 1469-1479
- DOI: 10.1016/j.combustflame.2010.12.011
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218010003652
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: methane_propane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218010003652_mmc1/NUIG_NGM_III_C4_49.inp, _processing/extracted/s0010218010003652_mmc2/CNF_7628_Supp MatRM1_s50r251.inp, _processing/extracted/s0010218010003652_mmc3/CNF_7628_Supp Mat_RM2_s50r186.inp
- Original thermodynamic source files: _processing/extracted/s0010218010003652_mmc1/NUIG_NGM_III_C4_49.inp, _processing/extracted/s0010218010003652_mmc2/CNF_7628_Supp MatRM1_s50r251.inp, _processing/extracted/s0010218010003652_mmc3/CNF_7628_Supp Mat_RM2_s50r186.inp
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 230
- Reaction count: 4978
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 2573 and 8007 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/methane_propane/2011/zs_ly_2011_methane_propane_1469-1479/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 => O + OH Reaction 2490: H + O2 => O + OH | Line | | 2568 | - [9.10784249, 5.27260434e-03, -1.88170543e-06, 3.00561364e-10, | 2569 | -1.77865959e-14, 3774.40183, -21.1741044] | 2570 | note: 1/14/ 5 THERM | 2571 | | 2572 | reactions: > 2573 > - equation: H + O2 => O + OH # Reaction 1 ^ | 2574 | rate-constant: {A: 3.547e+15, b: -0.406, Ea: 1.66e+04} | 2575 | - equation: O + OH => H + O2 # Reaction 2 | 2576 | ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 2

- Status: cantera_failed
- Species count: 51
- Reaction count: 914
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 576 and 1666 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/methane_propane/2011/zs_ly_2011_methane_propane_1469-1479/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 => O + OH Reaction 458: H + O2 => O + OH | Line | | 571 | - [11.3456574, 0.0180843428, -6.17276514e-06, 9.56925815e-10, | 572 | -5.54586212e-14, -5886.5945, -36.4627206] | 573 | note: '062904' | 574 | | 575 | reactions: > 576 > - equation: H + O2 => O + OH # Reaction 1 ^ | 577 | rate-constant: {A: 3.547e+15, b: -0.406, Ea: 1.66e+04} | 578 | - equation: O + OH => H + O2 # Reaction 2 | 579 | rate-constant: {A: ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 3

- Status: cantera_failed
- Species count: 51
- Reaction count: 552
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 576 and 1299 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/methane_propane/2011/zs_ly_2011_methane_propane_1469-1479/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 => O + OH Reaction 277: H + O2 => O + OH | Line | | 571 | - [11.3456574, 0.0180843428, -6.17276514e-06, 9.56925815e-10, | 572 | -5.54586212e-14, -5886.5945, -36.4627206] | 573 | note: '062904' | 574 | | 575 | reactions: > 576 > - equation: H + O2 => O + OH # Reaction 1 ^ | 577 | rate-constant: {A: 3.547e+15, b: -0.406, Ea: 1.66e+04} | 578 | - equation: O + OH => H + O2 # Reaction 2 | 579 | rate-constant: {A: ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S0010218010003652_mmc1.zip
- extracted S0010218010003652_mmc2.zip
- extracted S0010218010003652_mmc3.zip
