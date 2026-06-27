# Current status of the high-temperature kinetic models of silane: Part I. Pyrolysis

## Bibliography

Karl P. Chatelain, Yizhuo He, Reham Alharbi, Rémy Mével, Eric L. Petersen, Deanna A. Lacoste. Current status of the high-temperature kinetic models of silane: Part I. Pyrolysis[J]. Combustion and Flame, 2021, 227: 526-537. DOI: 10.1016/j.combustflame.2020.11.030.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 227 / May
- Article number: 526-537
- DOI: 10.1016/j.combustflame.2020.11.030
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218020305320
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: yes
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218020305320_mmc1/Kondo_chem.inp, _processing/extracted/s0010218020305320_mmc1/Miller_chem.inp, _processing/extracted/s0010218020305320_mmc1/Slakman_chem.inp, _processing/extracted/s0010218020305320_mmc1/Chatelain_Chem.inp, _processing/extracted/s0010218020305320_mmc1/PeOx_chem.inp, _processing/extracted/s0010218020305320_mmc1/Mevel_chem.inp, _processing/extracted/s0010218020305320_mmc1/Babushok_chem.inp
- Original thermodynamic source files: _processing/extracted/s0010218020305320_mmc1/Chatelain_therm.dat, _processing/extracted/s0010218020305320_mmc1/Babushok_therm.dat, _processing/extracted/s0010218020305320_mmc1/Slakman_therm.dat, _processing/extracted/s0010218020305320_mmc1/PeOx_therm.dat, _processing/extracted/s0010218020305320_mmc1/Miller_therm.dat, _processing/extracted/s0010218020305320_mmc1/Mevel_therm.dat, _processing/extracted/s0010218020305320_mmc1/Kondo_therm.dat
- Original transport source files: _processing/extracted/s0010218020305320_mmc1/Chatelain_tran.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Issue while reading reaction in chem.inp starting on line 121: """ OH*=OH+HV 1.400E+06 0.0 0.0 """ Found a reversible reaction containing a product photon. Converting to an irreversible reaction with the photon removed. No thermo data found for species 'O' No thermo data found for species 'N2O' No thermo data found for species 'N' No thermo data found for species 'SIO' No thermo data found for species 'OH*' No thermo data found for species 'O2' No thermo data found for species 'OH' No thermo data found for species 'HO2' No thermo data found for species 'H2O2' No thermo data found for species 'NH' No thermo data found for species 'NO' No thermo data found for species 'NH2' No thermo data found for species 'N2O3' No thermo data found for species 'HNO' No thermo data found for spe ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'O' Ignoring redundant declaration for species 'N2O' Ignoring redundant declaration for species 'N' Ignoring redundant declaration for species 'OH*' Ignoring redundant declaration for species 'H' Suppressed 26 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Issue while reading reaction in chem.inp starting on line 120: """ OH*=OH+HV 1.400E+06 0.0 0.0 """ Found a reversible reaction containing a product photon. Converting to an irreversible reaction with the photon removed. No thermo data found for species 'N2O' No thermo data found for species 'H2O' No thermo data found for species 'HONO' No thermo data found for species 'O' No thermo data found for species 'O ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 3

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: missing cantera result json
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 4

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'N2' Ignoring redundant declaration for species 'H2' Ignoring redundant declaration for species 'N2O' Ignoring redundant declaration for species 'H2O' Ignoring redundant declaration for species 'HONO' Suppressed 26 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Issue while reading reaction in chem.inp starting on line 48: """ OH*=OH+HV 1.400E+06 0.0 0.0 """ Found a reversible reaction containing a product photon. Converting to an irreversible reaction with the photon removed. No thermo data found for species 'N2O' No thermo data found for species 'H2O' No thermo data found for species 'HONO' No thermo data found for species 'O' No thermo data found for specie ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 5

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'N2' Ignoring redundant declaration for species 'OH*' Ignoring redundant declaration for species 'H' Ignoring redundant declaration for species 'O' Ignoring redundant declaration for species 'OH' Suppressed 27 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Issue while reading reaction in chem.inp starting on line 126: """ OH*=OH+HV 1.400E+06 0.0 0.0 """ Found a reversible reaction containing a product photon. Converting to an irreversible reaction with the photon removed. Error while reading reaction in chem.inp starting on line 3432: """ C6H5 (+M) = o-C6H4 + H (+M) 4.300E+12 0.616 77313. ! RRKM 00-HAI-FRE LOW/ 1.000E+84 -18.866 90064 / """ could not convert ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 6

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: No transport data for species 'He'. No transport data for species 'Ne'. No transport data for species 'cSI3H6(1)'. No transport data for species 'H6SI3(2)'. No transport data for species 'SIH3(5)'. No transport data for species 'SI2H5(6)'. No transport data for species 'SIH3SIH(8)'. No transport data for species 'cSI4H8(9)'. No transport data for species 'H8SI4(10)'. No transport data for species 'SI3H8(12)'. No transport data for species 'H4SI2(13)'. No transport data for species 'SIH2SI(16)'. No transport data for species 'H4SI2(17)'. No transport data for species 'H2SI2(18)'. No transport data for species 'SI2H2(19)'. No transport data for species 'H5SI3(20)'. No transport data for species 'H4SI3(22)'. No transport data for species 'H3SI2(23)'. No transport data for species ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 7

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: No transport data for species 'He'. No transport data for species 'Ne'. No transport data for species 'cSI3H6(1)'. No transport data for species 'H6SI3(2)'. No transport data for species 'SIH3(5)'. No transport data for species 'SI2H5(6)'. No transport data for species 'SIH3SIH(8)'. No transport data for species 'cSI4H8(9)'. No transport data for species 'H8SI4(10)'. No transport data for species 'SI3H8(12)'. No transport data for species 'H4SI2(13)'. No transport data for species 'SIH2SI(16)'. No transport data for species 'H4SI2(17)'. No transport data for species 'H2SI2(18)'. No transport data for species 'SI2H2(19)'. No transport data for species 'H5SI3(20)'. No transport data for species 'H4SI3(22)'. No transport data for species 'H3SI2(23)'. No transport data for species ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

The present work compares the performance of seven reaction models with respect to a large experimental dataset relevant to the high-temperature pyrolysis of both silane (SiH 4 ) and disilane (Si 2 H 6 ). Their performances were established based on different validation criteria that account for the shape and the amplitude of the validation profile. Then, the model performances were quantified with a global error, which accounts for the experimental uncertainties. The most satisfactory model has a global error as low as 3.1 (i.e., meaning 3.1 times higher than the experimental uncertainty) and the highest fraction (74%) of criteria with a low error ( < 2 ), while most of the models have large discrepancies with the validation dataset, global error near 8 and up to 110 for the less accurate model. The origins of these discrepancies are identified with reaction pathway and sensitivity analyses. Among the seven tested model, three main decomposition pathways are evidenced, including one more specific to the models presenting the lowest errors. Based on the global error values, the ability to reproduce all the experimental conditions, and the model analyses, the reaction pathways relevant to the high-temperature pyrolysis of silane and disilane are determined. In addition, the present study provides experimental and numerical guidance for the future developments of silicon hydride reaction models. The limited performance of most of the oldest reaction models may have a significant impact on our current understanding of the pyrolysis and oxidation kinetics of silane.

## Processing Notes

- extracted S0010218020305320_mmc1.zip
