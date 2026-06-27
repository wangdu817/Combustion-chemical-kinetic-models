# LT-HyChem - A physics-based chemical kinetic modeling approach for low-temperature oxidation of real fuels I: Rationale, methodology, and application to a simple fuel mixture

## Bibliography

Rishav Choudhary, Pujan Biswas, Vivek Boddapati, Hai Wang, Ronald K. Hanson. LT-HyChem - A physics-based chemical kinetic modeling approach for low-temperature oxidation of real fuels I: Rationale, methodology, and application to a simple fuel mixture[J]. Combustion and Flame, 2025, 271: 113852. DOI: 10.1016/j.combustflame.2024.113852.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 271 / January
- Article number: 113852
- DOI: 10.1016/j.combustflame.2024.113852
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024005613
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218024005613/pdfft?md5=d3003ea1184e715c12b097c1029471b4&pid=1-s2.0-S0010218024005613-main.pdf
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218024005613_mmc1/mmc3.yaml, _processing/extracted/s0010218024005613_mmc1/mmc1.cti, _processing/extracted/s0010218024005613_mmc1/mmc2.inp
- Original thermodynamic source files: _processing/extracted/s0010218024005613_mmc1/mmc4.dat, _processing/extracted/s0010218024005613_mmc1/mmc3.yaml, _processing/extracted/s0010218024005613_mmc1/mmc1.cti
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 138
- Reaction count: 895
- Message: CanteraError: ******************************************************************************* CanteraError thrown by newSolution: The CTI and XML formats are no longer supported. *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 2

- Status: cantera_failed
- Species count: 138
- Reaction count: 895
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by Reaction::checkBalance: Error on line 1600 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/unknown_fuel/2025/choudhary_2025_unknown_fuel_113852/mechanism.yaml: The following reaction is unbalanced: GSC7H14OOHO2 => 0.0741833 C2H4 + 0.0968092 C3H6 + 0.0109643 C4H81 + 0.0931942 C6H5CH3 + 0.00349031 C6H6 + 0.0503571 CH2CO + 0.503571 CH2O + 2.44154 CH3 + 0.239196 CH3CHO + 0.214018 CH3COCH3 + 1.34286 CO + GSC7H14OOHO2 + 0.5 H + 0.225 HO2 + 1.2 OH + 0.0837307 iC4H8 Element Reactants Products C 7 14.000000296000001 H 15 30.00000124 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 3

- Status: ok
- Species count: 138
- Reaction count: 895
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

The diversity of reactivities, intermediates, and pathways associated with the low-temperature (low-T) oxidation of various component classes that constitute real fuels is perhaps the most challenging aspect of modeling their combustion chemistry. Unlike high-temperature oxidation (T > 1100 K), where the combustion properties of multicomponent fuels are relatively insensitive to compositional variations, reactions governing low-T oxidation exhibit pronounced sensitivity to fuel composition. Despite the fuel specificity, intermediate formation during low-T oxidation exhibits characteristic behaviors. Combining such observations and the already mature Hybrid Chemistry (HyChem) methodology for high-temperature oxidation of real fuels [1], we propose a framework to develop simplified, physics-based chemical kinetic models for low-T oxidation of real fuels. The proposed model captures the complexity of low-T oxidation through concise, fuel-specific reactions whose stoichiometric parameters and rate constants are experimentally constrained. Shock tube experiments needed for constraining model parameters are identified and plausible validation targets are discussed. The present paper outlines the model's description, its underlying physical principles, and an initial application to a simple, multi-component mixture, TPRF-60. Detailed uncertainty analyses and application to three real fuels will be presented in a companion paper.

## Processing Notes

- extracted S0010218024005613_mmc1.zip
