# %%
import pandas as pd

# %%
df = pd.read_csv("../data/transacoes.csv", sep=";")

# %%
filter = df["QtdePontos"] >= 50
df[filter]

# %%
filter = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
df[filter]

# %%
filter = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filter]

# %%
df2 = pd.read_csv("../data/transacao_produto.csv", sep=";")
df2

# %%
filter2 = (df2["IdProduto"] == "5") | (df2["IdProduto"] == "11")
df2[filter2]

# %%
filter2 = df2["IdProduto"].isin(["5", "11"])
df2[filter2]

# ----------- 

# %%
clients = pd.read_csv("../data/clientes.csv", sep=";")

# %%
# True em valores nulos
clients["DtCriacao"].isna()

# %%
# False em valores nulos
clients["DtCriacao"].notna()

# ----------- 

# %%
# Não é criado uma cópia, mas sim uma referência
filter3 = clients["qtdePontos"] == 2
clients2 = clients[filter3]
clients2["blabla"] = "teste"

# %%
clients2.head()

# %%
clients.head()
