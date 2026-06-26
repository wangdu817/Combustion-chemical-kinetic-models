# Cumene pyrolysis: a combined experimental and Ab initio modeling approach

## Bibliography

Boris Roux, Yves Simon, Sandra Poeuf, Marc Bouchez, ... René Fournet. Cumene pyrolysis: a combined experimental and Ab initio modeling approach[J]. Combustion and Flame, 2026, 286: 114840. DOI: 10.1016/j.combustflame.2026.114840.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 286 / April
- Article number: 114840
- DOI: 10.1016/j.combustflame.2026.114840
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218026000763
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: cumene
- Plasma-related mechanism: no
- Validation reactor/type from abstract: jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218026000763_mmc2/SM1_Mechanism_R.inp
- Original thermodynamic source files: _processing/extracted/s0010218026000763_mmc3/SM2_NASA_polynomial_R.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 1028: """ styrene+C2H5 = A1CHCH+C2H6 5.00+11 0.000 19700.0 ! [3] """ could not convert string to float: '5.00+11' Unparsable lines while reading thermo data in therm.dat starting on line 957: """ R-stilbene C 14H 11 G 0290.00 5000.00 1500.00 1 !QCISD(T) 0.35587210E+02 0.30044893E-01-0.10132261E-04 0.15657523E-08-0.91359710E-13 2 0.40303762E+05-0.16725841E+03-0.10510095E+02 0.14963773E+00-0.13388848E-03 3 0.61497180E-07-0.11372155E-10 0.55415521E+05 0.76552245E+02 """ Lines could not be parsed as a NASA7 entry. No thermo data found for species 'R-stilbene' Please check https://cantera.org/stable/userguide/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files for the correct Chemkin syntax.; numeric cleanup retry faile ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

An experimental study of the pyrolysis of cumene was performed at atmospheric pressure, in a jet-stirred reactor (JSR) with 2% fuel diluted in helium, a residence time of 1 s, and for temperatures ranging from 863 to 1023 K. Fifty-four species were identified from light compounds to C20, by gas chromatography coupled with mass spectrometry (GC–MS) and quantified by GC-FID (flame ionization detector) and GC-PDHID (pulsed discharged helium ionization detector). Among these products, several aromatic species (C₉+) were detected for the first time. In addition, a comprehensive kinetic model, including a growth sub-mechanism to bicycle compounds with sizes up to C14, has been developed, based on electronic structure calculations, performed at the QCISD(T)/CBS//B2PLYP-D3/6–311+G(d,p) level of theory. Calculations were used to derive kinetic parameters and thermodynamic data. Comparisons between experiments and simulations showed good agreement for thirty-six species, including the most important products and a marked improvement from previous modeling studies reported in the literature. The allylic H-atom and tertiary carbon atom allows cumene to readily decompose to form styrene, benzene and α-methylstyrene, the main primary aromatic compounds. These species are less reactive than cumene, and our study clearly shows the importance of addition reactions on their side chain or aromatic ring, leading to the formation of bicyclic structures that are key intermediates in the formation of heavier PAHs. In particular, our mechanism models the formation of mono- and bi-aromatic products that had not previously been reported during cumene pyrolysis, such as trimethylbenzene, butenylbenzene, an important precursor of 3-methylindene, as well as diphenylethylene and diphenylstyrene, which are PAH precursors. In addition, a detailed investigation of the potential energy surfaces has clarified the elementary steps involved in the formation pathways of all modeled species, including various isomers, such as methylnaphthalene and methylindene. In particular, the involvement of sigmatropic rearrangements accounts for the formation of 2-methylindene and 2-methylnaphthalene.

## Processing Notes

- extracted S0010218026000763_mmc4.zip
- extracted S0010218026000763_mmc2.zip
- extracted S0010218026000763_mmc3.zip
- extracted S0010218026000763_mmc1.docx
