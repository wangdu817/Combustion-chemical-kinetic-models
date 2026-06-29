# Effect of nitric oxide and exhaust gases on gasoline surrogate autoignition: iso-octane experiments and modeling

## Bibliography

Ruozhou Fang, Chiara Saggese, Scott W. Wagnon, Amrit B. Sahu, Henry J. Curran, William J. Pitz, et al.. Effect of nitric oxide and exhaust gases on gasoline surrogate autoignition: iso-octane experiments and modeling[J]. Combustion and Flame, 2022, 236: 111807. DOI: 10.1016/j.combustflame.2021.111807.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 236 / 2
- Article number: 111807
- DOI: 10.1016/j.combustflame.2021.111807
- ScienceDirect URL: https://doi.org/10.1016/j.combustflame.2021.111807
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: nitric_oxide_iso_octane_n_octane_gasoline
- Plasma-related mechanism: no
- Validation reactor/type from abstract: rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: not available
- Original mechanism source files: _processing/extracted/s0010218021005502_mmc4/mmc4.cti, _processing/extracted/s0010218021005502_mmc6/mmc6.inp
- Original thermodynamic source files: _processing/extracted/s0010218021005502_mmc4/mmc4.cti, _processing/extracted/s0010218021005502_mmc5/mmc5.dat
- Original transport source files: not found

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 1543
- Reaction count: 8743
- Message: CanteraError: ******************************************************************************* CanteraError thrown by newSolution: The CTI and XML formats are no longer supported. *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

### Mechanism 2

- Status: ok
- Species count: 1543
- Reaction count: 8743
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: not available

## Abstract

Exhaust gas recirculation (EGR) is widely used in advanced internal combustion engines to reduce engine emissions as well as control combustion phasing. Among various species present in EGR gases, CO2 and H2O are two major components that can thermally and chemically affect fuel autoignition. It is of fundamental interest to isolate the thermal and chemical effects of CO2 and H2O on fuel autoignition, especially as such an effort has not been reported in the literature. Moreover, nitric oxide (NO) is known to exhibit strong chemical effects on fuel autoignition, which in turn affects engine combustion phasing. The effects of ultra-low NO addition (< 100 ppm) on fuel autoignition at low temperatures are also not well understood. Recognizing these problems, autoignition experiments of iso-octane (a major gasoline surrogate component) in air are performed in this study using a rapid compression machine at varying compressed pressures, equivalence ratios, dilution levels with an EGR gas analogue (consisting of CO2, H2O, O2, and N2) and N2 only, and varying amounts of NO addition. The thermal and chemical effects of the EGR gas analogue are isolated and evaluated by comparing the ignition delay time datasets of EGR and N2-only diluted cases. It is found that the dilution/thermal effect on autoignition dominates at all test conditions, and the combined chemical effect of CO2 and H2O is insignificant. The NO doping experiments show that the promoting and inhibiting effects of NO addition on iso-octane ignition delay time are temperature dependent. Furthermore, a chemical kinetic model for gasoline surrogate components and NOx is developed by validating it against the experimental data obtained in this study and those available in the literature for various gasoline surrogate components. The validation of the model across different experimental datasets and for several fuels demonstrates its reliability and wide applicability in several operating conditions. Comparisons with previously developed models shed light on the gaps still present in understanding the effect of nitrogen species on the reactivity of gasoline surrogate molecules. Chemical kinetic analyses have also been conducted to identify the important reaction pathways controlling iso-octane autoignition at various conditions, and to elucidate the underlying mechanism leading to different reactivity trends at different NO doping levels and temperatures.

## Processing Notes

- extracted S0010218021005502_mmc4.zip
- extracted S0010218021005502_mmc2.zip
- extracted S0010218021005502_mmc6.zip
- extracted S0010218021005502_mmc5.zip
