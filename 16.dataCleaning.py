import pandas as pd

# Data cleaning = the process of fixing/removing:
#                 incomplete, incorrect, or irrelevant data.
#                 ~75% of work done with pandas is data cleaning

df = pd.read_csv("10.importing.csv")

# 1. Drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"]) # It is droping the column name legendary

# 2. Handle missing data
# df = df.dropna(subset=["Type2"]) # It is droping the missing value
df = df.fillna({"Type2": "None"}) # It is filling the missing values

# 3. Fix inconsistent values
df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
                                   "Fire": "FIRE",
                                   "Water": "WATER"})

# 4. Standardize text
df["Name"] = df["Name"].str.lower()

# 5. Fix or change Data types
df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicates Values
df = df.drop_duplicates()

print(df.to_string())