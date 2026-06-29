# Reduced reaction mechanism for natural gas combustion in novel power cycles

## Bibliography

Simon Drost, Miguel Sierra Aznar, Robert Schießl, Marcus Ebert, Jyh-Yuan Chen, Ulrich Maas. Reduced reaction mechanism for natural gas combustion in novel power cycles[J]. Combustion and Flame, 2021, 223: 486-494. DOI: 10.1016/j.combustflame.2020.09.029.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 223 / Jan
- Article number: 486-494
- DOI: 10.1016/j.combustflame.2020.09.029
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218020304132
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: methane_ethane_propane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: not available
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218020304132_mmc4/mmc4.mech, _processing/extracted/s0010218020304132_mmc5/mmc5.mech
- Original thermodynamic source files: not found
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 545: """ CH3O(+M)<=>CH2O+H(+M) 6.8000E+13 0.000 2.6170E+04 ! 173 LOW/ 1.8670E+25 -3.000 2.4307E+04 / TROE/ 0.9000 2500. 1300. 0.1000+100 / H2/ 2.00/ H2O/ 6.00/ CO/ 1.50/ CO2/ 2.00/ CH4/ 2.00/ C2H6/ 3.00/ """ could not convert string to float: '0.1000+100' No thermo data found for species 'AR' No thermo data found for species 'N2' No thermo data found for species 'H2' No thermo data found for species 'H' No thermo data found for species 'O2' No thermo data found for species 'O' No thermo data found for species 'H2O' No thermo data found for species 'OH' No thermo data found for species 'H2O2' No thermo data found for species 'HO2' No thermo data found for species 'CO' No thermo data found for species 'CO2' No thermo data ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: not available
- Standard tran.dat: not available

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 545: """ CH3O(+M)<=>CH2O+H(+M) 6.8000E+13 0.000 2.6170E+04 ! 173 LOW/ 1.8670E+25 -3.000 2.4307E+04 / TROE/ 0.9000 2500. 1300. 0.1000+100 / H2/ 2.00/ H2O/ 6.00/ CO/ 1.50/ CO2/ 2.00/ CH4/ 2.00/ C2H6/ 3.00/ """ could not convert string to float: '0.1000+100' No thermo data found for species 'AR' No thermo data found for species 'N2' No thermo data found for species 'H2' No thermo data found for species 'H' No thermo data found for species 'O2' No thermo data found for species 'O' No thermo data found for species 'H2O' No thermo data found for species 'OH' No thermo data found for species 'H2O2' No thermo data found for species 'HO2' No thermo data found for species 'CO' No thermo data found for species 'CO2' No thermo data ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: not available
- Standard tran.dat: not available

## Abstract

We study the auto-ignition behavior of several natural gas surrogates; in particular, the influence of ethane and propane on the ignition delay time of methane is studied. A rapid compression machine was used to obtain experimental measurements of ignition delay times at two different compression pressures (10 and 15 bar) and a wide range of compression temperatures (904–1151 K), for both stoichiometric and fuel-rich ( ϕ = 2 ) mixtures. The experimental results are compared to homogeneous reactor model simulations (HOMREA). A first set of simulations treats chemical reaction in detail, using the AramcoMech 3.0 reaction mechanism. It was observed that the mechanism predicted the observed ignition delay times well. Experimental results indicate that both ethane and propane have an ignition enhancing effect on the mixture, shortening the ignition delay time. Propane, in particular, appears to have a higher influence compared to ethane at low temperatures. In general, fuel rich mixtures show shorter ignition delay times. These trends are well captured by the AramcoMech 3.0 mechanism showing great agreement with experimental data. To make the chemistry underlying the AramcoMech 3.0 available in a concise form, e.g., for CFD applications or similar, a reduced chemistry scheme was developed (reaction mechanism with 49 species and 332 reactions). Simulations using the reduced model showed a similarly good agreement to which was developed based on the detailed AramcoMech 3.0 reaction mechanism. The experimental results are predicted well by the reduced model, in a similar fashion like the detailed scheme. Furthermore, the reduced reaction mechanism is validated against experimental data found in literature, covering a wide range of conditions. This establishes the reduced model as a useful, computationally efficient substitute for describing the effect of ethane and propane onto the auto-ignition of methane.

## Processing Notes

- extracted S0010218020304132_mmc8.docx
- extracted S0010218020304132_mmc6.docx
- extracted S0010218020304132_mmc7.docx
- extracted S0010218020304132_mmc2.xlsx
- extracted S0010218020304132_mmc5.zip
- extracted S0010218020304132_mmc4.zip
- extracted S0010218020304132_mmc3.xlsx
- extracted S0010218020304132_mmc1.xlsx
