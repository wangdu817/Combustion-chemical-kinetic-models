# Laminar flame speed modification by Nanosecond Repetitively Pulsed Discharges, Part I: Numerical model

## Bibliography

Colin A. Pavan, Carmen Guerra-Garcia. Laminar flame speed modification by Nanosecond Repetitively Pulsed Discharges, Part I: Numerical model[J]. Combustion and Flame, 2025, 282: 114484. DOI: 10.1016/j.combustflame.2025.114484.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 282 / December
- Article number: 114484
- DOI: 10.1016/j.combustflame.2025.114484
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025005218
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025005218/pdfft?md5=f5d6f5fee9c14b0a1d4739e502e68595&pid=1-s2.0-S0010218025005218-main.pdf
- Fuel type: methane
- Plasma-related mechanism: yes
- Validation reactor/type from abstract: laminar flame speed, burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: not available
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218025005218_mmc1/kinet_CH4_PAC.inp
- Original thermodynamic source files: not found
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading entry in chem.inp starting on line 16: """ #================================================================================================================================== """ Section starts with unrecognized keyword '#==================================================================================================================================' Please check https://cantera.org/stable/userguide/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files for the correct Chemkin syntax.; cleanup retry failed: InputError: Error while reading entry in chem_cantera_clean.inp starting on line 6: """ #================================================================================================================================== """ Section starts with unrecog ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: not available
- Standard tran.dat: not available

## Abstract

Plasma-assisted combustion (PAC) offers significant potential to enhance combustion processes by modifying thermal, kinetic, and transport properties. Despite progress in the field, challenges remain in reconciling disparate experimental results and understanding the mechanisms of plasma-flame interaction. This work develops a numerical modeling framework to systematically evaluate the impact of Nanosecond Repetitively Pulsed Discharges (NRPDs) on PAC systems. The focus of this contribution is modeling laminar premixed flames; and the main metric to assess the impact of plasma on flame is the laminar flame speed. The model is exercised on a stoichiometric methane/air flame. A combined 0D plasma-combustion model, PlasmaChem, is presented, enabling accurate energy tracking and coupling of detailed plasma and combustion mechanisms. The model is extended to 1D to incorporate compressible fluid dynamics, capturing the interaction between plasma and flame propagation. The results reveal distinct phases of plasma-flame interaction, demonstrating both beneficial effects, such as increased laminar flame speed due to radical production, and adverse effects, including flame deceleration from pressure disturbances. The model is compared to experiments in an accompanying paper, Part II of this work. Novelty and significance This work complements prior modeling studies that have included detailed 0D chemical kinetic models, phenomenological 3D models of plasma-assisted combustion, and self-consistent 1D and 2D simulations mostly devoted to ignition. In this work, we develop the first 1D flame model that integrates detailed plasma and combustion chemistry with compressible fluid dynamics, and allows for simulations over tens of milliseconds and parametric explorations. The model focuses on quantifying the impact of nanosecond repetitively pulsed discharges (NRPDs) on an important fundamental parameter, the laminar flame speed, unlike previous studies focusing exclusively on ignition delay time. The approach has revealed that the plasma can have both beneficial (increase) and adverse (decrease) effects on the laminar flame speed; reconciling discrepancies in the literature and offering a predictive tool to optimize PAC systems. The model is a step forward in enabling systematic parametric exploration, and facilitating rapid design iterations of plasma-assisted combustion phenomena.

## Processing Notes

- extracted S0010218025005218_mmc1.zip
