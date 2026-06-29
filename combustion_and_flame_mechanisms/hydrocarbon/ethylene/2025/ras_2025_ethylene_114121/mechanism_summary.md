# A fundamental investigation of the pyrolysis chemistry of Oxymethylene Ethers. Part I: Quantum chemical calculations and kinetic model development

## Bibliography

Kevin De Ras, Olivier Herbinet, Frédérique Battin-Leclerc, Yann Fenard, ... Kevin M. Van Geem. A fundamental investigation of the pyrolysis chemistry of Oxymethylene Ethers. Part I: Quantum chemical calculations and kinetic model development[J]. Combustion and Flame, 2025, 275: 114121. DOI: 10.1016/j.combustflame.2025.114121.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 275 / May
- Article number: 114121
- DOI: 10.1016/j.combustflame.2025.114121
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025001592
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025001592/pdfft?md5=3fbaf7bbf8ee050503426dc13becf7eb&pid=1-s2.0-S0010218025001592-main.pdf
- Fuel type: ethylene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218025001592_mmc1/KineticModel.inp
- Original thermodynamic source files: _processing/extracted/s0010218025001592_mmc1/KineticModel.inp
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 398
- Reaction count: 6384
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 4475 and 12395 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ethylene/2025/ras_2025_ethylene_114121/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 <=> O + OH Reaction 3193: H + O2 <=> O + OH | Line | | 4470 | - [26.9555951, 0.0361205599, -1.46000681e-05, 2.43012418e-09, | 4471 | -1.4098528e-13, -7.49798658e+04, -108.453726] | 4472 | note: "!\tInChI=1S/C6H12O5/c1-7-3-9-5-11-6-10-4-8-2/h1H,3-6H2,2H3" | 4473 | | 4474 | reactions: > 4475 > - equation: H + O2 <=> O + OH # Reaction 1 ^ | 4476 | rate-constant: {A: 1.04e+14, b: 0.0, Ea: 1.5286e+04} | 4477 | note: | | 4478 | RE ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Oxymethylene ethers (OMEs) have emerged as a promising and sustainable alternative for fossil-based fuels in recent years. This class of synthetic fuels can be produced from captured CO2 with renewable electricity, so-called e-fuels, using carbon capture and utilization technology resulting in environmentally cleaner combustion. However, before OMEs can be used globally, it is essential to have a thorough understanding of their radical decomposition chemistry. In this study, combined experimental and kinetic modeling work is conducted to unravel the pyrolysis chemistry of oxymethylene ether-3 (OME-3), oxymethylene ether-4 (OME-4), and oxymethylene ether-5 (OME-5). A detailed kinetic model for pyrolysis of these long-chain OMEs with elementary reaction steps is developed based on first principles with the automatic kinetic model generation tool ‘Genesys’. The unimolecular decomposition pathways are explored by constructing potential energy surfaces, which highlight the importance of formaldehyde elimination reactions. In addition, rate rules are regressed for the unimolecular decomposition reactions of radicals, based on the quantum chemical results, to enable extrapolation of the kinetic data. The developed kinetic model is validated using experimental datasets from the literature, and benchmarking against other pyrolysis models demonstrates better predictive performance. The experimental observations are accurately predicted, on average within the uncertainty margin (∼10 mol% relative) for major compounds, without fitting model parameters. Part II of this study presents six newly acquired experimental datasets from jet-stirred and tubular reactors, additional kinetic model validation, and a comprehensive model analysis through rate of production and sensitivity analyses.

## Processing Notes

- extracted S0010218025001592_mmc1.zip
- extracted S0010218025001592_mmc4.zip
- extracted S0010218025001592_mmc3.zip
- extracted S0010218025001592_mmc6.docx
- extracted S0010218025001592_mmc2.zip
- extracted S0010218025001592_mmc5.docx
