# Understanding the moderate-temperature oxidation of 3-ethyltoluene and 3-n-propyltoluene in presence of n-heptane

## Bibliography

S. Hossain, M. Abdulrahman, P.T. Lynch, Eric K. Mayhew, K. Brezinsky. Understanding the moderate-temperature oxidation of 3-ethyltoluene and 3-n-propyltoluene in presence of n-heptane[J]. Combustion and Flame, 2026, 285: 114776. DOI: 10.1016/j.combustflame.2026.114776.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 285 / March
- Article number: 114776
- DOI: 10.1016/j.combustflame.2026.114776
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026000131
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: n_heptane_toluene_3_ethyltoluene_3_n_propyltoluene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218026000131_mmc2/mmc2.yaml, _processing/extracted/s0010218026000131_mmc1/mmc1.yaml
- Original thermodynamic source files: _processing/extracted/s0010218026000131_mmc2/mmc2.yaml, _processing/extracted/s0010218026000131_mmc1/mmc1.yaml
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: ok
- Species count: 647
- Reaction count: 18629
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 2

- Status: cantera_failed
- Species count: 647
- Reaction count: 18629
- Message: CanteraError: ******************************************************************************* InputFileError thrown by AnyMap::fromYamlFile: Error on line 0 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/n_heptane_toluene_3_ethyltoluene_3_n_propyltoluene/2026/hossain_2026_n_heptane_toluene_3_ethyltoluene_3_n_propyltoluene_114776/mechanism.yaml: bad conversion | Line | *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

3-Ethyltoluene (ET) and 3-n-propyltoluene (PT) are key aromatic constituents of Virent’s synthetic aromatic kerosene (SAK), necessitating detailed understanding of their oxidation chemistry for surrogate fuel development. This study investigates the high-pressure oxidation behavior of n-heptane/ET (HET) and n-heptane/PT (HPT) blends through single-pulse shock tube experiments conducted at 50 atm, with a residence time range of 12-14 ms, and temperatures ranging from 800–1400 K. Experiments were performed across equivalence ratios φ = 0.5, 1.0, and 2.0 to capture lean, stoichiometric, and rich combustion regimes. Post-shock gases were analyzed using gas chromatography, providing speciation data for ∼30 products, including H₂, CO, CO₂, CH₄, C₂H₄, C₃H₆, CH₂O, benzene, toluene, and methylstyrene. The CRECK_ET_Theory mechanism (incorporating literature ET submodel) and CRECK_PT_Theory mechanism (developed by integrating PT decomposition chemistry) were used for kinetic modeling with Cantera, showing good agreement with experimental trends across all φ. Both mechanisms include ab initio rate calculations for key hydrogen abstraction reactions, improving the fidelity of fuel-specific pathways. Rate-of-production and sensitivity analyses revealed distinct oxidation behaviors driven by alkyl side-chain structure. ET oxidation was dominated by OH abstraction at the α-CH₂ site, especially under lean conditions, whereas PT exhibited enhanced reactivity under rich conditions due to faster unimolecular decomposition and a lower activation barrier for H-abstraction by H atoms, particularly at the benzylic and β-CH₂ positions. Neither ET nor PT suppressed n-heptane oxidation, in contrast to the radical-scavenging effects previously observed for 1,2,4-trimethylbenzene (TMB124). This study provides the first detailed oxidation dataset for ET and PT under engine-relevant conditions and delivers validated kinetic mechanisms essential for constructing accurate multi-component surrogates for SAK. The insights into structure–reactivity relationships offer a mechanistic foundation for predictive combustion modeling of synthetic fuels in propulsion applications.

## Processing Notes

- extracted S0010218026000131_mmc3.docx
- extracted S0010218026000131_mmc2.zip
- extracted S0010218026000131_mmc1.zip
