# Effect of trace amount of Nitric Oxide (NO) addition on ammonia autoignition in a rapid compression machine

## Bibliography

Gabriel J. Gotama, Yueying Liang, Liang Yu, Yongxiang Zhang, ... Xingcai Lu. Effect of trace amount of Nitric Oxide (NO) addition on ammonia autoignition in a rapid compression machine[J]. Combustion and Flame, 2025, 277: 114182. DOI: 10.1016/j.combustflame.2025.114182.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 277 / July
- Article number: 114182
- DOI: 10.1016/j.combustflame.2025.114182
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218025002202
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: https://www.sciencedirect.com/science/article/pii/S0010218025002202/pdfft?md5=eccc6137a1c95ca944c7664963d1a17c&pid=1-s2.0-S0010218025002202-main.pdf
- Fuel type: ammonia_nitric_oxide
- Plasma-related mechanism: no
- Validation reactor/type from abstract: rapid compression machine

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218025002202_mmc1/Kinetic model/Mech-Thermo.inp
- Original thermodynamic source files: _processing/extracted/s0010218025002202_mmc1/Kinetic model/Mech-Thermo.inp
- Original transport source files: _processing/extracted/s0010218025002202_mmc1/Kinetic model/Transport.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 31
- Reaction count: 408
- Message: CanteraError: ******************************************************************************* CanteraError thrown by Kinetics::checkDuplicates: Error on lines 554 and 1554 of /home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms/ammonia_nitric_oxide/2025/gotama_2025_ammonia_nitric_oxide_114182/mechanism.yaml: Undeclared duplicate reactions detected: Reaction 1: H2 + M <=> 2 H + M Reaction 205: H2 + M <=> 2 H + M | Line | | 549 | geometry: linear | 550 | well-depth: 80.0 | 551 | diameter: 2.75 | 552 | | 553 | reactions: > 554 > - equation: H2 + M <=> 2 H + M # Reaction 1 ^ | 555 | type: three-body | 556 | rate-constant: {A: 4.577e+19, b: -1.4, Ea: 1.044e+05} | 557 | efficiencies: {H2: 2.5, H2O: 12.0, HE: 0.83} ... | 1549 | R0203 | 1550 | - equation: HONO2 + OH <=> ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

not available

## Processing Notes

- extracted S0010218025002202_mmc2.xlsx
- extracted S0010218025002202_mmc1.zip
