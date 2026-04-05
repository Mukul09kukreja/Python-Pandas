import pandas as pd

# aggregation functions = Reduce a set of values into a single summary value
#                         Used to summarize and analyze data
#                         Often used with groupby() function

df = pd.read_csv("10.importing.csv")

# Whole dataframe
print(df.mean(numeric_only= True)) # It is used to find mean of numeric column
print(df.sum(numeric_only= True)) # Sum of the numeric column
print(df.min(numeric_only= True)) # min value of numeric column
print(df.max(numeric_only= True)) # max value of numeric column
print(df.count())

# Single column
print(df["Height"].mean()) # It is used to find mean of numeric column
print(df["Height"].sum()) # Sum of the numeric column
print(df["Height"].min()) # min value of numeric column
print(df["Height"].max()) # max value of numeric column
print(df["Height"].count())

# Group by object
group = df.groupby("Type1")

print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())