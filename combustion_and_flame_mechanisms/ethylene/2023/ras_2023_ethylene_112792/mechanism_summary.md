# An experimental and kinetic modeling study on the low-temperature oxidation of oxymethylene ether-2 (OME-2) by means of stabilized cool flames

## Bibliography

Kevin De Ras, Thomas Panaget, Yann Fenard, Jeroen Aerssens, Laure Pillier, Joris W. Thybaut, et al.. An experimental and kinetic modeling study on the low-temperature oxidation of oxymethylene ether-2 (OME-2) by means of stabilized cool flames[J]. Combustion and Flame, 2023, 253: 112792. DOI: 10.1016/j.combustflame.2023.112792.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 253 / July
- Article number: 112792
- DOI: 10.1016/j.combustflame.2023.112792
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023001761
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ethylene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218023001761_mmc1/mmc1.inp
- Original thermodynamic source files: _processing/extracted/s0010218023001761_mmc1/mmc1.inp
- Original transport source files: _processing/extracted/s0010218023001761_mmc5/mmc5.inp

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 376
- Reaction count: 7976
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 6906 and 15472 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ethylene/2023/ras_2023_ethylene_112792/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 <=> O + OH Reaction 3989: H + O2 <=> O + OH | Line | | 6901 | rotational-relaxation: 1.0 | 6902 | note: '! InChI=1S/CHO3/c2-1(3)4/h(H,2,3)' | 6903 | note: "!\tInChI=1S/CHO3/c2-1(3)4/h(H,2,3)" | 6904 | | 6905 | reactions: > 6906 > - equation: H + O2 <=> O + OH # Reaction 1 ^ | 6907 | rate-constant: {A: 1.04e+14, b: 0.0, Ea: 1.5286e+04} | 6908 | - equation: O + H2 <=> H + OH # Reaction 2 | 6909 | rate-constant: {A: 5.08e+04, b ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Oxymethylene ethers have received much attention in recent years as a high-potential alternative for fossil-based fuels. These alternative fuels produced via carbon capture and utilization technologies driven by renewable energy can contribute to the solution of environmental issues in the short term. In this study, the low-temperature oxidation chemistry of oxymethylene ether-2 was investigated by combining experimental and kinetic modeling work. New experimental data were acquired from stabilized, ozone-seeded oxymethylene ether-2/dimethyl ether/oxygen premixed cool flames in a heated stagnation plate burner. Two fuel-lean equivalence ratios were investigated, i.e., ϕ = 0.3 and ϕ = 0.5. The observed and quantified reaction products were methoxymethyl formate, methyl formate, methanol, formaldehyde, CO and CO2. A new detailed kinetic model based on first principles was constructed for the pyrolysis and oxidation of oxymethylene ether-2 with the in-house developed automatic kinetic model generation code Genesys. Compared to an earlier study by De Ras et al. (Combustion and Flame, 2022), additional species and reactions were added to describe the low-temperature oxidation chemistry with more detail, in addition to an update of several thermodynamic and kinetic parameters based on new quantum chemical calculations. The newly developed kinetic model is able to predict the experimental observations of the stabilized cool flames satisfactorily and can reproduce ignition delay times from the literature on average within the experimental uncertainty margin. Rate of production and sensitivity analyses were performed for different reaction conditions to unravel the important decomposition pathways during low-temperature oxidation. It is concluded that oxymethylene ether-2 is a highly reactive fuel, and this without fuel-specific chain branching reactions significantly contributing to the low-temperature oxidation chemistry.

## Processing Notes

- extracted S0010218023001761_mmc3.docx
- extracted S0010218023001761_mmc2.docx
- extracted S0010218023001761_mmc1.zip
- extracted S0010218023001761_mmc4.xlsx
- extracted S0010218023001761_mmc5.zip
