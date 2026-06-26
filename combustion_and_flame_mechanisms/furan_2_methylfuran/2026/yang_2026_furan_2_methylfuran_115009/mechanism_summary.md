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
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S0010218026002452_mmc2.txt
- Original thermodynamic source files: _processing/raw_downloads/S0010218026002452_mmc3.txt
- Original transport source files: _processing/raw_downloads/S0010218026002452_mmc4.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 3189: """ OH*<=>R2OH+Hv 1.400e+06 0.0 0.0 """ Unexpected token '+Hv' in reaction expression 'OH*<=>R2OH+Hv'. May be due to undeclared species 'Hv'. Error while reading reaction in chem.inp starting on line 3204: """ CH*<=>B4CH+Hv 1.860e+06 0.0 0.0 """ Unexpected token '+Hv' in reaction expression 'CH*<=>B4CH+Hv'. May be due to undeclared species 'Hv'. Ignoring redundant thermo data for species 'RC3H5O' starting on line 986 of therm.dat. Ignoring redundant thermo data for species 'CH3CHCO' starting on line 1078 of therm.dat. Ignoring redundant thermo data for species 'C3H2' starting on line 2032 of therm.dat. Ignoring redundant thermo data for species 'pC3H4' starting on line 2036 of therm.dat. Ignoring redundant thermo d ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

The experimental and kinetic studies of furan derivatives are essential for advancing the reliable utilization of bioenergy. This study reports laser-based diagnostics of furan and 2-methylfuran oxidation behind reflected shock waves at temperatures ranging from 1235 to 1680 K and pressures of approximately 2 bar. Time-resolved temperature, H₂O, CO, and CO₂ were simultaneously quantified using mid-infrared laser absorption spectroscopy, with H₂O measured via a newly developed calibration-free method. CO₂ onset times were extracted from measured profiles to characterize system reactivity and were compared against predictions from several kinetic mechanisms. Detailed comparisons were made between the experimental and the mechanism-simulated profiles. Under fuel-rich conditions, the Tran mechanism significantly overpredicted early CO₂ formation for both fuels. Rate-of-production and pathway analyses revealed that this discrepancy arises from excessive HCCO formation, which rapidly converts to CO₂ through the reaction HCCO + O₂ = CO + CO₂ + H. For furan, the overprediction originates from an overly strong ring-opening pathway (furan = C₂H₂ + CH₂CO), producing acetylene and ketene that promote HCCO formation. For 2-methylfuran, the dominant reaction of early HCCO formation is C₃H₂ + O₂ = HCCO + CO + H, reflecting deficiencies in the C₃H₂ and C₃H₃ sub-mechanisms of the Tran model. By updating the furan initiation chemistry and replacing the C₃H₂ and C₃H₃ sub-models, a revised mechanism was developed, yielding improved predictive performance, particularly under fuel-rich conditions.

## Processing Notes

- extracted S0010218026002452_mmc1.docx
- extracted Microsoft_Visio_Drawing.vsdx
- extracted Microsoft_Visio_Drawing1.vsdx
- extracted Microsoft_Visio_Drawing2.vsdx
