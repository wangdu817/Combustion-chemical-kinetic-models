# High-temperature oxidation of acetylene by N2O at high Ar dilution conditions and in laminar premixed C2H2 + O2 + N2 flames

## Bibliography

Vladimir A. Alekseev, Nikita Bystrov, Alexander Emelianov, Alexander Eremin, Pavel Yatsenko, Alexander A. Konnov. High-temperature oxidation of acetylene by N2O at high Ar dilution conditions and in laminar premixed C2H2 + O2 + N2 flames[J]. Combustion and Flame, 2022, 238: 111924. DOI: 10.1016/j.combustflame.2021.111924.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 238 / 4
- Article number: 111924
- DOI: 10.1016/j.combustflame.2021.111924
- ScienceDirect URL: https://doi.org/10.1016/j.combustflame.2021.111924
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: acetylene_n2o
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218021006672_mmc4/c2h2_mech_mod.txt
- Original thermodynamic source files: _processing/extracted/s0010218021006672_mmc6/therm_20210418.txt, _processing/extracted/s0010218021006672_mmc5/therm_20210418.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 284
- Reaction count: 3445
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by PlogRate::validate: Error on line 9176 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/acetylene_n2o/2022/alekseev_2022_acetylene_n2o_111924/mechanism.yaml: Invalid rate coefficient for reaction 'C2H3O2 <=> CH3 + CO2' at P = 1.0132e+07, T = 500.0 To fix this error, remove this reaction or contact the author of the reaction/mechanism in question, because the rate expression is mathematically unsound at the temperatures and pressures noted above. | Line | | 9171 | fit btw. 550 and 1650 K with MAE of 0.9%, 4.4% | 9172 | fit bt ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S0010218021006672_mmc2.xlsx
- extracted S0010218021006672_mmc4.zip
- extracted S0010218021006672_mmc6.zip
- extracted S0010218021006672_mmc5.zip
- extracted S0010218021006672_mmc3.xlsx
