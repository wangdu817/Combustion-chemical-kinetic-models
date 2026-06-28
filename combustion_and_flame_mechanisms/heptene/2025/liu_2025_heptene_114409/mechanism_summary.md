# An ignition delay time and automated chemical kinetic modeling study of three heptene isomers

## Bibliography

Jiaxin Liu, Yichen Gao, Pengzhi Wang, Hossein S. Saraee, ... Henry J. Curran. An ignition delay time and automated chemical kinetic modeling study of three heptene isomers[J]. Combustion and Flame, 2025, 280: 114409. DOI: 10.1016/j.combustflame.2025.114409.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 280 / October
- Article number: 114409
- DOI: 10.1016/j.combustflame.2025.114409
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025004468
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025004468/pdfft?md5=ed32c4b117d72f373f1a5f98f0c28318&pid=1-s2.0-S0010218025004468-main.pdf
- Fuel type: heptene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218025004468_mmc6/chem.inp
- Original thermodynamic source files: _processing/extracted/s0010218025004468_mmc8/therm.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'NC5KET21' Ignoring redundant declaration for species 'C6KET21' Ignoring redundant declaration for species 'NC5KET21O' Ignoring redundant declaration for species 'NC5KET23' Ignoring redundant declaration for species 'NC5KET32' Suppressed 22 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Error while reading reaction in chem.inp starting on line 1848: """ H+O2(+M)=HO2(+M) 4.66E12 0.44 0.0E0 !\Author: SP !\Ref: TROE, PROCI Volume 28, Issue 2, 2000, 1463-1469 / PCCP FERNANDES 2008 HE/1.0/ AR/0.0/ N2/1.0/ O2/1.0/ H2/2.0/ CH4/2.0/ CO2/3.25/ H2O/17.6/ CO/4.0/ LOWMX / 4.0662E19 -1.4E0 -1.80537E2 / TROEMX / 5.0E-1 1.0E0 1.0E10 1.0E30 / LOWSP / N2 1.91E+20 -1.5568 253. ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

An experimental and kinetic modeling study of the ignition of 1-heptene (C7H14-1), trans-2-heptene (C7H14-2), and trans-3-heptene (C7H14-3) is performed. Ignition delay times (IDTs) of these three isomers are measured using both a high-pressure shock tube and a rapid compression machine over the temperature range of 613–1257 K, at pressures of 15 and 30 bar diluted in air. An automated kinetic model development procedure is utilized in this study. We extended the capabilities of the MAMOX++ program, originally designed for alkane mechanism generation, to generate alkene reaction mechanisms. Using this enhanced framework, we systematically construct a detailed kinetic model for C5–C7 linear alkenes involving 52 reaction classes based on the core C0–C4 GalwayMech1.0 chemistry. The rate constants of each reaction class of the initial model are systematically optimized within their predefined uncertainty limits by comparing simulations with the new IDT data including 1st-stage and total IDTs as well as existing experimental data in the literature. Sensitivity and flux analyses reveal that HȮ2 addition to alkenes, forming β-Q̇OOH radicals, significantly enhances reactivity at low and intermediate temperatures by converting HȮ2 radicals into more reactive ȮH radicals. Furthermore, by comparing the IDTs of the three heptene isomers with those of n-heptane, it is observed that reactivity is inhibited and is more pronounced as the CC bond shifts toward the center of the molecular structure. Notably, C7H14-1 and C7H14-2 display similar reactivities due to their comparable levels of γ-hydroperoxyl alkenyl radical formation. Additionally, by comparing the IDTs of C5–C7 1-alkenes and 2-alkenes, it is observed that, at low and intermediate temperatures, the reactivity increases with increasing chain length, whereas similar reactivities of all C5–C7 alkenes are observed at high temperatures.

## Processing Notes

- extracted S0010218025004468_mmc8.zip
- extracted S0010218025004468_mmc5.zip
- extracted S0010218025004468_mmc4.xlsx
- extracted S0010218025004468_mmc1.docx
- extracted S0010218025004468_mmc7.zip
- extracted S0010218025004468_mmc6.zip
- extracted S0010218025004468_mmc3.xlsx
