# SELECTION BY ROWS
import pandas as pd

df = pd.read_csv("10.importing.csv", index_col="Name")

print(df.loc["Pikachu"])
print(df.loc["Charizard", ["Height", "Weight"]])
# here in chrizard we only display height and weight

# Slicing
print(df.loc["Charizard":"Blastoise"])

print(df.iloc[0:11:2, 0:3])# 0:3 is for coloumn