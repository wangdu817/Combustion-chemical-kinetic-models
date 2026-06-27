# An experimental and kinetic modeling study of the autoignition mechanism of 2-ethylhexyl nitrate combustion

## Bibliography

Jiaxin Xie, Mengmeng Jia, Frederick Nii Ofei Bruce, Chong-Wen Zhou, ... Yang Li. An experimental and kinetic modeling study of the autoignition mechanism of 2-ethylhexyl nitrate combustion[J]. Combustion and Flame, 2026, 285: 114743. DOI: 10.1016/j.combustflame.2025.114743.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 285 / March
- Article number: 114743
- DOI: 10.1016/j.combustflame.2025.114743
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025007783
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: 2_ethylhexyl_nitrate
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218025007783_mmc1/EHN.inp
- Original thermodynamic source files: _processing/extracted/s0010218025007783_mmc1/EHN.dat
- Original transport source files: _processing/extracted/s0010218025007783_mmc1/EHN=ECHO+HONO.inp, _processing/extracted/s0010218025007783_mmc1/EHO=ECHO+H.inp

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading transport data in tran.dat starting on line 32: """ C 1.500780000000 0.069052000000 0.294433000000 """ 6 transport parameters were expected, but found 3. Error while reading transport data in tran.dat starting on line 33: """ H 1.449105000000 1.097383000000 -0.080709000000 """ 6 transport parameters were expected, but found 3. Error while reading transport data in tran.dat starting on line 34: """ H 1.661088000000 0.135413000000 1.378696000000 """ 6 transport parameters were expected, but found 3. Error while reading transport data in tran.dat starting on line 35: """ C 2.699908000000 -0.624625000000 -0.349110000000 """ 6 transport parameters were expected, but found 3. Error while reading transport data in tran.dat starting on line 36: """ H 2.527055000000 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

2-Ethylhexyl nitrate (EHN) has attracted attention for its high reactivity, making it a promising candidate for use in propellants and as a combustion-enhancing fuel additive. To gain a fundamental understanding of its combustion behavior and support its practical application in advanced propulsion systems, it is essential to develop an accurate and reliable chemical kinetic model. In this study, ignition delay times (IDTs) of EHN/O₂/N₂ mixtures were systematically measured using a high-pressure shock tube. Experiments were conducted over a temperature range of 900–2000 K, at pressures of 5 and 10 bar, and under equivalence ratios of 0.5 and 1.0. The results clearly demonstrate the characteristic two-stage ignition behavior of EHN. Moreover, the IDTs were found to be highly sensitive to changes in both equivalence ratio and pressure. In the theoretical investigation, the initial decomposition pathways of EHN were systematically explored using high-level quantum chemical calculations at the QCISD(T)/CBS//M06–2X/6–311++G (d,p) level. The results indicate that cleavage of the O–N bond is the dominant reaction channel. A detailed kinetic model for EHN was developed based on the C3MechV3.3 reaction mechanism. The model predictions show good agreement with experimentally measured IDT. Furthermore, based on the current kinetic model, sensitivity, flux, and OH radical rate of production analyses were performed to identify key controlling steps and characterize radical-driven kinetics. The results show that in the first stage of ignition, over 90% of EHN is consumed via O–N bond cleavage, producing the 2-ethylhexoxy radical (EHO) and NO₂, which spontaneously initiate the NO₂–NO catalytic cycle and significantly enhance the system’s initial reactivity. In contrast, during the second stage, the chain-branching reaction H + O₂ → O + OH becomes dominant and serves as the primary driving force behind the rapid acceleration of system reactivity.

## Processing Notes

- extracted S0010218025007783_mmc1.zip
