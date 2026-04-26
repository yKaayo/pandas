# %%
import pandas as pd

# %%
df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %%
newDf = df.rename(columns={"DtCriacao": "DataCriacao"})
newDf

# %%
