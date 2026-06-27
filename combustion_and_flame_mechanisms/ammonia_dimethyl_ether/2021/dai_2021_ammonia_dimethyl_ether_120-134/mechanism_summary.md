# Ignition delay times of NH3 /DME blends at high pressure and low DME fraction: RCM experiments and simulations

## Bibliography

Liming Dai, Hamid Hashemi, Peter Glarborg, Sander Gersen, Paul Marshall, Anatoli Mokhov, et al.. Ignition delay times of NH3 /DME blends at high pressure and low DME fraction: RCM experiments and simulations[J]. Combustion and Flame, 2021, 227: 120-134. DOI: 10.1016/j.combustflame.2020.12.048.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 227 / May
- Article number: 120-134
- DOI: 10.1016/j.combustflame.2020.12.048
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218020306039
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ammonia_dimethyl_ether
- Plasma-related mechanism: no
- Validation reactor/type from abstract: rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218020306039_mmc3/chem file NH3_DME mechanism.inp
- Original thermodynamic source files: _processing/extracted/s0010218020306039_mmc2/therm file NH3_DME mechanism.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'CO' Ignoring redundant declaration for species 'CO2' Ignoring redundant declaration for species 'CH2CHOOH' Ignoring redundant declaration for species 'CH3CH2OO' Ignoring redundant declaration for species 'CH3CHOOH' Suppressed 5 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. No thermo data found for species 'H2' No thermo data found for species 'O2' No thermo data found for species 'O3' No thermo data found for species 'H' No thermo data found for species 'O' No thermo data found for species 'OH' No thermo data found for species 'HO2' No thermo data found for species 'H2O' No thermo data found for species 'H2O2' No thermo data found for species 'CO' No thermo ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Autoignition delay times of ammonia/dimethyl ether (NH3/DME) mixtures were measured in a rapid compression machine with DME fractions of 0, 2 and 5 and 100% in the fuel. The measurements were performed at equivalence ratios φ =0.5, 1.0 and 2.0 and pressures in the range 10–70 bar; depending on the fuel composition, the temperatures after compression varied from 610 K to 1180 K. Admixture of DME is seen to have a dramatic effect on the ignition delay time, effectively shifting the curves of ignition delay vs. temperature to lower temperatures, up to ~250 K compared to pure ammonia. Two-stage ignition is observed at φ =1.0 and 2.0 with 2% and 5% DME in the fuel, despite the pressure being higher than that at which pure DME shows two-stage ignition. At φ =0.5, a reproducible pre-ignition pressure rise is observed for both DME fractions, which is not observed in the pure fuel components. A novel NH3/DME mechanism was developed, including modifications in the NH3 subset and addition of the NH2+CH3OCH3 reaction, with rate coefficients calculated from ab initio theory. Simulations faithfully reproduce the observed pre-ignition pressure rise. While the mechanism also exhibits two-stage ignition for NH3/DME mixtures, both qualitative and quantitative improvement is recommended. The overall ignition delay times for ammonia/DME mixtures are predicted well, generally being within 50% of the experimental values, although reduced performance is observed for pure ammonia at φ =2.0. Simulating the ignition process, we observe that the DME is oxidized much more rapidly than ammonia. Analysis of the mechanism indicates that this ‘early DME oxidation’ generates reactive species that initiate the oxidation of ammonia, which in turn begins heat release that raises the temperature and accelerates the oxidation process towards ignition. The reaction path analysis shows that the low-temperature chain-branching reactions of DME are important in the early oxidation of the fuel, while the sensitivity analysis indicates that several reactions in the oxidation of DME, including cross reactions between DME and NH3 species presented here, are critical to ignition, even at fractions of 2% DME in the fuel.

## Processing Notes

- extracted S0010218020306039_mmc2.zip
- extracted S0010218020306039_mmc1.xlsx
- extracted S0010218020306039_mmc3.zip
