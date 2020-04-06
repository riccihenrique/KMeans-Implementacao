import math

class KMeans(object):    
    def __init__(self, dados, k=2):
        self.k = k
        self.dados = dados
        self.trata_dados() # Trata os dados caso haja campos que não sejam numéricos
        
    def train(self):
        centroids = []
        
        for i in range(self.k): #inicializa os centroids com os primeiros dados
            centroids.append([])            
            for j in range(len(self.dados[0])):
                centroids[i].append(self.dados[i][j])
        
        while True:            
            self.distancias = []

            for linha in range(len(self.dados)): # Para cada linha dos dados
                self.distancias.append([0] * (self.k + 1)) # K + 1 serve para adicionar uma coluna a mais para guardar o index da menor distância
                for centroids_index in range(self.k): # Para cada um dos centroids
                    distancia = 0
                    for coluna in range(len(self.dados[0])): # calcula-se a distancia de cada atributo
                        distancia += pow(centroids[centroids_index][coluna] - self.dados[linha][coluna], 2)

                    distancia = math.sqrt(distancia)
                    self.distancias[linha][centroids_index] = distancia

                #calcula o menor e armazena o index na ultima coluna
                self.distancias[linha][self.k] = self.distancias[linha].index(min(self.distancias[linha][ : self.k]))
            
            #calcula novo centroids            
            novos_centroids = [[]] * self.k
            count_centroids = [0] * self.k            

            for i in range(len(self.dados)):
                if(novos_centroids[self.distancias[i][self.k]] == []):
                    novos_centroids[self.distancias[i][self.k]] = [0] * len(self.dados[0])        
                for j in range(len(self.dados[0])):
                    novos_centroids[self.distancias[i][self.k]][j] += self.dados[i][j]                
                
                count_centroids[self.distancias[i][self.k]] += 1
            
            for i in range(self.k): 
                for j in range(len(self.dados[0])):
                    novos_centroids[i][j] /= count_centroids[i]
            
            if(novos_centroids == centroids): # Verifica se não há mais variações nos centorides
                break
            centroids = novos_centroids            
                    
    def labels(self):
        l = []
        for i in self.distancias:
            l.append(i[self.k])
        
        return l
    
    def trata_dados(self):
        for i in range(len(self.dados[0])):
            if(not (type(self.dados[0][i]) == int or type(self.dados[0][i]) == float)):
                c = 0
                obj = {}
                for j in range(len(self.dados)):
                    if(obj.get(self.dados[j][i]) == None):
                        obj[self.dados[j][i]] = c
                        c += 1
                        
                    self.dados[j][i] = obj[self.dados[j][i]]
        
