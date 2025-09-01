from collections import deque
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.visitado = []
        self.grafo = [[] for _ in range(self.vertices)]
        
    def adiciona_aresta(self, u, v):
        self.grafo[u-1].append(v)
        self.grafo[v-1].append(u)
        
        
    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo[i]:
                print(f' -> {j}', end='  ')
            print('')
         
    def buscaDFS(self):
        self.visitado = ['N' for _ in range(self.vertices)]
        
        for i in range(self.vertices):  # Itera sobre os vértices
            if self.visitado[i] == 'N':
                print(f'Iniciando DFS a partir do vértice {i+1}')
                self.buscaDFSProf(i)
                
    def buscaDFSProf(self, posicao):
        self.visitado[posicao] = 'S'
        print(f'Visitando vértice {posicao+1}')
        
        for i in self.grafo[posicao]:
            if self.visitado[i-1] == 'N':  # Corrige índice (i-1) para acessar corretamente
                self.buscaDFSProf(i-1)
# Exemplo de uso
    def buscaBFS(self, vertice_inicial):
        # Iniciando a lista de vértices visitados
        self.visitado = ['N' for _ in range(self.vertices)]
        
        # Inicializando a fila (queue) e marcando o vértice inicial como visitado
        fila = deque([vertice_inicial])
        self.visitado[vertice_inicial - 1] = 'S'
        print(f'Iniciando BFS a partir do vértice {vertice_inicial}')
        
        while fila:
            # Remove o vértice da fila (usamos o termo "desenfileirar")
            vertice_atual = fila.popleft()
            print(f'Visitando vértice {vertice_atual}')
            
            # Explorar os vértices adjacentes
            for vizinho in self.grafo[vertice_atual - 1]:
                if self.visitado[vizinho - 1] == 'N':
                    fila.append(vizinho)
                    self.visitado[vizinho - 1] = 'S'
                    print(f'Colocando vértice {vizinho} na fila')  
            
g = Grafo(12)
# 1
g.adiciona_aresta(1,2)
g.adiciona_aresta(1,4)
g.adiciona_aresta(1,5)
# 2
g.adiciona_aresta(2,5)
g.adiciona_aresta(2,7)
g.adiciona_aresta(2,3)
g.adiciona_aresta(2,9)
# 3
g.adiciona_aresta(3,12)
g.adiciona_aresta(3,6)
g.adiciona_aresta(3,10)
# 4
g.adiciona_aresta(4,5)
g.adiciona_aresta(4,7)
# 5
g.adiciona_aresta(5,8)
g.adiciona_aresta(5,6)
# 6
g.adiciona_aresta(6,9)
g.adiciona_aresta(6,11)
# 7
g.adiciona_aresta(7,8)
# 8
g.adiciona_aresta(8,9)
# 9
g.adiciona_aresta(9,12)
g.adiciona_aresta(9,10)
# 10
g.adiciona_aresta(10,11)
# 11
g.adiciona_aresta(11,12)



g.mostra_lista()