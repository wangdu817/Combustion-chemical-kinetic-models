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
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: extracted\s0010218025006091_mmc3\Mech.inp
- Original thermodynamic source files: extracted\s0010218025006091_mmc3\Mech.inp
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: CanteraError: 
*******************************************************************************
CanteraError thrown by addReactions:

*******************************************************************************
InputFileError thrown by PlogRate::validate:
Error on line 17297 of E:\mech_collection\combustion_and_flame_2026_mechanisms\ammonia_propane\yueying_liang_2026_114572_experimental_and_kinetic_insight_on_auto_igni\mechanism.yaml:

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
Error on line 31740 of E:\mech_collection\combustion_and_flame_2026_mechanisms\ammonia_propane\yueying_liang_2026_114572_experimental_and_kinetic_insight_on_auto_igni\mechanism.yaml:

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

not available

## Processing Notes

- extracted S0010218025006091_mmc1.docx
- extracted S0010218025006091_mmc3.zip
