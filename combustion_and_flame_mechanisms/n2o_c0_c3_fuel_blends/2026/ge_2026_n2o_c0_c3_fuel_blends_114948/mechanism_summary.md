# Combustion reaction mechanism of C0-C3/N2O flames: Experimental and kinetic modeling study of laminar burning velocity

## Bibliography

Yun Ge, Hong-Hao Ma, Yue Jiao, Shuo Yang, ... Lu-Qing Wang. Combustion reaction mechanism of C0-C3/N2O flames: Experimental and kinetic modeling study of laminar burning velocity[J]. Combustion and Flame, 2026, 288: 114948. DOI: 10.1016/j.combustflame.2026.114948.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 288 / June
- Article number: 114948
- DOI: 10.1016/j.combustflame.2026.114948
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026001847
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: n2o_c0_c3_fuel_blends
- Plasma-related mechanism: no
- Validation reactor/type from abstract: laminar flame speed, burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing\extracted\s0010218026001847_mmc2\Chem.txt
- Original thermodynamic source files: _processing\extracted\s0010218026001847_mmc3\Thermo.txt
- Original transport source files: _processing\extracted\s0010218026001847_mmc4\Trans.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 96
- Reaction count: 626
- Message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 3196 and 3382 of E:\mech_collection\combustion_and_flame_mechanisms\n2o_c0_c3_fuel_blends\2026\ge_2026_n2o_c0_c3_fuel_blends_114948\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 448: NNH + M <=> H + N2 + M
Reaction 400: NNH + O2 <=> H + N2 + O2

|  Line |
|  3191 |   note: GRI Mech 3.0
|  3192 | - equation: NH2 + H <=> NH + H2  # Reaction 399
|  3193 |   duplicate: true
|  3194 |   rate-constant: {A: 4.0e+13, b: 0.0, Ea: 3650.0}
|  3195 |   note: GRI Mech 3.0
>  3196 > - equation: NNH + M <=> N2 + H + M  # Reaction 400
            ^
|  3197 |   type: three-body
|  3198 |   rate-constant: {A: 1.3e+14, b: -0.11, Ea: 4980.0}
|  3199 |   efficiencies: {H2: 2.0, H2O: 6.0, CH4: 2.0, CO: 1.5, CO2: 2.0, C2H6: 3.0,
...
|  3377 |   note: J.W. Bozzelli, et al., International journal of chemical kinetics
|  3378 |     27 (1995) 1097-1109
|  3379 | - equation: NNH + O2 <=> N2 + HO2  # Reaction 447
|  3380 |   rate-constant: {A: 5.6e+14, b: -0.385, Ea: -13.0}
|  3381 |   note: S.J. Klippenstein, et al., Combustion and Flame 158 (2011) 774-789
>  3382 > - equation: NNH + O2 <=> N2 + H + O2  # Reaction 448
            ^
|  3383 |   rate-constant: {A: 5.0e+13, b: 0.0, Ea: 0.0}
|  3384 |   note: P. Glarborg, et al., Combustion and Flame 115 (1998) 1-27.
|  3385 | - equation: NNH + NO <=> N2 + HNO  # Reaction 449
*******************************************************************************

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Due to the special property of N2O decomposition with heat release, the fundamental flame structures and combustion characteristics of fuel/N2O flames are expected to be distinct from fuel/O2 and fuel/air flames. This study reports an experimental and kinetic modelling study of laminar burning velocities of C3H8/H2/N2O/Ar flames. Experiments were conducted using the spherical flame method under various equivalence ratios and H2 fractions at 1 atm and 298 K. Several relevant mechanisms from the literature were tested; none of them could accurately predict the laminar burning velocities for all the tested conditions. A new mechanism with 96 species and 626 elementary reactions for C0-C3/N2O flames was proposed and validated, where the mechanism update focused on the rate constants of dominant elementary reactions derived from sensitivity analyses based on the deviation between simulated and experimental results. The new model performed well in predicting the combustion parameters of C0-C3/N2O relevant flames (such as laminar burning velocities, ignition delay times, and species mole fraction profiles), and the performance was superior to the literature mechanisms. Kinetic analyses were performed using the present model to elucidate the main reaction paths and the dominant elementary reactions for C3H8/H2/N2O/Ar flames and C0-C3/N2O flames. Results show that the kinetics of N2O, as well as N chemistry, play a crucial role during the combustion process for C0-C3/N2O flames. The present model can be regarded as a significant advancement in combustion kinetics of fuel/N2O flames, as well as a foundation for developing kinetic mechanisms of heavy fuel/N2O flames.

## Processing Notes

- none
