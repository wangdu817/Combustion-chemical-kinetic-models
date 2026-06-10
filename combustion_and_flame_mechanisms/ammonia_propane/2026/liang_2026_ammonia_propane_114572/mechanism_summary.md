# Experimental and kinetic insight on auto-ignition process of ammonia/propane mixture: Focus on oxygen effect

## Bibliography

Yueying Liang, Zimu Wang, Liang Yu, Xingcai Lu. Experimental and kinetic insight on auto-ignition process of ammonia/propane mixture: Focus on oxygen effect[J]. Combustion and Flame, 2026, 283: 114572. DOI: 10.1016/j.combustflame.2025.114572.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 283 / January
- Article number: 114572
- DOI: 10.1016/j.combustflame.2025.114572
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025006091
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ammonia_propane
- Validation reactor/type from abstract: rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ammonia_propane\liang_2026_ammonia_propane_114572\extracted\s0010218025006091_mmc3\Mech.inp
- Original thermodynamic source files: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\ammonia_propane\liang_2026_ammonia_propane_114572\extracted\s0010218025006091_mmc3\Mech.inp
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 612
- Reaction count: 6668
- Message: CanteraError: 
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

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Propane is a major component of liquefied petroleum gas. Ignition delay times of NH3/C3H8 mixtures were measured in a rapid compression machine over 750–1100 K and 20–100 bar, with propane blending ratios from 10 % to 100 %. A new kinetic model, SJTU-2025, was developed based on POLIMI-2023 and Aramco 3.0 model. The model shows good agreement with IDTs, particularly at high dilution ratios. The model also improves speciation predictions for O2, H2, CO2, C2H2, C3H6, and C3H8. A plateau in simulated mole fractions of O2, NH3, and N2 is observed within 900–1000 K, partially consistent with experimental trends. The NTC trend of oxygen should result from the competition between NC3H7/IC3H7+O2HO2+C3H6 and NC3H7/IC3H7+O2NC3H7O2/IC3H7O2. The effect of propane addition is pronounced at high ammonia proportions, and small propane fraction is suggested because HCN is prone to being produced at high propane content. A new parameter, the O2-IDT ratio, reveals the oxygen effect on IDTs over wide conditions. The reason for the pronounced oxygen effect at low temperature is that oxygen participates actively in the R·→RO2· and C3H7O2=C3H6+HO2 pathways, which are dominant at low temperatures. An important chain-terminating reaction, 2HO2H2O2+O2, gains importance at reduced oxygen concentration, further decreasing the reactivity of the fuel mixtures. The model considers reactions between peroxy radicals C3H7O2 and NH3/NH2, which improve the model predictive ability in IDTs at NTC region and oxygen concentration profile. The source of these kinds of reactions comes from analogy to CH3OCH2O2+NH3/NH2 reactions, and large uncertainty exists in the determination of the rate constants. More accurate kinetic parameters are imperative to improve model performance in the low-temperature region.

## Processing Notes

- extracted S0010218025006091_mmc1.docx
- extracted S0010218025006091_mmc2.xlsx
- extracted S0010218025006091_mmc3.zip
