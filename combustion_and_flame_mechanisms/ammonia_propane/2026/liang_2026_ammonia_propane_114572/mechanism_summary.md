# Experimental and kinetic insight on auto-ignition process of ammonia/propane mixture: Focus on oxygen effect

## Bibliography

Yueying Liang, Zimu Wang, Liang Yu, Xingcai Lu. Experimental and kinetic insight on auto-ignition process of ammonia/propane mixture: Focus on oxygen effect[J]. Combustion and Flame, 2026, 283: 114572. DOI: 10.1016/j.combustflame.2025.114572.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 283 / January
- Article number: 114572
- DOI: 10.1016/j.combustflame.2025.114572
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025006091
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ammonia_propane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218025006091_mmc3/Mech.inp
- Original thermodynamic source files: _processing/extracted/s0010218025006091_mmc3/Mech.inp
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 612
- Reaction count: 6668
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 6564 and 24117 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ammonia_propane/2026/liang_2026_ammonia_propane_114572/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H2 + M <=> 2 H + M Reaction 3335: H2 + M <=> 2 H + M | Line | | 6559 | - [4.16893487, 6.17767838e-03, -2.35286422e-06, 3.24605288e-10, | 6560 | -8.03245562e-15, -1.59903892e+04, 3.07758328] | 6561 | note: '\COMMENT:' | 6562 | | 6563 | reactions: > 6564 > - equation: H2 + M <=> 2 H + M # Reaction 1 ^ | 6565 | type: three-body | 6566 | rate-constant: {A: 4.577e+19, b: -1.4, Ea: 1.044e+05} | 6567 | efficiencies: {H2: 2 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Propane is a major component of liquefied petroleum gas. Ignition delay times of NH3/C3H8 mixtures were measured in a rapid compression machine over 750–1100 K and 20–100 bar, with propane blending ratios from 10 % to 100 %. A new kinetic model, SJTU-2025, was developed based on POLIMI-2023 and Aramco 3.0 model. The model shows good agreement with IDTs, particularly at high dilution ratios. The model also improves speciation predictions for O2, H2, CO2, C2H2, C3H6, and C3H8. A plateau in simulated mole fractions of O2, NH3, and N2 is observed within 900–1000 K, partially consistent with experimental trends. The NTC trend of oxygen should result from the competition between NC3H7/IC3H7+O2HO2+C3H6 and NC3H7/IC3H7+O2NC3H7O2/IC3H7O2. The effect of propane addition is pronounced at high ammonia proportions, and small propane fraction is suggested because HCN is prone to being produced at high propane content. A new parameter, the O2-IDT ratio, reveals the oxygen effect on IDTs over wide conditions. The reason for the pronounced oxygen effect at low temperature is that oxygen participates actively in the R·→RO2· and C3H7O2=C3H6+HO2 pathways, which are dominant at low temperatures. An important chain-terminating reaction, 2HO2H2O2+O2, gains importance at reduced oxygen concentration, further decreasing the reactivity of the fuel mixtures. The model considers reactions between peroxy radicals C3H7O2 and NH3/NH2, which improve the model predictive ability in IDTs at NTC region and oxygen concentration profile. The source of these kinds of reactions comes from analogy to CH3OCH2O2+NH3/NH2 reactions, and large uncertainty exists in the determination of the rate constants. More accurate kinetic parameters are imperative to improve model performance in the low-temperature region.

## Processing Notes

- extracted S0010218025006091_mmc2.xlsx
- extracted S0010218025006091_mmc1.docx
- extracted S0010218025006091_mmc3.zip
