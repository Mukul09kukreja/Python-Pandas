import pandas as pd

data = [100, 102, 104, 200, 202]

series = pd.Series(data, index=["a", "b", "c", "d", "e"])

print(series[series >= 200])
# This is represent like series[condition]
# Flow is if condition --> series