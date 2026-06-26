# Flame dynamics and kinetic coupling of ammonia and dimethyl-ether in non-premixed cool and warm flames at elevated pressure

## Bibliography

Wenbin Xu, Bowen Mei, Andy Thawko, Ziyu Wang, ... Yiguang Ju. Flame dynamics and kinetic coupling of ammonia and dimethyl-ether in non-premixed cool and warm flames at elevated pressure[J]. Combustion and Flame, 2026, 286: 114865. DOI: 10.1016/j.combustflame.2026.114865.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 286 / April
- Article number: 114865
- DOI: 10.1016/j.combustflame.2026.114865
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S001021802600101X
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ammonia_dimethyl_ether
- Plasma-related mechanism: no
- Validation reactor/type from abstract: burner/flame structure, counterflow flame

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s001021802600101x_mmc2/chem.inp
- Original thermodynamic source files: _processing/extracted/s001021802600101x_mmc3/therm.dat
- Original transport source files: _processing/extracted/s001021802600101x_mmc4/tran.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 1261: """ C6H5(+M)=o-C6H4+H(+M) 4.30E+12 0.62 77313. LOW/ 1.00E+84 -18.87 90064 / TROE/ 0.902, 696., 358., 3856. / H2/2.0/ H2O/6.0/ CH4/2.0/ CO/1.5/ CO2/2.0/ """ could not convert string to float: '0.902,' Ignoring redundant thermo data for species 'OCH2O2H' starting on line 1188 of therm.dat. Ignoring redundant thermo data for species 'HOCH2O2' starting on line 1194 of therm.dat. Ignoring redundant thermo data for species 'NH3' starting on line 1216 of therm.dat. Ignoring redundant thermo data for species 'NH2' starting on line 1222 of therm.dat. Ignoring redundant thermo data for species 'NH' starting on line 1228 of therm.dat. Suppressed 20 additional warnings about redundant thermo data. Run ck2yaml again with the '- ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Developing advanced low-temperature combustion engines with ammonia-biofuel blends requires a comprehensive understanding of low-temperature flame dynamics and kinetic interactions between ammonia and oxygenated fuels at elevated pressures. This work aims to study the dynamics and kinetics of non-premixed Dimethyl Ether (DME)/Ammonia (NH3) cool and warm flames, and their reignition to hot flames. A counterflow burner is employed to establish DME/NH3 cool/warm flames at pressures up to 5 atm. The extinction limits of cool flame and the reignition limits of warm flame to hot flame are measured by varying NH3 concentrations and compared to simulations to quantitatively examine the effects on DME/NH3 flames. It is found that NH3 inhibits low-temperature DME oxidation and results in lower cool flame extinction limits. Warm flames in the presence of NH3 are observed for the first time, revealing a non-monotonic effect of NH3 addition: a small amount of NH3 presence enhances warm flame chemistry and promotes reignition to hot flames, while a high NH3 concentration weakens the warm flame. This trend is further explained by 0-D PSR kinetic simulations and 1-D S-curve flame dynamic calculations. Three flame transition regimes between cool flames (CF), warm flames (WF), and hot flames (HF) by different levels of NH3 additions at a specific strain rate are identified, namely WF-HF reignition, WF-CF transition, and WF extinction. Reaction sensitivity analyses of OH at low temperatures show that NH3 inhibits DME oxidation through OH consumption via H-abstraction and the kinetic couplings of RO2/NH2, RO2/NOx, R/NOx, and O2QOOH/NOx further suppress the low-temperature branching. At intermediate-temperatures, NH2/NOx/HO2 coupling promotes warm flames via the pathway NH2 → H2NO → HNO → NO by converting O2 → HO2 → OH. At even higher NH₃ concentrations, radical termination reactions of NH2 + NO/NO2 and excessive OH consumption via H-abstraction inhibit the flame. The insights into the kinetic coupling between NH3 and low-temperature chemistry at elevated pressure and its impact on the dynamics of cool-warm-hot flame transitions will contribute to advancing combustion technologies with reduced emissions and improved energy-efficiency.

## Processing Notes

- extracted S001021802600101X_mmc2.zip
- extracted S001021802600101X_mmc4.zip
- extracted S001021802600101X_mmc1.docx
- extracted S001021802600101X_mmc3.zip
