# A detailed analysis of the key steps of the cyclopentene autoignition mechanism from calculated RRKM rate constants associated with ignition delay time simulations

## Bibliography

João G.S. Monteiro, Arthur C.P.G. Ventura, Eric B. Lindgren, Felipe P. Fleming, ... André G.H. Barbosa. A detailed analysis of the key steps of the cyclopentene autoignition mechanism from calculated RRKM rate constants associated with ignition delay time simulations[J]. Combustion and Flame, 2025, 272: 113862. DOI: 10.1016/j.combustflame.2024.113862.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 272 / February
- Article number: 113862
- DOI: 10.1016/j.combustflame.2024.113862
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024005716
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218024005716/pdfft?md5=b301c85432793c99d238c5d49bd26129&pid=1-s2.0-S0010218024005716-main.pdf
- Fuel type: pentene_cyclopentene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218024005716_mmc1/supp_chemkin.inp
- Original thermodynamic source files: _processing/extracted/s0010218024005716_mmc3/supp_thermo.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading thermo entry in therm.dat starting on line 477: """ CPTOH-2 201810C 5H 9O 1N 0G 298.0 5000.0 1000.00 11 1.124374327E+01 2.9663860E-02-1.15700000E-05 2.07654049E-09-1.40301694E-13 2 -1.317735530E+04-3.5309024E+01-1.16600022E+00 4.74732800E-02 1.10200000E-05 3 -5.061993330E-08 2.4445651E-11-8.94795479E+03 3.27252566E+01 4 """ could not convert string to float: '1 2.9663860e-02' No thermo data found for species 'CPTOH-2' Please check https://cantera.org/stable/userguide/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files for the correct Chemkin syntax.; numeric cleanup retry failed: InputError: Error while reading thermo entry in therm.dat starting on line 477: """ CPTOH-2 201810C 5H 9O 1N 0G 298.0 5000.0 1000.00 11 1.124374327E+01 2.9663860E-02-1.1570000 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Cyclopentene, a prototype for studying the combustion chemistry of cyclic olefins, appears in the oxidation of cyclic hydrocarbons and can provide key information in the understanding of the formation of polycyclic aromatic hydrocarbons. The addition to the double-bond is one of the main steps in low-temperature oxidation mechanisms of unsaturated organic compounds. In the case of cyclopentene, addition of yields a hydroxycyclopentyl radical, that can further react with O2. In this work, we studied the potential energy surface and reaction rates for the subsequent reactions of O2 with the hydroxycyclopentyl radical. The temperature and pressure dependence of the rate constants were determined using master equation simulations, with microcanonical rate coefficients calculated by RRKM theory. The potential energy surface was extracted from high-level electronic structure theory, based on geometries and frequencies obtained using density functional theory. Our results indicate that a Waddington-type mechanism, which produces glutaraldehyde and regenerates , is the dominant reaction pathway. However, at low-temperatures, a secondary pathway leading to the formation of epoxycyclopentanol and becomes equally significant. The thermochemistry of all radicals involved were also evaluated. The kinetic and thermodynamic data were incorporated into a comprehensive mechanism of cyclopentene autoignition, in order to simulate the associated ignition delays. The updated reaction mechanism resulted in shorter ignition delays compared to the non-updated mechanism. Sensitivity analysis was performed to identify the primary contributors. Novelty and Significance Statement Cyclopentene is an important intermediate in the oxidation of cyclic olefins and serves as a precursor in the formation of polycyclic aromatic hydrocarbons. Kinetic modeling studies require detailed information on elementary reactions, much of which is typically unavailable from experiments. The novelty and significance of this study lie in the theoretical calculations of rate constants for key reactions in the oxidation of cyclopentene and their evaluation within the comprehensive mechanism proposed by Lokachari et al. The results demonstrate that the studied reactions significantly influence the ignition delays of cyclopentene at low temperatures. Furthermore, the data presented here can be applied in future studies focusing on the oxidation of cyclic olefins.

## Processing Notes

- extracted S0010218024005716_mmc2.zip
- extracted S0010218024005716_mmc1.zip
- extracted S0010218024005716_mmc3.zip
