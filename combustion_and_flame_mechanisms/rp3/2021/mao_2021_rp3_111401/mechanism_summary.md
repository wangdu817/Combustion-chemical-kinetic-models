# Development and validation of a detailed kinetic model for RP-3 aviation fuel based on a surrogate formulated by emulating macroscopic properties and microscopic structure

## Bibliography

Yebing Mao, Liang Yu, Yong Qian, Sixu Wang, Zhiyong Wu, Mohsin Raza, et al.. Development and validation of a detailed kinetic model for RP-3 aviation fuel based on a surrogate formulated by emulating macroscopic properties and microscopic structure[J]. Combustion and Flame, 2021, 229: 111401. DOI: 10.1016/j.combustflame.2021.111401.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 229 / Jul
- Article number: 111401
- DOI: 10.1016/j.combustflame.2021.111401
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218021001280
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: rp3
- Plasma-related mechanism: no
- Validation reactor/type from abstract: rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S0010218021001280_mmc3.txt
- Original thermodynamic source files: _processing/extracted/s0010218021001280_mmc4/mmc4.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'NC5H11CHO' Ignoring redundant declaration for species 'NC5H11CO' Ignoring redundant declaration for species 'C6Y2-1J' Ignoring redundant declaration for species 'C7H15-1' Ignoring redundant declaration for species 'C6H13-1' Suppressed 344 additional warnings about redundant species declarations. Run ck2yaml again with the '--verbose' option to see all warnings. Error while reading reaction in chem.inp starting on line 21167: """ NBCH-1ENE+CH3O2 => NBCH-1N3J+CH3O2H 7.23+03 2.55 1.05E+04 """ could not convert string to float: '7.23+03' Error while reading reaction in chem.inp starting on line 21179: """ NBCH-1ENE+CH3O2 => NBCH-1N6J+CH3O2H 7.23+03 2.55 1.05E+04 """ could not convert string to float: '7.23+03' Error while reading reaction ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

This work proposed a kinetic model for RP-3, the most widely used military-civilian aviation fuel in China. Four hydrocarbons within the typical size of major components in RP-3, i.e., n-dodecane, iso-dodecane (2,2,4,6,6-pentamethylheptane), decalin and n-butylbenzene, were included in the component palette to improve the ability of the surrogate to mimic the properties related to the molecular weight. Seven properties, cetane number, molecular weight, H/C ratio, threshold sooting index, lower heating value, the proportion of -CH3 and -CH2 in the total carbons were selected as targets aiming at the comprehensive emulation of the chemical and physical propensities of RP-3. By sequential use of the genetic algorithm and a local search method, a surrogate containing 27.44% n-dodecane, 28.81% iso-dodecane, 26.12% decalin and 17.63% n-butylbenzene by mole was formulated. The autoignition delay times of the surrogate were measured using a heated rapid compression machine at pressures of 10, 15, 20 bar and equivalence ratios of 0.5, 1.0 and 2.0 over low-to-intermediate temperature range. Results show that the surrogate can not only emulate the target properties but also the key non-targeted properties. A kinetic model of 3065 species and 11,898 reactions was then developed based on the proposed surrogate to describe the chemical process during the combustion of RP-3. Simulations show that the model can predict the fundamental combustion datasets in the present work and literature satisfactorily, suggesting the rationality and applicability of the model. Rate of production and evolution histories of OH and HO2 were then conducted using the kinetic model to provide insight into the combustion of RP-3. Analysis suggests that negative temperature coefficient behavior also exists in the first stage ignition.

## Processing Notes

- extracted S0010218021001280_mmc4.zip
- extracted S0010218021001280_mmc2.xlsx
- extracted S0010218021001280_mmc1.xlsx
