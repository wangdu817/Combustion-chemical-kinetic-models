# Low-temperature oxidation chemistry of secondary pentanols: An ozone-assisted study of 2- and 3-pentanol

## Bibliography

Ashenafi Emiru Teka, Qingbo Zhu, Long Zhu, Bin Dong, ... Zhandong Wang. Low-temperature oxidation chemistry of secondary pentanols: An ozone-assisted study of 2- and 3-pentanol[J]. Combustion and Flame, 2026, 291: 115110. DOI: 10.1016/j.combustflame.2026.115110.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 291 / 
- Article number: 115110
- DOI: 10.1016/j.combustflame.2026.115110
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026003469
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: pentanol
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: extracted\s0010218026003469_mmc3\MECH.inp
- Original thermodynamic source files: extracted\s0010218026003469_mmc4\THERM.dat
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
Error on line 12864 of E:\mech_collection\combustion_and_flame_2026_mechanisms\pentanol\ashenafi_emiru_teka_2026_115110_low_temperature_oxidation_chemistry_of_second\mechanism.yaml:

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

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S0010218026003469_mmc3.zip
- extracted S0010218026003469_mmc4.zip
