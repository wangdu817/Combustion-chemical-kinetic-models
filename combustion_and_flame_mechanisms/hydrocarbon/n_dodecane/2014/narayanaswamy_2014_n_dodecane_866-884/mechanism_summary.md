# A chemical mechanism for low to high temperature oxidation of n-dodecane as a component of transportation fuel surrogates

## Bibliography

Krithika Narayanaswamy, Perrine Pepiot, Heinz Pitsch. A chemical mechanism for low to high temperature oxidation of n-dodecane as a component of transportation fuel surrogates[J]. Combustion and Flame, 2014, 161: 866-884. DOI: 10.1016/j.combustflame.2013.10.012.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 161 / Apr
- Article number: 866-884
- DOI: 10.1016/j.combustflame.2013.10.012
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218013003866
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: n_dodecane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S0010218013003866_mmc4.txt, _processing/raw_downloads/S0010218013003866_mmc2.txt
- Original thermodynamic source files: _processing/raw_downloads/S0010218013003866_mmc6.txt
- Original transport source files: _processing/raw_downloads/S0010218013003866_mmc7.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring duplicate transport data for species "C6H2" on line 128 of "tran.dat". Error while reading transport data in tran.dat starting on line 227: """ I-C8H18 -1 458.500 6.414 0.000 0.000 0.000 """ Invalid geometry flag value '-1' for species 'I-C8H18'. Flag value must be 0, 1, or 2. Error while reading transport data in tran.dat starting on line 228: """ C-C8H17 -1 458.500 6.414 0.000 0.000 0.000 """ Invalid geometry flag value '-1' for species 'C-C8H17'. Flag value must be 0, 1, or 2. Error while reading transport data in tran.dat starting on line 229: """ Y-C7H15 -1 437.300 6.168 0.000 0.000 0.000 """ Invalid geometry flag value '-1' for species 'Y-C7H15'. Flag value must be 0, 1, or 2. Error while reading transport data in tran.dat starting on line 230: """ Y-C7H14 -1 439 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring duplicate transport data for species "C6H2" on line 128 of "tran.dat". Error while reading transport data in tran.dat starting on line 227: """ I-C8H18 -1 458.500 6.414 0.000 0.000 0.000 """ Invalid geometry flag value '-1' for species 'I-C8H18'. Flag value must be 0, 1, or 2. Error while reading transport data in tran.dat starting on line 228: """ C-C8H17 -1 458.500 6.414 0.000 0.000 0.000 """ Invalid geometry flag value '-1' for species 'C-C8H17'. Flag value must be 0, 1, or 2. Error while reading transport data in tran.dat starting on line 229: """ Y-C7H15 -1 437.300 6.168 0.000 0.000 0.000 """ Invalid geometry flag value '-1' for species 'Y-C7H15'. Flag value must be 0, 1, or 2. Error while reading transport data in tran.dat starting on line 230: """ Y-C7H14 -1 439 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Using surrogate fuels in lieu of real fuels is an appealing concept for combustion studies. A major limitation however, is the capability to design compact and reliable kinetic models that capture all the specificities of the simpler, but still multi-component surrogates. This task is further complicated by the fairly large nature of the hydrocarbons commonly considered as potential surrogate components, since they typically result in large detailed reaction schemes. Towards addressing this challenge, the present work proposes a single, compact, and reliable chemical mechanism, that can accurately describe the oxidation of a wide range of fuels, which are important components of surrogate fuels. A well-characterized mechanism appropriate for the oxidation of smaller hydrocarbon species [G. Blanquart, P. Pepiot-Desjardins, H. Pitsch, Chemical mechanism for high temperature combustion of engine relevant fuels with emphasis on soot precursors, Combust. Flame 156 (2009) 588–607], and several substituted aromatic species [K. Narayanaswamy, G. Blanquart, H. Pitsch, A consistent chemical mechanism for the oxidation of substituted aromatic species, Combust. Flame 157 (10) (2010) 1879–1898], ideally suited as a base to model surrogates, has now been extended to describe the oxidation of n-dodecane, a representative of the paraffin class, which is often used in diesel and jet fuel surrogates. To ensure compactness of the kinetic scheme, a short mechanism for the low to high temperature oxidation of n-dodecane is extracted from the detailed scheme of Sarathy et al. [S. M. Sarathy, C. K.Westbrook, M. Mehl, W. J. Pitz, C. Togbe, P. Dagaut, H. Wang, M. A. Oehlschlaeger, U. Niemann, K. Seshadri, Comprehensive chemical kinetic modeling of the oxidation of 2-methylalkanes from C7 to C20, Combust. Flame 158 (12) (2011) 2338–2357] and integrated in a systematic way into the base model. Rate changes based on recent rate recommendations from literature are introduced to the resulting chemical mechanism in a consistent manner, which improve the model predictions. Extensive validation of the revised kinetic model is performed using a wide range of experimental conditions and data sets.

## Processing Notes

- none
