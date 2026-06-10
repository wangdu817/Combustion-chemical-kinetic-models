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
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: extracted\s0010218025007783_mmc1\EHN.inp
- Original thermodynamic source files: extracted\s0010218025007783_mmc1\EHN.dat
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
Error on line 43696 of E:\mech_collection\combustion_and_flame_2026_mechanisms\2_ethylhexyl_nitrate\jiaxin_xie_2026_114743_an_experimental_and_kinetic_modeling_study_of\mechanism.yaml:

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

not available

## Processing Notes

- extracted S0010218025007783_mmc1.zip
