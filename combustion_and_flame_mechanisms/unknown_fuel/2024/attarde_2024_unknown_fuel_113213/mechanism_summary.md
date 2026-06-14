# Development and validation of a comprehensive combustion kinetic model for the oxidation of 3-hexene

## Bibliography

Lalit Y. Attarde, Krithika Narayanaswamy. Development and validation of a comprehensive combustion kinetic model for the oxidation of 3-hexene[J]. Combustion and Flame, 2024, 260: 113213. DOI: 10.1016/j.combustflame.2023.113213.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 260 / February
- Article number: 113213
- DOI: 10.1016/j.combustflame.2023.113213
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023005874
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218023005874_mmc1/3-hexene.inp
- Original thermodynamic source files: _processing/extracted/s0010218023005874_mmc3/therm.dat
- Original transport source files: _processing/extracted/s0010218023005874_mmc4/trans.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 665
- Reaction count: 3859
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by PlogRate::validate: Error on line 31198 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/unknown_fuel/2024/attarde_2024_unknown_fuel_113213/mechanism.yaml: Invalid rate coefficient for reaction 'C6H101-3 + H <=> C6H113-3' at P = 1013.3, T = 300.0 at P = 1.0132e+07, T = 300.0 To fix this error, remove this reaction or contact the author of the reaction/mechanism in question, because the rate expression is mathematically unsound at the temperatures and pressures noted above. | Line | | 31193 | - {P: 10.0 atm, A: 2.03e+26, b: - ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S0010218023005874_mmc2.zip
- extracted S0010218023005874_mmc1.zip
- extracted S0010218023005874_mmc4.zip
- extracted S0010218023005874_mmc3.zip
- extracted comparative_analysis.ods
