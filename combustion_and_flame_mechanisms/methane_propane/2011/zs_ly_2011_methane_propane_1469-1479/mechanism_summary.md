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
- Species count: 51
- Reaction count: 552
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 576 and 1299 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/methane_propane/2011/zs_ly_2011_methane_propane_1469-1479/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 => O + OH Reaction 277: H + O2 => O + OH | Line | | 571 | - [11.3456574, 0.0180843428, -6.17276514e-06, 9.56925815e-10, | 572 | -5.54586212e-14, -5886.5945, -36.4627206] | 573 | note: '062904' | 574 | | 575 | reactions: > 576 > - equation: H + O2 => O + OH # Reaction 1 ^ | 577 | rate-constant: {A: 3.547e+15, b: -0.406, Ea: 1.66e+04} | 578 | - equation: O + OH => H + O2 # Reaction 2 | 579 | rate-constant: {A: ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 2

- Status: cantera_failed
- Species count: 51
- Reaction count: 552
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 576 and 1299 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/methane_propane/2011/zs_ly_2011_methane_propane_1469-1479/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 => O + OH Reaction 277: H + O2 => O + OH | Line | | 571 | - [11.3456574, 0.0180843428, -6.17276514e-06, 9.56925815e-10, | 572 | -5.54586212e-14, -5886.5945, -36.4627206] | 573 | note: '062904' | 574 | | 575 | reactions: > 576 > - equation: H + O2 => O + OH # Reaction 1 ^ | 577 | rate-constant: {A: 3.547e+15, b: -0.406, Ea: 1.66e+04} | 578 | - equation: O + OH => H + O2 # Reaction 2 | 579 | rate-constant: {A: ... [truncated; see _processing logs]
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

Natural gas is the primary fuel for industrial gas turbines, which provide about one quarter of the world’s primary energy supply. Beside methane it also contains larger hydrocarbons in small, varying ratios. This variation is expected to rise due to the increasing usage of non-traditional gas sources. Fuel composition has a large impact on auto-ignition delay time, which is a fundamental parameter for the optimal design and operation of gas turbines. For the oxidation of such mixtures, Curran, Petersen and co-workers recently developed a detailed reaction mechanism (NUIG NGM), which reproduces the ignition delays over a wide range of conditions. However, due to its large size: 229 species and 1359 reactions, it cannot be used in computational fluid dynamics simulations, which is an important fundamental tool in the development of gas turbines. A mechanism reduction case study of the NUIG NGM is presented using the recently developed simulation error minimization methods (SEM). A new version of the SEM program package is also proposed, which allows the reduction of mechanisms for a wider range of combustion phenomena. Combinational strategies have been introduced in the SEM connectivity method to enhance the reduction procedure and a hierarchical reduction procedure is proposed for multi-scenario problems. Ignition of lean and stoichiometric mixtures containing 90% methane and 10% propane as fuel were investigated for 22 conditions relevant to gas turbines, covering temperature and pressure ranges of 877–1465K and 7–40atm, respectively. The smallest reduced mechanism developed contains 50 species and 186 reactions. It can reproduce ignition delays with 3.1% maximum error and reproduces pressure rise precisely (error∼10−3%). The mechanism can be simulated 62 times faster than the full mechanism. Robustness analysis showed that it is reliably applicable over a much wider range of conditions compared to that for which it was developed.

## Processing Notes

- extracted S0010218010003652_mmc1.zip
- extracted S0010218010003652_mmc2.zip
- extracted S0010218010003652_mmc3.zip
