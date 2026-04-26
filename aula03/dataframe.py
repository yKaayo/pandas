# %%
import pandas as pd

# %%
df = pd.read_csv("../data/clientes.csv", sep=";")

# %%
# Mostra alguns dados iniciais
df.head(n=10)

# Mostra alguns dados finais
df.tail()

# Mostra algum dado aleatório
df.sample(5)

# %%
# Exibe o número de linhas e colunas
df.shape

# Exibe os nomes das colunas
df.columns

# Exibe os índices
df.index

# %%
# Exibe o tipo de cada coluna
df.info(memory_usage="deep")
df.dtypes

# %%
