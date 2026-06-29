# Experimental and modeling study of the laminar burning velocity of C7C9 aromatic hydrocarbons and C7C8 aromatic oxygenates

## Bibliography

Nicolas Delort, Olivier Herbinet, Roda Bounaceur, Frédérique Battin-Leclerc. Experimental and modeling study of the laminar burning velocity of C7C9 aromatic hydrocarbons and C7C8 aromatic oxygenates[J]. Combustion and Flame, 2025, 273: 113915. DOI: 10.1016/j.combustflame.2024.113915.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 273 / March
- Article number: 113915
- DOI: 10.1016/j.combustflame.2024.113915
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024006242
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218024006242/pdfft?md5=11063a2cbd2dcd68bd2f360c464ac151&pid=1-s2.0-S0010218024006242-main.pdf
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: laminar flame speed, burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218024006242_mmc3/COLIBRv4_Mech.inp
- Original thermodynamic source files: _processing/extracted/s0010218024006242_mmc3/COLIBRIv4_thermo.dat
- Original transport source files: _processing/extracted/s0010218024006242_mmc3/COLIBRIv4_tran_.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'C9H7CH3' Ignoring redundant declaration for species 'O-CH3A1CH2O' Error while reading reaction in chem.inp starting on line 8078: """ CH3C6H3CH3+O2=>O2CH3A1CH3 1.950E+11 0.420 -631.1 !WAGNON1@LLNL.GOV! AS P-C6H4CH3+O2=>P-O2C6H4CH3 DA SILVA JPCA 117 (2007) 8663-8676 PLOG/ 1.00E-01 6.51+107 -32.05 12220 / PLOG/ 1.00E+00 3.21+132 -38.08 33960 / PLOG/ 1.00E+01 2.35+160 -45.03 60240 / PLOG/ 1.00E+02 6.57+179 -49.68 81660 / """ could not convert string to float: '6.51+107' Error while reading thermo entry in therm.dat starting on line 1221: """ C9H8CH3 C 10H 11 G 300.000 5000.000 5000.00 1 5.89344512E+01 0.00000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00 2 -2.21709548E+04-3.29232464E+02 1.57041459E+00 6.95644403E-02-3.28229474E-05 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

The combustion of lignin-derived biofuels was investigated through the study of the laminar burning velocity (LBV) of arenes and oxygenated aromatic as typical surrogate compounds. For this purpose, the laminar burning velocity of ten aromatic hydrocarbons, in which the benzene ring is connected to at least a C-atom, toluene, styrene, the three xylene isomers, two of the trimethylbenzene isomers, and of three oxygenated aromatics, benzaldehyde, benzylalcohol, 2-phenylethanol, was measured using a flat flame burner coupled to the heat flux method under atmospheric pressure. Experiments were performed for three fresh gas temperatures, 298 K (ambient temperature), 358 K and 398 K, as far as the volatility of the investigated compounds allows it. The obtained results confirm the reliability of the flat flame burner, which has been rarely used to measure the LBV of such compounds. The dataset extends the covered conditions of available experimental results and constitutes the first flame experiments for benzaldehyde, benzylalcohol, and 2-phenylethanol. A detailed kinetic model was also developed as part of this work. It gathers all the compounds of interest and is validated against the obtained LBVs and all available experimental literature data for these fuels. Analyses of the combustion process were performed and allowed to explain the observed tendencies of LBV values. The key role of benzyl-like radicals, which are resonance stabilized, is highlighted, as well as that of C5 oxygenated species.

## Processing Notes

- extracted S0010218024006242_mmc2.xlsx
- extracted S0010218024006242_mmc3.zip
