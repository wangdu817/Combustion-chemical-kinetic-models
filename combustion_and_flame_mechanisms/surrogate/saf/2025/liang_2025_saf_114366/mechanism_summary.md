# Surrogate formulation for HEFA sustainable aviation fuels: a new approach based on pyrolysis experiments

## Bibliography

Yilun Liang, Juan Wang. Surrogate formulation for HEFA sustainable aviation fuels: a new approach based on pyrolysis experiments[J]. Combustion and Flame, 2025, 280: 114366. DOI: 10.1016/j.combustflame.2025.114366.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 280 / October
- Article number: 114366
- DOI: 10.1016/j.combustflame.2025.114366
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025004031
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025004031/pdfft?md5=39c195d7792e1fb6733582504772779b&pid=1-s2.0-S0010218025004031-main.pdf
- Fuel type: saf
- Plasma-related mechanism: no
- Validation reactor/type from abstract: flow reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S0010218025004031_mmc3.txt, _processing/extracted/s0010218025004031_mmc5/mech-skeletal.dat
- Original thermodynamic source files: _processing/raw_downloads/S0010218025004031_mmc4.txt, _processing/extracted/s0010218025004031_mmc6/therm-skeletal.dat
- Original transport source files: _processing/extracted/s0010218025004031_mmc7/tran-skeletal.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 66
- Reaction count: 189
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: 66
- Reaction count: 189
- Message: InputError: Ignoring redundant declaration for species 'C5H6' Ignoring redundant declaration for species 'C5H5' Ignoring redundant declaration for species 'CYC5H71-3' Ignoring redundant declaration for species 'C5H4O' Ignoring redundant declaration for species 'C5H5CH3-1' Suppressed 493 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Unparsable lines while reading thermo data in therm.dat starting on line 299: """ """ Lines could not be parsed as a NASA7 entry. Unparsable lines while reading thermo data in therm.dat starting on line 326: """ END """ Lines could not be parsed as a NASA7 entry. No thermo data found for species 'CYC5H71-3' No thermo data found for species 'CYC5H71-4' No thermo data found for species ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Pyrolysis experiments were conducted in a flow reactor at atmospheric pressure on three distinct hydroprocessed esters and fatty acids synthetic paraffinic kerosene (HEFA-SPK) fuels, with species concentration profiles obtained via online gas chromatography (GC). The results indicated similar pyrolysis characteristics across the fuels. A surrogate for HEFA-SPK was developed by selecting n-dodecane and isododecane as the surrogate components. The ratio of these components was determined based on the concentration profiles of pyrolysis products. A detailed kinetic model for the n-dodecane and isododecane mixture was developed, encompassing 2464 species and 8939 reactions, to simulate pyrolysis across various composition ratios and identify the optimal surrogate composition. Simulations highlighted the sensitivity of C2H4, C2H6, C3H4-A, and C3H4-P concentration profiles to the n-dodecane and isododecane ratio. These profiles served as matching targets to ascertain the optimal composition, yielding a surrogate of 73 % n-dodecane and 27 % isododecane by weight. Validation against experimental data, including pyrolysis data from this study and oxidation species concentration and ignition delay time data from literature, confirmed the surrogate's ability in replicating HEFA-SPK's combustion characteristics and the method's validity. Furthermore, a skeletal mechanism for the surrogate, comprising 66 species and 186 reactions, was developed and validated against literature data, demonstrating its accuracy in predicting the oxidation behavior of pure n-dodecane, pure isododecane, and HEFA-SPK.

## Processing Notes

- extracted S0010218025004031_mmc2.docx
- extracted S0010218025004031_mmc5.zip
- extracted S0010218025004031_mmc6.zip
- extracted S0010218025004031_mmc7.zip
- extracted S0010218025004031_mmc1.xlsx
