# Reaction mechanism and kinetic modeling of gas-phase thermal decomposition of prototype nitramine compound HMX

## Bibliography

Lili Ye, Zhihe Zhang, Fan Wang, Xiaodong Wang, Yiming Lu, Lei Zhang. Reaction mechanism and kinetic modeling of gas-phase thermal decomposition of prototype nitramine compound HMX[J]. Combustion and Flame, 2024, 259: 113181. DOI: 10.1016/j.combustflame.2023.113181.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 259 / January
- Article number: 113181
- DOI: 10.1016/j.combustflame.2023.113181
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023005564
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: unknown_fuel
- Plasma-related mechanism: possible
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218023005564_mmc2/smm1-HMX-kinetic.inp
- Original thermodynamic source files: _processing/extracted/s0010218023005564_mmc3/smm2-HMX-thermal.dat
- Original transport source files: _processing/extracted/s0010218023005564_mmc4/smm3-HMX-trans.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 207
- Reaction count: 1605
- Message: CanteraError: ******************************************************************************* CanteraError thrown by addReactions: ******************************************************************************* InputFileError thrown by PlogRate::validate: Error on line 14123 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/unknown_fuel/2024/ye_2024_unknown_fuel_113181/mechanism.yaml: Invalid rate coefficient for reaction 'RDX <=> NO2 + RDXR' at P = 1013.3, T = 300.0 at P = 1013.3, T = 500.0 To fix this error, remove this reaction or contact the author of the reaction/mechanism in question, because the rate expression is mathematically unsound at the temperatures and pressures noted above. | Line | | 14118 | - {P: 100.0 atm, A: 8.2459e+118, b: -30.943, Ea: ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

The combustion, detonation, and explosion chemistry of energetic materials is regulated by the formation and decay of critical intermediates that are generated during the process. In this study, the pyrolysis mechanism of a commonly used cyclic nitramine explosive called octahydro-1,3,5,7-tetranitro-1,3,5,7-tetrazocine, also known as HMX or octogen, has been investigated by performing ab initio based RRKM/master equation analysis coupled with kinetic modeling simulations. The potential energy profiles of reaction network were constructed at the DLPNO-CCSD(T)/cc-pV[T,Q]Z level based on B3LYPD3/6-311+G(d,p) optimized geometries. The master equation calculations and kinetic modeling simulations indicated that the N-NO2 bond fission, leading to the formation of HMXR (the radical formed after NO2 loss) and nitro radicals, is the most important channel during the initial decomposition of HMX. The C-N and C-H β-scissions play an important role in the subsequent decomposition of the HMXR radical, with the C-H β-scission to form INT249 being the more favored consumption channel. Furthermore, this study also provided a preliminary exploration into the contribution of bimolecular reactions between HMX and H/OH/NO/NO2 radicals. The kinetic simulation results demonstrated that decomposition through these bimolecular reactions is of negligible importance under the investigated conditions.

## Processing Notes

- extracted S0010218023005564_mmc5.zip
- extracted S0010218023005564_mmc3.zip
- extracted S0010218023005564_mmc2.zip
- extracted S0010218023005564_mmc1.docx
- extracted S0010218023005564_mmc4.zip
