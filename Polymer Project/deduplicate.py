import pandas as pd

csv_path_and_name = 'polymer_project_dataset_Ver4.0(basic).csv'
save_path = 'polymer_project_dataset_Ver4.0_deduplicate(basic).csv'

csv_file = pd.read_csv(csv_path_and_name)
csv_result = csv_file.iloc[0:0, :].copy
for i in range(1276):
    pass
print(csv_result)
