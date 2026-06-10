# Bayesian sequential experimental design for combustion kinetic models: A surrogate-assisted nonlinear framework with improved information gain

## Bibliography

Chengcheng Liu, Chenyue Tao, Chenxuan Li, Peng Zhang, ... Bin Yang. Bayesian sequential experimental design for combustion kinetic models: A surrogate-assisted nonlinear framework with improved information gain[J]. Combustion and Flame, 2026, 284: 114610. DOI: 10.1016/j.combustflame.2025.114610.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 284 / February
- Article number: 114610
- DOI: 10.1016/j.combustflame.2025.114610
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025006479
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Validation reactor/type from abstract: jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: extracted\s0010218025006479_mmc2\mmc2.yaml
- Original thermodynamic source files: extracted\s0010218025006479_mmc2\mmc2.yaml
- Original transport source files: extracted\s0010218025006479_mmc2\mmc2.yaml

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 38
- Reaction count: 262
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Informative experimental data are critical for developing predictive combustion kinetic models. Bayesian Sequential Experimental Design (BSED) provides a principled framework to identify experimental conditions that maximize the Expected Information Gain (EIG). However, its application to kinetic model optimization is often limited by high computational cost and potential model misspecification which leads to suboptimal designs. To address these challenges, this study introduces the Surrogate Accelerated BSED (SABSED) framework and demonstrates its implementation on a semi-automated Jet-Stirred Reactor (JSR) platform. SABSED is a surrogate-assisted nonlinear design framework that avoids input–output linearization approximations and improves experimental efficiency through enhanced information gain. The framework integrates multiple strategies to enhance both efficiency and robustness. For efficiency, it employs Artificial Neural Networks (ANNs) trained on multi-scenario datasets to accelerate simulations, utilizes reverse Kullback–Leibler divergence for rapid EIG evaluation, and applies ANN-based Hamiltonian Monte Carlo for efficient Bayesian inference. For robustness, it introduces a heteroscedastic Gaussian Process Regression (GPR) surrogate model to define a modified EIG criterion (EIG_GPR) that accounts for prediction–measurement difference, improving real-world design reliability. Validation using ammonia combustion data, including ignition delay times (IDT), laminar burning velocities (LBV), and species profiles from JSR experiments, demonstrates that both EIG and EIG_GPR substantially reduce predictive errors and uncertainties within 20 iterations. In the LBV case, EIG_GPR achieved the target error threshold with five times fewer iterations than EIG. For newly designed JSR experiments, EIG_GPR accelerated the design and optimization process by 15 times, completing the design within 30 s on a single-core CPU. Overall, the SABSED framework significantly enhances the efficiency of developing combustion reaction kinetic models, paving the way for autonomous experimentation and automatic model optimization.

## Processing Notes

- extracted S0010218025006479_mmc1.docx
- extracted S0010218025006479_mmc2.zip
- extracted S0010218025006479_mmc3.xlsx
- extracted S0010218025006479_mmc4.xlsx
- extracted S0010218025006479_mmc5.xlsx
- extracted S0010218025006479_mmc6.zip
