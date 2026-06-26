# Methyl formate oxidation kinetics up to 100 atm

## Bibliography

Yuanxinxin Cao, Bowen Mei, Wenbin Xu, Mohammad Adil, ... Yiguang Ju. Methyl formate oxidation kinetics up to 100 atm[J]. Combustion and Flame, 2026, 290: 115098. DOI: 10.1016/j.combustflame.2026.115098.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 290 / 
- Article number: 115098
- DOI: 10.1016/j.combustflame.2026.115098
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026003342
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: methyl_formate_ethyl_formate
- Plasma-related mechanism: no
- Validation reactor/type from abstract: jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218026003342_mmc3/UpdatedHP.inp
- Original thermodynamic source files: _processing/extracted/s0010218026003342_mmc2/UpdatedHP.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 156
- Reaction count: 1051
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Methyl formate (MF, CH3OCHO), the simplest ester, is a representative oxygenated fuel with high oxygen content, and low sooting tendency. However, its oxidation behavior under high-pressure and intermediate-temperature conditions remains insufficiently understood, especially where low-temperature peroxy radical chemistry, methanol chemistry, and pressure-dependent reaction pathways play a critical role. In this study, MF oxidation experiments were conducted in the Princeton supercritical-pressure jet-stirred reactor (SP-JSR) at 20 and 100 atm over the temperature range of 400–950 K under both fuel-lean and fuel-rich conditions. Based on the experimental results, an updated HP-Mech was developed by incorporating previous MF sub-mechanisms, expanded low-temperature peroxy pathways, and evaluated pressure-dependent decomposition kinetics. The newly updated HP-Mech shows greatly improved performance in predicting the onset temperature, the key intermediate species fractions, methanol formation, and the progression of MF oxidation across all the experimental conditions. Path flux analysis indicates that MF consumption at the onset stage is dominated by H-abstraction at the methyl site, forming CH2OCHO radicals that lead to the formation and isomerization of O2CH2OCHO, driving low-temperature chain propagation. Moreover, H-abstraction at the formate site forms CH3OCO radicals that preferentially decompose to CH3, initiating the methanol formation pathway linked to CH3O2 and HO2 chemistry. At the same time, HO2 formation is strongly coupled to MF oxidation through multiple MF-derived radical pathways. HCO originates from MF oxidation and acts as a key coupling species linking fuel consumption to HO2 buildup, especially under high-pressure and intermediate-temperature conditions. In addition to this dominant channel, supplementary HO2 formation pathways involving CH3, CH3O, CH2OH, and CH3O2 reacting with O2 further connect methanol chemistry and oxygenated radical chemistry to the HO2 pool, indicating the central role of HO2 in governing MF oxidation. Sensitivity analysis identifies MF with OH/HO2/CH3O2 reactions and the HO2/H2O2/OH sequence as the key factors controlling reactivity in the high-pressure and intermediate-temperature regime. MF directly reacts with OH/HO2/CH3O2 to consume the fuel and produce reactive radicals like CH2OCHO and CH3OCO that undergo subsequent oxidation pathways. Moreover, HO2 recombination suppresses oxidation at lower temperatures, while thermal decomposition of H2O2 accelerates OH production and promotes fuel consumption as temperature increases. The direct formation of active OH from HO2 radicals further completes the mechanism, improving its prediction especially during the oxidation onset stage.

## Processing Notes

- extracted S0010218026003342_mmc3.zip
- extracted S0010218026003342_mmc1.docx
- extracted S0010218026003342_mmc2.zip
