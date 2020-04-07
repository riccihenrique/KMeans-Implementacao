# KMeans-Implementação

Implementação do algoritmo K-Means em Python

### Parâmetros
dados: DataSet em formato list
k: quantidade de clusters. Por padrão são 2


### Exemplo usando Pandas e CSV (Não esqueça de instalar as dependências)

import pandas as pd <br>
import numpy as np <br>
from KMeans import KMeans <br>

dataset = pd.read_csv('iris.csv') # Leitura do CSV <br>
X = np.array(dataset).tolist() # Converter dataset em list <br>
kmeans = KMeans(dados=X, k=3) <br>

kmeans.train() <br>
print(kmeans.labels()) <br>


### Dependências
pip install numpy <br>
pip install pandas <br>
