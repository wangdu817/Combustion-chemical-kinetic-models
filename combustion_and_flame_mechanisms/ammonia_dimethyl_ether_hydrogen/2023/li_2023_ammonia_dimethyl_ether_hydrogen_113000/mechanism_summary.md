# Effect of H2 addition on laminar burning velocity of NH3/DME blends by experimental and numerical method using a reduced mechanism

## Bibliography

Huizhen Li, Huahua Xiao. Effect of H2 addition on laminar burning velocity of NH3/DME blends by experimental and numerical method using a reduced mechanism[J]. Combustion and Flame, 2023, 257: 113000. DOI: 10.1016/j.combustflame.2023.113000.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 257 / November
- Article number: 113000
- DOI: 10.1016/j.combustflame.2023.113000
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023003760
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ammonia_dimethyl_ether_hydrogen
- Plasma-related mechanism: possible
- Validation reactor/type from abstract: laminar flame speed

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218023003760_mmc1/chem.inp
- Original thermodynamic source files: _processing/extracted/s0010218023003760_mmc1/therm.dat, _processing/extracted/s0010218023003760_mmc1/chem.inp
- Original transport source files: _processing/extracted/s0010218023003760_mmc1/tran.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 78
- Reaction count: 900
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 1430 and 3481 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ammonia_dimethyl_ether_hydrogen/2023/li_2023_ammonia_dimethyl_ether_hydrogen_113000/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 <=> O + OH Reaction 451: H + O2 <=> O + OH | Line | | 1425 | diameter: 3.63 | 1426 | rotational-relaxation: 1.0 | 1427 | note: OIS | 1428 | | 1429 | reactions: > 1430 > - equation: H + O2 <=> O + OH # Reaction 1 ^ | 1431 | rate-constant: {A: 3.547e+15, b: -0.406, Ea: 1.6599e+04} | 1432 | note: |2 | 1433 | H2/O2 mechanism of Li et al. IJCK 36:565 (2004) ... | 3476 | 1 atm | 3477 | - ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S0010218023003760_mmc1.zip
