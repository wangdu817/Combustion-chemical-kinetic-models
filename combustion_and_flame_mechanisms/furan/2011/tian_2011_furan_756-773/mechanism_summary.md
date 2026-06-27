# An experimental and kinetic investigation of premixed furan/oxygen/argon flames

## Bibliography

Zhenyu Tian, Tao Yuan, René Fournet, Pierre-Alexandre Glaude, Baptiste Sirjean, Frédérique Battin-Leclerc, et al.. An experimental and kinetic investigation of premixed furan/oxygen/argon flames[J]. Combustion and Flame, 2011, 158: 756-773. DOI: 10.1016/j.combustflame.2010.12.022.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 158 / Apr
- Article number: 756-773
- DOI: 10.1016/j.combustflame.2010.12.022
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218010003767
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: furan
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218010003767_mmc1/Supplemental 2-Furan Mech.txt
- Original thermodynamic source files: _processing/extracted/s0010218010003767_mmc1/Supplemental 2-Furan Mech.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant thermo data for species 'naphthalene' starting on line 1082 of chem.inp. Unparsable lines while reading thermo data in chem.inp starting on line 563: """ !coefficients de CHEMKIn a haute temperature et THERGAS a basse temperature! """ Lines could not be parsed as a NASA7 entry. Error while reading reaction in chem.inp starting on line 4265: """ iC4H8+R2OH=>iC4H7+H2O 6.0D+06 2.000 -298.0 ! MES 878<C.M.>!(idem RF) """ could not convert string to float: '6.0D+06' Error while reading reaction in chem.inp starting on line 4436: """ C5H9#=C5H9 2.0D+14 0.005 35600.0 !SIRJEAN05 """ could not convert string to float: '2.0D+14' Error while reading reaction in chem.inp starting on line 4437: """ C5H9=C3H5Y+C2H4Z 3.3D+13 0.000 22500.0 ! EXGAS """ could not convert string ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

The detailed chemical structures of three low-pressure (35Torr) premixed laminar furan/oxygen/argon flames with equivalence ratios of 1.4, 1.8 and 2.2 have been investigated by using tunable synchrotron vacuum ultraviolet (VUV) photoionization and molecular-beam mass spectrometry. About 40 combustion species including hydrocarbons and oxygenated intermediates have been identified by measurements of photoionization efficiency spectra. Mole fraction profiles of the flame species including reactants, intermediates and products have been determined by scanning burner position with some selected photon energies near ionization thresholds. Flame temperatures have been measured by a Pt–6%Rh/Pt–30%Rh thermocouple. A new mechanism involving 206 species and 1368 reactions has been proposed whose predictions are in reasonable agreement with measured species profiles for the three investigated flames. Rate-of-production and sensitivity analyses have been performed to track the key reaction paths governing furan consumption for different equivalence ratios. Both experimental and modeling results indicate that few aromatics could be formed in these flames. Furthermore, the current model has been validated against previous pyrolysis results of the literature obtained behind shock waves and the agreement is reasonable as well.

## Processing Notes

- extracted S0010218010003767_mmc1.zip
