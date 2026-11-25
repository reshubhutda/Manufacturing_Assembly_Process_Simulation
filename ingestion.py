import os
import csv
import pandas as pd

file_path = r"C:\Users\reshu\Downloads\mes"
file_name = os.listdir(file_path)[0]

with open(os.path.join(file_path, file_name), 'r') as file:
    if file_name.endswith(".txt"):
        contents = file.readlines()
    else:
        reader = csv.DictReader(file)
        contents = list(reader)

data = pd.DataFrame(data=contents)