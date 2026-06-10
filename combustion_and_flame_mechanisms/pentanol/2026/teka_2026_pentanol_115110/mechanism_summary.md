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
- Validation reactor/type from abstract: jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\pentanol\teka_2026_pentanol_115110\extracted\s0010218026003469_mmc3\MECH.inp
- Original thermodynamic source files: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\pentanol\teka_2026_pentanol_115110\extracted\s0010218026003469_mmc4\THERM.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 627
- Reaction count: 3724
- Message: CanteraError: 
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

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Low-temperature oxidation chemistry plays a key role in controlling ignition and emissions in advanced low-temperature combustion (LTC) engines. While pentanol isomers have attracted increasing attention as promising biofuel candidates, the low-temperature oxidation mechanisms of secondary pentanols remain poorly constrained due to their intrinsically weak reactivity under atmospheric conditions. In this work, ozone-assisted oxidation is employed as a controlled chemical probe to activate low-temperature reaction pathways and elucidate the structure-dependent oxidation chemistry of 2-pentanol and 3-pentanol. Experiments were performed in a jet-stirred reactor at atmospheric pressure over a temperature range of 380–800 K. Synchrotron vacuum ultraviolet photoionization mass spectrometry (SVUV-PIMS) was used to detect a wide range of reaction intermediates and final products. The addition of trace ozone dramatically enhances low-temperature oxidation reactivity. As a result, more than twenty species were identified for each fuel, including ketones, cyclic ethers, acids, and C5 keto-hydroperoxides. Distinct intermediate formation reveals strong structure dependence between 2- and 3-pentanol, particularly in the competition between α-site ketone formation and low-temperature chain-branching pathways. The updated kinetic model based on the Chatterjee model captures most major species distributions. However, it fails to predict the experimentally observed C5H8O2, C5H10O2, and C5H10O3 intermediates, suggesting that RO2-derived chemistry is missing or incompletely described. These results demonstrate that ozone-assisted oxidation provides a powerful framework for exploring low-temperature fuel chemistry and highlights critical gaps in current kinetic descriptions of secondary pentanol oxidation.

## Processing Notes

- extracted S0010218026003469_mmc2.xlsx
- extracted S0010218026003469_mmc3.zip
- extracted S0010218026003469_mmc4.zip
