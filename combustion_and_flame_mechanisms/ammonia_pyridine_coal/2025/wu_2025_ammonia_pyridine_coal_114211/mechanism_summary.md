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
- Validation reactor/type from abstract: jet-stirred reactor, stirred reactor

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
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 2732 and 9703 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ammonia_pyridine_coal/2025/wu_2025_ammonia_pyridine_coal_114211/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: C5H5N + NH2 <=> C5H4N + NH3 Reaction 1576: C5H5N + NH2 <=> C5H4N + NH3 | Line | | 2727 | note: |- | 2728 | T.8.03 | 2729 | Burcat/Goos 2017 | 2730 | | 2731 | reactions: > 2732 > - equation: C5H5N + NH2 <=> C5H4N + NH3 # Reaction 1 ^ | 2733 | rate-constant: {A: 0.0488, b: 4.3749, Ea: 5503.5} | 2734 | note: | | 2735 | ********* PYRIDINE SUBSET ************ ... | 9698 | T.Kathrotia 2011 | 9699 | - equation: OH* ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

The co-oxidation of pyridine and ammonia was studied as a model compound to investigate the kinetics of coal-ammonia co-firing. Experiments were conducted in a jet-stirred reactor coupled with synchrotron vacuum ultraviolet photoionization molecular beam mass spectrometer at atmospheric pressure up to 900 K with ammonia to pyridine molar blend ratio of 1:5. Compared with previous pyridine kinetic studies, several new oxidation intermediates were detected during the co-oxidation process, including nitrous acid, methyleneaminoacetonitrile, 2-, and 4-cyanopyridine. The pyridine LTO 3.1 kinetic model, comprising 233 species and 1572 reactions, was developed and used to simulate the reaction process with reasonable predictions, which incorporates the direct interaction between pyridine and NH2 radical (NH2+C5H5N=C5H4N+NH3) and updates the rate constants of C5H5N+OH=C5H4N+H2O, NH3+NCO=HNCO+NH2, NH3+NCO=HOCN+NH2. The major nitrogen-containing products are HCN, N2, HNCO, N2O, pyrrole, and NO. The co-oxidation of pyridine and NH3 shows a mutual-sensitization effect, promoting the consumption of both pyridine and ammonia. The presence of ammonia boosts pyridine consumption by providing NO and more OH radicals at lower temperatures through the NO-NO2 looping process (NO+HO2=NO2+OH and NO2+H=NO+OH). The initial reaction temperature of NH3 is lowered by around 200 K when co-oxidized with pyridine compared with its neat oxidation, as pyridine could supply OH radicals at a lower temperature and trigger the chain-branching reactions. NOx emissions are also generated at lower temperatures compared with neat pyridine and NH3 oxidation conditions. N2O production reaches 367 ppm at 900 K, which is an order of magnitude higher than NO. The results could help better understand the microscopic mechanism of coal-ammonia interactions during the co-firing process, and the design, organization, and optimization of coal-ammonia co-firing applications.

## Processing Notes

- extracted S0010218025002494_mmc1.docx
- extracted S0010218025002494_mmc2.zip
