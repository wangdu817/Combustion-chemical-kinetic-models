# Kinetic modeling of carbonaceous particle morphology, polydispersity and nanostructure through the discrete sectional approach

## Bibliography

Andrea Nobili, Niccolò Fanari, Timoteo Dinelli, Edoardo Cipriano, Alberto Cuoci, Matteo Pelucchi, et al.. Kinetic modeling of carbonaceous particle morphology, polydispersity and nanostructure through the discrete sectional approach[J]. Combustion and Flame, 2024, 269: 113697. DOI: 10.1016/j.combustflame.2024.113697.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 269 / November
- Article number: 113697
- DOI: 10.1016/j.combustflame.2024.113697
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024004061
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: burner/flame structure, counterflow flame

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218024004061_mmc2/kinetics.CHEMKIN.CKI
- Original thermodynamic source files: _processing/extracted/s0010218024004061_mmc3/thermo.CHEMKIN.CKT
- Original transport source files: _processing/extracted/s0010218024004061_mmc4/trans.CHEMKIN.TRC

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading thermo entry in therm.dat starting on line 1059: """ BIN4AJ G 300.00 3500.00 1330.00 1& C 160.00 H 115.00 3.13388326e+02 4.53632950e-01-1.61287498e-04 2.52639660e-08-1.42054928e-12 2 6.43001833e+04-1.63197350e+03-1.27820190e+02 1.78057585e+00-1.65783965e-03 3 7.75415418e-07-1.42426461e-10 1.81661648e+05 6.22425921e+02 4 """ invalid literal for int() with base 10: '160.00' Error while reading thermo entry in therm.dat starting on line 1064: """ BIN4BJ G 300.00 3500.00 1390.00 1& C 160.00 H 31.00 2.72480905e+02 2.70088841e-01-7.56449720e-05 6.37621195e-09 2.02304742e-13 2 -2.88261298e+04-1.45963715e+03-1.38632883e+02 1.45315010e+00-1.35232978e-03 3 6.18695067e-07-1.09926986e-10 8.54635032e+04 6.59130542e+02 4 """ invalid literal for int() with base 10: '160.00 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Carbon nanoparticle (CNP) formation from hydrocarbons combustion is of high interest not only for the study of pollutant (soot) emissions, but, above all, in the area of advanced materials. CNP optical and electronical properties, relevant for practical applications, significantly change with their size, morphology, and nanostructure. This work extends a detailed soot kinetic model, based on the discrete sectional approach, to explicitly incorporate the description of CNP polydispersity, maintaining the CHEMKIN-like format. The model considers various nanosized primary particles, generated from liquid-like counterparts through the carbonization process, which successively grow or aggregate forming fractal structures. The model is validated against experimental measurements from the literature including CNP volume fraction, several morphological characteristics, number density and particle H/C ratio. Data are taken from 19 laminar flames, in different configurations (counterflow diffusion flames, premixed flat flames established on the McKenna-type burner and burner-stabilized stagnation flames) and over a wide range of operating conditions (P=1–10 atm, Tmax=1556-2264 K). The model captures the measured trends of all the analyzed CNP properties as a function of equivalence ratio, residence time and fuel type in premixed flames, and pressure and strain rate in counterflow flames. Model deviations from the experiments are discussed, also in comparison with other state-of-the-art soot models based on different approaches. Sensitivity analyses are performed on carbonization, coalescence, and aggregation rates, which have the largest impact on CNP morphology and are characterized by larger uncertainty compared to elementary chemical pathways.

## Processing Notes

- extracted S0010218024004061_mmc3.zip
- extracted S0010218024004061_mmc2.zip
- extracted S0010218024004061_mmc4.zip
- extracted S0010218024004061_mmc1.docx
