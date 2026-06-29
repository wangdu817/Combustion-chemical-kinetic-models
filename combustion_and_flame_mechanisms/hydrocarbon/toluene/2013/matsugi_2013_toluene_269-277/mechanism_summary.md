# Modeling of two- and three-ring aromatics formation in the pyrolysis of toluene

## Bibliography

Akira Matsugi, Akira Miyoshi. Modeling of two- and three-ring aromatics formation in the pyrolysis of toluene[J]. Combustion and Flame, 2013, 34: 269-277. DOI: 10.1016/j.proci.2012.06.032.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 34 / 
- Article number: 269-277
- DOI: 10.1016/j.proci.2012.06.032
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S154074891200140X
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: toluene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S154074891200140X_mmc1.txt
- Original thermodynamic source files: _processing/raw_downloads/S154074891200140X_mmc1.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 289
- Reaction count: 1934
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 3243 and 7476 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/toluene/2013/matsugi_2013_toluene_269-277/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: 2 H + M <=> H2 + M Reaction 968: 2 H + M <=> H2 + M | Line | | 3238 | - [57.0008589, 0.0572256729, -2.16260755e-05, 3.61159401e-09, | 3239 | -2.19832148e-13, 1.13399177e+05, -290.191298] | 3240 | note: 10/07/93 MM395 | 3241 | | 3242 | reactions: > 3243 > - equation: H + H + M <=> H2 + M # Reaction 1 ^ | 3244 | type: three-body | 3245 | rate-constant: {A: 1.0e+18, b: -1.0, Ea: 0.0} | 3246 | efficiencies: {H2: 0.0} ... | 7471 | ref ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- none
