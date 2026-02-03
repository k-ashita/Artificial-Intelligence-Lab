def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = [(start, [start])]   # (node, path)

    while queue:
        vertex, path = queue.pop(0)

        if vertex == goal:
            return path

        if vertex not in visited:
            visited.add(vertex)

            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': ['G'],
    'E': ['F'],
    'F': ['H'],
    'G': [],
    'H': ['I', 'J'],
    'I': [],
    'J': ['K'],
    'K': ['L'],
    'L': []
}

start = 'A'
goal = 'H'

path = bfs_shortest_path(graph, start, goal)

if path:
    print("Shortest path:", " -> ".join(path))
else:
    print("No path found")
