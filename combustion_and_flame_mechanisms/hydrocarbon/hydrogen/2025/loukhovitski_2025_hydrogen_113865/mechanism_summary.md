# A detailed kinetic submechanism for OH* chemiluminescence in hydrocarbon combustion

## Bibliography

Boris I. Loukhovitski, Alexander S. Sharipov. A detailed kinetic submechanism for OH* chemiluminescence in hydrocarbon combustion[J]. Combustion and Flame, 2025, 272: 113865. DOI: 10.1016/j.combustflame.2024.113865.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 272 / February
- Article number: 113865
- DOI: 10.1016/j.combustflame.2024.113865
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024005741
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218024005741/pdfft?md5=0bd19b01f6b5b5df23557ab6e795d76b&pid=1-s2.0-S0010218024005741-main.pdf
- Fuel type: hydrogen
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218024005741_mmc3/JIHT-OHex(CxHy).yaml, _processing/extracted/s0010218024005741_mmc2/JIHT-OHex(CxHy)_kin.dat
- Original thermodynamic source files: _processing/extracted/s0010218024005741_mmc3/JIHT-OHex(CxHy).yaml, _processing/extracted/s0010218024005741_mmc2/JIHT-OHex(CxHy)_therm.dat
- Original transport source files: _processing/extracted/s0010218024005741_mmc3/JIHT-OHex(CxHy).yaml

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 1
- Reaction count: 77
- Message: InputError: No thermo data found for species 'H' No thermo data found for species 'H2' No thermo data found for species 'O' No thermo data found for species 'O2' No thermo data found for species 'OH' No thermo data found for species 'H2O' No thermo data found for species 'N2' No thermo data found for species 'HO2' No thermo data found for species 'H2O2' No thermo data found for species 'AR' No thermo data found for species 'HE' No thermo data found for species 'KR' No thermo data found for species 'NO' No thermo data found for species 'N2O' No thermo data found for species 'NO2' No thermo data found for species 'HNO' No thermo data found for species 'HNO2' No thermo data found for species 'NH3' No thermo data found for species 'NH' No thermo data found for species 'NNH' No thermo data foun ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: cantera_failed
- Species count: 1
- Reaction count: 77
- Message: CanteraError: ******************************************************************************* InputFileError thrown by addSpecies: Error on lines 65 and 74 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/hydrogen/2025/loukhovitski_2025_hydrogen_113865/mechanism.yaml: Could not find a species named 'H'. | Line | | 60 | - name: "JIHT-OHex(CxHy)" | 61 | transport: multicomponent | 62 | kinetics: gas | 63 | thermo: ideal-gas | 64 | elements: [H, O, N, Ar, He, Kr, C] > 65 > species: [H, H2, O, O2, OH, H2O, N2, HO2, H2O2, AR, HE, KR, OHEX, NO, N2O, NO2, ^ | 66 | HNO, HNO2, NH3, NH, NNH, CO, CO2, CH4, CH3, CH2, C, CH, CH3OH, CH2OH, | 67 | CH2O, HCO, C2H6, C2H4, C2H2, C2H, CH3CO, CH2CO, C3H6, C3H5, C3H4, | 68 | C3H3, C3H2, C2H3CHO, C4H10, C4H6, C4H2, CH2COOH, C5H ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Here, we propose a new physically consistent modeling scheme, JIHT-OHex(C x H y ) , that accurately predicts the formation and consumption of electronically excited chemiluminescent OH ∗ molecules in hydrocarbon flames over a wide range of temperatures, pressures, and mixture compositions. It incorporates (unchanged) our recent well-founded JIHT-OHex(H 2 ) reaction submodel (Sharipov et al., 2024, Combust. Flame, 263, 113417), aimed at describing the OH ∗ evolution in hydrogen oxidation, and contains a necessary set of elementary processes involving OH ∗ and carbon-containing species with the rate constants that are based either on a critical review of known, sometimes conflicting literature data on the elementary reaction kinetics of OH ∗ or, where necessary and appropriate, on semiempirical estimates. To improve the JIHT-OHex(C x H y ) performance against a representative data set for the observed OH( A 2 Σ + → X 2 Π ) chemiluminescent emission (near 309 nm) accompanying high-temperature oxidation of various (from C 1 to C10) hydrocarbon-based mixtures that we aggregated at the preparatory stage of the work, the rate coefficients of reaction and quenching processes that the overall OH ∗ kinetics is most sensitive to (or for which there is a particular scatter in the available kinetic data, if any) were jointly optimized within their theoretical expectations and experimental uncertainties. It is shown that our universal detailed OH ∗ submechanism, which includes a much larger pool of elementary processes (32 reactions and 36 quenching partners) than previous essentially global models (consisting of only a few processes and tailored to specific mixtures and combustion conditions), clearly outperforms the competitors in terms of integral accuracy (when tested against the multitude of the collected OH ∗ emission measurements). Accordingly, there is reason to believe, as exemplified for the conditions of the laminar premixed methane-air flame, that our detailed OH ∗ submodel with physically realistic (to the extent possible) rate constants will perform adequately over a wider range of burning conditions and flow parameters than that for which it was validated and tuned. Novelty and significance statement Although it is widely accepted that UV chemiluminescent OH( A 2 Σ + − X 2 Π ) emission as an optical signature of the combustion process as a whole and of the underlying chemistry offers unique diagnostic capabilities, in recent years, definitely insufficient attention has been paid to the development of the detailed reaction mechanisms for quantitative interpretation of the OH ∗ chemiluminescence measurements in various burning environments. This is especially true for the oxidation of hydrocarbons. Indeed, the pertinent OH ∗ models known to date are essentially global, meaning that they all contain a surprisingly small number of processes (in most cases, only a couple of OH ∗ -forming reactions are involved alongside the quenching processes) and their rate constants are adjusted to specific hydrocarbon-based mixtures and burning conditions. Accordingly, a revision of the current understanding of the OH ∗ kinetics in the presence of hydrocarbons is highly desired; therefore, our detailed physically-based reaction mechanism, which comprises dozens of plausible pathways of OH ∗ formation and depletion with realistic rate coefficients and thus is capable of simulating the OH ∗ emission in hydrocarbon flames more accurately than previous models, is in itself a fundamentally significant and novel contribution to the practice of chemiluminescence modeling. No less importantly, the rate constant fits, recommended here, are also of independent interest in the context of excited-state chemistry.

## Processing Notes

- extracted S0010218024005741_mmc1.zip
- extracted S0010218024005741_mmc3.zip
- extracted S0010218024005741_mmc2.zip
