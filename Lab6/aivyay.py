import networkx as nx
import pylab as plt
import time

# Импорт данных из файла .txt и распаковка данных
n=8
D = [[] for i in range(n)] # "объявляет" матрицу(двумерный массив)
with open('g.txt') as file:
    for i in range(n):
        D[i] = [int(t) for t in file.readline().split()] #читает всю строку, делит по пробелам, и сохраняет как массив интов записывая в строку матрицы






edags = D
print(edags)
G = nx.Graph()
G.add_weighted_edges_from(edags)
nx.draw(G, with_labels=True)
plt.savefig('graph.png')
plt.close()

# Выбер исходной вершину
start_time = time.time()
source = 0

""""Алгоритм Беллмана-Форда - Возвращает кратчайший путь от исходной вершины ко всем остальным вершинам"""

# Первый шаг
edges = list(G.edges(data=True))
dist = [0 if node == source else float("INF") for index, node in enumerate(G.nodes)]
pred = [None for node in enumerate(G.nodes)]

# Второй шаг
for i in range(len(G.nodes) - 1):
    updated = False

    for index, edge in enumerate(G.edges):
        u = edges[index][0]
        v = edges[index][1]
        weight = edges[index][2]['weight']

        if dist[u] is not float("INF") and dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight
            pred[v] = u
            is_updated = True

    if not updated:
        break

# Третий шаг
for index, edge in enumerate(G.edges):
    u = edges[index][0]
    v = edges[index][1]
    weight = edges[index][2]['weight']

    if dist[u] is not float("INF") and dist[u] + weight < dist[v]:
        raise Exception("Negative-weight cycle")

print(f"Distances: {dist}")
print(f"Predecessors: {pred}")
print(f"{time.time() - start_time} sec.")