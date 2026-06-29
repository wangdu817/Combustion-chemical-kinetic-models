# Hydrogen–nitrous oxide delay times: Shock tube experimental study and kinetic modelling

## Bibliography

R. Mével, S. Javoy, F. Lafosse, N. Chaumeix, G. Dupré, C.-E. Paillard. Hydrogen–nitrous oxide delay times: Shock tube experimental study and kinetic modelling[J]. Combustion and Flame, 2009, 32: 359-366. DOI: 10.1016/j.proci.2008.06.171.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 32 / 
- Article number: 359-366
- DOI: 10.1016/j.proci.2008.06.171
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S1540748908003180
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: n2o_hydrogen
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S1540748908003180_mmc1.txt
- Original thermodynamic source files: _processing/raw_downloads/S1540748908003180_mmc1.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 32
- Reaction count: 406
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 368 and 1304 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/n2o_hydrogen/2009/m_vel_2009_n2o_hydrogen_359-366/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H2 + M <=> 2 H + M Reaction 204: H2 + M <=> 2 H + M | Line | | 363 | - [2.672146, 3.056293e-03, -8.73026e-07, 1.200996e-10, | 364 | -6.391618e-15, -2.989921e+04, 6.862817] | 365 | note: '20387' | 366 | | 367 | reactions: > 368 > - equation: H2 + M <=> H + H + M # Reaction 1 ^ | 369 | type: three-body | 370 | rate-constant: {A: 4.57e+19, b: -1.4, Ea: 1.0438e+05} | 371 | efficiencies: {H2: 2.5, H2O: 12.0, AR: 0.0} ... | 1299 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- none
