# Machine learned compact kinetic models for methane combustion

## Bibliography

Mark Kelly, Mark Fortune, Gilles Bourque, Stephen Dooley. Machine learned compact kinetic models for methane combustion[J]. Combustion and Flame, 2023, 253: 112755. DOI: 10.1016/j.combustflame.2023.112755.

## Metadata

- Journal: Combustion and Flame
- Volume/issue month: 253 / July
- Article number: 112755
- DOI: 10.1016/j.combustflame.2023.112755
- ScienceDirect URL: https://www.sciencedirect.com/science/article/pii/S0010218023001396
- Paper PDF: pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed
- Paper PDF link: 
- Fuel type: methane
- Plasma-related mechanism: no
- Validation reactor/type from abstract: not clear from abstract

## Mechanism Files

- Standard mechanism file: chem.inp
- Standard thermodynamic file: therm.dat
- Standard transport file: tran.dat
- Original mechanism source files: _processing/extracted/s0010218023001396_mmc1/Machine Learned Compact Models for Methane Combustion Supplemental Material/Model Files/NUIGMECH1.0_15sOp.cti, _processing/extracted/s0010218023001396_mmc1/Machine Learned Compact Models for Methane Combustion Supplemental Material/Model Files/NUIGMECH1.0_15sOp.inp
- Original thermodynamic source files: _processing/extracted/s0010218023001396_mmc1/Machine Learned Compact Models for Methane Combustion Supplemental Material/Model Files/therm.dat, _processing/extracted/s0010218023001396_mmc1/Machine Learned Compact Models for Methane Combustion Supplemental Material/Model Files/NUIGMECH1.0_15sOp.cti
- Original transport source files: _processing/extracted/s0010218023001396_mmc1/Machine Learned Compact Models for Methane Combustion Supplemental Material/Model Files/NUIGMECH1.0_15sOp.cti, _processing/extracted/s0010218023001396_mmc1/Machine Learned Compact Models for Methane Combustion Supplemental Material/Model Files/tran.dat

## Cantera Preprocessing Results

### Mechanism 1

- Status: cantera_failed
- Species count: 15
- Reaction count: not parsed
- Message: CanteraError: ******************************************************************************* CanteraError thrown by newSolution: The CTI and XML formats are no longer supported. *******************************************************************************
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

### Mechanism 2

- Status: ok
- Species count: 15
- Reaction count: 60
- Message: cantera conversion ok
- Method: cantera
- Cantera YAML: mechanism.yaml
- Standard chem.inp: chem.inp
- Standard therm.dat: therm.dat
- Standard tran.dat: tran.dat

## Abstract

Chemical kinetic models are an essential component in the development and optimisation of combustion devices through their coupling to multi-dimensional simulations such as computational fluid dynamics (CFD). Due to the significant level of detail contained within, detailed chemical kinetic models are computationally prohibitive for use in CFD. Therefore, low-dimensional kinetic models which retain good fidelity to the reality are needed, the production of which requires considerable human-time cost and expert knowledge. Here, we present a novel automated compute intensification methodology to produce overly-reduced and optimised (“compact”) chemical kinetic models. The Machine Learned Optimisation of Chemical Kinetics (MLOCK) coded algorithm systematically perturbs each of the four chemical kinetic model components to discover what combinations of terms results in a model with high fidelity calculations. A virtual reaction network comprised of n species is first obtained using conventional mechanism reduction procedures. Once n is lower than a threshold value, the model performance is typically of low fidelity. To adjust for this, the weights (virtual reaction rate constants) of important connections (virtual reactions) between each node (species) of the virtual reaction network are numerically optimised across four sequential phases to replicate select calculations. The first version of MLOCK (MLOCK1.0), simultaneously perturbs all three virtual Arrhenius reaction rate constant parameters for important connections and assesses the suitability of the new parameters through objective error functions, which quantify the error in the calculations of each model candidate to a set of optimisation targets, comprised of detailed model calculations. In this study, the MLOCK algorithm is demonstrated by automatic creation of compact models for the archetypal case of methane/air combustion. It is shown that the NUGMECH1.0 detailed model comprised of 2789 species is reliably compacted to 15 species (nodes), whilst retaining an overall fidelity of 79–90% to the detailed model at Industry-defined performance target calculations, outperforming the prior state-of-art.

## Processing Notes

- extracted S0010218023001396_mmc1.zip
- extracted Supplemental Bound Refinement.docx
