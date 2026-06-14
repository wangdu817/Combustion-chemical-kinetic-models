# High-pressure oxidation of hydrogen diluted in N2 with added H2O or CO2 at 100 atm in a supercritical-pressure jet-stirred reactor

## Bibliography

Hao Zhao, Chao Yan, Guohui Song, Ziyu Wang, Ahren W. Jasper, Stephen J. Klippenstein, et al.. High-pressure oxidation of hydrogen diluted in N2 with added H2O or CO2 at 100 atm in a supercritical-pressure jet-stirred reactor[J]. Combustion and Flame, 2024, 266: 113543. DOI: 10.1016/j.combustflame.2024.113543.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 266 / August
- Article number: 113543
- DOI: 10.1016/j.combustflame.2024.113543
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218024002529
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: hydrogen
- Plasma-related mechanism: no
- Validation reactor/type from abstract: jet-stirred reactor, stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218024002529_mmc2/HPMech.inp
- Original thermodynamic source files: _processing/extracted/s0010218024002529_mmc3/therm.dat
- Original transport source files: _processing/extracted/s0010218024002529_mmc4/tran.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 2931: """ C6H5(+M)=o-C6H4+H(+M) 4.30E+12 0.62 77313. ! Hai Wang et al., Proc combust. Inst. 28(2000) 1545-1555 LOW/ 1.00E+84 -18.87 90064 / TROE/ 0.902, 696., 358., 3856. / H2/2.0/ H2O/6.0/ CH4/2.0/ CO/1.5/ CO2/2.0/ """ could not convert string to float: '0.902,' Unparsable lines while reading thermo data in therm.dat starting on line 400: """ """ Lines could not be parsed as a NASA7 entry. Please check https://cantera.org/stable/userguide/ck2yaml-tutorial.html#debugging-common-errors-in-ck-files for the correct Chemkin syntax.; numeric cleanup retry failed: InputError: Error while reading reaction in chem_cantera_numeric_clean.inp starting on line 2920: """ C6H5(+M)=o-C6H4+H(+M) 4.30E+12 0.62 77313. ! Hai Wang et al., P ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

The oxidation of H2 diluted in N2 with and without 10 % H2O or 20 % CO2 additions are studied at fuel-lean conditions at 100 atm and 500–1000 K in a supercritical-pressure jet-stirred reactor. The mole fractions of H2 and O2 are quantified by using micro-gas chromatography (µ-GC). Experiment shows that H2 oxidation is inhibited at lower temperatures (850–950 K) while it is promoted at higher temperatures (950–1050 K) with 10 % H2O additions or 20 % CO2 additions. In addition, the effect of H2O is more significant than that of CO2. Five models are employed in simulations of the observables. Unfortunately, all of these models fail to capture the effect of H2O and CO2 additions on H2 oxidation. Pathway and sensitivity analyses of H2 show that the reactions of H + O2 + (M) = HO2 + (M) and H2O2 + (M) = 2OH + (M) dominate the radical production (HO2 and OH) and H2 oxidation at 100 atm. A further perturbation of pre-exponential coefficients and collisional factors of these reactions indicates that collisional factors of H2O and CO2 have small effect under the experimental conditions, while a smaller reaction rate for H2O2 + (M) = 2OH + (M) may explain the inhibiting effect of H2O and CO2 additions at lower temperatures. Real-fluid corrections on intermolecular interactions and mixing rules should be further investigated to explain the effect of H2O and CO2 additions.

## Processing Notes

- extracted S0010218024002529_mmc4.zip
- extracted S0010218024002529_mmc3.zip
- extracted S0010218024002529_mmc1.docx
- extracted S0010218024002529_mmc2.zip
