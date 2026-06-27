# A chemical mechanism for low to high temperature oxidation of methylcyclohexane as a component of transportation fuel surrogates

## Bibliography

Krithika Narayanaswamy, Heinz Pitsch, Perrine Pepiot. A chemical mechanism for low to high temperature oxidation of methylcyclohexane as a component of transportation fuel surrogates[J]. Combustion and Flame, 2015, 162: 1193-1213. DOI: 10.1016/j.combustflame.2014.10.013.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 162 / Apr
- Article number: 1193-1213
- DOI: 10.1016/j.combustflame.2014.10.013
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218014003344
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: cyclohexane_ethylcyclohexane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S0010218014003344_mmc4.txt, _processing/raw_downloads/S0010218014003344_mmc5.txt
- Original thermodynamic source files: _processing/raw_downloads/S0010218014003344_mmc2.txt
- Original transport source files: _processing/raw_downloads/S0010218014003344_mmc3.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant thermo data for species 'C7H13' starting on line 1002 of therm.dat. Ignoring duplicate transport data for species "C6H2" on line 128 of "tran.dat". Error while reading transport data in tran.dat starting on line 469: """ H HE -9.66994265100 2.10026266000 -0.07705964500 0.00546112600 ! Middha et al, Proc. Comb. Inst., Vol. 29 """ 6 transport parameters were expected, but found 5. Error while reading transport data in tran.dat starting on line 473: """ H H2 -11.74984983000 3.15068443400 -0.25747189600 0.01589155500 ! Middha et al, Proc. Comb. Inst., Vol. 29 """ 6 transport parameters were expected, but found 5. Error while reading transport data in tran.dat starting on line 477: """ H2 HE -12.75127347000 3.42444798700 -0.28472577300 0.01593170100 ! Middha et al ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant thermo data for species 'C7H13' starting on line 1002 of therm.dat. Ignoring duplicate transport data for species "C6H2" on line 128 of "tran.dat". Error while reading transport data in tran.dat starting on line 469: """ H HE -9.66994265100 2.10026266000 -0.07705964500 0.00546112600 ! Middha et al, Proc. Comb. Inst., Vol. 29 """ 6 transport parameters were expected, but found 5. Error while reading transport data in tran.dat starting on line 473: """ H H2 -11.74984983000 3.15068443400 -0.25747189600 0.01589155500 ! Middha et al, Proc. Comb. Inst., Vol. 29 """ 6 transport parameters were expected, but found 5. Error while reading transport data in tran.dat starting on line 477: """ H2 HE -12.75127347000 3.42444798700 -0.28472577300 0.01593170100 ! Middha et al ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Surrogate fuels consisting of a mixture of well-studied hydrocarbons are often used to model real fuels in typical combustion studies. A major challenge, however, is the capability to design compact and reliable kinetic models that capture all the specificities of the simpler, but still multi-component surrogates. This task is further complicated by the diverse nature of the hydrocarbons commonly considered as potential surrogate components, since they typically result in large detailed reaction schemes. Towards addressing this challenge, the present work proposes a single, compact, and reliable chemical mechanism, that can accurately describe the oxidation of a wide range of fuels, which are important components of surrogate fuels. A well-characterized mechanism appropriate for the oxidation of smaller hydrocarbon species (Blanquart et al., 2009), as well as several substituted aromatic species and n-dodecane (Narayanaswamy et al., 2010, 2014), well suited as a base to model surrogates, has now been extended to describe the oxidation of methylcyclohexane, a representative of the cyclic alkane class, which is often used in jet fuel surrogates. To ensure compactness of the kinetic scheme, a short mechanism for the low to high temperature oxidation of methylcyclohexane is extracted from the detailed scheme of Pitz et al. (2007) and integrated in a systematic way into the previous model. Rate coefficient changes based on recent recommendations from literature, and an additional concerted elimination pathway important at moderate to low temperatures are introduced to the resulting chemical mechanism, which improve the model predictions. Extensive validation of the revised kinetic model is performed using a wide range of experimental conditions and data sets.

## Processing Notes

- none
