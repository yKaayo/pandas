# %%
import pandas as pd

# %%
df = pd.read_csv("../data/clientes.csv", sep=';')
df

# %%
df.to_parquet("clients.parquet", index=False)
df_parquet = pd.read_parquet("clients.parquet")
df_parquet

# %%
df.to_excel("clients.xlsx", index=False)
df_excel = pd.read_excel("clients.xlsx")
df_excel

# %%
url = "https://en.wikipedia.org/wiki/List_of_best-selling_singles"

dfs = pd.read_html(
    url,
    storage_options={
        "User-Agent": "Mozilla/5.0"
    }
)

dfs[6].to_csv("single.csv")
dfs[6]

# %%
