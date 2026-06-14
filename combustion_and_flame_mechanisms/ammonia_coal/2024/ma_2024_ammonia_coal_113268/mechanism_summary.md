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
- Validation reactor/type from abstract: burner/flame structure

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

Co-firing ammonia with coal is a promising and feasible technology for reducing coal-related carbon emissions. Pyrolysis and ignition of ammonia-coal blended fuels are the key steps for flame stability and boiler operation safety throughout the conversion process but remain unclear. In this work, an extended Euler–Lagrange framework coupled to detailed solid-phase pyrolysis kinetics and gas-phase reactions mechanism is introduced and validated against experimental results for ammonia-coal co-firing in a two-stage flat flame burner. First, the CRECK-S coal pyrolysis model was validated with TGA experiments and the CPD model at different heating rates to determine parameters for a competing two-step model for CFD simulations. Second, a detailed gas-phase mechanism with 116 species and 1513 elementary reactions was derived from the volatile and ammonia reaction mechanisms. Thirdly, the co-firing simulations were validated for the ignition delay time for various ammonia co-firing ratios. The results show that increasing the co-firing ratios from 0.0 to 1.0 results in gradually increasing ignition delay times in a low-oxygen atmosphere. Further analysis demonstrates that adding ammonia accelerates the coal particle heating rate due to the reduced coal particle number density and ammonia reaction induced gas-phase temperature increase, and thus the coal devolatilization rate is increased. The latter plays a dominant role. Hydrogen produced from ammonia pyrolysis is negligible, so ammonia predominantly participates in the ignition. Time scale analysis shows that homogeneous ignition is dominant during the ignition process. The presence of ammonia inhibits the inward oxygen diffusion and causes the reaction zone to move away from the pulverized coal particle flow. The oxygen diffusion inhibition and low reactivity of ammonia compared to volatiles lead to an increase in ignition delay time for ammonia co-firing, even though pulverized coal devolatilization is accelerated.

## Processing Notes

- extracted S0010218023006429_mmc4.zip
- extracted S0010218023006429_mmc1.zip
- extracted S0010218023006429_mmc3.zip
- extracted S0010218023006429_mmc2.zip
- extracted S0010218023006429_mmc5.zip
- extracted S0010218023006429_mmc6.zip
