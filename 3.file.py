import pandas as pd

data = [100, 102, 104]

# By using change the index of the series
series = pd.Series(data, index=["a", "b", "c"])

series.loc["c"] = 200

print(series) # loc means location by lable and it use to access the value
# Output of series.loc["a"] is 100

print(series.iloc[0]) # It access the value like list
# iloc called integer location or ocassion by value
# Output: 100