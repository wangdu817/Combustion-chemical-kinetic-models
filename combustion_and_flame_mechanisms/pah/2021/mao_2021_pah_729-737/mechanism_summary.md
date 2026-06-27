# Unimolecular reactions of the resonance-stabilized cyclopentadienyl radicals and their role in the polycyclic aromatic hydrocarbon formation

## Bibliography

Qian Mao, Can Huang, Martina Baroncelli, Li Shen, Liming Cai, Kai Leonhard, et al.. Unimolecular reactions of the resonance-stabilized cyclopentadienyl radicals and their role in the polycyclic aromatic hydrocarbon formation[J]. Combustion and Flame, 2021, 38: 729-737. DOI: 10.1016/j.proci.2020.08.009.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 38 / 
- Article number: 729-737
- DOI: 10.1016/j.proci.2020.08.009
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S1540748920305939
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: pah
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s1540748920305939_mmc1/PROCI-D-19-01570_Revision_SM/CRECK_revised.mech.mech, _processing/extracted/s1540748920305939_mmc1/PROCI-D-19-01570_Revision_SM/CRECK_decompose.mech.mech, _processing/extracted/s1540748920305939_mmc1/PROCI-D-19-01570_Revision_SM/CRECK Model/CRECK.mech.mech
- Original thermodynamic source files: _processing/extracted/s1540748920305939_mmc1/PROCI-D-19-01570_Revision_SM/CRECK Model/PAH_Milano.thermo
- Original transport source files: _processing/extracted/s1540748920305939_mmc1/PROCI-D-19-01570_Revision_SM/CRECK Model/PAH_Milano.trans

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 244
- Reaction count: 6010
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: ok
- Species count: 244
- Reaction count: 6010
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 3

- Status: cantera_failed
- Species count: 244
- Reaction count: 6010
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by Reaction::checkBalance: Error on line 18176 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/pah/2021/mao_2021_pah_729-737/mechanism.yaml: The following reaction is unbalanced: DCYC5 + H => 3.68 C5H6 + 0.16 C5H7 + 1.68 H + 2.16 H2 + H2O Element Reactants Products C 10 19.200000000000003 H 17 31.200000000000003 O 0 1 | Line | | 18171 | C5H7 # Reaction 5803 | 18172 | rate-constant: {A: 4.079e+05, b: 2.0, Ea: 1.378128e+04} | 18173 | - equation: C3H5-A + DCYC5 => H2 + 0.84 H + C3H6 + 1.84 C5H6 + 0.16 | 18174 | C5H7 # Reaction 58 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S1540748920305939_mmc1.zip
