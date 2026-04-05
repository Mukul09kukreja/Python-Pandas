# Dataframes = A tabular data structure with row AND columns. (2 Dimensionals)
#              Similar to an Excel spreadsheet
import pandas as pd

data = {"Name":["Spongbob", "Patrick", "Squidward"],
        "Age": [30, 35, 50]}

df = pd.DataFrame(data, index=["Employee 1", "Emploayee 2", "Emploayee 3"])

print(df)
'''
Output:
    Name    Age
0   Spongbob    30
1   Patrick   35
2   Squidward   50
'''
print(df.loc["Emploayee 3"])
print(df.iloc[1])