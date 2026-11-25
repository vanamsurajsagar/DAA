
from itertools import permutations

def tsp(graph, n):
    vertices = []

    for i in range(1, n):
        vertices.append(i)

    min_cost = float('inf')
    best_path = []

    for path in permutations(vertices):
        cost = 0
        current = 0

        for city in path:
            cost += graph[current][city]
            current = city

        cost += graph[current][0]

        if cost < min_cost:
            min_cost = cost
            best_path = [0] + list(path) + [0]

    print("Shortest path:", best_path)
    print("Minimum cost:", min_cost)


n = int(input("Enter number of cities: "))

graph = []

print("Enter cost matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

tsp(graph, n)
