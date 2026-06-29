# Detailed kinetic mechanism of polyoxymethylene dimethyl ether 3 (PODE3). Part I: Ab initio thermochemistry and kinetic predictions for key reactions

## Bibliography

Qiren Zhu, Jie-Yao Lyu, Ruining He, Xin Bai, Yang Li, Wenming Yang. Detailed kinetic mechanism of polyoxymethylene dimethyl ether 3 (PODE3). Part I: Ab initio thermochemistry and kinetic predictions for key reactions[J]. Combustion and Flame, 2023, 256: 112990. DOI: 10.1016/j.combustflame.2023.112990.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 256 / October
- Article number: 112990
- DOI: 10.1016/j.combustflame.2023.112990
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023003668
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ethylene_dimethyl_ether_polyoxymethylene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: not available
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S0010218023003668_mmc2.docx
- Original thermodynamic source files: not found
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 30: """ PODE3+H<=>PODE3_R_1+H2 8.110E-05 5.261 3677.54 """ Unexpected token '+H2' in reaction expression 'PODE3+H<=>PODE3_R_1+H2'. May be due to undeclared species 'H2'. Error while reading reaction in chem.inp starting on line 31: """ PODE3+H<=>PODE3_R_2+H2 4.630E+07 2.059 8409.25 """ Unexpected token '+H2' in reaction expression 'PODE3+H<=>PODE3_R_2+H2'. May be due to undeclared species 'H2'. Error while reading reaction in chem.inp starting on line 32: """ PODE3+H<=>PODE3_R_3+H2 7.102E+07 1.944 10726.92 """ Unexpected token '+H2' in reaction expression 'PODE3+H<=>PODE3_R_3+H2'. May be due to undeclared species 'H2'. Error while reading reaction in chem.inp starting on line 33: """ PODE3+OH<=>PODE3_R_1+H2O 1.136E+02 2. ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: not available
- Standard tran.dat: not available

## Abstract

In recent years, polyoxymethylene dimethyl ether 3 (PODE3) has emerged as a promising fuel additive to mitigate soot emissions in diesel engines, garnering significant research attention. Several detailed kinetic mechanisms of PODE3 have been developed to investigate its reaction pathways and to simulate its combustion process. Typically, these mechanisms employ analogy methods based on rate constants derived primarily from PODE1 sub-mechanisms. However, in this study, we present, for the first time, high-level ab initio quantum chemical calculations directly on PODE3 itself. (1) The bond dissociation energies (BDEs) of all CH and CO bonds in dimethyl ether (DME) and PODEn (n = 1–5) were calculated using combined compound methods (CBS-APNO/G3/G4). (2) The obtained BDE results were then utilized to investigate the unimolecular decomposition reactions of PODE3, demonstrating good agreement with previous Molecular Dynamics simulation results. (3) The rate constants of hydrogen abstraction reactions of PODE3 by H ˙ , C ˙ H 3 , C H 3 O ˙ , O ˙ H , H O ˙ 2 , O 2 were calculated with all possible pre-reaction or post-reaction complexes identified. The rate constants of the H-atom abstraction reactions were found to primarily depend on the energy barriers following the order: O ˙ H > C H 3 O ˙ > H ˙ > C ˙ H 3 > H O ˙ 2 > O 2 . However, the abstraction by H ˙ can dominate as temperature increases. (4) The rate constants of β-scission and isomerization reactions of PODE3 radicals were also computed. The calculated β-scission reaction rates supported the suitability of the rate analogy for PODEn, employing the long-chain PODE3. The energy barriers of the isomerization reactions with long chain transition states were comparable to the energy barrier of the β-scission reactions and are much lower than that in the case of PODE1 radicals. (5) The thermochemistry properties of all involved species, including PODE4–5 and their radicals, were calculated with the combined compound methods (CBS-APNO/G3/G4) for further combustion modeling. Considering PODE3′s nature as a long-chain PODEn, the rate constants computed for PODE3 can serve as a solid foundation for developing detailed mechanisms for PODE4–5.

## Processing Notes

- extract failed S0010218023003668_mmc2.docx: File is not a zip file
- extracted S0010218023003668_mmc1.docx
