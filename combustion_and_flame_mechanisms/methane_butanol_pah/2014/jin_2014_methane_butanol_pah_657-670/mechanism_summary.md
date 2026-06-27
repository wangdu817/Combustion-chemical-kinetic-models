# Experimental and kinetic modeling study of PAH formation in methane coflow diffusion flames doped with n-butanol

## Bibliography

Hanfeng Jin, Alberto Cuoci, Alessio Frassoldati, Tiziano Faravelli, Yizun Wang, Yuyang Li, et al.. Experimental and kinetic modeling study of PAH formation in methane coflow diffusion flames doped with n-butanol[J]. Combustion and Flame, 2014, 161: 657-670. DOI: 10.1016/j.combustflame.2013.10.020.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 161 / Mar
- Article number: 657-670
- DOI: 10.1016/j.combustflame.2013.10.020
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218013003945
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: methane_butanol_pah
- Plasma-related mechanism: no
- Validation reactor/type from abstract: burner/flame structure

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218013003945_mmc2/2-Mechanism
- Original thermodynamic source files: _processing/extracted/s0010218013003945_mmc3/3-Thermodynamic
- Original transport source files: _processing/extracted/s0010218013003945_mmc4/4-Transport

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading entry in chem.inp starting on line 2496: """ References """ Section starts with unrecognized keyword 'References' Error while reading reaction in chem.inp starting on line 951: """ C5H6+H=lC5H7 8.27+126 -32.3 82348.0 !USC Mech II (02-MOS-LIN) """ could not convert string to float: '8.27+126' Ignoring redundant thermo data for species 'sC4H9' starting on line 415 of therm.dat. Ignoring redundant thermo data for species 'N2' starting on line 629 of therm.dat. Ignoring redundant thermo data for species 'N2' starting on line 636 of therm.dat. Ignoring redundant thermo data for species 'AR' starting on line 640 of therm.dat. Error while reading thermo entry in therm.dat starting on line 641: """ HE+ L10/90HE+ 1 0 0 0G 200.000 6000.000 1000. 1 2.50000000E+00 0.000 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

In order to understand the interactions between butanol and hydrocarbon fuels in the PAH formation, experimental and kinetic modeling investigations were combined to study methane laminar coflow diffusion flames doped with two inlet mole fractions of n-butanol (1.95% and 3.90%) in this work. Mole fractions of flame species along the flame centerline were measured using synchrotron VUV photoionization mass spectrometry. A detailed kinetic model of n-butanol combustion, extended from a recent published n-butanol model, was provided in this work to reproduce the fuel decomposition and the formation of benzene and PAHs in the investigated flames. Numerical simulations were performed with laminarSMOKE code, a CFD code specifically conceived to handle large kinetic mechanisms. The simulation results were able to follow the observed effects of n-butanol addition from the experimental results. In particular, unsaturated hydrocarbons, especially C6–C16 aromatics, were predicted satisfactorily. The reaction flux analysis revealed that benzene precursors, especially C3 radicals, increase significantly with increasing inlet mole fraction of n-butanol. This enhances the formation of phenyl and benzyl radicals, which are important PAH precursors. Reactions of benzyl, phenyl radicals and benzene with C2–C3 species are the major formation pathways for indene and naphthalene. And PAHs with more carbon atoms are dominantly formed from naphthyl and indenyl radicals.

## Processing Notes

- extracted S0010218013003945_mmc2.zip
- extracted S0010218013003945_mmc3.zip
- extracted S0010218013003945_mmc4.zip
