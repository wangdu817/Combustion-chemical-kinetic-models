# Investigating the impacts of thermochemical group additivity values on kinetic model predictions through sensitivity and uncertainty analyses

## Bibliography

Florian vom Lehn, Liming Cai, Heinz Pitsch. Investigating the impacts of thermochemical group additivity values on kinetic model predictions through sensitivity and uncertainty analyses[J]. Combustion and Flame, 2020, 213: 394-408. DOI: 10.1016/j.combustflame.2019.12.011.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 213 / Mar
- Article number: 394-408
- DOI: 10.1016/j.combustflame.2019.12.011
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218019305632
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218019305632_mmc1/optSequential.chmech, _processing/extracted/s0010218019305632_mmc1/optJoint.chmech
- Original thermodynamic source files: _processing/extracted/s0010218019305632_mmc1/optJoint.chthermo, _processing/extracted/s0010218019305632_mmc1/optSequential.chthermo
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 1024
- Reaction count: 5569
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

The accuracy of species thermochemical properties is important for predicting combustion characteristics by chemical kinetic models due to their impacts on chemical equilibria of elementary reactions and on backward rate coefficients. As they are frequently estimated based on the group additivity method, the underlying group values directly influence the model prediction accuracy. While a number of studies have recently aimed to improve the accuracy of group values, the dependence of kinetic model predictions on the different groups has not yet been investigated in detail before. In the present work, the impact of group thermochemical parameters on ignition prediction is systematically analyzed by means of sensitivity analysis, employing the oxidation of 2-methylhexane (2-MH) as an example. Very high sensitivities are observed at intermediate temperatures for the peroxy group OO/C/H and its adjacent groups in low-temperature intermediate species. Based on uncertainty analysis, optimization potentials are then determined for the group values of enthalpy of formation, standard entropy, and heat capacity, and they are observed to be considerable for certain groups, especially for the enthalpy of formation values of OO/C/H and its adjacent groups. It is also found that the correct and consistent application of optical isomer corrections in the group additivity method is essential for accurate model predictions. The high optimization potentials of a number of groups motivate the extension of an established kinetic model optimization framework as part of this work, calibrating jointly the rate rules and group values against sets of both global model prediction targets and known species thermochemical properties. This methodology is applied to the considered 2-MH model, yielding very good posterior predictions of ignition characteristics. Overall, the results of this study demonstrate that uncertainties in certain group values will strongly propagate into the model prediction, which motivates future research towards a reduction of those uncertainties.

## Processing Notes

- extracted S0010218019305632_mmc1.zip
