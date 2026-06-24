# Measurements of the laminar burning velocities and an improved low-to-high temperature kinetic model of 2-butanone

## Bibliography

Liqing Guo, Shusen Wang, Qianjin Lin, Bo Wei, ... Alexander A. Konnov. Measurements of the laminar burning velocities and an improved low-to-high temperature kinetic model of 2-butanone[J]. Combustion and Flame, 2026, 288: 114947. DOI: 10.1016/j.combustflame.2026.114947.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 288 / June
- Article number: 114947
- DOI: 10.1016/j.combustflame.2026.114947
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026001835
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: 2_butanone
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing\extracted\s0010218026001835_mmc3\Butanone_V4MECH.inp
- Original thermodynamic source files: _processing\extracted\s0010218026001835_mmc4\Butanone_V4THER.dat
- Original transport source files: _processing\extracted\s0010218026001835_mmc5\Butanone_V4TRAN.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 417: """ H+O2(+M)=HO2(+M) 4.66E12 0.44 0.0E0 N2/1.0/ HE/0.57/ AR/0.65/ O2/1.0/ H2/2.0/ CH4/2.0/ CO2/3.25/ H2O/17.6/ CO/4.0/ LOWMX/1.225E19 -1.2E0 0.0E0/ TROEMX/5.0E-1 1.0E0 1.0E10 1.0E30/ LOWSP/N2 4.5E20 -1.73E0 0.0E0/ TROESP/N2 5.0E-1 1.0E0 1.0E10 1.0E30/ """ could not convert string to float: 'N2' Please check https://cantera.org/stable/userguide/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files for the correct Chemkin syntax.; numeric cleanup retry failed: InputError: Error while reading reaction in chem_cantera_numeric_clean.inp starting on line 413: """ H+O2(+M)=HO2(+M) 4.66E12 0.44 0.0E0 N2/1.0/ HE/0.57/ AR/0.65/ O2/1.0/ H2/2.0/ CH4/2.0/ CO2/3.25/ H2O/17.6/ CO/4.0/ LOWMX/1.225E19 -1.2E0 0.0E0/ TROEMX/5.0E-1 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Laminar burning velocities (SL) of 2-butanone + air mixtures were measured using the heat flux method at atmospheric pressure over unburnt temperatures of 298–343 K and equivalence ratios of 0.7–1.4. The consistency among the present measurements, literature data, and model predictions was evaluated by means of the temperature and pressure dependences of SL. It was found that the present measurements accurately follow the empirical formula across all equivalence ratios, while notable inconsistencies were observed between the present measurements and the literature data on the fuel-rich side. Furthermore, the latest 2-butanone combustion kinetic model, PCFC_butanone V3, underpredicts SL, as well as the ignition delay times (IDTs) under low-temperature conditions. Accordingly, a new 2-butanone combustion kinetic model (Present model) was developed, which is based on the 2-butanone sub-mechanism of PCFC_butanone V3 with updates to six key low-temperature reaction classes (including H-abstraction reactions of 2-butanone and O2-addition reactions of butanoyl radicals) and adopts NUIG 1.3 as the C0-C4 base mechanism. Comprehensive model evaluation results demonstrate that the Present model well predicts the new measurements of SL, as well as the low-to-high temperature IDTs, SL, and species profiles data reported in the literature. Sensitivity and reaction flux analyses reveal that the accurate prediction of SL by the Present model is primarily attributed to the revised rate constants for the reaction CH2+O2=>CO2+2H and the incorporation of the CH2→CH2O→CO pathway in the NUIG 1.3. The updates to the rate constants of the four reaction classes (the HȮ2+HȮ2 reactions, 2-butanone H-abstraction reactions by CH3Ȯ and HȮ2 radicals, concerted HȮ2-elimination of alkylperoxy reactions, and CH3Ȯ+O2 reactions) are the primary reasons for the Present model's good prediction of low-temperature IDTs and species profiles.

## Processing Notes

- none
