# Laminar burning velocity of acetic acid + air flames

## Bibliography

Moah Christensen, Alexander A. Konnov. Laminar burning velocity of acetic acid + air flames[J]. Combustion and Flame, 2016, 170: 12-29. DOI: 10.1016/j.combustflame.2016.05.007.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 170 / Aug
- Article number: 12-29
- DOI: 10.1016/j.combustflame.2016.05.007
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218016300827
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: laminar flame speed

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218016300827_mmc2/Mechanism.txt
- Original thermodynamic source files: _processing/extracted/s0010218016300827_mmc2/Mechanism.txt
- Original transport source files: _processing/extracted/s0010218016300827_mmc2/trans.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 100
- Reaction count: 2280
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 1700 and 6703 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/unknown_fuel/2016/christensen_2016_unknown_fuel_12-29/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: 2 H + M <=> H2 + M Reaction 1141: 2 H + M <=> H2 + M | Line | | 1695 | polarizability: 1.76 | 1696 | rotational-relaxation: 4.0 | 1697 | note: ivanov | 1698 | | 1699 | reactions: > 1700 > - equation: 2 H + M <=> H2 + M # Reaction 1 ^ | 1701 | type: three-body | 1702 | rate-constant: {A: 7.0e+17, b: -1.0, Ea: 0.0} | 1703 | efficiencies: {H2: 0.0, N2: 0.0, H: 0.0, H2O: 14.3, CO: 3.0, CO2: ... | 6698 | 1139 | 6699 | - eq ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S0010218016300827_mmc2.zip
