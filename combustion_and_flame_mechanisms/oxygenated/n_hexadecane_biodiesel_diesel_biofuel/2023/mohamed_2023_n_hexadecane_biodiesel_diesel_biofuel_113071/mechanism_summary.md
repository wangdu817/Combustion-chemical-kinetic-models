# Effect of the β-hydroxy group on ester reactivity: Combustion kinetics of methyl hexanoate and methyl 3-hydroxyhexanoate

## Bibliography

Samah Y. Mohamed, Nimal Naser, Gina Fioroni, Jon Luecke, Yeonjoon Kim, Peter C. St. John, et al.. Effect of the β-hydroxy group on ester reactivity: Combustion kinetics of methyl hexanoate and methyl 3-hydroxyhexanoate[J]. Combustion and Flame, 2023, 258: 113071. DOI: 10.1016/j.combustflame.2023.113071.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 258 / December
- Article number: 113071
- DOI: 10.1016/j.combustflame.2023.113071
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023004467
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: n_hexadecane_biodiesel_diesel_biofuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: flow reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/raw_downloads/S0010218023004467_mmc2.docx, _processing/raw_downloads/S0010218023004467_mmc1.docx
- Original thermodynamic source files: _processing/raw_downloads/S0010218023004467_mmc1.docx, _processing/raw_downloads/S0010218023004467_mmc5.docx
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 901
- Reaction count: 6825
- Message: CanteraError: ******************************************************************************* InputFileError thrown by AnyMap::fromYamlFile: Error on line 160 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/n_hexadecane_biodiesel_diesel_biofuel/2023/mohamed_2023_n_hexadecane_biodiesel_diesel_biofuel_113071/mechanism.yaml: illegal block entry | Line | | 155 | bucomeco, prcoetco, prcomeco, etcoetco, etcomeco, mecoetco, | 156 | mecomeco, c4h8cho-3, c4h8cho-4, mhx5oh6j, mhx4oh5j, mhx3oh4j, | 157 | mhx2oh3j, mhx5oh6oo, mhx4oh5oo, mhx3oh4oo, mhx2oh3oo, meall, | 158 | c6h615, hex1245, | 159 | species: > 160 > - name: CH2O ^ | 161 | composition: {H: 2, C: 1, O: 1} | 162 | thermo: | 163 | model: ********************************************************************* ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 2

- Status: cantera_failed
- Species count: 901
- Reaction count: 6825
- Message: CanteraError: ******************************************************************************* InputFileError thrown by AnyMap::fromYamlFile: Error on line 160 of /home/icaurs/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/n_hexadecane_biodiesel_diesel_biofuel/2023/mohamed_2023_n_hexadecane_biodiesel_diesel_biofuel_113071/mechanism.yaml: illegal block entry | Line | | 155 | bucomeco, prcoetco, prcomeco, etcoetco, etcomeco, mecoetco, | 156 | mecomeco, c4h8cho-3, c4h8cho-4, mhx5oh6j, mhx4oh5j, mhx3oh4j, | 157 | mhx2oh3j, mhx5oh6oo, mhx4oh5oo, mhx3oh4oo, mhx2oh3oo, meall, | 158 | c6h615, hex1245, | 159 | species: > 160 > - name: CH2O ^ | 161 | composition: {H: 2, C: 1, O: 1} | 162 | thermo: | 163 | model: ********************************************************************* ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

One of the major biofuels used today is biodiesel, composed of fatty acid methyl esters. The fats and oils feedstocks used to make biodiesel are in relatively short supply. To meet increasing global demand, engineered microorganisms have been developed to catalyze conversion of sugar to fatty acid esters that contain unique β‑hydroxy-esters. This study investigated the effect of a hydroxyl group on the combustion characteristics of methyl esters by comparing the chemical behavior of methyl hexanoate (MHx) and methyl 3-hydroxyhexanoate (M3OHHx)—used as surrogates for diesel-boiling-range esters with longer fatty acid chains. The oxidation of these esters was studied experimentally in a flow reactor at 0.84 and 10 bar, 600 to 1,100 K, and stoichiometric conditions; and in a constant volume combustion chamber at 5 and 10 bar, 600 to 900 K, and equivalence ratios of 0.3 and 0.6. MHx was more reactive in the constant volume chamber at temperatures below 800 K at 10 bar and equivalence ratio of 0.6. MHx also exhibited a higher indicated cetane number (16.4) than M3OHHx (8.1). We investigated this reactivity trend using an updated MHx kinetic model and M3OHHx model developed as part of this work. The kinetic models predicted that radicals formed from MHx were consumed by low-temperature chemistry reactions, whereas the M3OHHx reactivity was significantly governed by the β-radical (on the same carbon as the OH group) chemistry which mainly terminated via the less reactive chain propagation pathway to methyl-3-oxohexanoate + HO2. This study extends our understanding of structural effects on ester reactivity, which will allow for accurate surrogate formulation and performance simulations.

## Processing Notes

- extracted S0010218023004467_mmc3.docx
- extracted S0010218023004467_mmc4.docx
- extract failed S0010218023004467_mmc2.docx: File is not a zip file
- extract failed S0010218023004467_mmc1.docx: File is not a zip file
- extracted S0010218023004467_mmc6.xlsx
- extract failed S0010218023004467_mmc5.docx: File is not a zip file
