# Searching in csv
import pandas as pd

df = pd.read_csv("10.importing.csv", index_col="Name")

pokemon = input("Enter a pokemon name")

try:
  print(df.loc[pokemon])
except KeyError:
  print(f"{pokemon} not found")