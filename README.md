# KMeans-Implementacao

Implementação do algoritmo K-Means em Python

### Parâmetros
dados: DataSet em formato list
k: quantidade de clusters. Por padrão são 2

### Exemplo usando Pandas e CSV


import pandas as pd <br>
import KMeans

dataset = pd.read_csv('iris.csv') # Leitura do CSV\n
X = np.array(df).tolist() # Converter dataset em list\n
kmeans = KMeans(dados=X, k=3)\n

kmeans.train()\n
print(kmeans.labels())\n
