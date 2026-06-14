# High temperature ignition of ammonia/di-isopropyl ketone: A detailed kinetic model and a shock tube experiment

## Bibliography

Qianjin Lin, Chun Zou, Lingfeng Dai. High temperature ignition of ammonia/di-isopropyl ketone: A detailed kinetic model and a shock tube experiment[J]. Combustion and Flame, 2023, 251: 112692. DOI: 10.1016/j.combustflame.2023.112692.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 251 / May
- Article number: 112692
- DOI: 10.1016/j.combustflame.2023.112692
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023000779
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: ammonia
- Plasma-related mechanism: no
- Validation reactor/type from abstract: shock tube, laminar flame speed

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/raw_downloads/S0010218023000779_mmc4.txt
- Original thermodynamic source files: _processing/raw_downloads/S0010218023000779_mmc6.txt
- Original transport source files: _processing/raw_downloads/S0010218023000779_mmc5.txt

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Ignoring redundant declaration for species 'HON' Ignoring redundant thermo data for species 'CHOCHO' starting on line 453 of therm.dat. Ignoring redundant thermo data for species 'HNO' starting on line 2390 of therm.dat. Ignoring redundant thermo data for species 'HONO' starting on line 2402 of therm.dat. Ignoring redundant thermo data for species 'N' starting on line 2418 of therm.dat. Ignoring redundant thermo data for species 'H2NO' starting on line 2422 of therm.dat. Suppressed 20 additional warnings about redundant thermo data. Run ck2yaml again with the '--verbose' option to see all warnings. Unparsable lines while reading thermo data in therm.dat starting on line 2366: """ """ Lines could not be parsed as a NASA7 entry. Ignoring duplicate transport data for species "N" o ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Ignition delay times (IDTs) of NH3/di-isopropyl ketone (DIPK) mixtures with DIPK fractions of 0%, 5%, 10%, and 50% were measured in a shock tube at pressures around 1.75 and 10bar, temperatures from 1300 to 2100 K, and an equivalence ratio of 0.5. A DIPK-NH3 model was proposed including the DIPK sub-model, NH3 sub-model, and reactions between nitrogen-containing species and hydrocarbon species. The proposed DIPK-NH3 model well predicts the IDTs measured in this study, and the IDT and laminar flame speed data of pure NH3 and pure DIPK reported in the literature. The reactions between nitrogen-containing species and hydrocarbon species consist of four reaction classes: (1) prompt NO and reburn mechanism; (2) recombination reactions and small amines mechanisms; (3) H-abstraction reactions; (4) disproportionation reactions. Reaction classes 1–4 were successively added into a combined NH3 and DIPK model. Comparison of the model predictions shows that the reaction class 1 and 2 have almost no influence on the ignition, while class 3 inhibits the ignition and class 4 significantly inhibits the ignition. The ignition inhibiting effects of class 3 mainly come from C3H6+NH2=C3H5-A+NH3 (R3032) at DIPK blending ratio of 5% and 10%, and C2H4+NO=C2H3+HNO (R3058) at DIPK blending ratio of 50% and 10 bar. The ignition inhibiting effects of class 4 mainly come from HCO+NH2=CO+NH3 (R3050), C2H3+NH2=C2H2+NH3 (R3047), and NH2+C3H5-A=C3H4-A+NH3 (R3065) at DIPK blending ratio of 5% and 10%, and C3H5-A+NO=C3H4-A+HNO (R3067) at DIPK blending ratio of 50% and 10 bar. The NH3/DIPK oxidation pathway and effects of DIPK blending ratio on the IDT of NH3 were also analyzed in detail.

## Processing Notes

- extracted S0010218023000779_mmc3.xlsx
- extracted S0010218023000779_mmc1.docx
- extracted S0010218023000779_mmc2.docx
