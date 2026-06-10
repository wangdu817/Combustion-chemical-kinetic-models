# Formation of (N-containing) polycyclic aromatic hydrocarbons from pyrrole pyrolysis and its co-pyrolysis with ethylene

## Bibliography

Guangda Luo, Hairong Ren, Mo Yang, Mengqi Wu, ... Feng Zhang. Formation of (N-containing) polycyclic aromatic hydrocarbons from pyrrole pyrolysis and its co-pyrolysis with ethylene[J]. Combustion and Flame, 2026, 290: 115096. DOI: 10.1016/j.combustflame.2026.115096.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 290 / 
- Article number: 115096
- DOI: 10.1016/j.combustflame.2026.115096
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026003329
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ethylene_pyrrole
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: extracted\s0010218026003329_mmc1\mmc1.inp
- Original thermodynamic source files: extracted\s0010218026003329_mmc3\mmc3.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 218
- Reaction count: 3665
- Message: CanteraError: 
*******************************************************************************
CanteraError thrown by addReactions:

*******************************************************************************
InputFileError thrown by PlogRate::validate:
Error on line 2317 of E:\mech_collection\combustion_and_flame_2026_mechanisms\ethylene_pyrrole\guangda_luo_2026_115096_formation_of_n_containing_polycyclic_aromatic\mechanism.yaml:

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

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- extracted S0010218026003329_mmc1.zip
- extracted S0010218026003329_mmc2.docx
- extracted S0010218026003329_mmc3.zip
