# Effects of buffer gas composition on autoignition

## Bibliography

Scott W. Wagnon, Margaret S. Wooldridge. Effects of buffer gas composition on autoignition[J]. Combustion and Flame, 2014, 161: 898-907. DOI: 10.1016/j.combustflame.2013.09.022.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 161 / Apr
- Article number: 898-907
- DOI: 10.1016/j.combustflame.2013.09.022
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218013003544
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: n_heptane_iso_octane_n_octane_butanol
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S0010218013003544_mmc4.txt, _processing/raw_downloads/S0010218013003544_mmc1.txt, _processing/raw_downloads/S0010218013003544_mmc5.txt
- Original thermodynamic source files: _processing/raw_downloads/S0010218013003544_mmc3.txt, _processing/raw_downloads/S0010218013003544_mmc2.txt, _processing/raw_downloads/S0010218013003544_mmc6.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'CH2O2H' Ignoring redundant declaration for species 'TIC4H7Q2-I' Ignoring redundant declaration for species 'IIC4H7Q2-I' Ignoring redundant declaration for species 'IIC4H7Q2-T' No thermo data found for species 'IC5H12' No thermo data found for species 'AC5H11' No thermo data found for species 'BC5H11' No thermo data found for species 'CC5H11' No thermo data found for species 'DC5H11' No thermo data found for species 'AC5H10' No thermo data found for species 'BC5H10' No thermo data found for species 'CC5H10' No thermo data found for species 'AC5H9-A2' No thermo data found for species 'AC5H9-C' No thermo data found for species 'AC5H9-D' No thermo data found for species 'CC5H9-A' No thermo data found for species 'CC5H9-B' No thermo data f ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 2

- Status: ok
- Species count: 243
- Reaction count: 2688
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 3

- Status: ok_after_cleanup
- Species count: 243
- Reaction count: 2688
- Message: normalized legacy numeric/reaction syntax; cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

This work quantifies the chemical kinetic and thermal effects of buffer gas composition on autoignition of three fuels at conditions relevant to engines, combustors, and experimental facilities used to study ignition kinetics. Computational simulations of autoignition of iso-octane, n-heptane, and of n-butanol were used to characterize the effects of buffer gas composition on ignition delay time and heat release rate. Stoichiometric mixtures, ϕ =1.0, and a temperature range of 600–1100K were considered. Iso-octane and n-heptane were studied at initial pressures of 9.0atm and 60.0atm, and n-butanol was studied at initial pressures of 3.2atm and 60.0atm. Two dilution levels of buffer gas to O2 of 3.76:1 (mole basis) and 5.64:1 were considered (∼21% and ∼15% O2 respectively, mole basis). The fuels and simulation conditions were selected based on the relevance to engine operating conditions and previously published ignition studies. The buffer gases considered were argon, nitrogen, water, and carbon dioxide. Simulation results predicted changes of greater than a factor of 2 in ignition delay time and heat release rate as a function of buffer gas composition in the negative temperature coefficient (NTC) region for n-heptane and iso-octane. Outside the NTC region, the predicted effects of changes in buffer gas composition were small ( a factor of 2). The heat release rates were also sensitive to buffer gas composition, with carbon dioxide exhibiting relatively high levels of early and late heat release relative to the other buffer gases. Sensitivity analysis of the third-body collision efficiencies for the buffer gases showed the effects of uncertainties in the third body collision efficiencies on ignition delay time and heat release rate. The results highlight the significance of buffer gas composition on low-temperature combustion chemistry, particularly via H2O2 and HO2 decomposition and recombination reactions.

## Processing Notes

- none
