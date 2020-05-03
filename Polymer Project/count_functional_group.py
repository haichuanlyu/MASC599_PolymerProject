# Count chemical group in formula dataset
# Create by Haichuan Lyu

import numpy as np

# What chemical groups you want to investigate? Add them to the list below.
# Because by an unknown reason, python cannot count a string with '#', therefore,
# substitute all '#' to 'A', because 'A' does not exist in SMILES Strings
# 'CAN' here is 'C#N' actually

# for basic functional groups check
check_list_basic = [
    'UID1', 'O1', 'O2',  # =sum
    'UID2', 'S1', 'S2',  # =sum
    'UID3', 'N2', 'N1',  # =sum
    'N2(C(C)(C)(C))', 'N1(C(C)(C)(C))',  # -UID22 (2 sub conditions)
    'UID4', 'C3=CC=CC=C3', 'C4=CC=CC=C4',  # =sum
    'CAN',  # UID5
    'UID6', 'C(F)(F)(F)', 'C(F)(F)F',  # =sum
    'UID7', 'C(C)(C)(C)',  # =sum
    'UID8', 'C45CC6CC(CC(C6)C4)C5', 'C34CC5CC(CC(C5)C3)C4', 'C23CC4CC(C2)CC(C4)C3', 'C12CC3CC(CC(C3)C1)C2',  # =sum
    'C(=O)N(R)C(=O)',  # = num - UID(12,13,14,15,16,17,18,19)
]

# for compound functional groups check
check_list = [
    'UID1', 'O1', 'O2',  # = sum
    'UID2', 'S1', 'S2',  # = sum
    'UID3', 'N2', 'N1', 'C3CN()CC3', 'C2CN()CC2',  # = sum
    'N2(C(C)(C)(C))', 'N1(C(C)(C)(C))', 'N2(C)', 'N1(C)',  # -UID22 (2 sub conditions), UID 21 (2 sub conditions)
    'UID4', 'C3=CC=CC=C3', 'C4=CC=CC=C4',  # = sum - UID10 - UID11
    'C2C(=O)N(C3=CC=CC=C3)C(=O)C2', 'C3C(=O)N(C4=CC=CC=C4)C(=O)C3',  # -UID16
    'CAN',  # UID5
    'UID6', 'C(F)(F)(F)', 'C(F)(F)F',  # = sum - UID15 - UID18 - UID24 - UID26
    'UID7', 'C(C)(C)(C)',  # = sum - UID14 - UID22
    'UID8', 'C45CC6CC(CC(C6)C4)C5', 'C34CC5CC(CC(C5)C3)C4', 'C23CC4CC(C2)CC(C4)C3',
    'C12CC3CC(CC(C3)C1)C2',  # = sum - UID19 - UID20
    'C(=O)N(R)C(=O)',  # = num - UID(12,13,14,15,16,17,18,19)
    'C=CC3=CC=CC=C3',  # UID 10
    '/C=C/C3=CC=CC=C3',  # UID 11
    'UID12', 'C3C(=O)N()C(=O)C3', 'C2C(=O)N()C(=O)C2',  # = sum
    'UID13', 'C3C(=O)N(C)C(=O)C3', 'C2C(=O)N(C)C(=O)C2',  # = sum
    'UID14', 'C3C(=O)N(C(C)(C)(C))C(=O)C3', 'C2C(=O)N(C(C)(C)(C))C(=O)C2',  # = sum
    'UID15', 'C3C(=O)N(C(F)(F)(F))C(=O)C3', 'C2C(=O)N(C(F)(F)(F))C(=O)C2',  # = sum
    'UID16', 'C2C(=O)N(C3=CC=CC=C3)C(=O)C2', 'C3C(=O)N(C4=CC=CC=C4)C(=O)C3',  # = sum
    'UID17', 'C2C(=O)N(C3=CC=C(CAN)C=C3)C(=O)C2', 'C3C(=O)N(C4=CC=C(CAN)C=C4)C(=O)C3',  # = sum
    'UID18', 'C2C(=O)N(C3=CC=C(C(F)(F)F)C=C3)C(=O)C2', 'C3C(=O)N(C4=CC=C(C(F)(F)F)C=C4)C(=O)C3',  # = sum
    'UID19', 'C2C(=O)N(C34CC5CC(CC(C5)C3)C4)C(=O)C2', 'C3C(=O)N(C45CC6CC(CC(C6)C4)C5)C(=O)C3',  # = sum
    'UID20', 'C3CN(C45CC6CC(CC(C6)C4)C5)CC3', 'C2CN(C34CC5CC(CC(C5)C3)C4)CC2',  # = sum
    'UID21', 'C2CN(C)CC2', 'C3CN(C)CC3', 'N2(C)', 'N1(C)',  # = sum
    'UID22', 'N2(C(C)(C)(C))', 'N1(C(C)(C)(C))', 'C3CN(C(C)(C)(C))CC3', 'C2CN(C(C)(C)(C))CC2',  # = sum
    'UID23', 'C3CN(C4=CC=CC=C4)CC3', 'C2CN(C3=CC=CC=C3)CC2',  # =sum
    'UID24', 'C2CN(C3=CC=C(C(F)(F)F)C=C3)CC2', 'C3CN(C4=CC=C(C(F)(F)F)C=C4)CC3',  # = sum
    'UID25', 'C2CN(C3=CC=C(CAN)C=C3)CC2', 'C3CN(C4=CC=C(CAN)C=C4)CC3',  # = sum
    'UID26', 'C2CN(C(F)(F)(F))CC2', 'C3CN(C(F)(F)(F))CC3',  # = sum
    'C(F)(F)C',  # UID27
    'C(F)C',  # UID28
]

# File save location
txt_name = 'smiles_mod.txt'  # The text file storing SMILES
csv_name = 'functional_group_check.csv'  # Name of the csv file which stores the counting result
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
    if 'R' not in functional_group:  # Normal condition
        for checker_loc in range(formula_len - group_len + 1):
            if formula[checker_loc: checker_loc + group_len] == functional_group:
                counter += 1
    else:
        # For count imide exclusive
        # Limitation: cannot deal with the situation that imide group appearing on R-group
        checker1_loc = 0
        checker2_loc = 6  # location is defined as number of char ahead of checker1
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
