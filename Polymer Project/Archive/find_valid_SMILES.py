import numpy as np

# File save location
txt_name = 'smiles_mod.txt'  # The text file storing SMILES
csv_name = 'smiles_mod_deduplicate.txt'  # Name of the csv file which stores the counting result
txt_loc = ''
csv_save_loc = ''

# Import all formula into a numpy list
all_formula_list = np.genfromtxt(f'{txt_loc}{txt_name}', dtype='str')
print(len(all_formula_list))
# valid_result = set(all_formula_list)
#
# open(f'{csv_save_loc}{csv_name}', 'w').close()
# txt_result = open(f'{csv_save_loc}{csv_name}', 'a')
# for i in valid_result:
#     txt_result.write(f'{i}\n')
#
# print(len(valid_result))

valid_dict = {}
valid_number = 0
i = 0
while i < len(all_formula_list):
    if all_formula_list[i] not in valid_dict:
        valid_dict[all_formula_list[i]] = 1
    else:
        valid_dict[all_formula_list[i]] += 1
    i += 1
print(len(valid_dict))
