import pandas as pd

df = pd.read_csv("10.importing.csv")

# SELECTION BY COLUMN
print(df["Name"].to_string()) 
# Here we search for name column if you want another one do the same above
print(df["Height"].to_string())
# If we want multiple ones
print(df[["Name", "Height", "Weight"]].to_string())