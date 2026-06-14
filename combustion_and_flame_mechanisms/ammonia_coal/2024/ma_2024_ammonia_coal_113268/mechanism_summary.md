# Numerical investigation on pyrolysis and ignition of ammonia/coal blends during co-firing

## Bibliography

Peng Ma, Hendrik Nicolai, Qian Huang, Paulo Debiagi, Leon Loni Berkel, Alessandro Stagni, et al.. Numerical investigation on pyrolysis and ignition of ammonia/coal blends during co-firing[J]. Combustion and Flame, 2024, 261: 113268. DOI: 10.1016/j.combustflame.2023.113268.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 261 / March
- Article number: 113268
- DOI: 10.1016/j.combustflame.2023.113268
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023006429
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ammonia_coal
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218023006429_mmc1/coal_devolatilazation.inp, _processing/extracted/s0010218023006429_mmc4/chem.inp
- Original thermodynamic source files: _processing/extracted/s0010218023006429_mmc6/thermal.dat, _processing/extracted/s0010218023006429_mmc2/thermo.dat
- Original transport source files: _processing/extracted/s0010218023006429_mmc5/trans.dat, _processing/extracted/s0010218023006429_mmc3/transport.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 116
- Reaction count: 1513
- Message: InputError: Error while reading reaction in chem.inp starting on line 33: """ COAL3=>2.73CHAR+3.38CHARH+.2CH3O+.1CH4M+.11CH2M+0.9H2M+.6COH2M+2.2H2OM+.1CO2+.4CO2M+COLM .1000E+10 0.000 35000.0 !.2000E+11 0.000 33000.0 """ Unexpected token 'COAL3' in reaction expression 'COAL3=>2.73CHAR+3.38CHARH+.2CH3O+.1CH4M+.11CH2M+0.9H2M+.6COH2M+2.2H2OM+.1CO2+.4CO2M+COLM'. May be due to undeclared species 'COAL3'. Error while reading reaction in chem.inp starting on line 34: """ COAL3=>COAL3M .2500E+18 0.000 66000.0 ! .5000E+19 0.000 65000.0 """ Unexpected token 'COAL3' in reaction expression 'COAL3=>COAL3M'. May be due to undeclared species 'COAL3'. Error while reading reaction in chem.inp starting on line 35: """ COAL3M=>2.26CHARH+2.23CHAR+1.9CO+.25CH3O+.17CH4+.74CH2+.5CO2+.65COH2M+.08BTXM+1.2H2O+1.005H ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: ok
- Species count: 116
- Reaction count: 1513
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S0010218023006429_mmc4.zip
- extracted S0010218023006429_mmc1.zip
- extracted S0010218023006429_mmc3.zip
- extracted S0010218023006429_mmc2.zip
- extracted S0010218023006429_mmc5.zip
- extracted S0010218023006429_mmc6.zip
