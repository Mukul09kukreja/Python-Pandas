import pandas as pd

calories = {"Day1": 1750,
            "Day2": 2100,
            "Day3": 1700,
            }

series = pd.Series(calories)
# So here we don't need to use index because we are using dictionaries

series.loc["Day3"] += 500

print(series)