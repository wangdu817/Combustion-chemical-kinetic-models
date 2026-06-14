# Revealing the high-pressure autoignition of ammonia/1-methylnaphthalene: RCM measurements and kinetic modeling

## Bibliography

Yongxiang Zhang, Yueying Liang, Zimu Wang, Wei Zhou, Liang Yu, Xingcai Lu. Revealing the high-pressure autoignition of ammonia/1-methylnaphthalene: RCM measurements and kinetic modeling[J]. Combustion and Flame, 2024, 268: 113610. DOI: 10.1016/j.combustflame.2024.113610.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 268 / October
- Article number: 113610
- DOI: 10.1016/j.combustflame.2024.113610
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024003195
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ammonia_naphtha
- Plasma-related mechanism: no
- Validation reactor/type from abstract: rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218024003195_mmc5/Mech.inp
- Original thermodynamic source files: _processing/extracted/s0010218024003195_mmc6/Therm.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'AR' Ignoring redundant declaration for species 'HE' Ignoring redundant declaration for species 'N2' Ignoring redundant declaration for species 'HOCO' Ignoring redundant declaration for species 'CH2(S)' Error while reading section in chem.inp starting on line 189: """ REACTIONS MAXSP=8 """ Unrecognized token 'MAXSP=8' on REACTIONS line Error while reading thermo entry in therm.dat starting on line 107: """ CHOHCO2H2 C 2H 3O 3 G 200.00 6000.00 1000.00 1 !Burcat - taken from another isomer; if = reactions present: TO BE REVISED 1.27662941E+01 1.02143437E-02-3.63547001E-06 5.83491588E-10-3.47179974E-14 2 -7.53528536E+04-3.96511752E+01 2.80443702E+00 2.10851644E-02 3.35863233E-05 3 -7.02669107E-08 3.26849274E-11-7.20649998E+04 1.51180675E+ ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Ammonia (NH3) as an attractive carbon-free fuel is gaining considerable attention in the industry for its enormous potential in global decarbonization, which is expected to achieve large-scale applications in the internal combustion engine by ammonia blending combustion strategy. Therefore, it is crucial to gain a fundamental understanding of the autoignition characteristics of ammonia-containing mixtures. 1-methylnaphthalene (C10H7CH3), a candidate component of diesel surrogate and typical aromatic hydrocarbon compound, was utilized to blend with ammonia to study the autoignition characteristics of NH3/C10H7CH3 mixtures. The ignition delay times (IDT) of NH3/C10H7CH3 mixtures with NH3 energy ratios of 50 %, 70 %, and 90 % were measured in a rapid compression machine (RCM) at the temperature of 852–1115 K, pressures of 40–100 bar, and equivalence ratios of 1.0–1.5. Experimental results show that with the increase of NH3 energy ratio, the mixture reactivity is inhibited and the ignition delay time is prolonged. A blending chemical reaction mechanism for NH3/C10H7CH3 mixtures was proposed based on combining individual sub-mechanism available in the literature. Modeling results indicate that the proposed mechanism is capable of quantitatively reproducing the dependence of ignition delay time on NH3 energy ratio, pressure, and oxygen concentration under most test conditions, except for the high-pressure conditions (60 bar, 80 bar and 100 bar) of the mixture with NH3 energy ratio of 90 %. Kinetic analysis (including species evolution profile, sensitivity, and reaction pathway analysis) was performed to reveal the effect of NH3 addition and NH3 energy ratio on the autoignition of NH3/C10H7CH3 mixtures. Analysis results show that NH3 addition and NH3 energy ratio present a significant impact by altering the sensitivity of some important reactions, the initial consumption pathways of C10H7CH3 molecules and the related important intermediates. In summary, this study provides high-pressure ignition delay time data of NH3/C10H7CH3 mixtures and proposes a NH3/C10H7CH3 blending mechanism.

## Processing Notes

- extracted S0010218024003195_mmc4.xlsx
- extracted S0010218024003195_mmc5.zip
- extracted S0010218024003195_mmc1.docx
- extracted S0010218024003195_mmc2.xlsx
- extracted S0010218024003195_mmc6.zip
- extracted S0010218024003195_mmc3.xlsx
