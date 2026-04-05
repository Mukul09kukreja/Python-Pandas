import pandas as pd

data = {"Name":["Spongbob", "Patrick", "Squidward"],
        "Age": [30, 35, 50]}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

# Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

# Add a new row
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}], index=["Employee 4"])
# Here we made a new Dataframe for a new person added to list and here we use list within dictionary to handle multiple dictionary and it confuse less
df = pd.concat([df, new_row]) # It means to add new row in existing row and column data frame df

print(df)
print(new_row)