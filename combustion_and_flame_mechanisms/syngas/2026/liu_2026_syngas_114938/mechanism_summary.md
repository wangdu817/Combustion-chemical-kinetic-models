# Experimental and modeling study of pressure and NOx addition effects on syngas oxidation in a flow reactor

## Bibliography

Yunyang Liu, Erjiang Hu, Jiajun You, Xiaoyang Guo, ... Zuohua Huang. Experimental and modeling study of pressure and NOx addition effects on syngas oxidation in a flow reactor[J]. Combustion and Flame, 2026, 287: 114938. DOI: 10.1016/j.combustflame.2026.114938.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 287 / May
- Article number: 114938
- DOI: 10.1016/j.combustflame.2026.114938
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026001744
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: syngas
- Plasma-related mechanism: no
- Validation reactor/type from abstract: flow reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing\extracted\s0010218026001744_mmc2\Supplementary Material 2_chem.inp
- Original thermodynamic source files: _processing\extracted\s0010218026001744_mmc3\Supplementary Material 3_thermo.dat
- Original transport source files: _processing\extracted\s0010218026001744_mmc4\Supplementary Material 4_tran.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 39
- Reaction count: 203
- Message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 689 and 914 of E:\mech_collection\combustion_and_flame_mechanisms\syngas\2026\liu_2026_syngas_114938\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 41: H2 + M <=> 2 H + M
Reaction 1: 2 H + O2 <=> H2 + O2

|  Line |
|   684 |     well-depth: 200.0
|   685 |     diameter: 3.9
|   686 |     rotational-relaxation: 1.0
|   687 | 
|   688 | reactions:
>   689 > - equation: H2 + M <=> H + H + M  # Reaction 1
            ^
|   690 |   type: three-body
|   691 |   rate-constant: {A: 4.577e+19, b: -1.4, Ea: 1.044e+05}
|   692 |   efficiencies: {H2: 2.5, H2O: 12.0, CO: 1.9, CO2: 3.8, HE: 0.83, CH4: 2.0,
...
|   909 |   rate-constant: {A: 3.93e+13, b: 0.0, Ea: 0.0}
|   910 |   note: '\Author: SP !\Ref: YU ET AL., JCP, 2008, 129(21) !\Comment: WARNING'
|   911 | - equation: CO + H2O <=> CO2 + H2  # Reaction 40
|   912 |   rate-constant: {A: 2.0e+11, b: 0.0, Ea: 3.8e+04}
|   913 |   note: POLIMI Mech
>   914 > - equation: H + O2 + H <=> H2 + O2  # Reaction 41
            ^
|   915 |   rate-constant: {A: 8.8e+22, b: -1.835, Ea: 800.0}
|   916 |   note: |-
|   917 |     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
*******************************************************************************

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Nitrogen oxides (NOx) are important pollutants in gas turbines, and their presence substantially influences fuel oxidation processes. Syngas is a promising clean alternative fuel. A systematic understanding of the interactions between syngas and NOx is crucial for controlling syngas combustion in gas turbines and for developing accurate kinetic models for high-carbon fuels. In this study, oxidation experiments of coal-derived syngas with 0-1850 ppm NOx added were conducted in a high-pressure flow reactor under conditions of 1.9-18.0 atm and 623-1273 K. A kinetic model for H2/CO/NOx mixtures applicable to high-pressure conditions was developed and extensively validated against species concentrations, laminar burning velocities, and ignition delay times. The present model accurately reproduces both newly measured and literature data. This validation covers a wide range of temperatures (298-2200 K), pressures (1.0-100.0 atm), and equivalence ratios (0.03-2.0). Experimental results show that increasing pressure markedly lowers the onset temperature of syngas oxidation but suppresses its intermediate-temperature oxidation rate, with maximum differences of 211.1 K and 37.1%, respectively. At 18.0 atm, the addition of NOx promotes low-temperature oxidation while inhibiting intermediate-temperature oxidation, whereas at 1.9 atm, it suppresses oxidation across the entire temperature range. Kinetic analysis reveals that both pressure and NOx addition regulate syngas oxidation primarily by affecting the formation and consumption of OH radicals. Under high-pressure and low-temperature conditions, the reactions H2 + NO2 = H + HONO, H2 + NO2 = H + HNO2, and CO + NO2 = CO2 + NO make significant contributions to syngas oxidation. In contrast, the NO–HNO cycles play key roles in radical consumption within the intermediate-temperature regime. These high-pressure experimental data and the kinetic model provide valuable guidance for high-pressure combustion control in syngas-fueled gas turbines. Novelty and significance statement The novelty of this work lies in the systematic investigation of syngas oxidation characteristics over a wide range of temperatures, pressures, and NOx addition levels. To ensure industrial relevance, experiments were conducted using a representative coal-derived syngas composition. In parallel, a detailed kinetic model was developed to describe syngas combustion as well as NOx formation and consumption. The model accurately captures the trends in species concentrations during the conversion processes of NOx and their interactions with syngas across the entire temperature range examined. It successfully reproduces both the new experimental measurements and data reported in the literature, including species concentration profiles, laminar burning velocities, and ignition delay times under a wide variety of conditions. Overall, this study provides essential data for elucidating the syngas-NOx interactions. It also provides a validated kinetic framework that supports high-carbon fuel combustion modeling and the development of practical syngas-fueled gas turbines.

## Processing Notes

- none
