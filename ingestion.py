import os
import csv
import pandas as pd


def read_file(folder_path):
    file_name = os.listdir(folder_path)[0]

    with open(os.path.join(folder_path, file_name), 'r') as file:
        if file_name.endswith(".csv"):
            reader = csv.DictReader(file)
            contents = list(reader)
        else:
            raise ValueError("Unsupported file type!")
    return pd.DataFrame(data=contents)
