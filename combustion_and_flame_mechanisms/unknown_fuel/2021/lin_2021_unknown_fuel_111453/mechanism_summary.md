# An improved 2-pentanone low to high-temperature kinetic model using Bayesian Optimization algorithm

## Bibliography

Qianjin Lin, Chun Zou, Shibo Liu, Yunpeng Wang, Lixin Lu, Chao Peng. An improved 2-pentanone low to high-temperature kinetic model using Bayesian Optimization algorithm[J]. Combustion and Flame, 2021, 231: 111453. DOI: 10.1016/j.combustflame.2021.111453.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 231 / Sep
- Article number: 111453
- DOI: 10.1016/j.combustflame.2021.111453
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218021001930
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: laminar flame speed

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218021001930_mmc2/MPK_optimized.inp
- Original thermodynamic source files: _processing/extracted/s0010218021001930_mmc2/SMM2_therm.dat
- Original transport source files: _processing/extracted/s0010218021001930_mmc2/SMM2_trans.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 576
- Reaction count: 3121
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

The ignition delay times (IDTs) of 2-pentanone (methyl propyl ketone, MPK) were measured at equivalence ratios of 0.5, 1.0, and 1.5, pressures of 1 bar and 5 bar, and temperatures ranging between 1227 and 1571 K. A MPK low to high-temperature model was constructed on the basis of Pieper model and Fenard model. The improvement of the model is that the rate constants of sixteen MPK decomposition and hydrogen abstraction reactions (R1–R16) obtained by the analogy-based method, were globally optimized by the Bayesian Optimization algorithm using the high-temperature IDTs. The optimized model well predicts the laminar flame speeds (measured by Li et al.) and the IDTs and species profiles in low-temperature (measured by Fenard et al.). There is no overfitting during the optimization process. Therefore, the optimization method and the optimized MPK model are reliable. The comparisons of the optimized model with Pieper model and Fenard model were performed by the reaction pathway analysis and sensitivity analysis for the predictions of the MPK profile, the low and high-temperature IDTs and the laminar flame speeds. Because of the difference in the molecular structure between MPK and 2-butanone, remaining the branching ratio among three MPK decompositions (R1–R3) and the ratio among the rate constants of the MPK hydrogen abstraction reactions by OH, H and CH3 unchanged is unnecessary in the development of the MPK model using the analogy-based method, while the branching ratio of the hydrogen abstraction reactions at carbon 1, 3, and 5 remains unchanged. The competition among the decomposition and hydrogen abstraction reactions of MPK is intricate and crucial to the low and high-temperature oxidation. It is necessary to globally optimize the rate constants of R1-R16 based on the multidimensional experimental results, such as low and high-temperature IDTs, laminar flame speeds, and species profiles.

## Processing Notes

- extracted S0010218021001930_mmc1.docx
- extracted S0010218021001930_mmc2.zip
