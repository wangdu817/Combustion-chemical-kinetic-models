# Chemical kinetics modeling of n-nonane oxidation in oxygen/argon using excited-state species time histories

## Bibliography

Brandon Rotavera, Philippe Dagaut, Eric L. Petersen. Chemical kinetics modeling of n-nonane oxidation in oxygen/argon using excited-state species time histories[J]. Combustion and Flame, 2014, 161: 1146-1163. DOI: 10.1016/j.combustflame.2013.11.008.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 161 / May
- Article number: 1146-1163
- DOI: 10.1016/j.combustflame.2013.11.008
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218013004215
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218013004215_mmc4/chem (HP).inp, _processing/extracted/s0010218013004215_mmc5/chem (LP).inp
- Original thermodynamic source files: _processing/extracted/s0010218013004215_mmc3/therm (v 3.1).dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading entry in chem.inp starting on line 7957: """ c2h3+o2=ch2hco+o 1.450E+15 -0.78 3135.0 ! Updated by Rotavera (4/2011) using rate parameters form "Bloc pression 1 atm" reaction set; initial values were: 10 atm divided by 3 /Bozelli&Dean 1993, J. Phys.Chem,vol.97,pp.4427-4441 """ Section starts with unrecognized keyword 'c2h3+o2=ch2hco+o 1.450E+15 -0.78 3135.0 ' Ignoring redundant declaration for species 'c2h4o' Ignoring redundant declaration for species 'h2' Ignoring redundant declaration for species 'o2' Ignoring redundant declaration for species 'h2o' Ignoring redundant declaration for species 'co' Suppressed 65 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Issue while reading reac ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading entry in chem.inp starting on line 7957: """ c2h3+o2=ch2hco+o 1.450E+15 -0.78 3135.0 ! Updated by Rotavera (4/2011) using rate parameters form "Bloc pression 1 atm" reaction set; initial values were: 10 atm divided by 3 /Bozelli&Dean 1993, J. Phys.Chem,vol.97,pp.4427-4441 """ Section starts with unrecognized keyword 'c2h3+o2=ch2hco+o 1.450E+15 -0.78 3135.0 ' Ignoring redundant declaration for species 'c2h4o' Ignoring redundant declaration for species 'h2' Ignoring redundant declaration for species 'o2' Ignoring redundant declaration for species 'h2o' Ignoring redundant declaration for species 'co' Suppressed 65 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Issue while reading reac ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Chemical reactions of ground-state species strongly govern the formation of excited-state species, including OH* and CH*, which are commonly used to determine ignition delay times of fuels. With well-characterized chemiluminescence rates embedded in chemical kinetics mechanisms, time histories of excited-state species can aid in identifying influential ground-state reactions which are important to processes such as ignition delay time. Placing emphasis on the high-temperature regime, improvements were made to a detailed chemical kinetics mechanism of n-nonane oxidation developed previously by the authors. Using characteristic features of OH* time histories measured in shock-tube experiments as a metric, detailed model analyses were performed over a broad range of conditions: T >1100K, 1.5<P (atm) < 10.5, ϕ =0.5, 1.0, 2.0. OH* time history measurements, particularly under fuel-rich conditions (ϕ =2.0), displayed a two-peak behavior, with the first peak occurring within the first 5–10μs after reflected-shock passage, and the second, wider peak corresponding to main oxidation and ignition. In the initial version of the kinetics mechanism, the two peaks at rich conditions were predicted to merge, blurring the main ignition process prior to the second peak. The work herein presents modifications to the initial chemical kinetics mechanism which led to improved agreement between measurements and model-based predictions, with emphasis on the fuel-rich condition. To this end, the predicted shapes of the OH* time histories were crucial to matching the two-peak behavior detected in the experiments. A first-order resistance–capacitance (RC) model of the experimental time response of the optical setup was developed and shown to reproduce the measured time dependence and peak behavior that are vital for matching the OH* behavior near time-zero. The RC model processes the kinetics predictions in a way that allows the kinetics model predictions to directly correspond to the true conditions in the experiment. In moving towards improved agreement in OH*-profile predictions for all conditions, improvements in the kinetics mechanism were also realized at the two leaner equivalence ratios (ϕ =1.0 and 0.5), both in terms of OH* profile shape and ignition delay times. Model calculations of oxidation processes indicate that reactions leading to the first OH* peak originate from fuel homolysis. The resulting (alkyl) radicals lead to the formation of methyl which then, through a series of H-abstraction reactions, leads to the production of the methylidyne radical (CH) that reacts with molecular oxygen to form OH*. The oxidation processes near time-zero terminate, in part, due to methyl depletion by methylene forming C2H4 +H2. In addition to the insight gained on n-nonane ignition and oxidation chemistry, the present study highlights the utility of correctly interpreted OH* measurements for inference of kinetic information other than ignition delay times.

## Processing Notes

- extracted S0010218013004215_mmc5.zip
- extracted S0010218013004215_mmc3.zip
- extracted S0010218013004215_mmc4.zip
