# %%
import pandas as pd

# %%
df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %%
df.info(memory_usage="deep")

# %%
df.dtypes

# %%
df["IdCliente"]

# %%
df[["IdCliente", "QtdePontos"]]

# %%
df[["IdCliente", "QtdePontos"]].head()
# %%
