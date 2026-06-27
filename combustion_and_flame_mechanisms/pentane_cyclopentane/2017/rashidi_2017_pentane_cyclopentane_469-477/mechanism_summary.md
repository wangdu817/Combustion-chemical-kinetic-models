# Elucidating reactivity regimes in cyclopentane oxidation: Jet stirred reactor experiments, computational chemistry, and kinetic modeling

## Bibliography

Mariam J. Al Rashidi, Sébastien Thion, Casimir Togbé, Guillaume Dayma, Marco Mehl, Philippe Dagaut, et al.. Elucidating reactivity regimes in cyclopentane oxidation: Jet stirred reactor experiments, computational chemistry, and kinetic modeling[J]. Combustion and Flame, 2017, 36: 469-477. DOI: 10.1016/j.proci.2016.05.036.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 36 / 
- Article number: 469-477
- DOI: 10.1016/j.proci.2016.05.036
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S1540748916300360
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: pentane_cyclopentane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s1540748916300360_mmc2/CPT_mech_REVIEWERS_ONLY.inp
- Original thermodynamic source files: _processing/extracted/s1540748916300360_mmc2/CPT_thermo_REVIEWERS_ONLY.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 1616
- Reaction count: 9566
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by Reaction::checkBalance: Error on line 22644 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/pentane_cyclopentane/2017/rashidi_2017_pentane_cyclopentane_469-477/mechanism.yaml: The following reaction is unbalanced: H + P-C6H3O2 <=> C2H2 + 2 CO Element Reactants Products C 6 4 H 4 2 | Line | | 22639 | rate-constant: {A: 1.4e+13, b: 0.0, Ea: 1.47e+04} | 22640 | - equation: P-C6H4O2 + OH <=> P-C6H3O2 + H2O # Reaction 1701 | 22641 | rate-constant: {A: 1.0e+06, b: 2.0, Ea: 4000.0} | 22642 | - equation: P-C6H3O2 + H <=> P-C6H4O2 # ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S1540748916300360_mmc2.zip
