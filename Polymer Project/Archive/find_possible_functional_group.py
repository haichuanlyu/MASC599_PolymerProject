# Finds strings which are possibly appeared as functional groups in smiles_mod.txt.
# The goal of this process is to generate new features from SMILES strings.

import numpy as np

# File save location
csv_save_loc = 'dic_csv.csv'
csv_check_paren_save_loc = 'dic_check_().csv'
txt_loc = 'smiles_mod.txt'

# Import all formula into a numpy list
all_formula_list = np.genfromtxt(txt_loc, dtype='str')

# test case
# formula = 'C=CC1C2C(=O)N(C(C)(C)(C))C(=O)C2C(C=CC2C3C(=O)N(C(C)(C)(C))' \
#           'C(=O)C3C(C=CC3=CC=CC=C3)N2(C(C)(C)(C)))N1(C(C)(C)(C))'

possible_functional_group = {}    # Dictionary: keywords: possible functional group, value: appearing times
# Functional group cannot start with following char
no_functional_group_start = [')', '=', 'A', '1', '2', '3', '4', '5', '6']
# Functional group cannot end with following char
no_functional_group_end = ['(', '=', 'A']


def first_paren_is_right(sth):
    k = 0
    while k < len(sth):
        if sth[k] == ')':
            return True
        if sth[k] == '(':
            return False
        k += 1
    return False


def last_paren_is_left(sth):
    k = len(sth) - 1
    while k >= 0:
        if sth[k] == '(':
            return True
        if sth[k] == ')':
            return False
        k -= 1
    return False


def valid_parenthesis_conf(sth):
    if first_paren_is_right(sth):
        return False
    if last_paren_is_left(sth):
        return False
    # if at the left part of any position, num of "(" is less than ")", not valid
    left_par_counter = 0
    right_par_counter = 0
    for pointer in range(len(sth)):
        if sth[pointer] == "(":
            left_par_counter += 1
        if sth[pointer] == ")":
            right_par_counter += 1
        if right_par_counter > left_par_counter:
            return False
    # if num of "(" != ")", not valid
    if left_par_counter != right_par_counter:
        return False
    return True


# Main Function
num_of_formula_counter = 0
for formula in all_formula_list:
    for i in range(0, len(formula)):
        # if start with these char, not possible functional group
        if formula[i] in no_functional_group_start:
            continue
        for j in range(i + 1, len(formula)):
            possible_str = formula[i:j]

            # if end with these char, not possible functional group
            if possible_str[-1] in no_functional_group_end:
                continue
            # not possible functional group
            if not valid_parenthesis_conf(possible_str):
                continue

            # Set value in dictionary
            if possible_str in possible_functional_group:
                possible_functional_group[possible_str] += 1
            else:
                possible_functional_group[possible_str] = 1

    # Show running status
    num_of_formula_counter += 1
    print(f'{num_of_formula_counter} formula finished.')
    print(f'Now the dict is {len(possible_functional_group)} long.')

# Only show (XXX) format
possible_functional_group_in_parenthesis = {}
for group in possible_functional_group:
    if len(group) >= 3 and group[1] == "(" and group[-1] == ")" and possible_functional_group[group] > 5:
        if group.count("C(=O)") % 2 == 1:
            continue
        possible_functional_group_in_parenthesis.update({group: possible_functional_group[group]})


# Save result to csv file
open(csv_save_loc, 'w').close()
open(csv_check_paren_save_loc, 'w').close()
csv_file = open(csv_save_loc, 'a')
for group in possible_functional_group:
    csv_file.write(f'{group},{possible_functional_group[group]}\n')
csv_file.close()
csv_file = open(csv_check_paren_save_loc, 'a')
for group in possible_functional_group_in_parenthesis:
    csv_file.write(f'{group},{possible_functional_group_in_parenthesis[group]}\n')
