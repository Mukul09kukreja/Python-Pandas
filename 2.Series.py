import pandas as pd

data = [100, 102, 104]

series = pd.Series(data) # This is a series constructor

print(series)
'''
Output: 
0   100
1   102
2   104
dtype: int64 # Here 64 is bit
'''
# dtype: float64
data1 = [100.1, 102.2, 104.3]

series1 = pd.Series(data1)
print(series1)

# dtype: str
data2 = ["A", "B", "C"]

series2 = pd.Series(data2)
print(series2)

# dtype: bool
data3 = [True, False, True]

series3 = pd.Series(data3)
print(series3)