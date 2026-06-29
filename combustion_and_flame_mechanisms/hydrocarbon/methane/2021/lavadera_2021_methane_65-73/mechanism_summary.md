# Laminar burning velocities of methane + formic acid + air flames: Experimental and modeling study

## Bibliography

Marco Lubrano Lavadera, Alexander A. Konnov. Laminar burning velocities of methane + formic acid + air flames: Experimental and modeling study[J]. Combustion and Flame, 2021, 225: 65-73. DOI: 10.1016/j.combustflame.2020.10.050.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 225 / Mar
- Article number: 65-73
- DOI: 10.1016/j.combustflame.2020.10.050
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218020304703
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: methane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S0010218020304703_mmc1.txt
- Original thermodynamic source files: _processing/raw_downloads/S0010218020304703_mmc3.txt
- Original transport source files: _processing/raw_downloads/S0010218020304703_mmc4.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 232
- Reaction count: 2769
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by PlogRate::validate: Error on line 10186 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/methane/2021/lavadera_2021_methane_65-73/mechanism.yaml: Invalid rate coefficient for reaction 'C2H3O2 <=> CH3 + CO2' at P = 1.0132e+07, T = 500.0 To fix this error, remove this reaction or contact the author of the reaction/mechanism in question, because the rate expression is mathematically unsound at the temperatures and pressures noted above. | Line | | 10181 | fit btw. 550 and 1650 K with MAE of 0.9%, 4.4% | 10182 | fit btw. 450 and ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Laminar burning velocities of methane + formic acid + air flames were determined using the heat flux method at 1 atm and initial gas temperature of 353 K. For fuel mixtures containing 75 or 50% mole fraction of HCOOH, a range of equivalence ratios from 0.7 to 1.3 was covered. In stoichiometric mixtures burning velocities were measured varying fuel composition from pure methane to 85% of formic acid. Due to the relatively high initial temperature close to the operational limit of the present burner, an extrapolation procedure had to be used leading to rather high experimental uncertainties up to ± 2 cm/s. New measurements have been compared with the predictions of the recent kinetic model of the authors and the model of Glarborg et al. [34]. Both models failed, and the reasons for the disagreement were analysed. A modification of the rate constant of reaction HOCO(+M)=H+CO2(+M) was suggested that dramatically improved the present model performance. This model was then compared with the predictions of the model developed by Marshall and Glarborg [19] at the conditions of the available experimental data for HCOOH flames. The comparison indicates some inconsistencies in the recent measurements of the burning velocity of formic acid.

## Processing Notes

- none
