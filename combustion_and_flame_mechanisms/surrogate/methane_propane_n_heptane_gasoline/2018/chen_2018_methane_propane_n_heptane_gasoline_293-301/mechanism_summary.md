# Towards improved automatic chemical kinetic model reduction regarding ignition delays and flame speeds

## Bibliography

Yulin Chen, Jyh-Yuan Chen. Towards improved automatic chemical kinetic model reduction regarding ignition delays and flame speeds[J]. Combustion and Flame, 2018, 190: 293-301. DOI: 10.1016/j.combustflame.2017.11.024.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 190 / Apr
- Article number: 293-301
- DOI: 10.1016/j.combustflame.2017.11.024
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218017304637
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: methane_propane_n_heptane_gasoline
- Plasma-related mechanism: possible
- Validation reactor/type from abstract: laminar flame speed

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218017304637_mmc1/supplement/prf/prf-207sp.inp, _processing/extracted/s0010218017304637_mmc1/supplement/propane/propane-32sp.inp, _processing/extracted/s0010218017304637_mmc1/supplement/methane/methane-27sp.inp, _processing/extracted/s0010218017304637_mmc1/supplement/nheptane/nc7h16-126sp.inp
- Original thermodynamic source files: _processing/extracted/s0010218017304637_mmc1/supplement/prf/therm-prf.dat, _processing/extracted/s0010218017304637_mmc1/supplement/propane/thermo-propane.dat, _processing/extracted/s0010218017304637_mmc1/supplement/methane/therm_methane.dat, _processing/extracted/s0010218017304637_mmc1/supplement/nheptane/therm-nc7h16.dat
- Original transport source files: _processing/extracted/s0010218017304637_mmc1/supplement/prf/tran-prf.dat, _processing/extracted/s0010218017304637_mmc1/supplement/propane/tran-propane.dat, _processing/extracted/s0010218017304637_mmc1/supplement/methane/transport_methane.dat, _processing/extracted/s0010218017304637_mmc1/supplement/nheptane/tran-nc7h16.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 207
- Reaction count: not parsed
- Message: InputError: No transport data for species 'h'. No transport data for species 'h2'. No transport data for species 'o'. No transport data for species 'o2'. No transport data for species 'oh'. No transport data for species 'h2o'. No transport data for species 'n2'. No transport data for species 'co'. No transport data for species 'hco'. No transport data for species 'co2'. No transport data for species 'ch3'. No transport data for species 'ch4'. No transport data for species 'ho2'. No transport data for species 'h2o2'. No transport data for species 'ch2o'. No transport data for species 'ch3o'. No transport data for species 'c2h6'. No transport data for species 'c2h4'. No transport data for species 'c2h5'. No transport data for species 'ch2'. No transport data for species 'ch'. No transport da ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: 282
- Reaction count: not parsed
- Message: InputError: No thermo data found for species 'H2' No thermo data found for species 'H' No thermo data found for species 'O' No thermo data found for species 'O2' No thermo data found for species 'OH' No thermo data found for species 'H2O' No thermo data found for species 'HO2' No thermo data found for species 'H2O2' No thermo data found for species 'CH2' No thermo data found for species 'CH2*' No thermo data found for species 'CH3' No thermo data found for species 'CH4' No thermo data found for species 'CO' No thermo data found for species 'CO2' No thermo data found for species 'HCO' No thermo data found for species 'CH2O' No thermo data found for species 'CH3O' No thermo data found for species 'C2H2' No thermo data found for species 'C2H3' No thermo data found for species 'C2H4' No thermo ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 3

- Status: cantera_failed
- Species count: 593
- Reaction count: not parsed
- Message: InputError: No thermo data found for species 'H2' No thermo data found for species 'H' No thermo data found for species 'O' No thermo data found for species 'O2' No thermo data found for species 'OH' No thermo data found for species 'H2O' No thermo data found for species 'HO2' No thermo data found for species 'H2O2' No thermo data found for species 'CH2' No thermo data found for species 'CH2*' No thermo data found for species 'CH3' No thermo data found for species 'CH4' No thermo data found for species 'CO' No thermo data found for species 'CO2' No thermo data found for species 'HCO' No thermo data found for species 'CH2O' No thermo data found for species 'CH3O' No thermo data found for species 'C2H2' No thermo data found for species 'C2H3' No thermo data found for species 'C2H4' No thermo ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 4

- Status: ok
- Species count: 207
- Reaction count: 1858
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

In chemical kinetic model reduction under internal combustion engine conditions, most implementations only consider ignition related chemistry without consideration of flame speed prediction. In practice, flame propagation commonly exists in spark ignition engines, dual-fuel with pilot injection compression ignition engines, reactivity controlled compression ignition engines, and etc. Due to the inherent time-consuming nature, it is impractical to run a 1-D flame code with trial-and-error methods for model reduction, especially when starting with a large chemical kinetic model. In this paper, an improved reduction methodology is proposed for construction of a small set of species that give accurate predictions of both flame speeds and ignition delays. First, a strong correlation is found between the errors of maximum H radical and the errors in prediction of laminar flame speeds. Addition of H to the search targets in graph-based methods is conducted showing improvement in accuracy of flame speed prediction. Second, the normalized flame speed sensitivity with rate constants is analyzed for identifying a set of species that strongly influences the prediction of flame speeds. Finally, a trial-and-error based method is used for further reduction with a 0-D testbed for prediction of ignition only, while keeping the species important to flame chemistry. The newly proposed reduction methodology is used for development of accurate skeletal models predicting both ignition and flame speeds for several hydrocarbon fuels. These skeletal models include methane (27 species), propane (32 species), n-heptane (126 species), and primary reference fuel gasoline surrogates (207 species) with high fidelity to be used in engine simulations.

## Processing Notes

- extracted S0010218017304637_mmc1.zip
