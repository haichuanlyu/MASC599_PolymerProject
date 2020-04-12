import numpy as np
import pandas as pd

basic_csv_path_and_name = 'polymer_project_dataset_Ver4.0(basic).csv'
basic_save_path = 'polymer_project_dataset_Ver4.0_deduplicate(basic).csv'
compound_csv_path_and_name = 'polymer_project_dataset_Ver4.0(compound).csv'
compound_save_path = 'polymer_project_dataset_Ver4.0_deduplicate(compound).csv'


def main(csv_path_and_name, save_path):
    csv_file = pd.read_csv(csv_path_and_name)
    res = csv_file.groupby('PROPERTY: SMILES').aggregate(np.mean)
    res.to_csv(save_path)


main(basic_csv_path_and_name, basic_save_path)
main(compound_csv_path_and_name, compound_save_path)
