# Count the Carbon number in a SMILES string
# Check the relation of index number and smiles_mod.txt

import pandas as pd

txt_loc_with_name = 'smiles_mod.txt'
a = pd.read_csv(txt_loc_with_name, header=None)
b = a.values.tolist()
c = []
for i in b:
    counter = 0
    for j in i[0]:
        if j == 'C':
            counter += 1
    c.append(counter)
print(c)
# If csv file not exist, create one
open('count_carbon_num.csv', 'w').close()
csv_file = open('count_carbon_num.csv', 'a')
for i in range(0, len(c)):
    csv_file.write(f'{c[i]}')
    csv_file.write(',\n')
csv_file.close()


