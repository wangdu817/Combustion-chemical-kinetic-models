# Experimental and kinetic modeling investigation on ethylcyclohexane low-temperature oxidation in a jet-stirred reactor

## Bibliography

Jiabiao Zou, Xiaoyuan Zhang, Yuyang Li, Lili Ye, Lili Xing, Wei Li, et al.. Experimental and kinetic modeling investigation on ethylcyclohexane low-temperature oxidation in a jet-stirred reactor[J]. Combustion and Flame, 2020, 214: 211-223. DOI: 10.1016/j.combustflame.2019.12.038.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 214 / Apr
- Article number: 211-223
- DOI: 10.1016/j.combustflame.2019.12.038
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218019305966
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ethylcyclohexane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218019305966_mmc2/SMM2-Reaction mechanism.inp
- Original thermodynamic source files: _processing/extracted/s0010218019305966_mmc3/SMM3-Thermodynamic data.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'CHX1*O2J' Ignoring redundant declaration for species 'HX1N36AL' Ignoring redundant declaration for species 'BT14AL1J' Ignoring redundant declaration for species 'HX1N4OJ6Al' Ignoring redundant declaration for species 'CYCHXDCHCH3' Suppressed 15 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Error while reading reaction in chem.inp starting on line 11251: """ ECH1QJ2 = ECH1ENE+HO2 1.0 0.0 0.0 ! MCH1QJ2 = MCH1ENE+HO2 PLOG/ 0.01 4.54E+08 1.05529 2.67E+04/ PLOG/ 0.1 1.46E+08 0.87848 2.53E+04/ PLOG/ 1 1.7144-119 41.2791 -1.49E+04/ PLOG/ 10 1.32E-58 21.54802 2.70E+03/ """ could not convert string to float: '1.7144-119' Error while reading reaction in chem.inp star ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

In this work, the oxidation of ethylcyclohexane was studied in a jet-stirred reactor at 780 Torr, 480–780 K and equivalence ratios of 0.5, 1.0 and 2.0. Synchrotron vacuum ultraviolet photoionization mass spectrometry (SVUV-PIMS) was used for the detection of oxidation products, including a series of reactive intermediates such as cycloalkylhydroperoxides, keto-hydroperoxides, alkenal-hydroperoxides and highly oxygenated molecules. Quantum chemistry calculations were performed to obtain ionization energies for the identification of some important intermediates and energy barriers of several important pathways. On the other hand, this work presents the first efforts on developing a low-temperature oxidation model of ethylcyclohexane. The present model can reasonably capture the low-temperature oxidation reactivities and negative temperature coefficient behaviors observed in both present and previous experimental work of ethylcyclohexane oxidation. Modeling analyses were performed to provide insight into the low-temperature oxidation chemistry of ethylcyclohexane. The two-stage O2 addition mechanism is concluded to dominate the chain-branching process in the low-temperature region. The concerted elimination reactions of cycloalkylperoxy radical and “formally direct” chemically activated reactions of cycloalkyl+O2 result in cycloalkenes and HO2 formation at the negative temperature coefficient region and serve as main chain-termination pathways. Compared with smaller cycloalkanes like cyclohexane and methylcyclohexane, the ethyl sidechain structure in ethylcyclohexane reduces the energy barriers of cycloalkylperoxy radical isomerization and facilitates the formation of keto-hydroperoxides which leads to more pronounced low-temperature oxidation reactivity of ethylcyclohexane.

## Processing Notes

- extracted S0010218019305966_mmc3.zip
- extracted S0010218019305966_mmc2.zip
