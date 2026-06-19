# Chemical kinetics modeling for combustion of Al in CO2

## Bibliography

Masatoshi Saba, Takafumi Kato, Tatsuo Oguchi. Chemical kinetics modeling for combustion of Al in CO2[J]. Combustion and Flame, 2021, 233: 111613. DOI: 10.1016/j.combustflame.2021.111613.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 233 / Nov
- Article number: 111613
- DOI: 10.1016/j.combustflame.2021.111613
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218021003564
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218021003564_mmc2/AlOCtotalmechv2.inp
- Original thermodynamic source files: _processing/extracted/s0010218021003564_mmc2/AlOCtotalmechv2.inp
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 35
- Reaction count: 210
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 397 and 1206 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/unknown_fuel/2021/saba_2021_unknown_fuel_111613/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: 2 O + M <=> O2 + M Reaction 106: 2 O + M <=> O2 + M | Line | | 392 | - [10.3942695, 2.95586337e-03, -1.31542646e-06, 2.58978621e-10, | 393 | -1.87286249e-14, -1.7112571e+04, -19.7026002] | 394 | note: gpop | 395 | | 396 | reactions: > 397 > - equation: O + O + M <=> O2 + M # Reaction 1 ^ | 398 | type: three-body | 399 | rate-constant: {A: 1.62e+14, b: 0.0, Ea: -1787.8} | 400 | efficiencies: {N2: 0.133, O2: 0.133, CO: 0.25, C ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

A detailed reaction mechanism for the oxidation of aluminum with CO2 in the gas phase has been investigated. Quantum chemical calculations were performed to obtain molecular structures of reaction intermediates and transition states on the reaction pathways. A highly accurate method was applied to calculate potential energies and thermodynamic properties for the molecular structures. The rate coefficients of each reaction path were also obtained from calculations on the chemical reaction theory. A detailed chemical kinetic model was constructed from obtained rate coefficients and thermodynamic properties of molecules. Chemical kinetic analysis showed the Al + CO2 ⇔ AlO + CO reaction and Al2 + CO2 ⇔ Al2O + CO reaction were predominant in that reaction system.

## Processing Notes

- extracted S0010218021003564_mmc2.zip
