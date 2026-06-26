# Enhanced C2-CN sub-mechanism: Impact on NO/N2O and soot precursor yields during C2H2/HCN oxidation

## Bibliography

Yu Yang, Shu Zheng, Huanhuan Wang, Bin Hu, Hao Liu, Ran Sui, et al.. Enhanced C2-CN sub-mechanism: Impact on NO/N2O and soot precursor yields during C2H2/HCN oxidation[J]. Combustion and Flame, 2024, 260: 113267. DOI: 10.1016/j.combustflame.2023.113267.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 260 / February
- Article number: 113267
- DOI: 10.1016/j.combustflame.2023.113267
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023006417
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: n2o
- Plasma-related mechanism: no
- Validation reactor/type from abstract: stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218023006417_mmc1/chem.inp
- Original thermodynamic source files: _processing/extracted/s0010218023006417_mmc2/therm.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 232
- Reaction count: 3204
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

The combustion of hydrocarbon-ammonia fuels poses challenges related to the formation of soot and nitrogen oxides (NOx) emissions. Various kinetic mechanisms have been developed to describe the pathways of soot and NOx formation, but limited attention has been paid to the role of the C2-CN species, such as HC3N and CH2CHCN, in influencing the yields of soot and NOx. To address this gap, we present a detailed C2-CN sub-mechanism integrated into a NOx and polycyclic aromatic hydrocarbons (PAHs) kinetic model. The rate constants of the barrierless association reactions of C2H+CN, C2H3+CN, C2H5+CN, and CH3+CH2CN were updated using the variable reaction coordinate transition state theory (VRC-TST). We numerically investigated the oxidation of C2H2 and HCN at equivalence ratios of 2.0 and 3.0, which are major precursors for NOx and PAHs, in a perfectly stirred reactor (PSR) employing two kinetic models (with/without the developed C2-CN sub-mechanism). By comparing the rates of production (ROPs) obtained via both models, we analyzed the formation pathways of NO/N2O and Benzo(ghi)fluoranthene (BGHIF). Our findings reveal temperature-dependent trends in the calculated rate constants of C2H5+CN and CH3+CH2CN associations (positive dependence) as well as C2H+CN and C2H3+CN associations (negative dependence). The peak mole fractions of BGHIF at equivalence ratio (φ) of 2.0 and 3.0 predicted by the updated mechanism were 18.4 % and 13.6 % lower than the base mechanism. This reduction can be attributed to an additional consumption channel of C2H2 (C2H2+CN=HC3N+H) predicted by the C2-CN sub-mechanism. Furthermore, the C2-CN sub-mechanism exhibited a stronger suppression effect on N2O formation compared with NO formation at φ=2.0 and 3.0. This limitation can be explained by an additional consumption channel of CN via CN+C2H2=HC3N+H, resulting in decreased NO/N2O through the reaction sequence CN→NO→N2O and CN→NCO→HNCO→NH2→HNO→NO→N2O.

## Processing Notes

- extracted S0010218023006417_mmc2.zip
- extracted S0010218023006417_mmc3.zip
- extracted S0010218023006417_mmc1.zip
