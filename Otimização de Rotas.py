import heapq

# Exemplo de grafo representando as conexões entre locais (nós) e distâncias (arestas)
grafo = {
    'LocalA': {'LocalB': 10, 'LocalC': 15},
    'LocalB': {'LocalD': 12},
    'LocalC': {'LocalD': 5},
    'LocalD': {}
}

def dijkstra(grafo, origem):
    distancias = {local: float('infinity') for local in grafo}
    distancias[origem] = 0
    fila = [(0, origem)]

    while fila:
        (distancia_atual, local_atual) = heapq.heappop(fila)

        if distancia_atual > distancias[local_atual]:
            continue

        for vizinho, peso in grafo[local_atual].items():
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila, (distancia, vizinho))

    return distancias
