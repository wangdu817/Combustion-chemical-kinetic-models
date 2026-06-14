# Corrigendum to “Chemiluminescence during the high-temperature pyrolysis and oxidation of ammonia” [Combust. Flame 269 (2024) 113706]

## Bibliography

Akira Matsugi. Corrigendum to “Chemiluminescence during the high-temperature pyrolysis and oxidation of ammonia” [Combust. Flame 269 (2024) 113706][J]. Combustion and Flame, 2025, 282: 114533. DOI: 10.1016/j.combustflame.2025.114533.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 282 / December
- Article number: 114533
- DOI: 10.1016/j.combustflame.2025.114533
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S001021802500570X
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S001021802500570X/pdfft?md5=7d0b63fea1d8d8043ed541bf102bc265&pid=1-s2.0-S001021802500570X-main.pdf
- Fuel type: ammonia
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S001021802500570X_mmc1.txt
- Original thermodynamic source files: _processing/raw_downloads/S001021802500570X_mmc1.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 50
- Reaction count: 780
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 620 and 2652 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ammonia/2025/matsugi_2025_ammonia_114533/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H2 + M <=> 2 H + M Reaction 391: H2 + M <=> 2 H + M | Line | | 615 | note: |- | 616 | p.w. | 617 | [p.w.] | 618 | | 619 | reactions: > 620 > - equation: H2 + M <=> 2 H + M # Reaction 1 ^ | 621 | type: three-body | 622 | rate-constant: {A: 4.577e+19, b: -1.4, Ea: 1.044e+05} | 623 | efficiencies: {C2H6: 3.0, CH4: 2.0, CO: 1.9, CO2: 3.8, H2: 2.5, H2O: ... | 2647 | konnov 20220925 chemi | 2648 | - equation: N2H4 + H <=> NH3 + NH2X # Re ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- none
