# Chemical flux analysis of low-temperature plasma-enhanced oxidation of methane and hydrogen in argon

## Bibliography

T. Hazenberg, J. van Dijk, J.A. van Oijen. Chemical flux analysis of low-temperature plasma-enhanced oxidation of methane and hydrogen in argon[J]. Combustion and Flame, 2023, 257: 113037. DOI: 10.1016/j.combustflame.2023.113037.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 257 / November
- Article number: 113037
- DOI: 10.1016/j.combustflame.2023.113037
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023004121
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: methane_hydrogen
- Plasma-related mechanism: yes
- Validation reactor/type from abstract: flow reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: not available
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218023004121_mmc3/mmc3.chem
- Original thermodynamic source files: not found
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 352: """ E+O2=>O2+E 0.000E+00 0.000E+00 0.0 BOLSIG/ O2 O2_elastic.dat / """ could not convert string to float: 'O2 O2_elastic.dat' Error while reading reaction in chem.inp starting on line 354: """ E+O2=>O2(a1)+E 1.000E+00 0.000E+00 0.0 BOLSIG/ O2 O2->O2(a1).dat / """ could not convert string to float: 'O2 O2->O2(a1).dat' Error while reading reaction in chem.inp starting on line 356: """ E+O2=>O2(b1)+E 1.000E+00 0.000E+00 0.0 BOLSIG/ O2 O2->O2(b1).dat / """ could not convert string to float: 'O2 O2->O2(b1).dat' Error while reading reaction in chem.inp starting on line 358: """ E+O2=>O2(A3)+E 1.000E+00 0.000E+00 0.0 BOLSIG/ O2 O2->O2(A3).dat / """ could not convert string to float: 'O2 O2->O2(A3).dat' Error while reading ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: not available
- Standard tran.dat: not available

## Abstract

Plasma can be used to enhance the reactivity of combustible mixtures at low temperatures. In this article, the chemical pathways predicted by three different reaction mechanisms are investigated for the low-temperature oxidation of hydrogen and methane. To validate our model and the reaction mechanisms, the numerical results are compared against experimental results in a diluted flow reactor. Our model with all three reaction mechanisms predicts trends similar to those observed in the experiments. Moreover, all predicted quantities show reasonable quantitative agreement with the experiments. Flux analysis is used to identify the main pathways of oxidation at different temperatures. Three different modes, each active in a different temperature range, are identified in the oxidation of hydrogen. When the temperature is increased, these modes become increasingly self-sustained. Similarly, three different pathways are identified in the oxidation of methane. Below 1000K, methane quickly removes hydroxyl radicals from the radical pool, inhibiting self-sustained oxidation. From our analysis, we conclude that plasma provides activation of the low-temperature chemistry by the generation of radicals.

## Processing Notes

- extracted S0010218023004121_mmc1.zip
- extracted S0010218023004121_mmc3.zip
- extracted S0010218023004121_mmc2.zip
