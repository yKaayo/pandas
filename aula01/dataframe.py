# %%
import pandas as pd

# %%
nums = [1, 5, 6, 3, 7, 8, 4, 565, 7, 3, 24, 63, 787, 678, 98, 54, 908, 351, 35]

#  %%
indexs = [
    "Ana",
    "Bruno",
    "Carlos",
    "Daniela",
    "Eduardo",
    "Fernanda",
    "Gabriel",
    "Helena",
    "Ígor",
    "Julia",
    "Kevin",
    "Larissa",
    "Mateus",
    "Natália",
    "Otávio",
    "Paula",
    "Ricardo",
    "Sara",
    "Thiago",
]

# %%
series = pd.Series(nums)
names = pd.Series(indexs)

# %%
df = pd.DataFrame()
df["Números"] = nums
df["Nomes"] = names
df

# %%
df.iloc[0]

# %%
df.index
