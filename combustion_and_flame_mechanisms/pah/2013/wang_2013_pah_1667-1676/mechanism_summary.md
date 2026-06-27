# A PAH growth mechanism and synergistic effect on PAH formation in counterflow diffusion flames

## Bibliography

Yu Wang, Abhijeet Raj, Suk Ho Chung. A PAH growth mechanism and synergistic effect on PAH formation in counterflow diffusion flames[J]. Combustion and Flame, 2013, 160: 1667-1676. DOI: 10.1016/j.combustflame.2013.03.013.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 160 / Sep
- Article number: 1667-1676
- DOI: 10.1016/j.combustflame.2013.03.013
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218013001016
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: pah
- Plasma-related mechanism: no
- Validation reactor/type from abstract: burner/flame structure, counterflow flame

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218013001016_mmc2/chem_sub.inp
- Original thermodynamic source files: _processing/extracted/s0010218013001016_mmc3/therm_sub.dat
- Original transport source files: _processing/extracted/s0010218013001016_mmc4/tran_sub.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading entry in chem.inp starting on line 3178: """ References and Notes: """ Section starts with unrecognized keyword ' References and Notes:' Error while reading reaction in chem.inp starting on line 1640: """ A1- (+M) = c-C6H4 + H (+M) 4.300E+12 0.616 77313. ! RRKM 00-HAI-FRE LOW/ 1.000E+84 -18.866 90064 / TROE/ 0.902, 696., 358., 3856. / H2/2.0/ H2O/6.0/ CH4/2.0/ CO/1.5/ CO2/2.0/ """ could not convert string to float: '0.902,' Error while reading reaction in chem.inp starting on line 2807: """ C7H6+C2H2=C9H8 1.44+292 -78.2 245010.0 !2009 da Silva & Bozzelli (C7H6+C2H2) """ could not convert string to float: '1.44+292' No thermo data found for species 'AR' No thermo data found for species 'N2' No thermo data found for species 'H' No thermo data found for species ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

A reaction mechanism having molecular growth up to benzene for hydrocarbon fuels with up to four carbon-atoms was extended to include the formation and growth of polycyclic aromatic hydrocarbons (PAHs) up to coronene (C24H12). The new mechanism was tested for ethylene premixed flames at low (20torr) and atmospheric pressures by comparing experimentally observed species concentrations with those of the computed ones for small chemical species and PAHs. As compared to several existing mechanisms in the literature, the newly developed mechanism showed an appreciable improvement in the predicted profiles of PAHs. The new mechanism was also used to simulate PAH formation in counterflow diffusion flames of ethylene to study the effects of mixing propane and benzene in the fuel stream. In the ethylene–propane flames, existing experimental results showed a synergistic effect in PAH concentrations, i.e. PAH concentrations first increased and then decreased with increasing propane mixing. This PAH behavior was successfully captured by the new mechanism. The synergistic effect was predicted to be more pronounced for larger PAH molecules as compared to the smaller ones, which is in agreement with experimental observations. In the experimental study in which the fuel stream of ethylene–propane flames was doped with benzene, a synergistic effect was mitigated for benzene, but was observed for large PAHs. This effect was also predicted in the computed PAH profiles for these flames. To explain these responses of PAHs in the flames of mixture fuels, a pathway analysis has been conducted, which show that several resonantly stabilized species as well as C4H4 and H atom contribute to the enhanced synergistic behaviors of larger PAHs as compared to the small ones in the flames of mixture fuels.

## Processing Notes

- extracted S0010218013001016_mmc3.zip
- extracted S0010218013001016_mmc2.zip
- extracted S0010218013001016_mmc1.docx
- extracted S0010218013001016_mmc4.zip
