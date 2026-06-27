# Measurements of the laminar burning velocities of small alkyl esters using the heat flux method: A comparative study

## Bibliography

Alexander A. Konnov, Jundie Chen, Marco Lubrano Lavadera. Measurements of the laminar burning velocities of small alkyl esters using the heat flux method: A comparative study[J]. Combustion and Flame, 2023, 255: 112922. DOI: 10.1016/j.combustflame.2023.112922.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 255 / September
- Article number: 112922
- DOI: 10.1016/j.combustflame.2023.112922
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023003036
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: methyl_formate_ethyl_formate_methyl_acetate_ethyl_acetate
- Plasma-related mechanism: no
- Validation reactor/type from abstract: laminar flame speed

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218023003036_mmc2/mmc1.inp
- Original thermodynamic source files: _processing/extracted/s0010218023003036_mmc2/mmc2.dat
- Original transport source files: _processing/raw_downloads/S0010218023003036_mmc3.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 498
- Reaction count: 5722
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by PlogRate::validate: Error on line 19220 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/methyl_formate_ethyl_formate_methyl_acetate_ethyl_acetate/2023/konnov_2023_methyl_formate_ethyl_formate_methyl_acetate_ethyl_acetate_112922/mechanism.yaml: Invalid rate coefficient for reaction 'C2H3O2 <=> CH3 + CO2' at P = 1.0132e+07, T = 500.0 To fix this error, remove this reaction or contact the author of the reaction/mechanism in question, because the rate expression is mathematically unsound at the temperatures and pressures noted ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Consistent datasets of the laminar burning velocity, LBV, for homologous fuels are indispensable for the elucidation of the structure-reactivity trends and the development and validation of pertinent detailed kinetic models. In the present study, all available LBV measurements for small alkyl esters obtained using the heat flux method have been reviewed. New results of the LBV for methyl propionate + air flames employing this method have been acquired at atmospheric pressure and initial gas temperatures from 298 to 348 K over equivalence ratios, ɸ = 0.7–1.5. Earlier experimental data for alkyl esters scattered across non-archival reports were re-examined and corrected when necessary. To prove the validity of the correction, additional LBV measurements for methyl formate and methyl butanoate were performed as well, and successfully demonstrated the consistency of the data obtained using different installations over an extended period of time. Then, the LBV of different families, such as methyl esters of various acids, formates, and acetates, along with isomers, were compared and structure-reactivity trends were assessed. Furthermore, the detailed kinetic mechanism of the authors was expanded by the reactions of methyl propionate and successfully compared with the LBV measurements for methyl formate, methyl acetate, methyl propionate, and ethyl formate. Distinct reactions controlling their flame propagation were revealed using sensitivity analysis and the origin of their rate constants is briefly discussed.

## Processing Notes

- extracted S0010218023003036_mmc2.zip
