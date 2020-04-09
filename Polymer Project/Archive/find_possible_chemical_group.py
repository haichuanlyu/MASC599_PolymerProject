import numpy as np

# File save location
csv_save_loc = 'dic_csv.csv'
txt_loc = 'smiles_mod.txt'

# Import all formula into a numpy list
all_formula_list = np.genfromtxt(txt_loc, dtype='str')

# test case
# formula = 'C=CC1C2C(=O)N(C(C)(C)(C))C(=O)C2C(C=CC2C3C(=O)N(C(C)(C)(C))' \
#           'C(=O)C3C(C=CC3=CC=CC=C3)N2(C(C)(C)(C)))N1(C(C)(C)(C))'

possible_functional_group = {}    # Dictionary: keywords: possible functional group, value: appearing times
# Functional group cannot start with following char
no_functional_group_start = ['(', ')', '=', '#', '1', '2', '3', '4']
# Functional group cannot end with following char
no_functional_group_end = ['(', ')', '=', '#']


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
            # num of '(' not equals ')', not possible functional group
            if possible_str.count('(') != possible_str.count(')'):
                continue
            # First appearing parenthesis is ')'，not possible functional group
            if first_paren_is_right(possible_str):
                continue
            # Last appearing parenthesis is '('，not possible functional group
            if last_paren_is_left(possible_str):
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


# Save result to csv file
open(csv_save_loc, 'w').close()
csv_file = open(csv_save_loc, 'a')
for i in possible_functional_group:
    csv_file.write(f'{i},{possible_functional_group[i]}\n')
