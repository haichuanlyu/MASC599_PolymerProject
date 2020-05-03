import numpy as np
import pandas as pd

csv_path_and_name = 'polymer_project_dataset_Ver5.0.csv'
save_path = 'polymer_project_dataset_(deduplicate)_Ver5.0.csv'

# alias
DC = 'PROPERTY: Dielectric Constant'
SMILES = 'PROPERTY: SMILES'

csv_file = pd.read_csv(csv_path_and_name)

appear_dict = {}  # key: SMILES, value: [index in res, appear times]
res = pd.DataFrame(columns=csv_file.columns)

res_index = 0  # index of result DataFrame
for i in range(len(csv_file)):
    current_SMILES = csv_file.iloc[i][SMILES]
    if current_SMILES not in appear_dict:
        appear_dict[current_SMILES] = [res_index, 1]  # input a new element into appear_dict
        res.loc[res_index] = csv_file.iloc[i]
        res_index += 1
    else:
        index_in_res = appear_dict[current_SMILES][0]
        times = appear_dict[current_SMILES][1]
        cur_dc = res.loc[index_in_res][DC]
        updated_dc = (cur_dc * times + csv_file.loc[i][DC]) / (times + 1)
        res.at[index_in_res, DC] = updated_dc
        appear_dict[current_SMILES][1] = times + 1
    print(f'{i + 1} formula checked and get {res_index} results.')
res.to_csv(save_path)



