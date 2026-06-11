# Understanding the formation of nitrogen-containing products in pyrrole pyrolysis

## Bibliography

Jibiao Xie, Jundie Chen, Alexander A. Konnov. Understanding the formation of nitrogen-containing products in pyrrole pyrolysis[J]. Combustion and Flame, 2026, 289: 115037. DOI: 10.1016/j.combustflame.2026.115037.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 289 / July
- Article number: 115037
- DOI: 10.1016/j.combustflame.2026.115037
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026002737
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218026002737/pdfft?md5=638154072b1c72a6b273ac919ce4e087&pid=1-s2.0-S0010218026002737-main.pdf
- Fuel type: pyrrole
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing\raw_downloads\S0010218026002737_mmc2.txt
- Original thermodynamic source files: _processing\raw_downloads\S0010218026002737_mmc3.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 2: """ C2H5CN+CH2CN=NCCH2CN+C2H5 1.77E+09 0.805 24190.95 PLOG / 1.31E-04 2.35E+04 2.197 21164.95 / PLOG / 1.31E-03 3.31E+04 2.154 21245.83 / PLOG / 1.00E+00 1.77E+09 0.805 24190.95 / PLOG / 1.00E+01 1.94E+11 0.277 26551.64 / PLOG / 1.00E+02 1.14E+07 1.612 26774.06 / """ Unexpected token 'C2H5CN+CH2CN' in reaction expression 'C2H5CN+CH2CN=NCCH2CN+C2H5'. May be due to undeclared species 'C2H5CNCH2CN'. Error while reading reaction in chem.inp starting on line 9: """ C2H5CN+CH2CN=CH3CN+CH2CH2CN 1.34E-04 4.915 13067.54 """ Unexpected token 'C2H5CN+CH2CN' in reaction expression 'C2H5CN+CH2CN=CH3CN+CH2CH2CN'. May be due to undeclared species 'C2H5CNCH2CN'. Error while reading reaction in chem.inp starting on line 10: """ C2H5CN ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Previous experimental studies of pyrrole pyrolysis reported numerous hydrocarbon and nitrogen-containing products from HCN up to pyridine and dinitriles. To develop a consistent detailed kinetic mechanism for pyrrole, the rate constants of H atom abstraction from C4H5N by NH2, and CH2CN radicals have been calculated at the DLPNO-CCSD(T)-F12/cc-pVDZ-F12//M06–2X/def2-TZVP level of theory while H atom abstraction by CN was at DLPNO-NEVPT2(11e,11o)/cc-pVTZ//M06–2X/def2-TZVP level of theory from 300 to 2000 K. Model analysis revealed the key role of cyanomethyl radicals in product formation, therefore the theoretical calculations were extended to reactions of CH2CN with pyrrolenine, allyl cyanide, crotonitrile, propionitrile and pyridine. The new rate constants were found to be significantly different from the previous estimates implemented in the literature models. Moreover, thermodynamic data of several intermediates important in pyrolytic reactions of pyrrole were calculated at the G4 theoretical level or updated using recent studies. A kinetic model of pyrrole pyrolysis was developed relying on the new rate constants and thermodynamic data, together with the rate constants from the literature. Experimental data on the formation of major and minor products previously obtained in a single pulse shock tube and jet-stirred reactors were compared with the predictions of this mechanism and two recent models by Chen et al. (Comb. Flame 276 (2025) 114136) and Wu et al. (Comb. Flame 277 (2025) 114211). The pathways of each nitrogen-containing product formation were discussed together with sensitivity analysis elucidating reactions controlling their yields.

## Processing Notes

- none
