# Reduced kinetic mechanisms of diesel fuel surrogate for engine CFD simulations

## Bibliography

Alessio Frassoldati, Gianluca D'Errico, Tommaso Lucchini, Alessandro Stagni, Alberto Cuoci, Tiziano Faravelli, et al.. Reduced kinetic mechanisms of diesel fuel surrogate for engine CFD simulations[J]. Combustion and Flame, 2015, 162: 3991-4007. DOI: 10.1016/j.combustflame.2015.07.039.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 162 / Oct
- Article number: 3991-4007
- DOI: 10.1016/j.combustflame.2015.07.039
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218015002473
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: diesel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: laminar flame speed, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218015002473_mmc2/mmc2.CKI
- Original thermodynamic source files: _processing/extracted/s0010218015002473_mmc2/mmc3.CKT
- Original transport source files: _processing/extracted/s0010218015002473_mmc2/mmc4.TRC

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 133
- Reaction count: 2275
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Detailed chemistry represents a fundamental pre-requisite for a realistic simulation of combustion process in diesel engines. In this work, the authors developed a reduced mechanism for n-dodecane starting from the comprehensive POLIMI_TOT_1407 kinetic mechanism, already well validated and tested in a wide range of operating conditions. This reduced mechanism (96 species and 993 reactions) is able to accurately describe the high and low-temperature reactivity of n-dodecane in a wide range of conditions. This kinetic scheme has been extended to soot precursors by adding a relatively small sub-mechanism (37 species and 1282 reactions). This work extensively validates this reduced kinetic scheme, together with similar skeletal mechanisms from the literature, using experimental data in a wide range of conditions, including flow and stirred reactors experiments, autoignition delay times, laminar flame speeds, and autoignition of isolated fuel droplets in microgravity conditions. These kinetic mechanisms were then applied to diesel spray combustion modeling. The simulations were performed by using the MRIF (Multiple Representative Interactive Flamelets) model implemented in the Lib-ICE code. Comparisons to measured flame-lift off and ignition delays of the ECN (Engine Combustion Network) database at different operating conditions are discussed. Even if all the kinetic mechanisms reasonably describe the ignition and combustion in ideal reactors and laminar flames and capture the important characteristics of spray ignition processes, relevant differences exist and are discussed in this work.

## Processing Notes

- extracted S0010218015002473_mmc2.zip
