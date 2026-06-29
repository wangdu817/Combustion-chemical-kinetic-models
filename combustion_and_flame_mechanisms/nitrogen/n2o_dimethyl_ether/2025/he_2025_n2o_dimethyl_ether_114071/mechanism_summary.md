# An experimental and modeling study on combustion characteristics of dimethyl ether/ nitrous oxide/ chlorine

## Bibliography

Ruining He, Xuan Ren, Xin Bai, Yiheng Tong, ... Yang Li. An experimental and modeling study on combustion characteristics of dimethyl ether/ nitrous oxide/ chlorine[J]. Combustion and Flame, 2025, 275: 114071. DOI: 10.1016/j.combustflame.2025.114071.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 275 / May
- Article number: 114071
- DOI: 10.1016/j.combustflame.2025.114071
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025001099
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025001099/pdfft?md5=70b02476ec57962c8618d603aef11dc7&pid=1-s2.0-S0010218025001099-main.pdf
- Fuel type: n2o_dimethyl_ether
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, laminar flame speed

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218025001099_mmc3/NUIGMech1.3_added Cl.inp
- Original thermodynamic source files: _processing/extracted/s0010218025001099_mmc1/NUIGMech1.3 added Cl.dat
- Original transport source files: _processing/extracted/s0010218025001099_mmc2/NUIGMech1.3 added Cl.TRAN

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'CH2O' Error while reading reaction in chem.inp starting on line 4007: """ H+O2(+M)=HO2(+M) +4.66000000E+012 +4.40000000E-001 +0.00000000E+000 !\AUTHOR: SP !\REF: TROE _ 2000 / PCCP FERNANDES 2008 LOWMX / +1.22500000E+019 -1.20000000E+000 +0.00000000E+000/!\AUTHOR: SP !\REF:SHAO ET AL. PROC. COMB. INST. 37,(2019):145-152. TROEMX / +5.00E-01 1.00E+00 1.00E+10 1.00E+30 / LOWSP / N2 +4.50E+20 -1.73E+00 0.00E+00/ !\AUTHOR: SP !\REF: LU, Z. 2020. HYDROGEN OXIDATION NEAR THE SECOND EXPLOSION LIMIT IN A FLOW REACTOR TROESP / N2 +5.00E-01 1.00E+00 1.00E+10 1.00E+30 / N2 / +1.0 / HE / +0.5700 / AR / +0.65 / O2 / 1.0 / H2 / +2.00 / CH4 / +2.0000 / CO2 / +3.2500 / H2O / +17.6000 / CO / 4.0/ """ could not convert string to float: 'N2' Please check ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

PEG and AP are widely used in strategic and tactical missile engines as key components of composite propellants. It remains a challenge to investigate the detailed combustion mechanism of PEG/AP due to the complex structure and complicated chemical reactions. DME, N2O and Cl2 are the main intermediates of PEG and AP pyrolysis, respectively, which play a crucial role in PEG/AP combustion. DME/N2O is also a promising combination propellant because of its high energy content and good combustion and environmental properties. This study systematically investigates the combustion characteristics of DME, N2O and Cl2 mixtures based on experimental measurements. The Ignition Delay Times (IDT) of DME/N2O mixtures at equivalence ratios of 0.5, 1.0, and 2.0 (N2O as the oxidant) were measured using a high-pressure shock tube at pressures of 10.0 and 20.0 bar and in the temperature range of 1250–1600 K. Besides, half of the N2O was replaced by Cl2 to investigate its impact on the ignition characteristics of DME/N2O. The result shows that although the addition of Cl2 reduces the activity of the fuel mixture system, the ignition activation energy required for ignition has not changed. The laminar flame speeds of DME/N2O mixtures were measured by a constant-volume reactor. The equivalence ratios ranged from 0.8 to 1.4, with N2 content controlled at 60 %, pressure at 1.0 bar, and initial temperature at 298/333 K. The experimental results were simulated using the NUIGMech1.3 model and a constructed model adding Cl2 related reactions to NUIGMech1.3 in this study. Sensitive and flux analyses were conducted to determine the crucial reactions for the IDT of DME/N2O and DME/N2O/Cl2. The results indicate that the decomposition of DME generates ĊH3 and ĊH3O, which is the most reactivity promoting reaction at all temperatures, and it doesn't be influenced by Cl2 presence. Meanwhile H-atom abstraction from DME by Ḣ is the most reactivity inhibiting reaction, while it shows promoting effect with the Cl2 addition, and the H-atom abstraction reaction by O2, which did not show significant sensitivity before the addition of Cl2, shows the strongest inhibitory effect at this time. H-atom abstraction reactions and C–O bond dissociation are two major pathways of DME primary consumption. Although the presence of Cl2 did not alter this macroscopic phenomenon, it had a significant impact on the flux of each pathway. Meanwhile, the addition of Cl2 directly changed the reaction after the third stage in the DME reaction pathways, making the reaction involving Cl2 dominant at this time. The results in the current study should be a positive contribution to the development and optimization of detailed gas-phase chemical kinetic mechanisms for PEG/AP multicomponent solid propellant.

## Processing Notes

- extracted S0010218025001099_mmc1.zip
- extracted S0010218025001099_mmc2.zip
- extracted S0010218025001099_mmc3.zip
