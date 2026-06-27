# A comprehensive experimental and modeling study of 2-methylbutanol combustion

## Bibliography

Sungwoo Park, Ossama Mannaa, Fethi Khaled, Rafik Bougacha, Morkous S. Mansour, Aamir Farooq, et al.. A comprehensive experimental and modeling study of 2-methylbutanol combustion[J]. Combustion and Flame, 2015, 162: 2166-2176. DOI: 10.1016/j.combustflame.2015.01.014.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 162 / May
- Article number: 2166-2176
- DOI: 10.1016/j.combustflame.2015.01.014
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218015000176
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: butanol
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, laminar flame speed, burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218015000176_mmc2/2methylbutanol_chem.inp, _processing/extracted/s0010218015000176_mmc3/2methylbutanol_chem_highT.inp
- Original thermodynamic source files: _processing/extracted/s0010218015000176_mmc4/2methylbutanol_therm.dat
- Original transport source files: _processing/extracted/s0010218015000176_mmc5/2methylbutanol_tran.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 269: """ h2o2(+m)<=>oh+oh(+m) 2.00e+12 0.90 4.8749+04 low/ 3.658e+24 -2.30 4.8749+04/ troe/ 0.43 1e-30 1e+30/ ar/ 0.68/ o2/ 0.68/ h2/ 2.5/ co/ 1.9/ co2/ 3.8/ h2o/ 0.0/ he/ 0.0/ h2o2/ 5.2/ ch4/ 2/ c2h6/ 3/ """ could not convert string to float: '4.8749+04' Error while reading reaction in chem.inp starting on line 273: """ h2o2(+he)<=>oh+oh(+he) 2.00e+12 0.90 4.8749+04 low/ 1.609e+24 -2.30 4.8749+04/ troe/ 0.44 1e-30 1e+30/ """ could not convert string to float: '4.8749+04' Error while reading reaction in chem.inp starting on line 276: """ h2o2(+h2o)<=>oh+oh(+h2o) 2.00e+12 0.90 4.8749+04 low/ 1.865e+25 -2.30 4.8749+04/ troe/ 0.51 1e-30 1e+30/ """ could not convert string to float: '4.8749+04' Issue while reading reaction i ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: ok_after_cleanup
- Species count: 324
- Reaction count: 2094
- Message: normalized legacy numeric/reaction syntax; cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

2-Methylbutanol (2-methyl-1-butanol) is one of several next-generation biofuels that can be used as an alternative fuel or blending component for combustion engines. This paper presents new experimental data for 2-methylbutanol, including ignition delay times in a high-pressure shock tube and premixed laminar flame speeds in a constant volume combustion vessel. Shock tube ignition delay times were measured for 2-methylbutanol/air mixtures at three equivalence ratios, temperatures ranging from 750 to 1250K, and at nominal pressures near 20 and 40bar. Laminar flame speed data were obtained using the spherically propagating premixed flame configuration at pressures of 1, 2, and 5bar. A detailed chemical kinetic model for 2-methylbutanol oxidation was developed including high- and low-temperature chemistry based on previous modeling studies on butanol and pentanol isomers. The proposed model was tested against new and existing experimental data at pressures of 1–40atm, temperatures of 740–1636K, equivalence ratios of 0.25–2.0. Reaction path and sensitivity analyses were conducted for identifying key reactions at various combustion conditions, and to obtain better understanding of the combustion characteristics of larger alcohols.

## Processing Notes

- extracted S0010218015000176_mmc4.zip
- extracted S0010218015000176_mmc2.zip
- extracted S0010218015000176_mmc1.docx
- extracted S0010218015000176_mmc3.zip
- extracted S0010218015000176_mmc5.zip
