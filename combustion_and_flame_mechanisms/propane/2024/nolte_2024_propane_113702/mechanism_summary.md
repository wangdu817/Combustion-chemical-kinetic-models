# Kinetic insights into double-branched acyclic ether: Methyl tert-butyl ether and 2,2-dimethoxypropane

## Bibliography

Adrian Nolte, Malte Döntgen, Karl Alexander Heufer. Kinetic insights into double-branched acyclic ether: Methyl tert-butyl ether and 2,2-dimethoxypropane[J]. Combustion and Flame, 2024, 269: 113702. DOI: 10.1016/j.combustflame.2024.113702.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 269 / November
- Article number: 113702
- DOI: 10.1016/j.combustflame.2024.113702
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024004115
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: propane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218024004115_mmc1/MTBE_DMP_HGD_mech.cti, _processing/extracted/s0010218024004115_mmc1/MTBE_DMP_HGD_mech.inp
- Original thermodynamic source files: _processing/extracted/s0010218024004115_mmc1/MTBE_DMP_HGD_therm.dat, _processing/extracted/s0010218024004115_mmc1/MTBE_DMP_HGD_mech.cti
- Original transport source files: _processing/extracted/s0010218024004115_mmc1/MTBE_DMP_HGD_mech.cti, _processing/extracted/s0010218024004115_mmc1/MTBE_DMP_HGD_tran.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: CanteraError: ******************************************************************************* CanteraError thrown by newSolution: The CTI and XML formats are no longer supported. *******************************************************************************
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'CH2CCH2OH' Ignoring redundant declaration for species 'IC4H7' Ignoring redundant declaration for species 'IC4H7O' Ignoring redundant declaration for species 'TC3H6CHO' Error while reading reaction in chem.inp starting on line 9556: """ MTBE2KET1OOH1OOH=>OH+CH2O+C3KET21+HCO 2.00E+16 0 3.90E+04 ___________________________________________________________________________________________________________ """ Unparsable line: '___________________________________________________________________________________________________________'. Ignoring duplicate transport data for species "AR" on line 3773 of "tran.dat". Ignoring duplicate transport data for species "N2" on line 3774 of "tran.dat". Ignoring duplicate transport data for species "HE" o ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

This study presents the first kinetic mechanism for methyl tert-butyl ether (MTBE) containing low-temperature chemistry, as well as the first mechanism for 2,2-dimethoxypropane (DMP). The mechanisms have been validated against ignition delay time experiments conducted in a high-pressure shock tube and rapid compression machine. The rapid compression machine conditions were set to 20 and 40 bar for MTBE, and 10 and 20 bar for DMP in a temperature range of 584 to 946 K. Shock tube experiments have been performed for DMP at 20 and 40 bar for stoichiometric and fuel-lean conditions in air at temperatures ranging from 913 to 1173 K. A pronounced negative temperature coefficient regime with two-stage ignition has been observed for both fuels. The developed mechanism consists of reaction rate constants that were primarily modeled in analogy to iso-octane and dimethoxymethane, and calculated thermodata on the G4//B3LYP-D3BJ/def2-TZVP level of theory. Simulations have been performed to analyze the fuel oxidation at different temperatures. Over the full temperature range, H-atom abstraction occurs mainly on the α -side for DMP and on the β -side for MTBE. At low temperatures, both fuels isomerize to the peroxy radical. The dominant MTBE radicals then tend to produce cyclic ether, while the DMP radicals react with O 2 , enabling significant chain branching and explaining the higher reactivity of DMP. With rising temperature, β -scission of the fuel radicals and unimolecular elimination reactions start to dominate the oxidation process. Novelty and Significance Statement The novelty of this research is the first observation of a two-stage ignition of methyl-tert butyl ether (MTBE) in an RCM and a discussion of its fundamental ignition chemistry, which is based on a developed detailed kinetic mechanism. In addition, 2,2-dimethoxypropane (DMP) has been investigated experimentally and theoretically to explain the difference in reactivity to MTBE despite their strong molecular similarity. The experiments include RCM and shock tube experiments. The kinetic model is based on rate constant analogies and newly calculated thermo data on the G4//B3LYP-D3BJ/def2-TZVP level of theory. This work is significant, as MTBE is still a widely used octane booster and the developed model could help to improve engine simulations. Furthermore, the findings of DMP provide insights into future fuel design.

## Processing Notes

- extracted S0010218024004115_mmc1.zip
