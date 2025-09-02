from collections import deque


class GrafoPageRank:
    def __init__(self, __qtdPaginas):
        self.__qtdPaginas = __qtdPaginas
        self.__fatorDeAmortecimento = 0.85
        self.__links = [""] *  self.__qtdPaginas
        self.__mensagens = [""] * self.__qtdPaginas
        self.__paginasApontam  = [[] for _ in range(self.__qtdPaginas)]
        self.__grafo = [[] for _ in range(self.__qtdPaginas)]
        
        
    def adiciona_aresta(self, u, v):
        # Apenas um sentido (u -> v)
        if u > self.__qtdPaginas or v > self.__qtdPaginas:
            print(f"Erro: Vértice {u} ou {v} fora do intervalo de 1 a {self.__qtdPaginas}")
            return
        self.__grafo[u-1].append(v)
        self.__paginasApontam[v-1].append(u)
    
    


    def calcular_pagerank_completo(self,numero_de_iteracoes=20):
        parte1 = (1 - self.__fatorDeAmortecimento) / self.__qtdPaginas
        importancia_anterior = [1/self.__qtdPaginas]  * self.__qtdPaginas
        print(f'Probabilidade Inicial = {importancia_anterior}')
        for _ in range(numero_de_iteracoes):
            importancia_atual = [0.0] * self.__qtdPaginas
            for posicao in range(self.__qtdPaginas):
                soma_das_importancias = 0.0
                for apontam in self.__paginasApontam[posicao]:
                    pr_apontam = importancia_anterior[apontam - 1]
                    links_de_saida = len(self.__grafo[apontam - 1])
                    soma_das_importancias += pr_apontam / links_de_saida 

                parte2_calculada = self.__fatorDeAmortecimento * soma_das_importancias
                importancia_atual[posicao] = parte1 + parte2_calculada
            
            importancia_anterior = importancia_atual
            print(f'Iteração {_+1} = {[(i+1,importancia_atual[i]) for i in range(len(importancia_atual)-1)]}')
        rankeamento = sorted(
                        [(i+1, importancia_atual[i]) for i in range(len(importancia_atual))],
                        key=lambda x: x[1],
                        reverse=True
                    )

        return rankeamento
          
          
    def set_link(self, vertice, link):
        self.__links[vertice-1] = link
    def get_importanciaInicial(self):
        return self.__importanciaInicial, self.__fatorDeAmortecimento,self.__paginasApontam
    def set_mensagem(self, vertice, mensagem):
        self.__mensagens[vertice-1] = mensagem
        
    def mostra_lista(self):
        for i in range(self.__qtdPaginas):
            print(f'Página {i+1}:', end='  ')
            for j in self.__grafo[i]:
                print(f' -> {j}', end='  ')
            print('')
