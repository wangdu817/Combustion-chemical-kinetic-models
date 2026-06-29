# High-pressure oxidation of methane

## Bibliography

Hamid Hashemi, Jakob M. Christensen, Sander Gersen, Howard Levinsky, Stephen J. Klippenstein, Peter Glarborg. High-pressure oxidation of methane[J]. Combustion and Flame, 2016, 172: 349-364. DOI: 10.1016/j.combustflame.2016.07.016.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 172 / Oct
- Article number: 349-364
- DOI: 10.1016/j.combustflame.2016.07.016
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218016301766
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: methane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218016301766_mmc2/mech.inp
- Original thermodynamic source files: _processing/extracted/s0010218016301766_mmc2/therm.DAT
- Original transport source files: _processing/extracted/s0010218016301766_mmc2/trans.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 68
- Reaction count: 631
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by PlogRate::validate: Error on line 5650 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/methane/2016/hashemi_2016_methane_349-364/mechanism.yaml: Invalid rate coefficient for reaction 'CH2CHOO <=> CH3 + CO2' at P = 1.0132e+07, T = 500.0 To fix this error, remove this reaction or contact the author of the reaction/mechanism in question, because the rate expression is mathematically unsound at the temperatures and pressures noted above. | Line | | 5645 | - {P: 31.6 atm, A: 1.97e+17, b: -2.23, Ea: 2.859e+04} | 5646 | - {P: 100. ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S0010218016301766_mmc2.zip
