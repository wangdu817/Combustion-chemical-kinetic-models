# Experimental and modeling study of the pyrolysis and combustion of dimethoxymethane

## Bibliography

Florence H. Vermeire, Hans-Heinrich Carstensen, Olivier Herbinet, Frédérique Battin-Leclerc, Guy B. Marin, Kevin M. Van Geem. Experimental and modeling study of the pyrolysis and combustion of dimethoxymethane[J]. Combustion and Flame, 2018, 190: 270-283. DOI: 10.1016/j.combustflame.2017.12.001.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 190 / Apr
- Article number: 270-283
- DOI: 10.1016/j.combustflame.2017.12.001
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218017304686
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: dimethoxymethane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218017304686_mmc1/DMMmodel_CHEMKIN.inp
- Original thermodynamic source files: _processing/extracted/s0010218017304686_mmc1/DMMmodel_CHEMKIN.inp
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 351
- Reaction count: 5808
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 3559 and 10951 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/dimethoxymethane/2018/vermeire_2018_dimethoxymethane_270-283/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 <=> O + OH Reaction 2905: H + O2 <=> O + OH | Line | | 3554 | - [2.27684246, -0.0163855063, 2.16051464e-05, -1.3022784e-08, | 3555 | 2.9763776e-12, 2.90968642e+04, -8.9103205] | 3556 | note: "!\tInChI=1S/CHO4/c2-1(3)5-4/h4H" | 3557 | | 3558 | reactions: > 3559 > - equation: H + O2 <=> O + OH # Reaction 1 ^ | 3560 | rate-constant: {A: 1.04e+14, b: 0.0, Ea: 1.5286e+04} | 3561 | note: | | 3562 | !!!!!!!!!! ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S0010218017304686_mmc2.docx
- extracted S0010218017304686_mmc1.zip
- extracted S0010218017304686_mmc3.xlsx
