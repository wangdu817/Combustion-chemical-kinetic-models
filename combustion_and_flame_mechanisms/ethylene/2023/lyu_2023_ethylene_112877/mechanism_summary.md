# A detailed chemical kinetic mechanism of 1,1-diamino-2,2-dinitroethylene (FOX-7) initial decomposition in the gas phase

## Bibliography

Jie-Yao Lyu, Qiren Zhu, Xin Bai, Xuan Ren, Jing Li, Dongping Chen, et al.. A detailed chemical kinetic mechanism of 1,1-diamino-2,2-dinitroethylene (FOX-7) initial decomposition in the gas phase[J]. Combustion and Flame, 2023, 255: 112877. DOI: 10.1016/j.combustflame.2023.112877.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 255 / September
- Article number: 112877
- DOI: 10.1016/j.combustflame.2023.112877
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023002584
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ethylene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218023002584_mmc2/FOX-7.inp
- Original thermodynamic source files: _processing/extracted/s0010218023002584_mmc2/FOX-7.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 38
- Reaction count: 131
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by PlogRate::validate: Error on line 428 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ethylene/2023/lyu_2023_ethylene_112877/mechanism.yaml: Invalid rate coefficient for reaction 'FOX-7 <=> P5d' at P = 1013.3, T = 300.0 at P = 1013.3, T = 500.0 at P = 1013.3, T = 1000.0 at P = 1013.3, T = 2000.0 at P = 1013.3, T = 5000.0 at P = 1013.3, T = 10000.0 at P = 10133, T = 300.0 at P = 10133, T = 500.0 at P = 10133, T = 1000.0 at P = 10133, T = 2000.0 at P = 10133, T = 5000.0 at P = 10133, T = 10000.0 at P = 1.0132e+05, T = 300.0 a ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

1,1-Diamino-2,2-dinitroethylene (FOX-7 or DADNE) is a promising ingredient of the low-vulnerability propellants. However, one of the major concerns in its further development and applications is the lack of detailed kinetic mechanism for its initial decomposition in the gas phase. In this study, a detailed chemical kinetic mechanism consisting of 38 species and 131 reactions was developed to describe the initial decomposition process of FOX-7. At first, a comprehensive reaction network was established with the aid of reactive molecular dynamics (MD) simulation. Then, the potential energy surfaces (PES) for both unimolecular and bimolecular reactions were identified at the QCISD(T)/CBS//M062X/6-311++G(d,p) level of theory. The rate coefficients were obtained by solving RRKM/ME, and the thermochemical properties of relevant species were calculated at CBS-APNO/G3/G4 levels with the atomization method. Finally, these kinetic and thermochemistry data were processed into a kinetic mechanism and used to simulate the initial decomposition process of FOX-7. The results demonstrated that the H-atom transfer to the beta carbon atom (enamino-imino isomerization) followed by the nitro group elimination dominates the initial decomposition, and the reaction FOX-7 = R3a + NO2 becomes the most significant one under high temperatures (Channel C3). Besides, bimolecular reactions also play a role as the decomposition goes on. Overall, this work provides quantitative predictions of the reaction pathways of gas-phase FOX-7 initial decomposition, and it would serve as a solid foundation for the development of a fully detailed combustion kinetic mechanism for FOX-7.

## Processing Notes

- extracted S0010218023002584_mmc1.docx
- extracted S0010218023002584_mmc2.zip
