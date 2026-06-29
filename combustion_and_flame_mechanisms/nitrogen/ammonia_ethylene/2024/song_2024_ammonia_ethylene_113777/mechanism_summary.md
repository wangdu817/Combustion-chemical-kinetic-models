# Experimental and modeling study of the oxidation of NH3/C2H4 mixtures in a shock tube

## Bibliography

Shubao Song, Wanting Jia, Jiachen Sun, Cheng Wang, Jiankun Shao. Experimental and modeling study of the oxidation of NH3/C2H4 mixtures in a shock tube[J]. Combustion and Flame, 2024, 270: 113777. DOI: 10.1016/j.combustflame.2024.113777.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 270 / December
- Article number: 113777
- DOI: 10.1016/j.combustflame.2024.113777
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024004863
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ammonia_ethylene
- Plasma-related mechanism: possible
- Validation reactor/type from abstract: shock tube

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218024004863_mmc2/NH3_C2H4 mech.inp
- Original thermodynamic source files: _processing/extracted/s0010218024004863_mmc2/NH3_C2H4 thermo.dat
- Original transport source files: _processing/extracted/s0010218024004863_mmc2/NH3_C2H4 trans.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'CH2(S)' Ignoring redundant declaration for species 'C' Ignoring redundant declaration for species 'CH3OH' Ignoring redundant declaration for species 'CH2OH' Ignoring redundant declaration for species 'CH3OOH' Suppressed 7 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. No thermo data found for species 'HE' No thermo data found for species 'AR' No thermo data found for species 'N2' No thermo data found for species 'H' No thermo data found for species 'H2' No thermo data found for species 'O' No thermo data found for species 'O2' No thermo data found for species 'OH' No thermo data found for species 'OH*' No thermo data found for species 'H2O' No thermo data fo ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Ammonia is a promising zero-carbon fuel, offering new possibilities for sustainable energy system development. In this study, ignition delay times (IDTs) of NH3/C2H4 mixtures with C2H4 contents of 0 %, 5 %, 10 %, and 25 % were measured using a shock tube at temperatures ranging from 1176 to 1904 K, pressures of 1.0–8.5 atm, and equivalence ratios of 0.5, 1.0 and 2.0. A laser absorption diagnostic system was developed to track the temporal evolution of NH3 concentration during the oxidation process behind the reflected shock waves. The experimental results indicate that the IDTs of the mixtures exhibit non-linear decrease with the addition of ethylene. Specifically, compared to pure ammonia, the addition of 5 %, 10 % and 25 % ethylene significantly increases the reactivity of the mixture, leading to a 36.7 %, 75.9 % and 90.2 % reduction in IDT at a temperature of 1563 K and a pressure of 1.0 atm, respectively. Moreover, the mixture exhibits similar reactivity under fuel-lean and stoichiometric conditions, which remains higher than the reactivity observed under fuel-rich conditions. Overall, the IDTs and the time required for complete consumption of the mixture decreases as temperature, pressure, and ethylene blending ratio increase. In order to simulate and analyze the reaction process of NH3/C2H4 mixtures, a detailed kinetic model was constructed based on previous studies by updating the interaction reaction between C2H4 and NH2 radical and validated against the current experimental results. Rate of production (ROP) and sensitivity analysis were performed to identify the primary consumption pathways of NH3/C2H4 and the significant impact of C2H4 on the reactivity. Additionally, due to the addition of C2H4, a substantial amount of NH2 radical participates in the H-abstraction reaction (C2H4 + NH2 C2H3 + NH3). This results in a reduced involvement of NH2 in the DeNOx process and, consequently, the NH3/C2H4 mixture exhibits a higher tendency to produce NOx compared to pure ammonia. Novelty and significance statement Ammonia offers new possibilities for sustainable energy systems but faces challenges like low combustion rate and mixing with reactive fuels can effectively enhance the ignition characteristics of NH3. The ignition delay times and speciation NH3/C2H4 mixtures are systemically measured by using shock tube and laser absorption spectroscopy. A newly detailed kinetic NH3-C2H4 model is also developed based on previous studies by updating the interaction reaction between C2H4 and NH2 radical and validated against the current experimental results. The rate of production and sensitivity analysis reveal that the interaction reaction (C2H4 + NH2 C2H3 + NH3) have a significant impact on the ignition performance of the binary mixtures. Additionally, the DeNOx process of binary mixtures is suppressed due to the addition of C2H4, resulting a higher tendency to produce NOx. To our best knowledge, this is the first experimental study to systematically measure the ignition delay times and speciation data of NH3/C2H4 mixtures.

## Processing Notes

- extracted S0010218024004863_mmc1.docx
- extracted S0010218024004863_mmc2.zip
