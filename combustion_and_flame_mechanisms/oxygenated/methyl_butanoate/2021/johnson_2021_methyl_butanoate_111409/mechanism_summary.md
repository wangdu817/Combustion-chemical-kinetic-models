# Oxidation kinetics of methyl crotonate: A comprehensive modeling and experimental study

## Bibliography

Praise Noah Johnson, Marco Lubrano Lavadera, Alexander A. Konnov, Krithika Narayanaswamy. Oxidation kinetics of methyl crotonate: A comprehensive modeling and experimental study[J]. Combustion and Flame, 2021, 229: 111409. DOI: 10.1016/j.combustflame.2021.111409.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 229 / Jul
- Article number: 111409
- DOI: 10.1016/j.combustflame.2021.111409
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S001021802100136X
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: methyl_butanoate
- Plasma-related mechanism: no
- Validation reactor/type from abstract: burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s001021802100136x_mmc2/mmc2.inp
- Original thermodynamic source files: _processing/extracted/s001021802100136x_mmc3/thermo.dat
- Original transport source files: _processing/extracted/s001021802100136x_mmc4/trans.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 346
- Reaction count: 1970
- Message: CanteraError: ******************************************************************************* CanteraError thrown by GasTransportData::validate: invalid geometry for species 'MB3OOHMJ'. 'atom' specified, but species contains multiple atoms. *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

The current study explores the combustion behavior of methyl crotonate (CH 3 CH=CHC(=O)OCH 3 ), which is a short ester representative of large unsaturated methyl esters. Starting with a detailed kinetic model for methyl butanoate (CH 3 CH 2 CH 2 C(=O)OCH 3 ) oxidation, revisions are introduced to the C 0 -C 4 chemistry based on the recent Aramco mechanism 3.0. The resulting mechanism is combined with a short model for methyl crotonate, derived from a suitable reference mechanism. Several new classes of reactions are included and the rate constants of the existing reactions are revised based on various theoretical studies and analogies to reactions of similar species. Furthermore, the low-temperature chemistry of methyl crotonate has been implemented in the current study to extend the validity of the mechanism to lower temperatures. The resulting methyl crotonate combustion mechanism has been comprehensively validated using various experiments in the literature. In addition, experiments are performed using a heat flux burner at atmospheric conditions to measure the laminar burning velocities of methyl crotonate at different unburnt mixture temperatures (318, 338, and 358 K). The mechanism is found to reproduce the experimental data for high-temperature combustion of methyl crotonate satisfactorily. The mechanism is also found to predict the low-temperature ignition delays accurately. Sensitivity and path flux analysis are performed to delineate the importance of the different reaction classes in methyl crotonate chemistry. The current study presents a comprehensive mechanism for methyl crotonate combustion, along with a new set of experimental results complementing the existing experimental database in the literature.

## Processing Notes

- extracted S001021802100136X_mmc4.zip
- extracted S001021802100136X_mmc5.xlsx
- extracted S001021802100136X_mmc2.zip
- extracted S001021802100136X_mmc3.zip
