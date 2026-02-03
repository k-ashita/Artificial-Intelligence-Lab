#advanced bfs
from collections import deque
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['I', 'J'],
    'E': ['G', 'H'],
    'F': [],
    'I': ['K', 'L'],
    'J': [],
    'G': [],
    'H': [],
    'K': [],
    'L': []
}

def bfs_minimum_path(graph, source, goal):
    visited = []
    queue = deque([[source]])
    step = 1

    vertices = list(graph.keys())
    edges = []
    for u in graph:
        for v in graph[u]:
            edges.append((u, v))

    print(f"\nSource Node: {source}")
    print(f"Vertices (V): {vertices}")
    print(f"Edges (E): {edges}\n")

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            visited.append(node)

            unvisited = [v for v in vertices if v not in visited]
            children = graph[node]

            print(f"Step {step}:")
            print(f"Visiting Node: {node}")
            print(f"Visited Nodes: {visited}")
            print(f"Unvisited Nodes: {unvisited}")
            print(f"Child Vertices: {children}")
            print(f"Edges from current node: {[(node, c) for c in children]}\n")

            step += 1

            if node == goal:
                print("---------------------------")
                print(f"Final Visited Nodes (BFS Order): {visited}")
                print("Non-Visited Nodes: 0")
                print(f"Path of {source}: {' → '.join(path)}")
                return

            for child in children:
                new_path = list(path)
                new_path.append(child)
                queue.append(new_path)


source = input("Enter source node: ").strip()
goal = input("Enter goal node: ").strip()

bfs_minimum_path(graph, source, goal)
