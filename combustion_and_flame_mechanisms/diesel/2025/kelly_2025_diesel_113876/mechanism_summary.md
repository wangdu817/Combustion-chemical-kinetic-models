# Machine learned compact kinetic model for liquid fuel combustion

## Bibliography

Mark Kelly, G. Bourque, M. Hase, S. Dooley. Machine learned compact kinetic model for liquid fuel combustion[J]. Combustion and Flame, 2025, 272: 113876. DOI: 10.1016/j.combustflame.2024.113876.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 272 / February
- Article number: 113876
- DOI: 10.1016/j.combustflame.2024.113876
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024005856
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218024005856/pdfft?md5=38fca8642259e047b95fcd7bdcd4a436&pid=1-s2.0-S0010218024005856-main.pdf
- Fuel type: diesel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218024005856_mmc1/SupplementalMaterial/TCD_32s.cti, _processing/extracted/s0010218024005856_mmc1/SupplementalMaterial/TCD_32s.yaml
- Original thermodynamic source files: _processing/extracted/s0010218024005856_mmc1/SupplementalMaterial/TCD_32s.cti, _processing/extracted/s0010218024005856_mmc1/SupplementalMaterial/TCD_32s.yaml
- Original transport source files: _processing/extracted/s0010218024005856_mmc1/SupplementalMaterial/TCD_32s.cti, _processing/extracted/s0010218024005856_mmc1/SupplementalMaterial/TCD_32s.yaml

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 33
- Reaction count: 153
- Message: CanteraError: ******************************************************************************* CanteraError thrown by newSolution: The CTI and XML formats are no longer supported. *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: 33
- Reaction count: 153
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by Reaction::checkBalance: Error on line 575 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/diesel/2025/kelly_2025_diesel_113876/mechanism.yaml: The following reaction is unbalanced: nFuel => 2 C3H5 + 0.333 C3H6 Element Reactants Products C 7 6.9990000000000006 H 12 11.998000000000001 | Line | | 570 | type: pressure-dependent-Arrhenius | 571 | rate-constants: | 572 | - {P: 0.9999999 atm, A: 1.29e+15, b: -0.065781, Ea: 3634.963} | 573 | - {P: 5.0000001 atm, A: 1.29e+15, b: -0.065781, Ea: 3634.963} | 574 | - {P: 9.9999999 atm, ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

A novel data-intensive methodology to produce a high fidelity, extremely-reduced “compact” kinetic model for a high boiling point complex liquid fuel is proposed and demonstrated. A five-component surrogate definition for the liquid fuel is developed that displays a high accuracy to the experimentally-derived combustion property targets. The calculations of the Lawrence Livermore National Lab diesel surrogate model containing 6476 species are used to serve as gas turbine industry-defined performance targets for this surrogate. Acknowledging that the retention of a multi-component surrogate definition is a limitation on the size of the model, the surrogate fuel is consolidated into a single virtual molecule. Subsequently, the reaction mechanism is simplified by replacing high carbon number chemistry with a virtual scheme. This scheme links the virtual fuel molecule to low carbon number chemistry using four virtual species and forty-four virtual reactions, resulting in a reduction to 429 species in the model. The Machine Learned Optimisation of Chemical Kinetics (MLOCK) algorithm is adapted to “compact” this model. Compaction is the over-reduction and optimisation of a kinetic model. Path flux analysis generates an overly-reduced model with 31 species that has a poor replication of the detailed model calculations. To address this, virtual reaction rate constants of important virtual reactions are numerically optimized to detailed model high temperature calculations. MLOCK systematically perturbs all three virtual Arrhenius reaction rate constant parameters to generate and evaluate numerous model candidates, refining the search space based on prior results, finding better models. A low temperature virtual reaction network, comprising one new virtual species and three new virtual reactions, is appended to the high temperature compact model. MLOCK is employed to reoptimize the model to calculations at low and intermediate temperatures. The application of this methodology results in a 32-species compact model in ChemKin/Cantera format, which retains fidelities in the range of 76 to 92 % across a comprehensive range of gas-turbine relevant performance calculations for low, intermediate and high temperatures.

## Processing Notes

- extracted S0010218024005856_mmc1.zip
