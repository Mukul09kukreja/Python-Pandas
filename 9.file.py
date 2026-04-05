import pandas as pd

data = {"Name":["Spongbob", "Patrick", "Squidward"],
        "Age": [30, 35, 50]}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

# Add new rows
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                         {"Name": "Eugene", "Age": 60, "Job": "Manager"}], index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_rows])

print(df)