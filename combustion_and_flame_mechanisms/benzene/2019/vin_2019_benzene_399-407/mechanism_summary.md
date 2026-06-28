# A study of chlorobenzene pyrolysis

## Bibliography

Nicolas Vin, Frédérique Battin-Leclerc, Hervé Le Gall, Nadia Sebbar, Henning Bockhorn, Dimosthenis Trimis, et al.. A study of chlorobenzene pyrolysis[J]. Combustion and Flame, 2019, 37: 399-407. DOI: 10.1016/j.proci.2018.05.067.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 37 / 
- Article number: 399-407
- DOI: 10.1016/j.proci.2018.05.067
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S1540748918300683
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: benzene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S1540748918300683_mmc2.txt
- Original thermodynamic source files: _processing/raw_downloads/S1540748918300683_mmc2.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 224
- Reaction count: 2910
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 2596 and 9321 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/benzene/2019/vin_2019_benzene_399-407/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: B1O + R1H + M <=> OHE + M Reaction 1456: B1O + R1H + M <=> OHE + M | Line | | 2591 | 5.2635643e-12, 1.15213737e+04, 53.618509] | 2592 | - [65.9373007, -0.0148068303, 2.21727696e-07, 5.57756369e-10, | 2593 | -5.61820855e-14, -1.6497877e+04, -341.890178] | 2594 | | 2595 | reactions: > 2596 > - equation: R1H + B1O + M <=> OHE + M # Reaction 1 ^ | 2597 | type: three-body | 2598 | rate-constant: {A: 6.0e+14, b: 0.0, Ea: 6940.0} | 2599 | n ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S1540748918300683_mmc1.docx
