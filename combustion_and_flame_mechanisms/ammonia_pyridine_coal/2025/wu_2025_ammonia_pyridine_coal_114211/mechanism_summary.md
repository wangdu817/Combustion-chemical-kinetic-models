# Experimental and kinetic study on the co-oxidation of pyridine and ammonia as a model compound of coal-ammonia co-firing

## Bibliography

Ling-Nan Wu, Zi-Cheng Wei, Wang Li, Kai-Ru Jin, ... Zhen-Yu Tian. Experimental and kinetic study on the co-oxidation of pyridine and ammonia as a model compound of coal-ammonia co-firing[J]. Combustion and Flame, 2025, 277: 114211. DOI: 10.1016/j.combustflame.2025.114211.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 277 / July
- Article number: 114211
- DOI: 10.1016/j.combustflame.2025.114211
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025002494
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025002494/pdfft?md5=4e5870f6c27e9f849d5b936f556bdd6b&pid=1-s2.0-S0010218025002494-main.pdf
- Fuel type: ammonia_pyridine_coal
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218025002494_mmc2/Mech_Pyridine LTO 3.1.inp
- Original thermodynamic source files: _processing/extracted/s0010218025002494_mmc2/Mech_Pyridine LTO 3.1.inp
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 233
- Reaction count: 3150
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 2732 and 9703 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ammonia_pyridine_coal/2025/wu_2025_ammonia_pyridine_coal_114211/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: C5H5N + NH2 <=> C5H4N + NH3 Reaction 1576: C5H5N + NH2 <=> C5H4N + NH3 | Line | | 2727 | note: |- | 2728 | T.8.03 | 2729 | Burcat/Goos 2017 | 2730 | | 2731 | reactions: > 2732 > - equation: C5H5N + NH2 <=> C5H4N + NH3 # Reaction 1 ^ | 2733 | rate-constant: {A: 0.0488, b: 4.3749, Ea: 5503.5} | 2734 | note: | | 2735 | ********* PYRIDINE SUBSET ************ ... | 9698 | T.Kathrotia 2011 | 9699 | - equation: OH* ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S0010218025002494_mmc2.zip
- extracted S0010218025002494_mmc1.docx
