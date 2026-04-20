# %%
import pandas as pd

# %%
nums = [1, 5, 6, 3, 7, 8, 4, 565, 7, 3, 24, 63, 787, 678, 98, 54, 908, 351, 35]

series = pd.Series(nums)

"""
O índice fica atrelada ao valor, mesmo se houver uma ordenação, o índice não se altera, ou seja, o índice é fixo com o valor.
"""
# %%
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
names = pd.Series(nums, index=indexs)
names

# %%
# Pegar o primeiro elemento
names.iloc[0]

# %%
# Pegar o último elemento
names.iloc[-1]

# %%
# Pegar o elemento usando o índice
names.loc["Carlos"]
