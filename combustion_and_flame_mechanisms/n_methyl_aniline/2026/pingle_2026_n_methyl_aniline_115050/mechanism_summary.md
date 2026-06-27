# Unravelling the combustion kinetics of N-methyl aniline: decomposition and OH-addition pathways from quantum chemistry and flame speed measurements

## Bibliography

Aboli Pingle, Sudarshan Kumar, Neeraj Kumbhakarna. Unravelling the combustion kinetics of N-methyl aniline: decomposition and OH-addition pathways from quantum chemistry and flame speed measurements[J]. Combustion and Flame, 2026, 289: 115050. DOI: 10.1016/j.combustflame.2026.115050.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 289 / July
- Article number: 115050
- DOI: 10.1016/j.combustflame.2026.115050
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026002865
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: n_methyl_aniline
- Plasma-related mechanism: no
- Validation reactor/type from abstract: laminar flame speed

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218026002865_mmc4/Nma_correctedrates_benzene_gas.inp, _processing/extracted/s0010218026002865_mmc4/NMA_decomp_oh_reactions.dat, _processing/extracted/s0010218026002865_mmc4/Updated barrierless reactions_rotor_hindered.txt, _processing/extracted/s0010218026002865_mmc4/mech.dat
- Original thermodynamic source files: _processing/extracted/s0010218026002865_mmc4/therm.dat, _processing/extracted/s0010218026002865_mmc4/Nma_correctedrates_benzene_gas.inp, _processing/extracted/s0010218026002865_mmc4/therm_decomp_oh_reactions.dat
- Original transport source files: _processing/extracted/s0010218026002865_mmc4/Nma_correctedrates_benzene_gas.inp, _processing/extracted/s0010218026002865_mmc4/trans.dat, _processing/extracted/s0010218026002865_mmc4/transport_decomp_oh_reactions.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 102
- Reaction count: 118
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: 102
- Reaction count: 118
- Message: InputError: Error while reading reaction in chem.inp starting on line 7: """ C6H5NHCH3=C6H5NCH3+H 4.4929810E15 0.3 6.4287762E4 """ Unexpected token 'C6H5NHCH3' in reaction expression 'C6H5NHCH3=C6H5NCH3+H'. May be due to undeclared species 'C6H5NHCH3'. Error while reading reaction in chem.inp starting on line 8: """ C6H5NHCH3=C6H4NHCH3+H 1.4747340E15 0.2 6.5159894E4 """ Unexpected token 'C6H5NHCH3' in reaction expression 'C6H5NHCH3=C6H4NHCH3+H'. May be due to undeclared species 'C6H5NHCH3'. Error while reading reaction in chem.inp starting on line 9: """ C6H5NHCH3=C6H4NHCH2+H2 3.017458E19 -1.2 6.477075E4 """ Unexpected token 'C6H5NHCH3' in reaction expression 'C6H5NHCH3=C6H4NHCH2+H2'. May be due to undeclared species 'C6H5NHCH3'. Error while reading reaction in chem.inp starting on line 10 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 3

- Status: ok
- Species count: 548
- Reaction count: 17853
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 4

- Status: ok
- Species count: 548
- Reaction count: 17853
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

N-methyl aniline (NMA) is a promising octane booster that enhances gasoline performance by influencing ignition and flame characteristics. However, its combustion chemistry remains insufficiently understood, owing to the absence of a detailed kinetic mechanism. The present study introduces the first detailed gas-phase reaction mechanism for NMA, focusing on decomposition and OH-initiated oxidation pathways. Bond dissociation energies (CH, NH, and CN) are computed for NMA, along with rate parameters for all elementary reaction pathways. The decomposition kinetics reveal methyl elimination and anilino radical formation as the dominant pathway. Pathways leading to nitrogenated polycyclic aromatic hydrocarbons via ring growth were identified, alongside alternative ring contraction routes forming cyclopentadienyl and other five-membered species. OH-initiated oxidation of RSR species proceeds via ring-opening pathways to form aliphatic nitriles like 4-pentenenitrile. The associated potential energy surfaces reveal lower-energy intermediates and transition states, indicating increased stability due to resonant structures. Subsequent reaction channels form vinylic and smaller nitrile species that significantly affect the PAH chemistry. These pathways were incorporated into a detailed gas-phase reaction mechanism for N-methylaniline (NMA), comprising 72 species and 59 elementary reactions, and were merged with the CRECK base mechanism (2003). The final merged mechanism is validated against laminar burning velocity (LBV) measurements conducted in an externally heated diverging channel at atmospheric pressure, over a temperature range of 400–650 K and equivalence ratios (φ) of 0.9, 1.0, and 1.1. Results indicate strong agreement with experimental data, with errors within 10 %. Laminar burning velocity simulations predict that the temperature-dependent species profiles indicate early formation and sustained stability of these five-membered aromatic RSRs (C₅H₄CN) across a wide temperature range. The proposed mechanism captures key combustion features of NMA, offering new insights into its decomposition, oxidation, and the behavior of nitrogenated intermediates. It also provides critical elementary reactions that can enhance the accuracy of models studying ignition, flame propagation, and emissions in ammonia-assisted and biofuel combustion systems.

## Processing Notes

- extracted S0010218026002865_mmc1.docx
- extracted S0010218026002865_mmc2.docx
- extracted S0010218026002865_mmc4.zip
- extracted S0010218026002865_mmc3.xlsx
