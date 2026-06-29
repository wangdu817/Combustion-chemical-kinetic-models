# An experimental and kinetic modeling study of the ignition of methane/n-decane blends

## Bibliography

Jiaxin Liu, Shangkun Zhou, Pengzhi Wang, Yuki Murakami, ... Henry J. Curran. An experimental and kinetic modeling study of the ignition of methane/n-decane blends[J]. Combustion and Flame, 2025, 272: 113884. DOI: 10.1016/j.combustflame.2024.113884.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 272 / February
- Article number: 113884
- DOI: 10.1016/j.combustflame.2024.113884
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024005935
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218024005935/pdfft?md5=88012a6e58e36ac46b8c61fb31046931&pid=1-s2.0-S0010218024005935-main.pdf
- Fuel type: methane_n_decane
- Plasma-related mechanism: yes
- Validation reactor/type from abstract: shock tube, rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218024005935_mmc6/GalwayMech1.0.MECH
- Original thermodynamic source files: _processing/extracted/s0010218024005935_mmc7/GalwayMech1.0.THERM
- Original transport source files: _processing/extracted/s0010218024005935_mmc8/GalwayMech1.0.TRAN

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'SC4H9CHO' Error while reading reaction in chem.inp starting on line 1752: """ H+O2(+M)=HO2(+M) 4.66E12 0.44 0.0E0 !\Author: SP !\Ref: TROE, PROCI Volume 28, Issue 2, 2000, 1463-1469 / PCCP FERNANDES 2008 HE/1.0/ AR/0.0/ N2/1.0/ O2/1.0/ H2/2.0/ CH4/2.0/ CO2/3.25/ H2O/17.6/ CO/4.0/ LOWMX / 4.0662E19 -1.4E0 -1.80537E2 / TROEMX / 5.0E-1 1.0E0 1.0E10 1.0E30 / LOWSP / N2 1.91E+20 -1.5568 253.86 / !Yuki Murakami 28 July 2023 H2 project recommended TROESP / N2 5.0E-1 1.0E0 1.0E10 1.0E30 / LOWSP / HE 1.216E+19 -1.23 +0.00 / !Yuki Murakami 17 May 2024, From AramcoMech3.0 He 0.64 -> 0.70 TROESP / HE 6.70E-1 1.0E-30 1.0E30 1.0E30 / """ could not convert string to float: 'N2' Ignoring duplicate transport data for species "AR" on line 3578 of "tran ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

An experimental and kinetic modeling study of the combustion of methane/n-decane blends is performed. Ignition delay times (IDTs) of the pure fuels in addition to their blends are measured using both a shock tube and a rapid compression machine at three different methane/n-decane (mol%) compositions of 99/1 (M99D1), 95/5 (M95D5), and 80/20 (M80D20) in ‘air’, over the temperature range of 610–1495 K, at a pressure of 30 bar. A new chemical kinetic mechanism, GalwayMech1.0, is proposed to describe the combustion of these blends and is validated against the new IDT data including 1st-stage and total IDTs as well as existing experimental n-decane data available in the literature. Sensitivity analyses reveal that H-atom abstraction from n-decane by methyl peroxy radicals (CH3Ȯ2) play an important role in promoting blend reactivity at intermediate temperatures, which is not observed for pure n-decane. By investigating the effect of the n-decane concentration on the ignition characteristics, we found that the low ignition temperature limit is extended with increasing n-decane content with a non-linear reactivity-promoting effect. Flux analyses reveal that CH4 oxidation in the blends is initiated via CH4 + ȮH = ĊH3 + H2O, driven by the ȮH radicals produced from the early oxidation of n-decane and the CH3Ȯ2 radicals formed from CH4 oxidation which subsequently accelerates nC10H22 consumption via H-atom abstraction. Comparisons of CH4/nC10H22 and H2/nC10H22 blends from a previous study demonstrate consistently higher reactivity for hydrogen blending compared to methane and that the magnitude of this increase diminishes with increasing n-decane content. Finally, we also compare our current model predictions of our new data with other n-decane models available in the literature.

## Processing Notes

- extracted S0010218024005935_mmc4.xlsx
- extracted S0010218024005935_mmc1.xlsx
- extracted S0010218024005935_mmc2.xlsx
- extracted S0010218024005935_mmc7.zip
- extracted S0010218024005935_mmc9.zip
- extracted S0010218024005935_mmc6.zip
- extracted S0010218024005935_mmc5.zip
- extracted S0010218024005935_mmc8.zip
- extracted S0010218024005935_mmc3.docx
- unsupported archive without 7z: VPROs.rar
