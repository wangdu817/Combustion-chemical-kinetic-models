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
- Validation reactor/type from abstract: shock tube

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\2_ethylhexyl_nitrate\xie_2026_2_ethylhexyl_nitrate_114743\extracted\s0010218025007783_mmc1\EHN.inp
- Original thermodynamic source files: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\2_ethylhexyl_nitrate\xie_2026_2_ethylhexyl_nitrate_114743\extracted\s0010218025007783_mmc1\EHN.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 3189
- Reaction count: 13797
- Message: CanteraError: 
*******************************************************************************
CanteraError thrown by addReactions:

*******************************************************************************
InputFileError thrown by PlogRate::validate:
Error on line 43696 of E:\mech_collection\combustion_and_flame_mechanisms\2_ethylhexyl_nitrate\2026\xie_2026_2_ethylhexyl_nitrate_114743\mechanism.yaml:

Invalid rate coefficient for reaction 'C4H6 <=> C3H3 + CH3'
at P = 15999, T = 200.0
at P = 31997, T = 200.0

|  Line |
|  43691 |   rate-constants:
|  43692 |   - {P: 0.0394737 atm, A: 2.34423e+73, b: -17.49, Ea: 1.085e+05}
|  43693 |   - {P: 0.0789474 atm, A: 4.57088e+71, b: -16.91, Ea: 1.087e+05}
|  43694 |   - {P: 0.157895 atm, A: 9.54993e+69, b: -16.33, Ea: 1.09e+05}
|  43695 |   - {P: 0.315789 atm, A: 2.04174e+67, b: -15.48, Ea: 1.085e+05}
>  43696 > - equation: C4H6 <=> CH3 + C3H3  # Reaction 2743
            ^
|  43697 |   type: pressure-dependent-Arrhenius
|  43698 |   rate-constants:
|  43699 |   - {P: 0.0394737 atm, A: 1.5849e+148, b: -37.24, Ea: 1.885e+05}
*******************************************************************************
*******************************************************************************

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

2-Ethylhexyl nitrate (EHN) has attracted attention for its high reactivity, making it a promising candidate for use in propellants and as a combustion-enhancing fuel additive. To gain a fundamental understanding of its combustion behavior and support its practical application in advanced propulsion systems, it is essential to develop an accurate and reliable chemical kinetic model. In this study, ignition delay times (IDTs) of EHN/O₂/N₂ mixtures were systematically measured using a high-pressure shock tube. Experiments were conducted over a temperature range of 900–2000 K, at pressures of 5 and 10 bar, and under equivalence ratios of 0.5 and 1.0. The results clearly demonstrate the characteristic two-stage ignition behavior of EHN. Moreover, the IDTs were found to be highly sensitive to changes in both equivalence ratio and pressure. In the theoretical investigation, the initial decomposition pathways of EHN were systematically explored using high-level quantum chemical calculations at the QCISD(T)/CBS//M06–2X/6–311++G (d,p) level. The results indicate that cleavage of the O–N bond is the dominant reaction channel. A detailed kinetic model for EHN was developed based on the C3MechV3.3 reaction mechanism. The model predictions show good agreement with experimentally measured IDT. Furthermore, based on the current kinetic model, sensitivity, flux, and OH radical rate of production analyses were performed to identify key controlling steps and characterize radical-driven kinetics. The results show that in the first stage of ignition, over 90% of EHN is consumed via O–N bond cleavage, producing the 2-ethylhexoxy radical (EHO) and NO₂, which spontaneously initiate the NO₂–NO catalytic cycle and significantly enhance the system’s initial reactivity. In contrast, during the second stage, the chain-branching reaction H + O₂ → O + OH becomes dominant and serves as the primary driving force behind the rapid acceleration of system reactivity.

## Processing Notes

- extracted S0010218025007783_mmc1.zip
- extracted S1.docx
- extracted S4_Sensitivity Analysis.xlsx
