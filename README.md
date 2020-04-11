# Python Script for MASC599_PolymerProject


**count_functional_group.py** counts the appearing times of functional group in a SMILES string.
- For normal functional groups such as C(F)(F)(F) works well.
- Because of an unknown reason, python cannot count a string with '#', therefore, substitute all '#' to 'A', because 'A' does not exist in SMILES Strings.
- Possible to count the number of imide C(=O)N(R)C(=O) in SMILES string.


In Archive folder:
- **count_carbon_in_formula.py** checks the relation of index number and smiles_mod.txt by count the Carbon atom number in a SMILES string.
- **find_possible_functional_group.py** finds strings which are possibly appeared as functional groups in smiles_mod.txt. The goal of this process is to generate new features from SMILES strings.
