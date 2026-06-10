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

Pyrolysis is a practical route for biomass conversion, and its co-pyrolysis with organic solid waste (OSW) can further enhance bio-oil quality. Both processes generate polycyclic aromatic hydrocarbons (PAHs), and nitrogen-containing PAHs (NPAHs) for nitrogenous feedstocks, posing environmental and health risks. In this work, pyrrole serves as a model nitrogenous biomass compound to probe (N)PAH formation during neat pyrolysis and co-pyrolysis with ethylene, a surrogate for the hydrogen-rich OSW environment. Species detection was performed using time-of-flight mass spectrometry (ToF-MS) and atmospheric pressure photoionization high-resolution mass spectrometry (APPI-HRMS), each coupled to a flow reactor. ToF-MS results reveal the formation of (N)PAHs with up to five rings, where single-nitrogen NPAHs representing the dominant NPAHs. Ethylene blending introduces no new m/z signals but enhances the formation of larger (N)PAHs, particularly above 1100 K. Furthermore, APPI-HRMS indicates that under experimental conditions, the growth rate of aromatic carbon rings is faster than that of nitrogen-containing heterocyclic aromatic hydrocarbons. To provide mechanistic interpretation of these observations, the formation pathways and rate constants of the bicyclic 2-quinolinyl radical (C9H6N) from pyrrole pyrolysis products were investigated theoretically. The results validate a novel nitrogen ring expansion mechanism involving the addition of cyanoacetylene (C3HN) to phenyl radicals. Kinetic analysis demonstrates that this N-expansion pathway outperforms the HAVA carbon-ring growth mechanism of C6H5 + C4H4 in terms of both species concentration and rate constants. Moreover, an alternative N-expansion between benzonitrile and C2H2 (also leading to C9H6N) exhibits even higher rate constants, further refining the growth network of nitrogenous aromatics. This combined experimental and theoretical study provides new mechanistic insight into (N)PAH formation, offering valuable guidance for mitigating hazardous emissions mitigation in biomass (co-)pyrolysis.

## Processing Notes

- extracted S0010218026003329_mmc1.zip
- extracted S0010218026003329_mmc2.docx
- extracted S0010218026003329_mmc3.zip
