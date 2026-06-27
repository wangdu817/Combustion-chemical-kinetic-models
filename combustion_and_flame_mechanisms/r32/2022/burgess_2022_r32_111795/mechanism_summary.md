# Burning velocities of R-32/O2/N2 mixtures: Experimental measurements and development of a validated detailed chemical kinetic model

## Bibliography

Donald R. Burgess, Robert R. Burrell, Valeri I. Babushok, Jeffrey A. Manion, Michael J. Hegetschweiler, Gregory T. Linteris. Burning velocities of R-32/O2/N2 mixtures: Experimental measurements and development of a validated detailed chemical kinetic model[J]. Combustion and Flame, 2022, 236: 111795. DOI: 10.1016/j.combustflame.2021.111795.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 236 / 2
- Article number: 111795
- DOI: 10.1016/j.combustflame.2021.111795
- ScienceDirect URL: https://doi.org/10.1016/j.combustflame.2021.111795
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: r32
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S0010218021005381_mmc2.txt
- Original thermodynamic source files: _processing/raw_downloads/S0010218021005381_mmc2.txt, _processing/extracted/s0010218021005381_mmc4/NIST HFC Thermo June 2019.th
- Original transport source files: _processing/extracted/s0010218021005381_mmc5/NIST HFC Transport May 2019.tp

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: IndexError: list index out of range; numeric cleanup retry failed: IndexError: list index out of range
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

This work entails characterizing the flammability of the refrigerant R-32 (CH2F2) by both experimental measurements and modeling. Burning velocities S u were measured using a constant-volume spherical-flame method for R-32/O2/N2 mixtures with O2/N2 ratios ranging from 21% (synthetic air) to 40%, pressures of (1 to 3) bar, and equivalence ratios ϕ of (0.8 to 1.3). Based on a critical assessment of available data, and extended by our own calculations, a detailed chemical kinetic model was developed and key reactions determined using reaction path and sensitivity analyses. Initiation and combustion were identified as distinct kinetic regimes and burning velocities were found to be controlled by two primary reactions: unimolecular decomposition of CH2F2 → CHF + HF and the subsequent reaction, CHF + O2 → CHFO + O, the latter reaction initiating the radical chain propagating and branching by producing O atoms. Sensitive rate constants in the kinetic model were critically adjusted within their uncertainties and current knowledge bounds to best fit the experimental burning velocities. We found that rate constants in the model could be adjusted to match a given experimental S u for specific conditions (O2 loading, P, T, ϕ). This, however, then fixes predicted burning velocities for other all conditions within (3 to 4)% if physically realistic rate parameters are maintained. Thus, the entire set of experimental data is fit, not just to particular conditions. Relative random uncertainties in the experimental S u measurements were (4 to 6)%, but assumptions made for thermal radiation lost by the burned gas in the spherical-flame experiments add an additional systematic uncertainty. Systematic differences between the limiting cases of adiabatic (no thermal radiation lost) and optically-thin (all thermal radiation lost) varied significantly with conditions and ranged from (4 to 30)% at high to low velocities, respectively, translating into uncertainties of (2 to 15)% considering the average of two limiting cases. Comparison of experimental and kinetically modeled S u values suggests that the burned gas tends towards the optically-thin limit at the lowest pressures and fuel loadings and toward the adiabatic limit at the highest pressures and loadings. We tested and found support for this conclusion with a detailed analysis as a function of all the conditions (T, P, % O2, ϕ). This behavior appears to transition from optically-thin to adiabatic as the density of the initial fuel increases, which results in increased CO2 in the burned gas and thus increased absorption of the thermal radiation (consistent with the Beer-Lambert Law). The validated detailed model based on evaluated kinetics is shown to accurately predict burning velocities for R-32 O2/N2 mixtures over a wide range of conditions and provides a reliable basis for extrapolation to other conditions.

## Processing Notes

- extracted S0010218021005381_mmc1.docx
- extracted S0010218021005381_mmc4.zip
- extracted S0010218021005381_mmc5.zip
