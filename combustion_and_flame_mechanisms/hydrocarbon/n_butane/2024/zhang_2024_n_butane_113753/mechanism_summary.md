# Oxidation of butane-2,3-dione at high pressure: Implications for ketene chemistry

## Bibliography

Xiaoyuan Zhang, Maxence Lailliau, Yuyang Li, Yumeng Zhu, Zehua Feng, Wei Li, et al.. Oxidation of butane-2,3-dione at high pressure: Implications for ketene chemistry[J]. Combustion and Flame, 2024, 270: 113753. DOI: 10.1016/j.combustflame.2024.113753.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 270 / December
- Article number: 113753
- DOI: 10.1016/j.combustflame.2024.113753
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024004620
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: n_butane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218024004620_mmc3/SMM3_kinetics.inp
- Original thermodynamic source files: _processing/extracted/s0010218024004620_mmc4/SMM4_Thermo.dat
- Original transport source files: _processing/extracted/s0010218024004620_mmc5/SMM5_Transport data.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 4634: """ A1- (+M) =o-C6H4+H (+M) 4.300E+12 0.616 77313 ! RRKM 00-HAI-FRE validated by shock tube pyrolysis of A1 (Laskin 1996) LOW/ 1.000E+84 -18.866 90064 / ! 20130218 TROE/ 0.902, 696. 358. 3856. / H2/2.0/ H2O/6.0/ CH4/2.0/ CO/1.5/ CO2/2.0/ """ could not convert string to float: '0.902,' Ignoring redundant thermo data for species 'SC4H9' starting on line 451 of therm.dat. Ignoring redundant thermo data for species 'N2' starting on line 668 of therm.dat. Ignoring redundant thermo data for species 'N2' starting on line 675 of therm.dat. Ignoring redundant thermo data for species 'AR' starting on line 679 of therm.dat. Error while reading thermo entry in therm.dat starting on line 680: """ HE+ L10/90HE+ 1 0 0 0G 200.000 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Ketene (CH2CO) mechanism is a building block for developing combustion kinetic models of practical fuels. To revisit the combustion chemistry related to ketene, oxidation experiments of butane-2,3‑dione (diacetyl, CH3COCOCH3), considered as an effective precursor of CH2CO, are conducted in a jet-stirred reactor (JSR) at 10 bar and temperatures ranging from 650 to 1160 K. Identification and quantification of intermediates are achieved by Fourier transform infrared spectrometry, gas chromatography, and mass spectrometry. A kinetic model of diacetyl is constructed based on recent theoretical and modeling studies on diacetyl and ketene, which has been validated against the present data and experimental data of diacetyl and CH2CO in literature. Generally, the present model can adequately predict most of them, and better predict the methyl-related intermediates under wide pyrolysis and combustion conditions than previous models. Based on modeling analyses, the unimolecular decomposition reaction of diacetyl is the dominant reaction pathway for fuel consumption under different equivalence ratio conditions, especially at high temperatures. Under lean conditions, both the H-atom abstraction reactions by methyl (i.e. CH3COCOCH3 + CH3 = CH4 + CH2CO + CH3CO, R3) and by OH (i.e. CH3COCOCH3 + OH = H2O + CH2CO + CH3CO, R5) are important for diacetyl consumption, while under rich conditions R5 becomes negligible. As the most important intermediates in diacetyl oxidation, the main consumption pathways of CH2CO and CH3 are dependent on the equivalence ratio conditions. Under lean conditions, CH2CO mainly reacts with OH to produce CH2OH and CO (i.e. CH2CO + OH = CH2OH + CO, R10), while methyl reacts with HO2 to produce CH3O and OH (i.e. CH3 + HO2 = CH3O + OH, R20). In contrast, under rich conditions, the addition-elimination reaction between CH2CO and H becomes competitive with R10, while the CH3 self-combination producing C2H6 plays a more important role than the CH3 oxidation pathway R20. Sensitivity analysis of CH2CO shows that not only the reactions of CH2CO, but also those of CH3 are sensitive to CH2CO formation. This is because CH3 related reactions influence the distribution of radical pool, which determines the oxidation reactivity of the reaction system.

## Processing Notes

- extracted S0010218024004620_mmc2.xlsx
- extracted S0010218024004620_mmc3.zip
- extracted S0010218024004620_mmc4.zip
- extracted S0010218024004620_mmc5.zip
