# KMeans-Implementacao

Implementação do algoritmo K-Means em Python

### Parâmetros
dados: DataSet em formato list
k: quantidade de clusters. Por padrão são 2

### Exemplo usando Pandas e CSV


import pandas as pd
import KMeans

dataset = pd.read_csv('iris.csv') # Leitura do CSV
X = np.array(df).tolist() # Converter dataset em list
kmeans = KMeans(dados=X, k=3)

kmeans.train()
print(kmeans.labels())
