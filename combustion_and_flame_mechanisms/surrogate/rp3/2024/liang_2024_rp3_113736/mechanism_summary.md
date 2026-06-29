# Experimental and kinetic modeling study of RP-3 kerosene: Development of a four-component surrogate for enhanced prediction of aromatic intermediates

## Bibliography

Yilun Liang, Mo Yang, Chi Zhang, Juan Wang. Experimental and kinetic modeling study of RP-3 kerosene: Development of a four-component surrogate for enhanced prediction of aromatic intermediates[J]. Combustion and Flame, 2024, 270: 113736. DOI: 10.1016/j.combustflame.2024.113736.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 270 / December
- Article number: 113736
- DOI: 10.1016/j.combustflame.2024.113736
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024004450
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: rp3
- Plasma-related mechanism: no
- Validation reactor/type from abstract: flow reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218024004450_mmc3/Mechanism
- Original thermodynamic source files: _processing/extracted/s0010218024004450_mmc4/Thermal.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading entry in chem.inp starting on line 31443: """ DUP """ Section starts with unrecognized keyword 'DUP' Error while reading reaction in chem.inp starting on line 21790: """ O2+TETRARB=>RTETRAOO .1500E+13 .000 .0 """ Unexpected token 'RTETRAO' in reaction expression 'O2+TETRARB=>RTETRAOO'. May be due to undeclared species 'RTETRAO'. Error while reading reaction in chem.inp starting on line 21791: """ RTETRAOO=>O2+TETRARB .1000E+14 .000 32000.0 """ Unexpected token 'RTETRAO' in reaction expression 'RTETRAOO=>O2+TETRARB'. May be due to undeclared species 'RTETRAO'. Error while reading reaction in chem.inp starting on line 21792: """ RTETRAOO=>HO2+C10H10 .1000E+12 .000 21000.0 """ Unexpected token 'RTETRAO' in reaction expression 'RTETRAOO=>HO2+C10H10'. May be due ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

RP-3 kerosene is currently the primary jet fuel used in China. However, limited attention has been paid to development of surrogate models that can predict formations of aromatics during RP-3 oxidation in a detailed way, such as by species mole fraction profiles. The present study aims to enrich the experimental database by measuring species mole fraction profiles, particularly focusing on aromatic intermediates, and propose a new surrogate model with a detailed kinetic model to enhance predictive accuracy for these intermediates. Oxidation experiments of real RP-3 kerosene were conducted using an atmospheric flow reactor at temperatures ranging from 800 to 1150 K and equivalence ratios of 0.5 and 2.0. The mole fraction profiles of species including oxygen, major products, important small molecular intermediates and several primary aromatic intermediates were measured using online gas chromatography (GC) and gas chromatography-mass spectrometry (GC–MS). Based on the chemical composition and fundamental physical properties of RP-3 kerosene, a surrogate consisting of 55.0 % n-undecane, 18.7 % trans-decalin, 19.8 % p-xylene and 6.5 % tetralin (by weight) was formulated. A detailed kinetic model of the surrogate was developed and validated against the measured data. Compared to the surrogate models proposed in the previous studies, the current model demonstrates superior predictive capabilities in forecasting the generation of major aromatic intermediates. According to the rate of production (ROP) analysis for the model, benzene generation is associated with three components: decalin, p-xylene and n-undecane. Decalin exhibits the highest contribution to benzene formation under both lean and rich conditions. Toluene predominantly originates from p-xylene, while indene and naphthalene are primarily produced by tetralin. These findings emphasize the significance of decalin as a representative bicyclic cycloalkane component and tetralin as a representative indane/tetralin component in establishing a surrogate for RP-3 fuel to enhance prediction of aromatic intermediates. Furthermore, validation through experimental data from the literature including species mole fraction profiles and ignition delay times confirms the broad applicability of this model.

## Processing Notes

- extracted S0010218024004450_mmc4.zip
- extracted S0010218024004450_mmc3.zip
- extracted S0010218024004450_mmc1.docx
- extracted S0010218024004450_mmc2.xlsx
