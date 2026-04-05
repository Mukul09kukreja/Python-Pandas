import pandas as pd

data = ("Bulbanesaur", "Ivysaur", "Venusar", "Charmander", "Charmeleon", "Charizard")

series = pd.Series(data, index=[1,2,3,4,5,6])

series.iloc[2] = "Donkey"
print(series)