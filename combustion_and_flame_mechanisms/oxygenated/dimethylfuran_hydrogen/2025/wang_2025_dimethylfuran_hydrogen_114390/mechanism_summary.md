# Unraveling the low-temperature chemistry of nitrogenous compounds by informatively kinetic modeling of N,N-dimethylformamide

## Bibliography

Du Wang, Zhi-Hao Zheng, Zhi-Min Wang, Xu-Peng Yu, ... Zhen-Yu Tian. Unraveling the low-temperature chemistry of nitrogenous compounds by informatively kinetic modeling of N,N-dimethylformamide[J]. Combustion and Flame, 2025, 281: 114390. DOI: 10.1016/j.combustflame.2025.114390.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 281 / November
- Article number: 114390
- DOI: 10.1016/j.combustflame.2025.114390
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025004274
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025004274/pdfft?md5=12527312d87290a5f6c8614491c17851&pid=1-s2.0-S0010218025004274-main.pdf
- Fuel type: dimethylfuran_hydrogen
- Plasma-related mechanism: possible
- Validation reactor/type from abstract: jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218025004274_mmc2/mech.inp
- Original thermodynamic source files: _processing/extracted/s0010218025004274_mmc2/thermo.dat
- Original transport source files: _processing/extracted/s0010218025004274_mmc2/trans.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'CH3NCO' Ignoring redundant declaration for species 'OCNCHO' Error while reading section in chem.inp starting on line 141: """ REACTIONS MOLES CAL/MOLE MAXSP=8 """ Unrecognized token 'MAXSP=8' on REACTIONS line Error while reading reaction in chem.inp starting on line 880: """ H+CH3N(CO)CHO=(CHO)2NCH3 1E14 0.00E 0.00 """ could not convert string to float: '0.00E' Error while reading reaction in chem.inp starting on line 882: """ H+(CHO)2NCH2=(CHO)2NCH3 1E14 0.00E 0.00 """ could not convert string to float: '0.00E' Error while reading reaction in chem.inp starting on line 3984: """ CH2NCH2OOH=CH2NCHO+H2O +1.48E+016 -1.12E+000 +4.59493E+004 ! PLOG / +1.00E-2 +1.990+50 -1.270+01 +5.35319E+4 / PLOG / +1.00E-1 +4.720+47 -1.150+01 +5.43609E+ ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

N,N-Dimethylformamide (DMF) is a volatile organic pollutant prevalent in many modern industrial processes and an intermediate formed in nitrogenous compound low-temperature oxidation. The low-temperature oxidation of DMF was performed between 450 and 900 K under fuel-lean conditions (Φ = 0.5) in a jet-stirred reactor coupled with synchrotron vacuum ultraviolet photoionization molecular beam mass spectrometry. Weak negative temperature coefficient (NTC) behavior was observed within 520 - 650 K. A comprehensive kinetic model was developed based on the previous pyrolysis model. Key reaction parameters, including hydrogen atom abstraction, first O2 addition to fuel radicals, and intermediate radical decomposition pathways, were determined through ab initio - transition state theory - RRKM/ME calculation. The model successfully predicts DMF consumption and major product formation, though discrepancies persist for certain intermediates due to remaining uncertainties in nitrogen chemistry. Kinetic analysis reveals that at NTC temperatures, DMF oxidation is predominantly controlled by carbonyl-site oxygen addition followed by rapid QOOH radical decomposition, generating CH3NCH2, CO2, and OH through Waddington-type reactions and inhibiting second O2 addition. In contrast, methyl-site O2 addition exhibits higher reaction barriers for QOOH decomposition, enabling second oxygen addition and subsequent low-temperature chain-branching reaction pathways critical for NTC behavior. Based on recent advances in nitrogen compound oxidation kinetics, the generalized behavior of different types of nitrogen-containing compounds was further discussed. Compounds with primary and secondary nitrogen atoms rarely exhibit NTC behavior due to preferential HO2 elimination from α-site ROO radicals via adjacent NH sites, effectively suppressing low-temperature reactivity. Conversely, tertiary nitrogen compounds lacking NH bonds can undergo efficient auto-oxidation through rapid intramolecular hydrogen migration. It generates highly oxygenated intermediates along with OH radicals and, therefore, is very likely to exhibit NTC behavior, though its magnitude depends on the competition between fuel-specific rates of oxygen addition and QOOH decomposition. Novelty and significance statement The negative temperature coefficient (NTC) behavior of nitrogenous compounds was first experimentally reported during the low-temperature oxidation of N,N-dimethylformamide. Leveraging advanced diagnostic techniques and comprehensive high-level ab initio calculations, we developed an informative kinetic model that successfully reproduces the observed oxidation behavior. Through detailed model analysis and integration with recent advances in nitrogenous compound low-temperature chemistry, we have formulated general principles governing NTC behavior in nitrogen-containing species. These findings significantly enhance our fundamental understanding of nitrogen chemical kinetics relevant to both low-temperature auto-ignition processes and pollutant abatement technologies.

## Processing Notes

- extracted S0010218025004274_mmc2.zip
