# Manual Download Handoff

Items below need user-side ScienceDirect/Elsevier download or review.

## Paper PDF pending: Kinetic study of high-temperature co-oxidation of ammonia and 1,2-dimethoxyethane

- DOI: 10.1016/j.combustflame.2025.114555
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025005929
- PDF link from issue page: 
- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\ammonia_dimethoxyethane\2026\qin_2026_ammonia_dimethoxyethane_114555

## Cantera conversion failed: A kinetic and experimental analysis of the co-oxidation of ammonia and dimethoxymethane employing SVUV-PIMS

- DOI: 10.1016/j.combustflame.2025.114575
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025006121
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ammonia_dimethoxymethane\qin_2026_ammonia_dimethoxymethane_114575\extracted\s0010218025006121_mmc4\USTC-NH3_DMM.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ammonia_dimethoxymethane\qin_2026_ammonia_dimethoxymethane_114575\extracted\s0010218025006121_mmc3\USTC-NH3_DMM.dat
- Last status: cantera_failed
- Last message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 4127 and 4136 of E:\mech_collection\combustion_and_flame_mechanisms\ammonia_dimethoxymethane\2026\qin_2026_ammonia_dimethoxymethane_114575\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 36: H + OH + M <=> H2O + M
Reaction 35: H2O + H2O <=> H + OH + H2O

|  Line |
|  4122 |   note: RAS/GLA08a HIP/TRO95
|  4123 | - equation: H2O2 + OH <=> H2O + HO2  # Reaction 34
|  4124 |   duplicate: true
|  4125 |   rate-constant: {A: 1.6e+18, b: 0.0, Ea: 2.941e+04}
|  4126 |   note: RAS/GLA08a HIP/TRO95
>  4127 > - equation: H + OH + M <=> H2O + M  # Reaction 35
            ^
|  4128 |   type: three-body
|  4129 |   rate-constant: {A: 8.62e+21, b: -2.0, Ea: 0.0}
|  4130 |   efficiencies: {H2O: 16.25, CO: 1.875, CO2: 3.75}
|  4131 |   note: |-
|  4132 |     r28
|  4133 |     OH+H+M=H2O+M                         4.5E22  -2.000       0 ! RAS/GLA08a CON/WES04
|  4134 |      AR/0.38/ H2/0.73/ H2O/12/ !HE/0.38/
|  4135 |     	BAULCH	76
>  4136 > - equation: 2 H2O <=> OH + H + H2O  # Reaction 36
            ^
|  4137 |   rate-constant: {A: 1.0e+26, b: -2.44, Ea: 1.2016e+05}
|  4138 | - equation: OH + H2 <=> H + H2O  # Reaction 37
|  4139 |   rate-constant: {A: 4.38e+13, b: 0.0, Ea: 6990.0}
*******************************************************************************

- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\ammonia_dimethoxymethane\2026\qin_2026_ammonia_dimethoxymethane_114575

## Cantera conversion failed: Experimental and kinetic insight on auto-ignition process of ammonia/propane mixture: Focus on oxygen effect

- DOI: 10.1016/j.combustflame.2025.114572
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025006091
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ammonia_propane\liang_2026_ammonia_propane_114572\extracted\s0010218025006091_mmc3\Mech.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ammonia_propane\liang_2026_ammonia_propane_114572\extracted\s0010218025006091_mmc3\Mech.inp
- Last status: cantera_failed
- Last message: CanteraError: 
*******************************************************************************
CanteraError thrown by addReactions:

*******************************************************************************
InputFileError thrown by PlogRate::validate:
Error on line 17297 of E:\mech_collection\combustion_and_flame_mechanisms\ammonia_propane\2026\liang_2026_ammonia_propane_114572\mechanism.yaml:

Invalid rate coefficient for reaction 'C4H6 <=> C3H3 + CH3'
at P = 15999, T = 200.0
at P = 31997, T = 200.0

|  Line |
|  17292 |   - {P: 0.0394737 atm, A: 2.34423e+73, b: -17.49, Ea: 1.085e+05}
|  17293 |   - {P: 0.0789474 atm, A: 4.57088e+71, b: -16.91, Ea: 1.087e+05}
|  17294 |   - {P: 0.157895 atm, A: 9.54993e+69, b: -16.33, Ea: 1.09e+05}
|  17295 |   - {P: 0.315789 atm, A: 2.04174e+67, b: -15.48, Ea: 1.085e+05}
|  17296 |   note: Added from donor mechanism
>  17297 > - equation: C4H6 <=> CH3 + C3H3  # Reaction 2351
            ^
|  17298 |   type: pressure-dependent-Arrhenius
|  17299 |   rate-constants:
|  17300 |   - {P: 0.0394737 atm, A: 1.5849e+148, b: -37.24, Ea: 1.885e+05}
*******************************************************************************

*******************************************************************************
InputFileError thrown by PlogRate::validate:
Error on line 31740 of E:\mech_collection\combustion_and_flame_mechanisms\ammonia_propane\2026\liang_2026_ammonia_propane_114572\mechanism.yaml:

Invalid rate coefficient for reaction 'C4H6 <=> C3H3 + CH3'
at P = 15999, T = 200.0
at P = 31997, T = 200.0

|  Line |
|  31735 |   - {P: 0.0394737 atm, A: 2.34423e+73, b: -17.49, Ea: 1.085e+05}
|  31736 |   - {P: 0.0789474 atm, A: 4.57088e+71, b: -16.91, Ea: 1.087e+05}
|  31737 |   - {P: 0.157895 atm, A: 9.54993e+69, b: -16.33, Ea: 1.09e+05}
|  31738 |   - {P: 0.315789 atm, A: 2.04174e+67, b: -15.48, Ea: 1.085e+05}
|  31739 |   note: Added from donor mechanism
>  31740 > - equation: C4H6 <=> CH3 + C3H3  # Reaction 5685
            ^
|  31741 |   type: pressure-dependent-Arrhenius
|  31742 |   rate-constants:
|  31743 |   - {P: 0.0394737 atm, A: 1.5849e+148, b: -37.24, Ea: 1.885e+05}
*******************************************************************************
*******************************************************************************

- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\ammonia_propane\2026\liang_2026_ammonia_propane_114572

## Paper PDF pending: Comprehensive kinetic modeling and shock tube study of acetone pyrolysis and oxidation

- DOI: 10.1016/j.combustflame.2025.114581
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025006182
- PDF link from issue page: 
- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\acetone\2026\song_2026_acetone_114581

## Cantera conversion failed: Experimental and kinetic modeling study of ethyl acetate pyrolysis and oxidation in a shock tube

- DOI: 10.1016/j.combustflame.2025.114576
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025006133
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ethyl_acetate\yang_2026_ethyl_acetate_114576\extracted\s0010218025006133_mmc5\Current mech.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ethyl_acetate\yang_2026_ethyl_acetate_114576\extracted\s0010218025006133_mmc4\Current thermo.dat
- Last status: cantera_failed
- Last message: ValueError: could not convert string to float: 'c2h5oco    2/ 9'; numeric cleanup retry failed: ValueError: could not convert string to float: 'c2h5oco    2/ 9'
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\ethyl_acetate\2026\yang_2026_ethyl_acetate_114576

## Cantera conversion failed: Experimental and kinetic study on polycyclic aromatic hydrocarbons formation in naphtha pyrolysis

- DOI: 10.1016/j.combustflame.2025.114600
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025006376
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\naphtha\wang_2026_naphtha_114600\extracted\s0010218025006376_mmc2\naphtha mechanism -FINAL.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\naphtha\wang_2026_naphtha_114600\extracted\s0010218025006376_mmc2\naphtha mechanism -FINAL.inp
- Last status: cantera_failed
- Last message: RuntimeError: bad allocation
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\naphtha\2026\wang_2026_naphtha_114600

## Paper PDF pending: Laminar flame speed of hydrogen-enriched sustainable aviation fuel: Experiments and chemical kinetic modeling

- DOI: 10.1016/j.combustflame.2025.114613
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025006509
- PDF link from issue page: 
- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\hydrogen_saf\2026\hong_2026_hydrogen_saf_114613

## Paper PDF pending: Detailed pyrolysis mechanism for ammonium nitrate and ammonium chloride mixtures

- DOI: 10.1016/j.combustflame.2025.114601
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025006388
- PDF link from issue page: https://www.sciencedirect.com/science/article/pii/S0010218025006388/pdfft?md5=36c58244e76bfe0438e917950f12b9b2&pid=1-s2.0-S0010218025006388-main.pdf
- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\ammonium_nitrate_ammonium_chloride\2026\izato_2026_ammonium_nitrate_ammonium_chloride_114601

## Paper PDF pending: Bayesian sequential experimental design for combustion kinetic models: A surrogate-assisted nonlinear framework with improved information gain

- DOI: 10.1016/j.combustflame.2025.114610
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025006479
- PDF link from issue page: 
- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\unknown_fuel\2026\liu_2026_unknown_fuel_114610

## Cantera conversion failed: Co-oxidation of ammonia with ethylene and acetylene: An experimental and kinetic modeling study

- DOI: 10.1016/j.combustflame.2025.114630
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025006674
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ammonia_ethylene_acetylene\wang_2026_ammonia_ethylene_acetylene_114630\raw_downloads\S0010218025006674_mmc3.txt
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ammonia_ethylene_acetylene\wang_2026_ammonia_ethylene_acetylene_114630\raw_downloads\S0010218025006674_mmc3.txt; E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ammonia_ethylene_acetylene\wang_2026_ammonia_ethylene_acetylene_114630\raw_downloads\S0010218025006674_mmc4.txt
- Last status: cantera_failed
- Last message: InputError: No thermo data found for species 'H2'
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\ammonia_ethylene_acetylene\2026\wang_2026_ammonia_ethylene_acetylene_114630

## Cantera conversion failed: Experimental and kinetic modeling studies on high-pressure oxidation of RP-3 surrogate fuel. Part Ⅱ: The effect of aromatic component

- DOI: 10.1016/j.combustflame.2025.114651
- URL: https://www.sciencedirect.com/science/article/pii/S001021802500687X
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\rp3\gao_2026_rp3_114651\extracted\s001021802500687x_mmc2\mmc2.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\rp3\gao_2026_rp3_114651\extracted\s001021802500687x_mmc3\mmc3.txt
- Last status: cantera_failed
- Last message: IndexError: list index out of range; numeric cleanup retry failed: IndexError: list index out of range
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\rp3\2026\gao_2026_rp3_114651

## Cantera conversion failed: Elucidating norbornane auto-ignition behavior via RCM experiments and kinetic modelling

- DOI: 10.1016/j.combustflame.2025.114656
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025006911
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\norbornane\xiao_2026_norbornane_114656\extracted\s0010218025006911_mmc4\Nor_O2-Xiao25-Mech.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\norbornane\xiao_2026_norbornane_114656\extracted\s0010218025006911_mmc5\Nor_O2-Xiao25-thermo.dat
- Last status: cantera_failed
- Last message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 16067 and 16094 of E:\mech_collection\combustion_and_flame_mechanisms\norbornane\2026\xiao_2026_norbornane_114656\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 989: H2 + M <=> 2 H + M
Reaction 985: 2 H + O2 <=> H2 + O2

|  Line |
|  16062 |   note: Added in v6
|  16063 | - equation: cCHC6H10-7-OO + cCHC6H10-7-OO <=> cCHC6H10-7-O + cCHC6H10-7-O
|  16064 |     + O2  # Reaction 984
|  16065 |   rate-constant: {A: 1.4e+16, b: -1.61, Ea: 1860.0}
|  16066 |   note: Added in v6
>  16067 > - equation: H2 + M <=> H + H + M  # Reaction 985
            ^
|  16068 |   type: three-body
|  16069 |   rate-constant: {A: 4.577e+19, b: -1.4, Ea: 1.044e+05}
|  16070 |   efficiencies: {HE: 0.83, CO: 1.9, CH4: 2.0, H2: 2.5, C2H6: 3.0, CO2: 3.8,
...
|  16089 |     CHEM REF DATA 2005, 34, 757-1397. !\Comment: WARNING'
|  16090 | - equation: H2 + OH <=> H + H2O  # Reaction 988
|  16091 |   rate-constant: {A: 2.2e+08, b: 1.51, Ea: 3430.0}
|  16092 |   note: '\Author: UB !\Ref: J.V.MICHAEL SUTHERLAND, J.PHYS.CHEM. 92(1988)
|  16093 |     3853 !\Comment: WARNING'
>  16094 > - equation: H + O2 + H <=> H2 + O2  # Reaction 989
            ^
|  16095 |   rate-constant: {A: 8.8e+22, b: -1.835, Ea: 800.0}
|  16096 |   note: '\Author: WARNING !\Ref: WARNING !\Comment: WARNING'
|  16097 | - equation: H + O2 + H <=> OH + OH  # Reaction 990
*******************************************************************************

- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\norbornane\2026\xiao_2026_norbornane_114656

## Cantera conversion failed: Investigation of kinetic inhibition effectiveness and mechanisms of HCFO-1233xf as a new fire extinguishing agent

- DOI: 10.1016/j.combustflame.2025.114663
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025006984
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\hcfo_1233xf\wang_2026_hcfo_1233xf_114663\raw_downloads\S0010218025006984_mmc1.txt
- Thermodynamic candidates: 
- Last status: cantera_failed
- Last message: ValueError: could not convert string to float: '0.902,'; numeric cleanup retry failed: ValueError: could not convert string to float: '696.,'
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\hcfo_1233xf\2026\wang_2026_hcfo_1233xf_114663

## Cantera conversion failed: Ignition and combustion characteristics of cyclopentanone and cyclopentanone/gasoline blends: An experimental and modeling study

- DOI: 10.1016/j.combustflame.2025.114647
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025006844
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\cyclopentanone_gasoline\zhang_2026_cyclopentanone_gasoline_114647\extracted\s0010218025006844_mmc1\Base_Gasoline_PAH_CPN.chmech
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\cyclopentanone_gasoline\zhang_2026_cyclopentanone_gasoline_114647\extracted\s0010218025006844_mmc2\Base_Gasoline_PAH_CPN.chthermo; E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\cyclopentanone_gasoline\zhang_2026_cyclopentanone_gasoline_114647\extracted\s0010218025006844_mmc5\Base_Gasoline_PAH_CPN.thermo
- Last status: cantera_failed
- Last message: InputError: No thermo data found for species 'A1-C6H6'
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\cyclopentanone_gasoline\2026\zhang_2026_cyclopentanone_gasoline_114647

## Paper PDF pending: Synergistic suppression of magnesium dust explosions by montmorillonite/ammonium polyphosphate composites: Experimental and kinetic modeling insights

- DOI: 10.1016/j.combustflame.2025.114667
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025007023
- PDF link from issue page: 
- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\magnesium\2026\qiu_2026_magnesium_114667

## Cantera conversion failed: Triptane (2,2,3-trimethylbutane) as an Anti-Knock Additive in Renewable Gasoline: Experiments and Kinetic Modelling

- DOI: 10.1016/j.combustflame.2025.114696
- URL: https://www.sciencedirect.com/science/article/pii/S001021802500731X
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\triptane_gasoline\aljohani_2026_triptane_gasoline_114696\extracted\s001021802500731x_mmc2\SM_for_TMB_MTG\SM_for_TMB_MTG\Kinetic_model\mech_TMB.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\triptane_gasoline\aljohani_2026_triptane_gasoline_114696\extracted\s001021802500731x_mmc2\SM_for_TMB_MTG\SM_for_TMB_MTG\Kinetic_model\thermo_TMB.dat
- Last status: cantera_failed
- Last message: InputError: Error parsing elemental composition for species thermo entry:
 2.42791871e+01 2.51543795e-02-8.59067806e-06 1.33406642e-09-7.74653905e-14    2
-5.10801725e+03-1.01377558e+02-1.30412122e+00 8.49858457e-02-6.36219850e-05    3
 2.57814973e-08-4.60828679e-12 3.80331867e+03 3.61105145e+01                   4

Element amounts can have no more than 3 digits.
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\triptane_gasoline\2026\aljohani_2026_triptane_gasoline_114696

## Paper PDF pending: A detailed kinetic mechanism for ammonia combustion informed by DFT calculations

- DOI: 10.1016/j.combustflame.2025.114697
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025007321
- PDF link from issue page: 
- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\ammonia\2026\ren_2026_ammonia_114697

## Cantera conversion failed: A synchrotron photoionization mass spectrometric study on plasma-assisted oxidation of propanol isomers in a nanosecond discharge

- DOI: 10.1016/j.combustflame.2025.114705
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025007400
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\propanol\li_2026_propanol_114705\extracted\s0010218025007400_mmc2\SMM2.inp; E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\propanol\li_2026_propanol_114705\extracted\s0010218025007400_mmc3\SMM3.inp
- Thermodynamic candidates: 
- Last status: cantera_failed
- Last message: ValueError: could not convert string to float: '+4.214+14'; numeric cleanup retry failed: InputError: No thermo data found for species 'E'
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\propanol\2026\li_2026_propanol_114705

## Paper PDF pending: A combined experimental and comprehensive kinetic modeling study of laminar burning velocities for C0–C1 multi-component fuel blends

- DOI: 10.1016/j.combustflame.2026.114881
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026001173
- PDF link from issue page: https://www.sciencedirect.com/science/article/pii/S0010218026001033/pdfft?md5=e31f686f77b544afbb1fd44dfbd6f2c9&pid=1-s2.0-S0010218026001033-main.pdf
- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\c0_c1_fuel_blends\2026\zhu_2026_c0_c1_fuel_blends_114881

## Cantera conversion failed: Carbon dioxide-driven dual effects on ignition delay and preignition behavior in plasma-assisted methanol ignition

- DOI: 10.1016/j.combustflame.2026.114882
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026001185
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\methanol\liu_2026_methanol_114882\extracted\s0010218026001185_mmc2\mmc2\SMM\Chem.inp; E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\methanol\liu_2026_methanol_114882\extracted\s0010218026001185_mmc2\mmc2\SMM\plasma kinetics.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\methanol\liu_2026_methanol_114882\extracted\s0010218026001185_mmc2\mmc2\SMM\Therm.dat
- Last status: cantera_failed
- Last message: InputError: Section starts with unrecognized keyword
"""
BOLSIG
"""
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.; cleanup retry failed: InputError: Section starts with unrecognized keyword
"""
BOLSIG
"""
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\methanol\2026\liu_2026_methanol_114882

## Cantera conversion failed: Experimental and modeling study of pressure and NOx addition effects on syngas oxidation in a flow reactor

- DOI: 10.1016/j.combustflame.2026.114938
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026001744
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\syngas\liu_2026_syngas_114938\extracted\s0010218026001744_mmc2\Supplementary Material 2_chem.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\syngas\liu_2026_syngas_114938\extracted\s0010218026001744_mmc3\Supplementary Material 3_thermo.dat
- Last status: cantera_failed
- Last message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 451 and 676 of E:\mech_collection\combustion_and_flame_mechanisms\syngas\2026\liu_2026_syngas_114938\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 41: H2 + M <=> 2 H + M
Reaction 1: 2 H + O2 <=> H2 + O2

|  Line |
|   446 |     - [4.04483566, 7.31130186e-03, -2.47625799e-06, 3.83733021e-10, -2.23107573e-14,
|   447 |       2.5324142e+04, 2.88423392]
|   448 |     note: T 7/11
|   449 | 
|   450 | reactions:
>   451 > - equation: H2 + M <=> H + H + M  # Reaction 1
            ^
|   452 |   type: three-body
|   453 |   rate-constant: {A: 4.577e+19, b: -1.4, Ea: 1.044e+05}
|   454 |   efficiencies: {H2: 2.5, H2O: 12.0, CO: 1.9, CO2: 3.8, HE: 0.83, CH4: 2.0,
...
|   671 |   rate-constant: {A: 3.93e+13, b: 0.0, Ea: 0.0}
|   672 |   note: '\Author: SP !\Ref: YU ET AL., JCP, 2008, 129(21) !\Comment: WARNING'
|   673 | - equation: CO + H2O <=> CO2 + H2  # Reaction 40
|   674 |   rate-constant: {A: 2.0e+11, b: 0.0, Ea: 3.8e+04}
|   675 |   note: POLIMI Mech
>   676 > - equation: H + O2 + H <=> H2 + O2  # Reaction 41
            ^
|   677 |   rate-constant: {A: 8.8e+22, b: -1.835, Ea: 800.0}
|   678 |   note: |-
|   679 |     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
*******************************************************************************

- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\syngas\2026\liu_2026_syngas_114938

## Cantera conversion failed: Combustion reaction mechanism of C0-C3/N2O flames: Experimental and kinetic modeling study of laminar burning velocity

- DOI: 10.1016/j.combustflame.2026.114948
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026001847
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\n2o_c0_c3_fuel_blends\ge_2026_n2o_c0_c3_fuel_blends_114948\extracted\s0010218026001847_mmc2\Chem.txt
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\n2o_c0_c3_fuel_blends\ge_2026_n2o_c0_c3_fuel_blends_114948\extracted\s0010218026001847_mmc3\Thermo.txt
- Last status: cantera_failed
- Last message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 2565 and 2751 of E:\mech_collection\combustion_and_flame_mechanisms\n2o_c0_c3_fuel_blends\2026\ge_2026_n2o_c0_c3_fuel_blends_114948\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 448: NNH + M <=> H + N2 + M
Reaction 400: NNH + O2 <=> H + N2 + O2

|  Line |
|  2560 |   note: GRI Mech 3.0
|  2561 | - equation: NH2 + H <=> NH + H2  # Reaction 399
|  2562 |   duplicate: true
|  2563 |   rate-constant: {A: 4.0e+13, b: 0.0, Ea: 3650.0}
|  2564 |   note: GRI Mech 3.0
>  2565 > - equation: NNH + M <=> N2 + H + M  # Reaction 400
            ^
|  2566 |   type: three-body
|  2567 |   rate-constant: {A: 1.3e+14, b: -0.11, Ea: 4980.0}
|  2568 |   efficiencies: {H2: 2.0, H2O: 6.0, CH4: 2.0, CO: 1.5, CO2: 2.0, C2H6: 3.0,
...
|  2746 |   note: J.W. Bozzelli, et al., International journal of chemical kinetics
|  2747 |     27 (1995) 1097-1109
|  2748 | - equation: NNH + O2 <=> N2 + HO2  # Reaction 447
|  2749 |   rate-constant: {A: 5.6e+14, b: -0.385, Ea: -13.0}
|  2750 |   note: S.J. Klippenstein, et al., Combustion and Flame 158 (2011) 774-789
>  2751 > - equation: NNH + O2 <=> N2 + H + O2  # Reaction 448
            ^
|  2752 |   rate-constant: {A: 5.0e+13, b: 0.0, Ea: 0.0}
|  2753 |   note: P. Glarborg, et al., Combustion and Flame 115 (1998) 1-27.
|  2754 | - equation: NNH + NO <=> N2 + HNO  # Reaction 449
*******************************************************************************

- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\n2o_c0_c3_fuel_blends\2026\ge_2026_n2o_c0_c3_fuel_blends_114948

## Cantera conversion failed: Measurements of the laminar burning velocities and an improved low-to-high temperature kinetic model of 2-butanone

- DOI: 10.1016/j.combustflame.2026.114947
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026001835
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\2_butanone\guo_2026_2_butanone_114947\extracted\s0010218026001835_mmc3\Butanone_V4MECH.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\2_butanone\guo_2026_2_butanone_114947\extracted\s0010218026001835_mmc4\Butanone_V4THER.dat
- Last status: cantera_failed
- Last message: ValueError: could not convert string to float: 'N2'; numeric cleanup retry failed: ValueError: could not convert string to float: 'N2'
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\2_butanone\2026\guo_2026_2_butanone_114947

## Paper PDF pending: Development and numerical analysis of a detailed kinetic for ammonia and volatiles co-combustion flames

- DOI: 10.1016/j.combustflame.2026.114976
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026002129
- PDF link from issue page: 
- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\ammonia\2026\ren_2026_ammonia_114976

## Paper PDF pending: The role of polyyne chemistry in soot formation: the case study of acetylene pyrolysis

- DOI: 10.1016/j.combustflame.2026.114989
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026002257
- PDF link from issue page: https://www.sciencedirect.com/science/article/pii/S0010218026002257/pdfft?md5=80d86537e038b12ab4d941fba60ebf9b&pid=1-s2.0-S0010218026002257-main.pdf
- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\acetylene\2026\viola_2026_acetylene_114989

## Cantera conversion failed: An experimental and modeling investigation of the oxidation chemistry of 1,2,4-trimethylbenzene in jet-stirred reactor and flow reactor

- DOI: 10.1016/j.combustflame.2026.115003
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026002397
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\trimethylbenzene_124\suzuki_2026_trimethylbenzene_124_115003\raw_downloads\S0010218026002397_mmc4.txt
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\trimethylbenzene_124\suzuki_2026_trimethylbenzene_124_115003\raw_downloads\S0010218026002397_mmc5.txt
- Last status: cantera_failed
- Last message: IndexError: list index out of range; numeric cleanup retry failed: IndexError: list index out of range
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\trimethylbenzene_124\2026\suzuki_2026_trimethylbenzene_124_115003

## Paper PDF pending: An experimental and modeling study of ammonia/methane combustion: The importance of carbon–nitrogen interaction reactions

- DOI: 10.1016/j.combustflame.2026.115015
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026002518
- PDF link from issue page: https://www.sciencedirect.com/science/article/pii/S0010218026002518/pdfft?md5=63d641dc599d8d7125fae187205917a6&pid=1-s2.0-S0010218026002518-main.pdf
- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\ammonia_methane\2026\zhu_2026_ammonia_methane_115015

## Cantera conversion failed: Mid-infrared multicomponent laser diagnostic and kinetic modelling studies of furan and 2-methylfuran combustion in a shock tube

- DOI: 10.1016/j.combustflame.2026.115009
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026002452
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\furan_2_methylfuran\yang_2026_furan_2_methylfuran_115009\raw_downloads\S0010218026002452_mmc2.txt
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\furan_2_methylfuran\yang_2026_furan_2_methylfuran_115009\raw_downloads\S0010218026002452_mmc3.txt
- Last status: cantera_failed
- Last message: InputError: Unexpected token "+Hv" in reaction expression "OH*<=>R2OH+Hv
".
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.; numeric cleanup retry failed: InputError: Unexpected token "+Hv" in reaction expression "OH*<=>R2OH+Hv
".
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\furan_2_methylfuran\2026\yang_2026_furan_2_methylfuran_115009

## Cantera conversion failed: Understanding the formation of nitrogen-containing products in pyrrole pyrolysis

- DOI: 10.1016/j.combustflame.2026.115037
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026002737
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\pyrrole\xie_2026_pyrrole_115037\raw_downloads\S0010218026002737_mmc2.txt
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\pyrrole\xie_2026_pyrrole_115037\raw_downloads\S0010218026002737_mmc3.txt
- Last status: cantera_failed
- Last message: InputError: Unexpected token "C2H5CN+CH2CN" in reaction expression "C2H5CN+CH2CN=NCCH2CN+C2H5
".
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.; numeric cleanup retry failed: InputError: Unexpected token "C2H5CN+CH2CN" in reaction expression "C2H5CN+CH2CN=NCCH2CN+C2H5
".
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\pyrrole\2026\xie_2026_pyrrole_115037

## Cantera conversion failed: Unravelling the combustion kinetics of N-methyl aniline: decomposition and OH-addition pathways from quantum chemistry and flame speed measurements

- DOI: 10.1016/j.combustflame.2026.115050
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026002865
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\n_methyl_aniline\pingle_2026_n_methyl_aniline_115050\extracted\s0010218026002865_mmc4\mech.dat; E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\n_methyl_aniline\pingle_2026_n_methyl_aniline_115050\extracted\s0010218026002865_mmc4\Nma_correctedrates_benzene_gas.inp; E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\n_methyl_aniline\pingle_2026_n_methyl_aniline_115050\extracted\s0010218026002865_mmc4\NMA_decomp_oh_reactions.dat; E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\n_methyl_aniline\pingle_2026_n_methyl_aniline_115050\extracted\s0010218026002865_mmc4\Updated barrierless reactions_rotor_hindered.txt
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\n_methyl_aniline\pingle_2026_n_methyl_aniline_115050\extracted\s0010218026002865_mmc4\Nma_correctedrates_benzene_gas.inp; E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\n_methyl_aniline\pingle_2026_n_methyl_aniline_115050\extracted\s0010218026002865_mmc4\therm.dat; E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\n_methyl_aniline\pingle_2026_n_methyl_aniline_115050\extracted\s0010218026002865_mmc4\therm_decomp_oh_reactions.dat
- Last status: cantera_failed
- Last message: InputError: Unexpected token "C6H5NHCH3" in reaction expression "C6H5NHCH3=C6H5NCH3+H
".
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.; numeric cleanup retry failed: InputError: Unexpected token "C6H5NHCH3" in reaction expression "C6H5NHCH3=C6H5NCH3+H
".
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\n_methyl_aniline\2026\pingle_2026_n_methyl_aniline_115050

## Cantera conversion failed: An experimental, theoretical and modeling study of the pyrolysis and oxidation of propan-1-ol using CO time-history measurements behind reflected shock waves

- DOI: 10.1016/j.combustflame.2026.115033
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026002695
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\propanol\gr_goire_2026_propanol_115033\extracted\s0010218026002695_mmc1\chem_pro1oh.inp
- Thermodynamic candidates: 
- Last status: cantera_failed
- Last message: ValueError: could not convert string to float: '2.400+07'; numeric cleanup retry failed: InputError: No thermo data found for species 'co'
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\propanol\2026\gr_goire_2026_propanol_115033

## Cantera conversion failed: Formation of (N-containing) polycyclic aromatic hydrocarbons from pyrrole pyrolysis and its co-pyrolysis with ethylene

- DOI: 10.1016/j.combustflame.2026.115096
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026003329
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ethylene_pyrrole\luo_2026_ethylene_pyrrole_115096\extracted\s0010218026003329_mmc1\mmc1.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ethylene_pyrrole\luo_2026_ethylene_pyrrole_115096\extracted\s0010218026003329_mmc3\mmc3.dat
- Last status: cantera_failed
- Last message: CanteraError: 
*******************************************************************************
CanteraError thrown by addReactions:

*******************************************************************************
InputFileError thrown by PlogRate::validate:
Error on line 2317 of E:\mech_collection\combustion_and_flame_mechanisms\ethylene_pyrrole\2026\luo_2026_ethylene_pyrrole_115096\mechanism.yaml:

Invalid rate coefficient for reaction 'C2H2 + C7H4N <=> C9H6N'
at P = 6666.2, T = 200.0

|  Line |
|  2312 |   rate-constants:
|  2313 |   - {P: 0.06579 atm, A: 4.26e+23, b: -3.6, Ea: 9212.0}
|  2314 |   - {P: 1.0 atm, A: 4.19e+68, b: -16.41, Ea: 3.995e+04}
|  2315 |   - {P: 10.0 atm, A: 2.55e+37, b: -8.03, Ea: 1.678e+04}
|  2316 |   - {P: 100.0 atm, A: 7.93e+40, b: -7.87, Ea: 3.37e+04}
>  2317 > - equation: C7H4N + C2H2 <=> C9H6N  # Reaction 20
            ^
|  2318 |   duplicate: true
|  2319 |   type: pressure-dependent-Arrhenius
|  2320 |   rate-constants:
*******************************************************************************
*******************************************************************************

- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\ethylene_pyrrole\2026\luo_2026_ethylene_pyrrole_115096

## Paper PDF pending: Methyl formate oxidation kinetics up to 100 atm

- DOI: 10.1016/j.combustflame.2026.115098
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026003342
- PDF link from issue page: 
- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\methyl_formate\2026\cao_2026_methyl_formate_115098

## Cantera conversion failed: Low-temperature oxidation chemistry of secondary pentanols: An ozone-assisted study of 2- and 3-pentanol

- DOI: 10.1016/j.combustflame.2026.115110
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026003469
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\pentanol\teka_2026_pentanol_115110\extracted\s0010218026003469_mmc3\MECH.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\pentanol\teka_2026_pentanol_115110\extracted\s0010218026003469_mmc4\THERM.dat
- Last status: cantera_failed
- Last message: CanteraError: 
*******************************************************************************
CanteraError thrown by addReactions:

*******************************************************************************
InputFileError thrown by PlogRate::validate:
Error on line 12864 of E:\mech_collection\combustion_and_flame_mechanisms\pentanol\2026\teka_2026_pentanol_115110\mechanism.yaml:

Invalid rate coefficient for reaction 'C4H6 <=> C3H3 + CH3'
at P = 16009, T = 200.0
at P = 32019, T = 200.0

|  Line |
|  12859 |   rate-constants:
|  12860 |   - {P: 0.0395 atm, A: 2.34e+73, b: -17.49, Ea: 1.085e+05}
|  12861 |   - {P: 0.0789 atm, A: 4.57e+71, b: -16.91, Ea: 1.087e+05}
|  12862 |   - {P: 0.158 atm, A: 9.55e+69, b: -16.33, Ea: 1.09e+05}
|  12863 |   - {P: 0.316 atm, A: 2.04e+67, b: -15.48, Ea: 1.085e+05}
>  12864 > - equation: C4H6 <=> CH3 + C3H3  # Reaction 1362
            ^
|  12865 |   type: pressure-dependent-Arrhenius
|  12866 |   rate-constants:
|  12867 |   - {P: 0.0395 atm, A: 1.58e+148, b: -37.24, Ea: 1.885e+05}
*******************************************************************************
*******************************************************************************

- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\pentanol\2026\teka_2026_pentanol_115110

## Cantera conversion failed: Assessment of conditional source-term estimation (CSE) with direct chemistry integration including detailed and reduced kinetics for the simulation of a turbulent DME flame

- DOI: 10.1016/j.combustflame.2025.114714
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025007497
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\dimethyl_ether\mahdipour_2026_dimethyl_ether_114714\extracted\s0010218025007497_mmc1\DME_reduced_CK_input
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\dimethyl_ether\mahdipour_2026_dimethyl_ether_114714\extracted\s0010218025007497_mmc1\DME_reduced_CK_input
- Last status: cantera_failed
- Last message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 241 and 398 of E:\mech_collection\combustion_and_flame_mechanisms\dimethyl_ether\2026\mahdipour_2026_dimethyl_ether_114714\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 64: H + O2 <=> O + OH
Reaction 1: H + O2 <=> O + OH

|  Line |
|   236 |       -1.123918e+04, 14.43229]
|   237 |     - [4.825938, 0.01384043, -4.557259e-06, 6.724967e-10, -3.598161e-14,
|   238 |       -1.271779e+04, -5.239507]
|   239 | 
|   240 | reactions:
>   241 > - equation: H + O2 <=> O + OH  # Reaction 1
            ^
|   242 |   rate-constant: {A: 3.5470000000000005e+15, b: -0.406, Ea: 1.6599e+04}
|   243 | - equation: H2 + O <=> H + OH  # Reaction 2
|   244 |   rate-constant: {A: 5.0800000000000015e+04, b: 2.67, Ea: 6290.0}
...
|   393 |   rate-constant: {A: 1.8550000000000003e-03, b: 5.29, Ea: -109.0}
|   394 | - equation: CH3OCH3 + HO2 <=> CH3OCH2 + H2O2  # Reaction 62
|   395 |   rate-constant: {A: 2.0000000000000004e+13, b: 0.0, Ea: 1.65e+04}
|   396 | - equation: CH3OCH2 <=> CH2O + CH3  # Reaction 63
|   397 |   rate-constant: {A: 1.2e+13, b: 0.0, Ea: 2.575e+04}
>   398 > - equation: H + O2 <=> O + OH  # Reaction 64
            ^
|   399 |   rate-constant: {A: 3.5470000000000005e+15, b: -0.406, Ea: 1.6599e+04}
|   400 | - equation: H2 + O <=> H + OH  # Reaction 65
|   401 |   rate-constant: {A: 5.0800000000000015e+04, b: 2.67, Ea: 6290.0}
*******************************************************************************

- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\dimethyl_ether\2026\mahdipour_2026_dimethyl_ether_114714

## Cantera conversion failed: An experimental and kinetic modeling study of the autoignition mechanism of 2-ethylhexyl nitrate combustion

- DOI: 10.1016/j.combustflame.2025.114743
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025007783
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\2_ethylhexyl_nitrate\xie_2026_2_ethylhexyl_nitrate_114743\extracted\s0010218025007783_mmc1\EHN.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\2_ethylhexyl_nitrate\xie_2026_2_ethylhexyl_nitrate_114743\extracted\s0010218025007783_mmc1\EHN.dat
- Last status: cantera_failed
- Last message: CanteraError: 
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

- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\2_ethylhexyl_nitrate\2026\xie_2026_2_ethylhexyl_nitrate_114743

## Cantera conversion failed: Experimental and kinetic study of pyridine pyrolysis with tunable synchrotron VUV photoionization and molecular beam mass spectrometry

- DOI: 10.1016/j.combustflame.2025.114742
- URL: https://www.sciencedirect.com/science/article/pii/S0010218025007771
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\pyridine\ye_2026_pyridine_114742\raw_downloads\S0010218025007771_mmc2.txt
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\pyridine\ye_2026_pyridine_114742\raw_downloads\S0010218025007771_mmc3.txt
- Last status: cantera_failed
- Last message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 11031 and 11098 of E:\mech_collection\combustion_and_flame_mechanisms\pyridine\2026\ye_2026_pyridine_114742\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 1812: H2 + M <=> 2 H + M
Reaction 1800: 2 H + O2 <=> H2 + O2

|  Line |
|  11026 |   note: M. Sangwan, L. N. Krasnoperov, The Journal of Physical Chemistry
|  11027 |     A 116 (2012) 11817?1822.
|  11028 | - equation: OH + OH <=> O + H2O  # Reaction 1799
|  11029 |   duplicate: true
|  11030 |   rate-constant: {A: 2.6e+11, b: -0.057, Ea: -827.0}
>  11031 > - equation: H2 + M <=> H + H + M  # Reaction 1800
            ^
|  11032 |   type: three-body
|  11033 |   rate-constant: {A: 4.6e+19, b: -1.4, Ea: 1.0438e+05}
|  11034 |   efficiencies: {H2: 2.5, H2O: 12.0, CO: 1.9, CO2: 3.8, AR: 0.0, HE: 0.0}
...
|  11093 |   note: M. P. Burke, S. J. Klippenstein, L. B. Harding, Proceedings of the
|  11094 |     Combustion Institute 34 (2013) 547?55.
|  11095 | - equation: HO2 + OH <=> H2O + O2  # Reaction 1811
|  11096 |   duplicate: true
|  11097 |   rate-constant: {A: 1.2e+09, b: 1.24, Ea: -1310.0}
>  11098 > - equation: H + O2 + H <=> H2 + O2  # Reaction 1812
            ^
|  11099 |   rate-constant: {A: 8.8e+22, b: -1.835, Ea: 800.0}
|  11100 |   note: M. Burke, S. Klippenstein, Nature Chemistry, 9, 1078 C1082 (2017)
|  11101 | - equation: H + O2 + H <=> OH + OH  # Reaction 1813
*******************************************************************************

- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\pyridine\2026\ye_2026_pyridine_114742

## Cantera conversion failed: High-temperature pyrolysis and oxidation of nitromethane: laser diagnostics and model development for C–N–O combustion chemistry

- DOI: 10.1016/j.combustflame.2026.114782
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026000192
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\nitromethane\song_2026_nitromethane_114782\extracted\s0010218026000192_mmc3\BIT_NM model_mech.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\nitromethane\song_2026_nitromethane_114782\extracted\s0010218026000192_mmc4\BIT_NM model_thermo.dat
- Last status: cantera_failed
- Last message: InputError: Error parsing elemental composition for species thermo entry:
 6.32493839E+00 1.76575862E-02-6.17090139E-06 9.77516780E-10-5.77372896E-14    2
-9.00803453E+03-9.89967541E+00 3.89535332E+00 5.25551488E-03 5.18067952E-05    3
-7.09274284E-08 2.87011677E-11-7.47885738E+03 7.07511548E+00-5.75277292E+03    4

Element amounts can have no more than 3 digits.
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\nitromethane\2026\song_2026_nitromethane_114782

## Paper PDF pending: Understanding the moderate-temperature oxidation of 3-ethyltoluene and 3-n-propyltoluene in presence of n-heptane

- DOI: 10.1016/j.combustflame.2026.114776
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026000131
- PDF link from issue page: 
- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\n_heptane_3_ethyltoluene_3_n_propyltoluene\2026\hossain_2026_n_heptane_3_ethyltoluene_3_n_propyltoluene_114776

## Cantera conversion failed: Direct NO removal driven by dielectric barrier discharge: An experimental and kinetic modeling study

- DOI: 10.1016/j.combustflame.2026.114790
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026000271
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\nitric_oxide\zheng_2026_nitric_oxide_114790\extracted\s0010218026000271_mmc3\kinetic.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\nitric_oxide\zheng_2026_nitric_oxide_114790\extracted\s0010218026000271_mmc4\therm.dat
- Last status: cantera_failed
- Last message: ValueError: could not convert string to float: 'E+'; numeric cleanup retry failed: ValueError: could not convert string to float: 'E+'
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\nitric_oxide\2026\zheng_2026_nitric_oxide_114790

## Cantera conversion failed: Cumene pyrolysis: a combined experimental and Ab initio modeling approach

- DOI: 10.1016/j.combustflame.2026.114840
- URL: https://www.sciencedirect.com/science/article/pii/S0010218026000763
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\cumene\roux_2026_cumene_114840\extracted\s0010218026000763_mmc2\SM1_Mechanism_R.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\cumene\roux_2026_cumene_114840\extracted\s0010218026000763_mmc3\SM2_NASA_polynomial_R.dat
- Last status: cantera_failed
- Last message: ValueError: could not convert string to float: '5.00+11'; numeric cleanup retry failed: ValueError: could not convert string to float: 'r-cis-stilbene'
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\cumene\2026\roux_2026_cumene_114840

## Cantera conversion failed: Flame dynamics and kinetic coupling of ammonia and dimethyl-ether in non-premixed cool and warm flames at elevated pressure

- DOI: 10.1016/j.combustflame.2026.114865
- URL: https://www.sciencedirect.com/science/article/pii/S001021802600101X
- Mechanism candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ammonia_dimethyl_ether\xu_2026_ammonia_dimethyl_ether_114865\extracted\s001021802600101x_mmc2\chem.inp
- Thermodynamic candidates: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ammonia_dimethyl_ether\xu_2026_ammonia_dimethyl_ether_114865\extracted\s001021802600101x_mmc3\therm.dat
- Last status: cantera_failed
- Last message: ValueError: could not convert string to float: '0.902,'; numeric cleanup retry failed: ValueError: could not convert string to float: '696.,'
- Target folder: E:\mech_collection\combustion_and_flame_mechanisms\ammonia_dimethyl_ether\2026\xu_2026_ammonia_dimethyl_ether_114865

