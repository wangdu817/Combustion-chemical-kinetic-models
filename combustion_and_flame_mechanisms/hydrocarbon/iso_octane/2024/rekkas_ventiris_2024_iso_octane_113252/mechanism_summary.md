# A novel machine learning based lumping approach for the reduction of large kinetic mechanisms for plasma-assisted combustion applications

## Bibliography

Georgios Rekkas-Ventiris, Alfredo Duarte Gomez, Nicholas Deak, Nicholas Kincaid, Perrine Pepiot, Fabrizio Bisetti, et al.. A novel machine learning based lumping approach for the reduction of large kinetic mechanisms for plasma-assisted combustion applications[J]. Combustion and Flame, 2024, 260: 113252. DOI: 10.1016/j.combustflame.2023.113252.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 260 / February
- Article number: 113252
- DOI: 10.1016/j.combustflame.2023.113252
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023006260
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: yes
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218023006260_mmc4/S300R2756.inp, _processing/extracted/s0010218023006260_mmc5/S415R2914.inp
- Original thermodynamic source files: _processing/extracted/s0010218023006260_mmc6/therm.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 316: """ E+N2=>E+N2 2.716000e-07 0.000000e+00 0.000000e+00 JAN/ -1.06590518e+0 7.10758952e-1 -4.03960537e-1 -5.12716486e-3 2.31501531e-1 -7.61748241e-2 -3.93507278e-2 2.47686721e-2 -3.50930457e-3/ TDEP/ E/ MOME DUP """ could not convert string to float: '-1.06590518e+0 7.10758952e-1 -4.03960537e-1 -5.12716486e-3 2.31501531e-1 -7.61748241e-2 -3.93507278e-2 2.47686721e-2 -3.50930457e-3' Error while reading reaction in chem.inp starting on line 320: """ E+N2=>N2(v1)+E 8.499000e-10 0.000000e+00 0.0 JAN/ -1.50263611e+0 2.92964327e-1 -5.42914759e-1 9.12856443e-1 -4.22917418e-2 -2.40028395e-1 3.75264393e-2 2.25394517e-2 -5.20697208e-3/ TDEP/ E/ EXCI/ 0.29/ DUP """ could not convert string to float: '-1.50263611e+0 2.92964327e-1 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 432: """ E+N2=>E+N2 2.716000e-07 0.000000e+00 0.000000e+00 JAN/ -1.06590518e+0 7.10758952e-1 -4.03960537e-1 -5.12716486e-3 2.31501531e-1 -7.61748241e-2 -3.93507278e-2 2.47686721e-2 -3.50930457e-3/ TDEP/ E/ MOME DUP """ could not convert string to float: '-1.06590518e+0 7.10758952e-1 -4.03960537e-1 -5.12716486e-3 2.31501531e-1 -7.61748241e-2 -3.93507278e-2 2.47686721e-2 -3.50930457e-3' Error while reading reaction in chem.inp starting on line 436: """ E+N2=>N2(v1)+E 8.499000e-10 0.000000e+00 0.0 JAN/ -1.50263611e+0 2.92964327e-1 -5.42914759e-1 9.12856443e-1 -4.22917418e-2 -2.40028395e-1 3.75264393e-2 2.25394517e-2 -5.20697208e-3/ TDEP/ E/ EXCI/ 0.29/ DUP """ could not convert string to float: '-1.50263611e+0 2.92964327e-1 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

The development of skeletal mechanisms has become essential for multi-dimensional simulations of plasma-assisted combustion (PAC). However, reduction tools developed for traditional combustion applications are not always applicable to PAC, due to the complex interplay between non-equilibrium plasma and combustion kinetics. Plasma direct relation graph with error propagation (P-DRGEP) is a recent plasma-specific reduction method developed in order to incorporate plasma energy branching in the reduction. In the first part of this work, the applicability of P-DRGEP to large kinetic mechanisms is investigated. A detailed isooctane/air plasma mechanism containing 2805 species and 18457 reactions is reduced to 415 species and 4716 reactions, keeping errors on ignition time within 3% for a wide range of initial conditions: from 750 K to 1200 K, 10 atm and equivalence ratios from 0.75 to 1.50. The second part focuses on isomer lumping, which is another reduction technique widely used in combustion. When applied to PAC, it is shown that the resulting lumped mechanism produces poor results. A novel plasma-specific isomer lumping strategy using machine learning is proposed instead. With the supervised algorithm of gradient boosting, predictive regression models are generated, which describe rate coefficients of lumped reactions adequately. These models are trained with simulation data. Leveraging this newly proposed lumping approach on the reduced mechanism, allows for an additional 28% reduction in the number of species and 19% reduction in the number of reactions. Two different versions are presented: in the first one the models are trained using one input feature (1D), while in the second one, two input features are selected (2D). The resulting lumped mechanism is shown to produce accurate predictions of PAC over the entire parameter space of interest, while significantly decreasing the computational time. Indicatively, with the 1D version the maximum error on ignition time in this range of conditions is 6%. The 2D approach produces even lower errors, which do not exceed 3%. Novelty and significance statement In this work, a novel approach for isomer lumping, in plasma-assisted combustion mechanisms, is demonstrated. This plasma-specific approach, uses predictive machine learning regression models to describe the complex evolution of lumped reaction rate coefficients. Combining it with the plasma direct relation graph with error propagation, a powerful reduction framework is created, which is successfully demonstrated on a detailed isooctane/air plasma kinetic mechanism, via zero-dimensional ignition simulations. This framework constitutes a useful tool towards the creation of highly accurate skeletal mechanisms, which significantly reduce the computational costs of simulations.

## Processing Notes

- extracted S0010218023006260_mmc6.zip
- extracted S0010218023006260_mmc3.zip
- extracted S0010218023006260_mmc4.zip
- extracted S0010218023006260_mmc1.zip
- extracted S0010218023006260_mmc2.zip
- extracted S0010218023006260_mmc5.zip
