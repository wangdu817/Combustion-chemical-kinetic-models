# Understanding low-temperature first-stage ignition delay: Propane

## Bibliography

Shamel S. Merchant, C. Franklin Goldsmith, Aäron G. Vandeputte, Michael P. Burke, Stephen J. Klippenstein, William H. Green. Understanding low-temperature first-stage ignition delay: Propane[J]. Combustion and Flame, 2015, 162: 3658-3673. DOI: 10.1016/j.combustflame.2015.07.005.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 162 / Oct
- Article number: 3658-3673
- DOI: 10.1016/j.combustflame.2015.07.005
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218015002060
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: propane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S0010218015002060_mmc3.txt, _processing/raw_downloads/S0010218015002060_mmc2.txt
- Original thermodynamic source files: _processing/raw_downloads/S0010218015002060_mmc3.txt, _processing/raw_downloads/S0010218015002060_mmc2.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 110
- Reaction count: 56
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 1509 and 1710 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/propane/2015/merchant_2015_propane_3658-3673/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: C3H8 + OH <=> H2O + npropyl Reaction 29: C3H8 + OH <=> H2O + npropyl | Line | | 1504 | Species # 134 RQCISD(T)/CBS//B3LYP/6-311++G(d,p) + BAC by C. F. Goldsmith | 1505 | 2-formyl-ethyl radical | 1506 | CH2CH2CHO H 5 C 3 O 1 G 298.0 3000.0 1000.0 1 | 1507 | | 1508 | reactions: > 1509 > - equation: C3H8 + OH <=> npropyl + H2O # Reaction 1 ^ | 1510 | rate-constant: {A: 1.054e+10, b: 0.97, Ea: 1586.0} | 1511 | note: | | 1512 | HEA ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 2

- Status: cantera_failed
- Species count: 110
- Reaction count: 56
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 1509 and 1710 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/propane/2015/merchant_2015_propane_3658-3673/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: C3H8 + OH <=> H2O + npropyl Reaction 29: C3H8 + OH <=> H2O + npropyl | Line | | 1504 | Species # 134 RQCISD(T)/CBS//B3LYP/6-311++G(d,p) + BAC by C. F. Goldsmith | 1505 | 2-formyl-ethyl radical | 1506 | CH2CH2CHO H 5 C 3 O 1 G 298.0 3000.0 1000.0 1 | 1507 | | 1508 | reactions: > 1509 > - equation: C3H8 + OH <=> npropyl + H2O # Reaction 1 ^ | 1510 | rate-constant: {A: 1.054e+10, b: 0.97, Ea: 1586.0} | 1511 | note: | | 1512 | HEA ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

The low-temperature auto-ignition of fuels is a complex process, occurring in multiple stages with distinct chemical processes governing each stage. The conversion from alkyl radical to chain branching products, which occurs through successive O2 additions followed by thermal decomposition of the products, is at the core of the auto-ignition process. Our detailed understanding of this central process continues to evolve, with recent theoretical kinetics studies providing a particularly comprehensive description of the radical oxidation process for propane. In this study, we employ this improved description in a detailed numerical and analytical exploration of the first-stage ignition delay for low-temperature auto-ignition of propane, which may be considered as a prototype for larger alkane fuels. The traditional first-stage of ignition can be divided into two stages (stage-1A and stage-1B). During stage-1A, the concentration of radicals grows exponentially, and both OH and HO2 are important in the consumption of the fuel and generation of alkyl radicals. Stage-1A ends when the concentration of HO2 is sufficiently high that the chain-terminating bimolecular reaction HO2 + HO2 becomes competitive with other HO2 reactions including HO2 + fuel, thus slowing the HO2 concentration rise such that it is no longer a key contributor to fuel consumption. During stage-1B, increasing temperature and growing side reactions with secondary chemistry reduce the positive feedback and the concentrations of ketohydroperoxide species stop growing exponentially. The end of this stage is associated with the maximum in ketohydroperoxide, after which it is depleted. We present simple analytical approximations for the time it takes to complete these two sub-stages. These expressions clarify which rate constants control first-stage ignition, and they quantify how the ignition is influenced by mixture composition, temperature and pressure. The analysis is also extended to longer alkane fuels and is shown to provide fairly reliable predictions of the first-stage ignition delay.

## Processing Notes

- extracted S0010218015002060_mmc1.docx
