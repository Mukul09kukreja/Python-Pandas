import pandas as pd

df = pd.read_csv("10.importing.csv") # .read_csv is to read the csv file

print(df.to_string()) # .to_string helps to read all data not know first five and last five identity

df1 = pd.read_json("10.importing.json")
print(df1)