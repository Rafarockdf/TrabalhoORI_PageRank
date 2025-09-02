from PageRank import GrafoPageRank
# ===============================
# Factory para gerar grafo de teste
# ===============================
def fabrica_grafo_page_rank():
    n = 4  # quantidade de vértices
    g = GrafoPageRank(n)

    # Definindo links e mensagens simuladas
    for i in range(1, n+1):
        g.set_link(i, f"http://site{i}.com")
        g.set_mensagem(i, f"Página {i} com conteúdo de exemplo")

    # Contexto de arestas (direcionadas)
    '''
    A página A tem links para B e C.

A página B tem um link para C.

A página C tem um link para A.

A página D tem um link para C.
    
    g.adiciona_aresta(1, 2)
    g.adiciona_aresta(1, 3)
    g.adiciona_aresta(2, 3)
    g.adiciona_aresta(2, 4)
    g.adiciona_aresta(3, 1)
    g.adiciona_aresta(3, 5)
    g.adiciona_aresta(4, 6)
    g.adiciona_aresta(5, 4)
    g.adiciona_aresta(5, 6)
    g.adiciona_aresta(6, 3)
    ''' 
    g.adiciona_aresta(1, 2)
    g.adiciona_aresta(1, 3)
    g.adiciona_aresta(2, 3)
    g.adiciona_aresta(3, 1)
    g.adiciona_aresta(4, 3)
    
    return g

g = fabrica_grafo_page_rank()
print(g.mostra_lista())
print(g.calcular_pagerank_completo())
