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
- Fuel type: unknown_fuel
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
- Message: CanteraError: ******************************************************************************* InputFileError thrown by addSpecies: Error on lines 65 and 74 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/unknown_fuel/2025/loukhovitski_2025_unknown_fuel_113865/mechanism.yaml: Could not find a species named 'H'. | Line | | 60 | - name: "JIHT-OHex(CxHy)" | 61 | transport: multicomponent | 62 | kinetics: gas | 63 | thermo: ideal-gas | 64 | elements: [H, O, N, Ar, He, Kr, C] > 65 > species: [H, H2, O, O2, OH, H2O, N2, HO2, H2O2, AR, HE, KR, OHEX, NO, N2O, NO2, ^ | 66 | HNO, HNO2, NH3, NH, NNH, CO, CO2, CH4, CH3, CH2, C, CH, CH3OH, CH2OH, | 67 | CH2O, HCO, C2H6, C2H4, C2H2, C2H, CH3CO, CH2CO, C3H6, C3H5, C3H4, | 68 | C3H3, C3H2, C2H3CHO, C4H10, C4H6, C4H2, CH2C ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S0010218024005741_mmc1.zip
- extracted S0010218024005741_mmc3.zip
- extracted S0010218024005741_mmc2.zip
