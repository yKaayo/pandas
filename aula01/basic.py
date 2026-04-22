# %%
import pandas as pd

# %%
nums = [1, 5, 6, 3, 7, 8, 4, 565, 7, 3, 24, 63, 787, 678, 98, 54, 908, 351, 35]

series = pd.Series(nums)

# %%
media = series.mean()
media

# %%
variancia = series.var()
variancia

# %%
summary = series.describe()
summary
