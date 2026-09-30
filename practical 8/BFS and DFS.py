# BFS and DFS 

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            for x in graph[node]:
                if x not in visited:
                    queue.append(x)


def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for x in graph[node]:
            dfs(graph, x, visited)


# User input
n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    graph[i] = list(map(int, input(
        f"Enter neighbours of vertex {i}: "
    ).split()))

start = int(input("Enter starting vertex: "))

# BFS
print("\nBFS Traversal:")
bfs(graph, start)

# DFS
print("\nDFS Traversal:")
visited = []
dfs(graph, start, visited)


#TC : O(V + E)
#SC : O(V)