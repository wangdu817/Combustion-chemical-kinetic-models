# Revealing the critical role of radical-involved pathways in high temperature cyclopentanone pyrolysis

## Bibliography

Xiaorui Dong, Erik Ninnemann, Duminda S. Ranasinghe, Andrew Laich, Robert Greene, Subith S. Vasu, et al.. Revealing the critical role of radical-involved pathways in high temperature cyclopentanone pyrolysis[J]. Combustion and Flame, 2020, 216: 280-292. DOI: 10.1016/j.combustflame.2020.03.001.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 216 / Jun
- Article number: 280-292
- DOI: 10.1016/j.combustflame.2020.03.001
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218020300961
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: cyclopentanone
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: not available
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218020300961_mmc3/chem.inp, _processing/extracted/s0010218020300961_mmc2/mmc2/rate.inp
- Original thermodynamic source files: not found
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 821
- Reaction count: 79859
- Message: InputError: Error while reading reaction in chem.inp starting on line 441: """ CPO <=> CO + C2H4 + C2H4 2.429e+14 0.614 81.219 """ Unexpected token 'CO+' in reaction expression 'CPO<=>CO+C2H4+C2H4'. May be due to undeclared species 'CO'. No thermo data found for species 'CPO' No thermo data found for species 'H' No thermo data found for species 'RO' No thermo data found for species 'aOH' No thermo data found for species 'bOH' No thermo data found for species 'enol' No thermo data found for species 'CH3RO' No thermo data found for species 'bCH3ROH' No thermo data found for species 'CH3ORJ' No thermo data found for species 'CH3ORD' No thermo data found for species 'aCPO' No thermo data found for species 'CH3' No thermo data found for species 'C2H4' No thermo data found for species 'CeqCeqC' ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: not available
- Standard tran.dat: not available

### Mechanism 2

- Status: ok
- Species count: 821
- Reaction count: 79859
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: not available
- Standard tran.dat: not available

## Abstract

Cyclopentanone (CPO) is a promising biofuel for spark-ignition engines due to its ring strain and high auto-ignition resistance. Understanding CPO decomposition is crucial for building a high-temperature combustion model. Here we present a comprehensive kinetic model for high-temperature pyrolysis of CPO with verified results from high-pressure shock tube (HPST) measurements. The time-histories of carbon monoxide (CO), ethylene (C2H4), and CPO absorbances over the temperature range of 1156–1416 K and pressure range of 8.53–10.06 atm were measured during current experiments. A corresponding detailed kinetic model was generated using the Reaction Mechanism Generator (RMG) with dominant unimolecular/radical-involved decomposition pathways from either previous studies or quantum calculations within the current work. The obtained model containing 821 species and 79,859 reactions exhibited a good agreement with the experimental results. In this study, the absorbance ratio between C2H4 and CO was used as an important factor to validate models and to prove that radical-involved bimolecular pathways were as significant as unimolecular decomposition of CPO. The rate of production (ROP) analysis showed H radicals play a major role in the decomposition, and the whole decomposition process could be divided into three stages based on the H radical concentration. The insights from present work can be used to generate a better CPO combustion model and help evaluate CPO as an advanced biofuel.

## Processing Notes

- extracted S0010218020300961_mmc2.zip
- extracted S0010218020300961_mmc3.zip
