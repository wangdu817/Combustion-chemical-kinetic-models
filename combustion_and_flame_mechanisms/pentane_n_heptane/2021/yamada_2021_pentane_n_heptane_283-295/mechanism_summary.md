# Measurements and simulations of ignition delay times and laminar flame speeds of nonane isomers

## Bibliography

Shimpei Yamada, Daisuke Shimokuri, Shenqyang Shy, Tomoaki Yatsufusa, Yuta Shinji, Yi-Rong Chen, et al.. Measurements and simulations of ignition delay times and laminar flame speeds of nonane isomers[J]. Combustion and Flame, 2021, 227: 283-295. DOI: 10.1016/j.combustflame.2020.12.043.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 227 / May
- Article number: 283-295
- DOI: 10.1016/j.combustflame.2020.12.043
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218020305988
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: pentane_n_heptane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, laminar flame speed, burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218020305988_mmc2/24mC7rev01_mech.txt, _processing/extracted/s0010218020305988_mmc2/2mC8rev01_mech.txt, _processing/extracted/s0010218020305988_mmc2/2244mC5rev01_mech.txt, _processing/extracted/s0010218020305988_mmc2/nC9rev01_mech.txt
- Original thermodynamic source files: _processing/extracted/s0010218020305988_mmc2/24mC7rev01_thrm.txt, _processing/extracted/s0010218020305988_mmc2/2244mC5rev01_thrm.txt, _processing/extracted/s0010218020305988_mmc2/2mC8rev01_thrm.txt, _processing/extracted/s0010218020305988_mmc2/nC9rev01_thrm.txt
- Original transport source files: _processing/extracted/s0010218020305988_mmc2/2mC8rev01_trn.txt, _processing/extracted/s0010218020305988_mmc2/nC9rev01_trn.txt, _processing/extracted/s0010218020305988_mmc2/2244mC5rev01_trn.txt, _processing/extracted/s0010218020305988_mmc2/24mC7rev01_trn.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: missing cantera result json
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 594: """ C3H6+H=aC3H5+H2 5.000e+12 0.000 1100.0 rev / 3.795e+11 0.150 16638.4 / ! ---------- """ Unparsable line: 'Added reactions for SL improvement'. Error while reading reaction in chem.inp starting on line 605: """ C3H6+CH3=aC3H5+CH4 1.400e+11 0.000 8800.0 rev / 1.441e+14 -0.660 26464.1 / ! ---------- """ Unparsable line: 'Added reactions for SL improvement'. Error while reading reaction in chem.inp starting on line 692: """ iC4H8+H=iC4H7a+H2 5.000e+12 0.000 1100.0 rev / 1.898e+11 0.149 16637.7 / ! ---------- """ Unparsable line: 'Added reactions for SL improvement'. Error while reading reaction in chem.inp starting on line 703: """ iC4H8+CH3=iC4H7a+CH4 1.400e+11 0.000 8800.0 rev / 7.206e+13 -0.660 26463.4 / ! ------ ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 3

- Status: ok
- Species count: 669
- Reaction count: 2763
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 4

- Status: ok
- Species count: 669
- Reaction count: 2763
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Ignition delay times (IDTs) and laminar flame speeds (S L) of C9H20 (nonane) isomers are systematically investigated. IDTs of normal nonane (n-C9), 2-methyloctane (2mC8), 2,4-dimethylheptane (24mC7), and 2,2,4,4-tetramethylpentane (2244mC5) are experimetally obtained by a shock tube facility and numerically simulated by a chemkin 0-D reactor model. Further, laminar flame speeds (S L) of n-C9 and 2244mC5 are measured by spherical expanding flames in a constant-temperature, constant-pressure dual-chamber cruciform burner over a wide range of the equivalence ratio (Φ = 0.7–1.4), which are used to compare with numerically simulated results obtained by chemkin 1-D flame speed model. Detailed reaction mechanisms of KUCRS, LLNL and JetSurF ver.02 are used for numerical simulations. It is found that experimental IDTs increase with the number of methyl branches, especially in low-temperature and negative temperature coefficient (NTC) regions, where the increase of IDT with the number of methyl branches are well predicted by KUCRS. We also find that the measured values of S L of highly branched 2244mC5 are smaller than those of n-C9 at all values of Φ studied, of which measured S L data are successfully reproduced by the 1-D flame speed model with KUCRS. These results are important to our understanding of reaction characteristics for highly branched nonane isomers and for the designing of optimal alternative fuels in internal combustion engines.

## Processing Notes

- extracted S0010218020305988_mmc2.zip
