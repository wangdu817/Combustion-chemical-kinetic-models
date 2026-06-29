# Sensitizing effects of NOx on CH4 oxidation at high pressure

## Bibliography

Christian Lund Rasmussen, Anja Egede Rasmussen, Peter Glarborg. Sensitizing effects of NOx on CH4 oxidation at high pressure[J]. Combustion and Flame, 2008, 154: 529-545. DOI: 10.1016/j.combustflame.2008.01.012.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 154 / Aug
- Article number: 529-545
- DOI: 10.1016/j.combustflame.2008.01.012
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218008000795
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: nitric_oxide_methane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S0010218008000795_mmc1.txt
- Original thermodynamic source files: _processing/raw_downloads/S0010218008000795_mmc1.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 62
- Reaction count: 832
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 1037 and 3296 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/nitric_oxide_methane/2008/rasmussen_2008_nitric_oxide_methane_529-545/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 <=> O + OH Reaction 417: H + O2 <=> O + OH | Line | | 1032 | H298 =-37.04 kcal/mol | 1033 | S298 = 78.59 cal/mol/K | 1034 | note: ' Ethylnitrate (CH3CH2-O-N(=O)=O)' | 1035 | | 1036 | reactions: > 1037 > - equation: H + O2 <=> O + OH # Reaction 1 ^ | 1038 | rate-constant: {A: 3.55e+15, b: -0.41, Ea: 1.66e+04} | 1039 | note: | | 1040 | ************************************************************** ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- none
