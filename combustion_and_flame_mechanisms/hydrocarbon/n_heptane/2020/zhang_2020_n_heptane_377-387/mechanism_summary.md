# A reduced reaction mechanism of biodiesel surrogates with low temperature chemistry for multidimensional engine simulation

## Bibliography

Lei Zhang, Xiaohua Ren, Zhigang Lan. A reduced reaction mechanism of biodiesel surrogates with low temperature chemistry for multidimensional engine simulation[J]. Combustion and Flame, 2020, 212: 377-387. DOI: 10.1016/j.combustflame.2019.11.002.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 212 / Feb
- Article number: 377-387
- DOI: 10.1016/j.combustflame.2019.11.002
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218019304997
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: n_heptane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: stirred reactor

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218019304997_mmc1/chem.inp
- Original thermodynamic source files: _processing/extracted/s0010218019304997_mmc1/therm.dat
- Original transport source files: _processing/extracted/s0010218019304997_mmc1/tran.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: not parsed
- Reaction count: not parsed
- Message: InputError: Error while reading reaction in chem.inp starting on line 62: """ h+o2(+M)<=>ho2(+M) 1.475E+12 0.60 0.0 low/ 0.34820E+17 -0.41100E+00 -0.11222E+04 / troe/ 0.50000E+00 0.10000E-29 0.10000E+31 0.10000+101 / h2 / 1.30/ h2o /14.00/ co / 1.90/ co2 / 3.80/ ch4 / 2.00/ c2h6/ 3.00/ """ could not convert string to float: '0.10000+101' Error while reading reaction in chem.inp starting on line 80: """ h2o2(+M)<=>oh+oh(+M) 2.951E+14 0.00 48430.0 low/ 0.12020E+18 0.00000E+00 0.45793E+05 / troe/ 0.50000E+00 0.10000E-29 0.10000E+31 0.10000+101 / h2 / 2.50/ h2o /12.00/ co / 1.90/ co2 / 3.80/ ch4 / 2.00/ c2h6/ 3.00/ """ could not convert string to float: '0.10000+101' Error while reading reaction in chem.inp starting on line 148: """ ch3o(+M)<=>ch2o+h(+M) 6.800E+13 0.00 26170.0 low/ 0.18670E+26 ... [truncated; see _processing logs]
- Method: cantera
- Cantera YAML: not available
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

A reduced biodiesel mechanism composed of 156 species and 589 reactions is reduced from an original complex mechanism (3299 species and 10806 reactions) based on MD, MD9D, and n-heptane as the surrogates. The mechanism reduction is conducted using the path flux analysis method, which considers multiple reaction path generations in the analysis of species interactions, and isomer lumping. Calculations of homogeneous auto-ignition and perfectly stirred reactor (PSR) combustion on a variety of reaction states, including pressures from 1 to 100 atm and equivalence ratios from 0.5 to 2, are the basis of the reduction. The initial temperatures are from 700 to 1800 K for the auto-ignition, and the inlet temperature is 300 K for the PSR. These reaction states cover the high-pressure and low-temperature operating conditions of future engines using advanced combustion technologies characterized by fuel–air premixing and auto-ignition. The fidelity of the resulting reduced mechanism with low-temperature chemistry is examined using a variety of applications. Close agreements between the reduced and original mechanisms are obtained in the predictions of ignition delay, history of mixture temperature, and species mole fraction during homogeneous auto-ignition and the temperature profile in PSR. The reduced mechanism, further integrated with a nitrogen oxides chemistry and a two-step soot model, is implemented into the KIVA/CHEMKIN program for the 3D simulation of biodiesel spray combustion. The predicted liquid and vapor penetrations agree with the experimental data in a non-reactive biodiesel spray simulation, indicating an accurate estimation of biodiesel physical properties. In the simulation of biodiesel spray combustion, predicted spatial distributions of hydroxyl radical and soot also agree with the corresponding experimental data.

## Processing Notes

- extracted S0010218019304997_mmc1.zip
