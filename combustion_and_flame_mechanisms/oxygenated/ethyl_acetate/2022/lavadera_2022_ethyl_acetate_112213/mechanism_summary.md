# Experimental and modeling study of NO formation in methyl acetate + air flames

## Bibliography

Marco Lubrano Lavadera, Shishi Li, Christian Brackmann, Alexander A. Konnov. Experimental and modeling study of NO formation in methyl acetate + air flames[J]. Combustion and Flame, 2022, 242: 112213. DOI: 10.1016/j.combustflame.2022.112213.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 242 / 8
- Article number: 112213
- DOI: 10.1016/j.combustflame.2022.112213
- ScienceDirect URL: https://doi.org/10.1016/j.combustflame.2022.112213
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ethyl_acetate
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S0010218022002280_mmc1.txt
- Original thermodynamic source files: _processing/extracted/s0010218022002280_mmc2/mmc2.dat
- Original transport source files: _processing/raw_downloads/S0010218022002280_mmc3.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 284
- Reaction count: 3445
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by PlogRate::validate: Error on line 11533 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ethyl_acetate/2022/lavadera_2022_ethyl_acetate_112213/mechanism.yaml: Invalid rate coefficient for reaction 'C2H3O2 <=> CH3 + CO2' at P = 1.0132e+07, T = 500.0 To fix this error, remove this reaction or contact the author of the reaction/mechanism in question, because the rate expression is mathematically unsound at the temperatures and pressures noted above. | Line | | 11528 | fit btw. 550 and 1650 K with MAE of 0.9%, 4.4% | 11529 | fit ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S0010218022002280_mmc2.zip
