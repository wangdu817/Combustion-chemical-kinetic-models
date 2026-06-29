# Kinetic modeling of particle size distribution of soot in a premixed burner-stabilized stagnation ethylene flame

## Bibliography

Chiara Saggese, Sara Ferrario, Joaquin Camacho, Alberto Cuoci, Alessio Frassoldati, Eliseo Ranzi, et al.. Kinetic modeling of particle size distribution of soot in a premixed burner-stabilized stagnation ethylene flame[J]. Combustion and Flame, 2015, 162: 3356-3369. DOI: 10.1016/j.combustflame.2015.06.002.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 162 / Sep
- Article number: 3356-3369
- DOI: 10.1016/j.combustflame.2015.06.002
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218015001807
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ethylene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218015001807_mmc1/Supplemental material/soot.CKI
- Original thermodynamic source files: _processing/extracted/s0010218015001807_mmc1/Supplemental material/soot.CKT
- Original transport source files: _processing/extracted/s0010218015001807_mmc1/Supplemental material/soot.TRC

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading thermo entry in therm.dat starting on line 939: """ BIN7C C 0H 0 G 300.00 5000.00 1000.00 1C 1250H 125 -.455580000E+03 .778183200E+01-.512707600E-02 .185581300E-05-.195017600E-09 2 .958214800E+06 .202948500E+04-.455580000E+03 .778183200E+01-.512707600E-02 3 .185581300E-05-.195017600E-09 .958214800E+06 .202948500E+04 4 """ Error parsing elemental composition for species thermo entry. Element amounts can have no more than 3 digits. Error while reading thermo entry in therm.dat starting on line 943: """ BIN7B C 0H 0 G 300.00 5000.00 1000.00 1C 1250H 375 -.405995200E+03 .837317600E+01-.531580300E-02 .179290400E-05-.207599400E-09 2 .134726000E+07 .237249600E+04-.405995200E+03 .837317600E+01-.531580300E-02 3 .179290400E-05-.207599400E-09 .134726000E+07 .237249600E ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

A detailed model of soot formation is proposed, which consists of a gas-phase kinetic model for the pyrolysis and oxidation of selected hydrocarbon fuels and a kinetic mechanism of soot nucleation and mass/size growth through coagulation and surface reactions. The gas-phase model (Ranzi et al., 2012) was expanded to include the chemistry of Polycyclic Aromatic Hydrocarbons (PAHs) up to four-to-five ring PAHs, with a modular and hierarchical approach. The discrete sectional method was employed to solve the size evolution of the particle size distribution function (PSDF). Analogy and similarity rules were employed to describe heterogeneous reaction kinetics of soot surface reactions. A variable collision efficiency was assumed for the coalescence of small soot particles. Larger particles were assumed to undergo aggregation. The predicted PSDFs are found to be in reasonably good agreement with the experimental data for nascent soot measured in an atmospheric-pressure premixed ethylene–oxygen–argon flame in the burner-stabilized stagnation flame configuration. Sensitivity analyses of the PSDF, number density, and volume fraction were carried out with respect to the rate parameters of addition reactions of acetylene, PAHs, resonantly stabilized radical reactions, and coalescence and aggregation. The results show that the reaction of PAHs and acetylene with soot surfaces and the kinetics of coalescence and aggregation exhibit dominant effects on the detailed and global soot properties for the flame studied, in agreement with conclusions of a large range of previous modeling studies.

## Processing Notes

- extracted S0010218015001807_mmc1.zip
