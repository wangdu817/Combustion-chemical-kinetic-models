# Experimental and kinetic study of pyridine pyrolysis with tunable synchrotron VUV photoionization and molecular beam mass spectrometry

## Bibliography

Cheng-Yin Ye, Ling-Nan Wu, Dong-Xu Tian, Jiu-Zhong Yang, ... Zhen-Yu Tian. Experimental and kinetic study of pyridine pyrolysis with tunable synchrotron VUV photoionization and molecular beam mass spectrometry[J]. Combustion and Flame, 2026, 285: 114742. DOI: 10.1016/j.combustflame.2025.114742.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 285 / March
- Article number: 114742
- DOI: 10.1016/j.combustflame.2025.114742
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025007771
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025007771/pdfft?md5=27adaf192e97203ba4c70054cfc1449f&pid=1-s2.0-S0010218025007771-main.pdf
- Fuel type: pyridine
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: raw_downloads\S0010218025007771_mmc2.txt
- Original thermodynamic source files: raw_downloads\S0010218025007771_mmc3.txt
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: CanteraError: 
*******************************************************************************
InputFileError thrown by Kinetics::checkDuplicates:
Error on lines 11031 and 11098 of E:\mech_collection\combustion_and_flame_2026_mechanisms\pyridine\cheng_yin_ye_2026_114742_experimental_and_kinetic_study_of_pyridine_py\mechanism.yaml:
Undeclared duplicate reactions detected:
Reaction 1812: H2 + M <=> 2 H + M
Reaction 1800: 2 H + O2 <=> H2 + O2

|  Line |
|  11026 |   note: M. Sangwan, L. N. Krasnoperov, The Journal of Physical Chemistry
|  11027 |     A 116 (2012) 11817?1822.
|  11028 | - equation: OH + OH <=> O + H2O  # Reaction 1799
|  11029 |   duplicate: true
|  11030 |   rate-constant: {A: 2.6e+11, b: -0.057, Ea: -827.0}
>  11031 > - equation: H2 + M <=> H + H + M  # Reaction 1800
            ^
|  11032 |   type: three-body
|  11033 |   rate-constant: {A: 4.6e+19, b: -1.4, Ea: 1.0438e+05}
|  11034 |   efficiencies: {H2: 2.5, H2O: 12.0, CO: 1.9, CO2: 3.8, AR: 0.0, HE: 0.0}
...
|  11093 |   note: M. P. Burke, S. J. Klippenstein, L. B. Harding, Proceedings of the
|  11094 |     Combustion Institute 34 (2013) 547?55.
|  11095 | - equation: HO2 + OH <=> H2O + O2  # Reaction 1811
|  11096 |   duplicate: true
|  11097 |   rate-constant: {A: 1.2e+09, b: 1.24, Ea: -1310.0}
>  11098 > - equation: H + O2 + H <=> H2 + O2  # Reaction 1812
            ^
|  11099 |   rate-constant: {A: 8.8e+22, b: -1.835, Ea: 800.0}
|  11100 |   note: M. Burke, S. Klippenstein, Nature Chemistry, 9, 1078 C1082 (2017)
|  11101 | - equation: H + O2 + H <=> OH + OH  # Reaction 1813
*******************************************************************************

- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

not available

## Processing Notes

- none
