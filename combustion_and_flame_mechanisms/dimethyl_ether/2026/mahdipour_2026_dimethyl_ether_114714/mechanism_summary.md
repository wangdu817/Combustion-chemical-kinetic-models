# Assessment of conditional source-term estimation (CSE) with direct chemistry integration including detailed and reduced kinetics for the simulation of a turbulent DME flame

## Bibliography

Amir H. Mahdipour, Fekadu Mosisa Wako, Cécile Devaud, W. Kendal Bushe. Assessment of conditional source-term estimation (CSE) with direct chemistry integration including detailed and reduced kinetics for the simulation of a turbulent DME flame[J]. Combustion and Flame, 2026, 285: 114714. DOI: 10.1016/j.combustflame.2025.114714.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 285 / March
- Article number: 114714
- DOI: 10.1016/j.combustflame.2025.114714
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025007497
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025007497/pdfft?md5=458f4982b7e1b849dd602a39c7cbf75c&pid=1-s2.0-S0010218025007497-main.pdf
- Fuel type: dimethyl_ether
- Plasma-related mechanism: no
- Validation reactor/type from abstract: laminar flame speed

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing\extracted\s0010218025007497_mmc1\DME_reduced_CK_input
- Original thermodynamic source files: _processing\extracted\s0010218025007497_mmc1\DME_reduced_CK_input
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 61
- Reaction count: 126
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 241 and 405 of E:\mech_collection\combustion_and_flame_mechanisms\dimethyl_ether\2026\mahdipour_2026_dimethyl_ether_114714\mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H + O2 <=> O + OH Reaction 64: H + O2 <=> O + OH | Line | | 236 | -1.123918e+04, 14.43229] | 237 | - [4.825938, 0.01384043, -4.557259e-06, 6.724967e-10, | 238 | -3.598161e-14, -1.271779e+04, -5.239507] | 239 | | 240 | reactions: > 241 > - equation: H + O2 <=> O + OH # Reaction 1 ^ | 242 | rate-constant: {A: 3.5470000000000005e+15, b: -0.406, Ea: 1.6599e+04} | 243 | - equation: H2 + O <=> H + OH # Reaction 2 | 244 | rate-constant: {A: 5.080000000 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

This study presents a numerical investigation of conditional source-term estimation (CSE) with direct integration of chemical kinetics, applied to one turbulent DME jet flame. This new CSE framework eliminates the need for pre-tabulated chemistry, therefore greater flexibility and accuracy are added when more complex fuels are considered. Two chemical mechanisms are considered: a detailed mechanism with 42 species and a tailored 21-species reduced mechanism. Both simulations are evaluated against a comprehensive experimental dataset including temperature and species concentration fields. Results show that simulations using both mechanisms yield nearly identical predictions for major scalars, with only minor differences observed in the conditional and Favre-averaged profiles. Discrepancies in peak temperature and species concentrations correlate with local deviations in predicted mixing statistics. While the detailed mechanism increases computational cost by nearly tenfold, the reduced mechanism retains accuracy at a fraction of the expense. These findings confirm that direct chemistry integration CSE, when combined with an optimized skeletal mechanism, offers an accurate and computationally efficient approach for modeling DME combustion in turbulent flows. Novelty and significance statement This study includes two novel components. One is focused on the assessment of a recent conditional source-term estimation (CSE) formulation with direct chemistry integration, in principle, capable of dealing with any chemical kinetics, without pre-tabulated chemistry. For the first time, this method is applied to the simulation of a turbulent flame burning DME with two different chemical mechanisms including over 20 species. A suitable stiff solver is added. A rigorous analysis is performed using experimental data. The second novelty is the derivation of a new reduced mechanism for DME, consisting of only 21 species, thoroughly validated over a range of combustion conditions for laminar flame speeds, species concentrations and ignition delays, and included in the CSE turbulent flame simulations, with excellent performance. This study, including direct chemistry integration CSE and optimized skeletal DME kinetics, provides significant contributions towards the advancement of accurate and efficient combustion simulation tools for industry-relevant conditions.

## Processing Notes

- none
