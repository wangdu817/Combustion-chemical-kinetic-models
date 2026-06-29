# Modeling of the oxidation of methyl esters—Validation for methyl hexanoate, methyl heptanoate, and methyl decanoate in a jet-stirred reactor

## Bibliography

Pierre Alexandre Glaude, Olivier Herbinet, Sarah Bax, Joffrey Biet, Valérie Warth, Frédérique Battin-Leclerc. Modeling of the oxidation of methyl esters—Validation for methyl hexanoate, methyl heptanoate, and methyl decanoate in a jet-stirred reactor[J]. Combustion and Flame, 2010, 157: 2035-2050. DOI: 10.1016/j.combustflame.2010.03.012.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 157 / Nov
- Article number: 2035-2050
- DOI: 10.1016/j.combustflame.2010.03.012
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218010001008
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S0010218010001008_mmc1.txt
- Original thermodynamic source files: _processing/raw_downloads/S0010218010001008_mmc1.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 1251
- Reaction count: 14342
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 13855 and 46125 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/unknown_fuel/2010/glaude_2010_unknown_fuel_2035-2050/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: C11H22O2S-1 => R1007C10H19O2S + R4CH3 Reaction 7172: C11H22O2S-1 => R1007C10H19O2S + R4CH3 | Line | | 13850 | data: | 13851 | - [2.5, 0.0, 0.0, 0.0, 0.0, -745.375, 4.366001] | 13852 | note: '120186' | 13853 | | 13854 | reactions: > 13855 > - equation: C11H22O2S-1 => R1007C10H19O2S + R4CH3 # Reaction 1 ^ | 13856 | rate-constant: {A: 1.6e+17, b: 0.0, Ea: 8.68774e+04} | 13857 | note: | | 13858 | 5165 reactions ... | 461 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- none
