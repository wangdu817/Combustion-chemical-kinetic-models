# Shock tube experiments and numerical study on ignition delay times of ethane in super lean and ultra-lean combustion

## Bibliography

Yanping Qu, Chun Zou, Wenxiang Xia, Qianjin Lin, Jinling Yang, Lixin Lu, et al.. Shock tube experiments and numerical study on ignition delay times of ethane in super lean and ultra-lean combustion[J]. Combustion and Flame, 2022, 246: 112462. DOI: 10.1016/j.combustflame.2022.112462.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 246 / 12
- Article number: 112462
- DOI: 10.1016/j.combustflame.2022.112462
- ScienceDirect URL: https://doi.org/10.1016/j.combustflame.2022.112462
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ethane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218022004795_mmc3/mmc3.inp
- Original thermodynamic source files: _processing/extracted/s0010218022004795_mmc2/mmc2.dat, _processing/extracted/s0010218022004795_mmc1/mmc1.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 495
- Reaction count: 2825
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by ThirdBody::checkSpecies: Error on line 5288 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ethane/2022/qu_2022_ethane_112462/mechanism.yaml: Reaction 'H + O + M <=> OHV + M' defines third-body efficiencies for undeclared species: 'X' | Line | | 5283 | | 5284 | reactions: | 5285 | - equation: H + O + M <=> OHV + M # Reaction 1 | 5286 | type: three-body | 5287 | rate-constant: {A: 1.5e+13, b: 0.0, Ea: 5975.0} > 5288 > efficiencies: {H2: 1.0, H2O: 6.5, O2: 0.4, X: 0.4, N2: 0.4, AR: 0.35} ^ | 5289 | note: | | 5290 | Replaced b ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S0010218022004795_mmc3.zip
- extracted S0010218022004795_mmc2.zip
- extracted S0010218022004795_mmc1.zip
