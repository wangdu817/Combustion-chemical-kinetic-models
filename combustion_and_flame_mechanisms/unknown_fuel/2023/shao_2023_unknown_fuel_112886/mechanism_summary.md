# High-resolution mass spectrometry of pyrene dimers formed in a jet-stirred reactor

## Bibliography

Can Shao, Yitong Zhai, A. Cardenas-Salvarez, Wen Zhang, E. Grajales-Gonzalez, Xin Bai, et al.. High-resolution mass spectrometry of pyrene dimers formed in a jet-stirred reactor[J]. Combustion and Flame, 2023, 255: 112886. DOI: 10.1016/j.combustflame.2023.112886.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 255 / September
- Article number: 112886
- DOI: 10.1016/j.combustflame.2023.112886
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023002675
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: no
- Validation reactor/type from abstract: jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218023002675_mmc2/mmc2.txt
- Original thermodynamic source files: _processing/extracted/s0010218023002675_mmc3/mmc3.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 9
- Reaction count: 9
- Message: CanteraError: ******************************************************************************* InputFileError thrown by setupPhase: Error on line 16 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/unknown_fuel/2023/shao_2023_unknown_fuel_112886/mechanism.yaml: Could not parse elements declaration of type 'vector<AnyValue>' | Line | | 11 | units: {length: cm, time: s, quantity: mol, activation-energy: cal/mol} | 12 | | 13 | phases: | 14 | - name: gas | 15 | thermo: ideal-gas > 16 > elements: [] ^ | 17 | species: [H, A4, A4-, C-DIM, P-DIM, PR-DIM, H2, AR, N2] | 18 | kinetics: gas | 19 | state: {T: 300.0, P: 1 atm} *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

In this work, pyrene was pyrolyzed in a jet-stirred reactor to study dimerization in the soot inception temperature region (700K-1200 K). Nucleated particles were collected, and their chemical composition was analyzed using high-resolution Fourier transform ion cyclotron resonance mass spectrometry with laser desorption ionization. The goal was to identify temperature regimes corresponding to i) the physical dimerization of two pyrene molecules (P-DIM), ii) the physical dimerization of a pyrenyl radical and a pyrene molecule (PR-DIM), and/or iii) the chemical dimerization of two pyrenyl radicals (C-DIM). A simple kinetic model was built to explain the competition between these three inception pathways. To this end, we calculated the rate constants for the radical-radical association reactions between the three isomeric pyrenyl radicals and H radical to yield pyrene, as well as the corresponding reverse dissociation rate constants. At low temperatures (700K-900 K), only pyrene-containing species were detected, indicating that pyrene molecules stacked together through Van der Waals forces (P-DIM). However, at 900–1100 K pyrenyl radicals can be formed, and the physical dimerization of a pyrenyl radical and a pyrene molecule is promoted (PR-DIM). When the temperature increased from 1100 K to 1200 K, species with a mass of 402 Da were detected and likely formed by the recombination of two pyrenyl radicals (C-DIM). It was found that chemical inception dominates the dimerization process at 1200 K due to increased pyrenyl radical concentrations. The developed model was able to capture the experimentally observed trends of the three dimerization pathways and reveals that while the physical dimerization of pyrene monomers cannot survive high temperatures in flames, the chemically-linked dimers likely play an important role in the inception process.

## Processing Notes

- extracted S0010218023002675_mmc3.zip
- extracted S0010218023002675_mmc1.docx
- extracted S0010218023002675_mmc2.zip
- extracted S0010218023002675_mmc4.zip
