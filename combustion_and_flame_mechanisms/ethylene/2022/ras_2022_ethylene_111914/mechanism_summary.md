# A detailed experimental and kinetic modeling study on pyrolysis and oxidation of oxymethylene ether-2 (OME-2)

## Bibliography

Kevin De Ras, Marvin Kusenberg, Guillaume Vanhove, Yann Fenard, Andreas Eschenbacher, Robin J. Varghese, et al.. A detailed experimental and kinetic modeling study on pyrolysis and oxidation of oxymethylene ether-2 (OME-2)[J]. Combustion and Flame, 2022, 238: 111914. DOI: 10.1016/j.combustflame.2021.111914.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 238 / 4
- Article number: 111914
- DOI: 10.1016/j.combustflame.2021.111914
- ScienceDirect URL: https://doi.org/10.1016/j.combustflame.2021.111914
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ethylene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s001021802100657x_mmc1/Model_OME-2.inp
- Original thermodynamic source files: _processing/extracted/s001021802100657x_mmc1/Model_OME-2.inp
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 301
- Reaction count: 4502
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 3398 and 9209 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ethylene/2022/ras_2022_ethylene_111914/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 <=> O + OH Reaction 2252: H + O2 <=> O + OH | Line | | 3393 | - [7.15171811, 0.023488931, -9.97303278e-06, 1.78819786e-09, | 3394 | -1.15096177e-13, -7503.74845, -8.16604577] | 3395 | note: "!\tInChI=1S/C3H6O2/c1-4-3-5-2/h1H,3H2,2H3" | 3396 | | 3397 | reactions: > 3398 > - equation: H + O2 <=> O + OH # Reaction 1 ^ | 3399 | rate-constant: {A: 1.04e+14, b: 0.0, Ea: 1.5286e+04} | 3400 | note: | | 3401 | REF:2 parameter fit to h ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S001021802100657X_mmc1.zip
- extracted S001021802100657X_mmc3.docx
- extracted S001021802100657X_mmc5.zip
- extracted S001021802100657X_mmc4.xlsx
- extracted S001021802100657X_mmc2.docx
