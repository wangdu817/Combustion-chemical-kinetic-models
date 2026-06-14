# Exploring the first-stage ignition and model optimization in the comprehensive study of n-dodecane oxidation

## Bibliography

Congjie Hong, Yilong Ao, Yuyang Zhang, Wuchuan Sun, Zemin Tian, Yingwen Yan, et al.. Exploring the first-stage ignition and model optimization in the comprehensive study of n-dodecane oxidation[J]. Combustion and Flame, 2024, 266: 113489. DOI: 10.1016/j.combustflame.2024.113489.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 266 / August
- Article number: 113489
- DOI: 10.1016/j.combustflame.2024.113489
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024001986
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: n_dodecane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S0010218024001986_mmc1.docx, _processing/raw_downloads/S0010218024001986_mmc3.docx
- Original thermodynamic source files: _processing/raw_downloads/S0010218024001986_mmc5.docx, _processing/raw_downloads/S0010218024001986_mmc2.docx
- Original transport source files: _processing/raw_downloads/S0010218024001986_mmc4.docx

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 1899
- Reaction count: 7579
- Message: InputError: Ignoring redundant declaration for species 'C7H15-1' Ignoring redundant declaration for species 'C6H13-1' Ignoring redundant declaration for species 'C5H11-1' Ignoring redundant declaration for species 'C5H10-1' Ignoring redundant declaration for species 'C6H12-1' Suppressed 17 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Unparsable lines while reading thermo data in therm.dat starting on line 1751: """ """ Lines could not be parsed as a NASA7 entry. No thermo data found for species 'C3H6O3' No thermo data found for species 'C2O' No thermo data found for species 'C2' No thermo data found for species 'CH2CO2' No thermo data found for species 'CH2COOH' No thermo data found for species 'CH3CCO' No ther ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: 1899
- Reaction count: 7579
- Message: CanteraError: ******************************************************************************* CanteraError thrown by GasTransportData::validate: invalid geometry for species 'NC5H12'. 'atom' specified, but species contains multiple atoms. *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extract failed S0010218024001986_mmc5.docx: File is not a zip file
- extracted S0010218024001986_mmc6.docx
- extract failed S0010218024001986_mmc1.docx: File is not a zip file
- extract failed S0010218024001986_mmc4.docx: File is not a zip file
- extracted S0010218024001986_mmc7.xlsx
- extract failed S0010218024001986_mmc3.docx: File is not a zip file
- extract failed S0010218024001986_mmc2.docx: File is not a zip file
