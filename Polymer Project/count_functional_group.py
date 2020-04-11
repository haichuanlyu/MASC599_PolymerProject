# Count chemical group in formula dataset
# Create by Haichuan Lyu

import numpy as np

# What chemical groups you want to investigate? Add them to the list below.
# Because by an unknown reason, python cannot count a string with '#', therefore,
# substitute all '#' to 'A', because 'A' does not exist in SMILES Strings
check_list = ['(C=CC3=CC=CC=C3)']  # 'CAN' here is 'C#N' actually

# File save location
txt_name = 'smiles_mod.txt'    # The text file storing SMILES
csv_name = 'functional_group_check.csv'     # Name of the csv file which stores the counting result
txt_loc = ''
csv_save_loc = ''


def count_chemical_group(formula, functional_group):
    """
    Using sliding window method to count functional group
    :type functional_group: the chemical group you want to count the appearing times
    :type formula: the formula you want to check
    :rtype: the appearing times of functional group in the formula
    """
    counter = 0
    formula_len = len(formula)
    group_len = len(functional_group)
    if 'R' not in functional_group:     # Normal condition
        for checker_loc in range(formula_len - group_len + 1):
            if formula[checker_loc: checker_loc + group_len] == functional_group:
                counter += 1
    else:
        # For count imide exclusive
        # Limitation: cannot deal with the situation that imide group appearing on R-group
        checker1_loc = 0
        checker2_loc = 6    # location is defined as number of char ahead of checker1
        # XXXXXXXXXXC(=O)N(XXXXX)C(=O)XXXXXXXXXX
        #           1-----       2----             1 -> check 6 char, 2 -> check 5 char
        while checker1_loc < formula_len - 11 + 1:
            if formula[checker1_loc: checker1_loc + 6] == 'C(=O)N':
                while checker1_loc + checker2_loc + 5 < formula_len + 1:
                    if formula[checker1_loc + checker2_loc: checker1_loc + checker2_loc + 5] == 'C(=O)':
                        counter += 1
                        checker2_loc = 6  # Reset checker2_loc
                        checker1_loc += checker2_loc + 10  # Remind that checker1_loc += 1 when out of while loop
                        break
                    checker2_loc += 1
            checker1_loc += 1
    return counter


# Import all formula into a numpy list
all_formula_list = np.genfromtxt(f'{txt_loc}{txt_name}', dtype='str')

# Initialize result list to [[], [], [], [], ...], which is 1276 [] in a []
result = []
for i in range(len(all_formula_list)):
    result.append([])

# Main function
# For all 1276 subarray, the storing result follows:
# [index, number_of_first_group, number_of_second_group, number_of_third_group, ...]
for i in range(len(all_formula_list)):
    result[i].append(str(i + 1))  # index start with 1
    for j in range(len(check_list)):
        result[i].append(count_chemical_group(all_formula_list[i], check_list[j]))
    print(f'{i + 1} formula checked.')

# Write to csv file
col_number = len(check_list) + 1
# If csv file not exist, create one
open(f'{csv_save_loc}{csv_name}', 'w').close()
# Write first line to csv file
csv_file = open(f'{csv_save_loc}{csv_name}', 'a')
csv_file.write('Index,')
for i in range(col_number - 1):
    csv_file.write(f'{check_list[i]}')
    if i < col_number - 2:
        csv_file.write(',')
# Write the count result into csv file
csv_file.write('\n')
for i in range(len(all_formula_list)):
    for j in range(0, col_number):
        csv_file.write(f'{result[i][j]}')
        if j < col_number - 1:
            csv_file.write(',')
    csv_file.write('\n')
csv_file.close()
print('Write result to csv file finished.')
