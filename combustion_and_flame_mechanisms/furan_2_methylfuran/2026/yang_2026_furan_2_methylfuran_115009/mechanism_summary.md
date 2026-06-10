# Mid-infrared multicomponent laser diagnostic and kinetic modelling studies of furan and 2-methylfuran combustion in a shock tube

## Bibliography

Youquan Yang, Zhimin Peng, Haodong Chen, Dao Zheng, ... Yanjun Du. Mid-infrared multicomponent laser diagnostic and kinetic modelling studies of furan and 2-methylfuran combustion in a shock tube[J]. Combustion and Flame, 2026, 289: 115009. DOI: 10.1016/j.combustflame.2026.115009.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 289 / July
- Article number: 115009
- DOI: 10.1016/j.combustflame.2026.115009
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026002452
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: furan_2_methylfuran
- Validation reactor/type from abstract: shock tube

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\furan_2_methylfuran\yang_2026_furan_2_methylfuran_115009\raw_downloads\S0010218026002452_mmc2.txt
- Original thermodynamic source files: E:\mech_collection\combustion_and_flame_mechanisms\_processing_archive\2026\furan_2_methylfuran\yang_2026_furan_2_methylfuran_115009\raw_downloads\S0010218026002452_mmc3.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Unexpected token "+Hv" in reaction expression "OH*<=>R2OH+Hv
".
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.; numeric cleanup retry failed: InputError: Unexpected token "+Hv" in reaction expression "OH*<=>R2OH+Hv
".
Please check https://cantera.org/tutorials/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files
for the correct Chemkin syntax.
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

The experimental and kinetic studies of furan derivatives are essential for advancing the reliable utilization of bioenergy. This study reports laser-based diagnostics of furan and 2-methylfuran oxidation behind reflected shock waves at temperatures ranging from 1235 to 1680 K and pressures of approximately 2 bar. Time-resolved temperature, H₂O, CO, and CO₂ were simultaneously quantified using mid-infrared laser absorption spectroscopy, with H₂O measured via a newly developed calibration-free method. CO₂ onset times were extracted from measured profiles to characterize system reactivity and were compared against predictions from several kinetic mechanisms. Detailed comparisons were made between the experimental and the mechanism-simulated profiles. Under fuel-rich conditions, the Tran mechanism significantly overpredicted early CO₂ formation for both fuels. Rate-of-production and pathway analyses revealed that this discrepancy arises from excessive HCCO formation, which rapidly converts to CO₂ through the reaction HCCO + O₂ = CO + CO₂ + H. For furan, the overprediction originates from an overly strong ring-opening pathway (furan = C₂H₂ + CH₂CO), producing acetylene and ketene that promote HCCO formation. For 2-methylfuran, the dominant reaction of early HCCO formation is C₃H₂ + O₂ = HCCO + CO + H, reflecting deficiencies in the C₃H₂ and C₃H₃ sub-mechanisms of the Tran model. By updating the furan initiation chemistry and replacing the C₃H₂ and C₃H₃ sub-models, a revised mechanism was developed, yielding improved predictive performance, particularly under fuel-rich conditions.

## Processing Notes

- extracted S0010218026002452_mmc1.docx
