
import networkx as nx
import algorithmx
import json
import time

# Создание графа
G = nx.DiGraph()

# Импорт данных из файла .json и распаковка данных
with open('G.json', 'r') as file:
    data = json.load(file)
    for row in data:
        G.add_weighted_edges_from([(row[0], row[1], row[2])])

print(G.edges)

# Здесь происходит визуализация графа
canvas = algorithmx.create_canvas()
canvas.size((900,500))
canvas.edgelength(120)

canvas.nodes(range(len(G.nodes))).add()
canvas.edges(G.edges).add().directed(True).label().text(lambda e: G.edges[e]['weight'])

canvas

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