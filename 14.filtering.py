import pandas as pd

df = pd.read_csv("10.importing.csv")

# Filtering = keeping the rows that match a conditon

# tall_pokemon = df[df["Height"] >= 2]
heavy_pokemon = df[df["Weight"] > 100]
legendary_pokemon = df[df["Legendary"] == 1]
water_pokemon = df[(df["Type1"] == "Water") | # | means logical or 
                   (df["Type2"] == "Water")]


ff_pokemon = df[(df["Type1"] == "Fire") &
                (df["Type2"] == "Flying")]
# print(tall_pokemon)
print(heavy_pokemon)
print(legendary_pokemon)
print(water_pokemon)
print(ff_pokemon)
