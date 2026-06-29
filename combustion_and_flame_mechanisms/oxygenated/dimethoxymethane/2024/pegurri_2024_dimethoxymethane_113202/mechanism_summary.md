# Coupling chemical lumping to data-driven optimization for the kinetic modeling of dimethoxymethane (DMM) combustion

## Bibliography

Alessandro Pegurri, Timoteo Dinelli, Luna Pratali Maffei, Tiziano Faravelli, Alessandro Stagni. Coupling chemical lumping to data-driven optimization for the kinetic modeling of dimethoxymethane (DMM) combustion[J]. Combustion and Flame, 2024, 260: 113202. DOI: 10.1016/j.combustflame.2023.113202.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 260 / February
- Article number: 113202
- DOI: 10.1016/j.combustflame.2023.113202
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S001021802300576X
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: dimethoxymethane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, flow reactor, laminar flame speed

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s001021802300576x_mmc3/kinetics/detailed/DMM_detailed.CKI, _processing/extracted/s001021802300576x_mmc3/kinetics/lumped/DMM_lumped.CKI, _processing/extracted/s001021802300576x_mmc3/kinetics/optimized/DMM_optimized.CKI
- Original thermodynamic source files: _processing/extracted/s001021802300576x_mmc3/kinetics/detailed/DMM_detailed.therm, _processing/extracted/s001021802300576x_mmc3/kinetics/lumped/DMM_lumped.therm, _processing/extracted/s001021802300576x_mmc3/kinetics/optimized/DMM_optimized.therm
- Original transport source files: _processing/extracted/s001021802300576x_mmc3/kinetics/detailed/DMM_detailed.TRAN, _processing/extracted/s001021802300576x_mmc3/kinetics/lumped/DMM_lumped.TRAN, _processing/extracted/s001021802300576x_mmc3/kinetics/optimized/DMM_optimized.TRAN

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: No thermo data found for species 'DMM-ket1' No thermo data found for species 'DMM-ketRO2' No thermo data found for species 'DMM-ket2' No thermo data found for species 'DMM-ketRO3' No thermo data found for species 'DMM-ketR2' No thermo data found for species 'DMM-ketR1' No thermo data found for species 'DMM-ketR3' No thermo data found for species 'DMM-cycleth2' No thermo data found for species 'DMM-cycleth1' No thermo data found for species 'DMM-ketR4' No thermo data found for species 'DMM-ketRO1' No thermo data found for species 'DMM-cyclethOOH1' No thermo data found for species 'DMM-cyclethOOH2' Ignoring duplicate transport data for species "O2CHO" on line 41 of "tran.dat". Ignoring duplicate transport data for species "AR" on line 125 of "tran.dat". Ignoring duplicate transpo ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading thermo entry in therm.dat starting on line 121: """ CHOHCO2H2 C 2H 3O 3 G 200.00 6000.00 1000.00 1 !Burcat - taken from another isomer; if = reactions present: TO BE REVISED 1.27662941E+01 1.02143437E-02-3.63547001E-06 5.83491588E-10-3.47179974E-14 2 -7.53528536E+04-3.96511752E+01 2.80443702E+00 2.10851644E-02 3.35863233E-05 3 -7.02669107E-08 3.26849274E-11-7.20649998E+04 1.51180675E+01-7.01183834E+04 4 """ Error parsing elemental composition for species 'CHOHCO2H2'. Error while reading thermo entry in therm.dat starting on line 125: """ CHOHCO C 2H 4O 3 G 200.00 6000.00 1000.00 1 ! Burcat 7.25265886E+00 7.09713194E-03-2.49703662E-06 3.97702132E-10-2.35907799E-14 2 -2.14840657E+04-9.51330315E+00 3.35107651E+00 1.55375306E-02-4.45397177E-06 3 -6.25820983E-09 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 3

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading thermo entry in therm.dat starting on line 122: """ CHOHCO2H2 C 2H 3O 3 G 200.00 6000.00 1000.00 1 !Burcat - taken from another isomer; if = reactions present: TO BE REVISED 1.27662941E+01 1.02143437E-02-3.63547001E-06 5.83491588E-10-3.47179974E-14 2 -7.53528536E+04-3.96511752E+01 2.80443702E+00 2.10851644E-02 3.35863233E-05 3 -7.02669107E-08 3.26849274E-11-7.20649998E+04 1.51180675E+01-7.01183834E+04 4 """ Error parsing elemental composition for species 'CHOHCO2H2'. Error while reading thermo entry in therm.dat starting on line 126: """ CHOHCO C 2H 4O 3 G 200.00 6000.00 1000.00 1 ! Burcat 7.25265886E+00 7.09713194E-03-2.49703662E-06 3.97702132E-10-2.35907799E-14 2 -2.14840657E+04-9.51330315E+00 3.35107651E+00 1.55375306E-02-4.45397177E-06 3 -6.25820983E-09 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

The kinetic mechanisms describing the combustion of longer-chain fuels often have limited applicability due to the high number of species involved in their oxidation and decomposition paths. This work proposes a combined methodology for developing compact but accurate kinetic mechanisms of these fuels and applies it to dimethoxymethane (DMM), or oxymethylene ether 1 (OME 1 ). An automatic chemical lumping procedure, performed by grouping structural isomers into pseudospecies, was proposed and applied to a detailed kinetic model of DMM pyrolysis and oxidation, built from state-of-the-art kinetic sub-models. Such a methodology proved particularly efficient in delivering a compact kinetic mechanism, requiring only 11 species instead of 35 to describe DMM sub-chemistry. The obtained lumped kinetic model was then improved through a data-driven optimization procedure, targeting data artificially generated by the reference detailed mechanism. The optimization was performed on the physically-constrained parameters of the modified-Arrhenius rate constants of the controlling reaction steps, identified via local sensitivity analyses. The dissimilarities between the predictions of the detailed and lumped models were minimized using a Curve Matching objective function for a comprehensive and quantitative characterization. Above all, the optimized mechanism was found to behave comparably to the starting detailed one, throughout most of the operating space and target properties (ignition delay times in shock tubes, laminar flame speeds, and speciations in stirred and flow reactors). The successful application of the proposed methodology to the DMM chemistry paves the way for its extensive use in the kinetic modeling of longer OMEs as well as heavier fuels, for which the computational advantages are expected to be even higher.

## Processing Notes

- extracted S001021802300576X_mmc3.zip
- extracted S001021802300576X_mmc2.xlsx
