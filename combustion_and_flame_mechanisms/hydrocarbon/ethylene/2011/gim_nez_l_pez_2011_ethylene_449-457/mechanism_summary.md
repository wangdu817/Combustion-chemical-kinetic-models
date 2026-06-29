# High pressure oxidation of C2H4/NO mixtures

## Bibliography

J. Giménez-López, M.U. Alzueta, C.T. Rasmussen, P. Marshall, P. Glarborg. High pressure oxidation of C2H4/NO mixtures[J]. Combustion and Flame, 2011, 33: 449-457. DOI: 10.1016/j.proci.2010.05.098.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 33 / 
- Article number: 449-457
- DOI: 10.1016/j.proci.2010.05.098
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S1540748910002245
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ethylene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S1540748910002245_mmc1.txt
- Original thermodynamic source files: _processing/raw_downloads/S1540748910002245_mmc1.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 136
- Reaction count: 1958
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 1919 and 6405 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ethylene/2011/gim_nez_l_pez_2011_ethylene_449-457/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 <=> O + OH Reaction 980: H + O2 <=> O + OH | Line | | 1914 | - [2.95257637, 1.3969004e-03, -4.92631603e-07, 7.86010195e-11, | 1915 | -4.60755204e-15, -923.948688, 5.87188762] | 1916 | note: BUR0302 G 8/02 | 1917 | | 1918 | reactions: > 1919 > - equation: H + O2 <=> O + OH # Reaction 1 ^ | 1920 | rate-constant: {A: 3.6e+15, b: -0.41, Ea: 1.66e+04} | 1921 | note: | | 1922 | ******************************************* ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- none
