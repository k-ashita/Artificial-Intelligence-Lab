#ucs
import heapq
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5),('G', 4)],
    'D': [('H', 2)],
    'E': [('I',2),('J', 6)],
    'F': [],
    'G': [('K', 5),('L', 4)],
    'H': [],
    'I': [('M', 3),('N', 5)],
    'J': [],
    'K': [],
    'L': [('O', 6)],
    'M': [('P',2)],
    'N': [],
    'O': [],
    'P':[('Q',2)],
    'Q':[]
}

def lcfs(graph, source, goal):
    visited = []
    priority_queue = [(0, [source])]
    step = 1

    vertices = list(graph.keys())
    edges = []
    for u in graph:
        for v, w in graph[u]:
            edges.append((u, v, w))

    print(f"\nSource Node: {source}")
    print(f"Vertices (V): {vertices}")
    print(f"Edges (E): {edges}\n")

    while priority_queue:
        cost, path = heapq.heappop(priority_queue)
        node = path[-1]

        if node not in visited:
            visited.append(node)

            unvisited = [v for v in vertices if v not in visited]
            children = graph[node]

            print(f"Step {step}:")
            print(f"Visiting Node: {node}")
            print(f"Current Cost: {cost}")
            print(f"Visited Nodes: {visited}")
            print(f"Unvisited Nodes: {unvisited}")
            print(f"Child Vertices: {[(c, w) for c, w in children]}")
            print(f"Edges from current node: {[(node, c, w) for c, w in children]}\n")

            step += 1

            if node == goal:
                print("---------------------------")
                print(f"Final Visited Nodes (LCFS Order): {visited}")
                print("Non-Visited Nodes: 0")
                print(f"Minimum Cost: {cost}")
                print(f"Shortest Path: {' → '.join(path)}")
                return

            for child, weight in children:
                new_path = list(path)
                new_path.append(child)
                new_cost = cost + weight
                heapq.heappush(priority_queue, (new_cost, new_path))


source = 'A'
goal = 'Q'

lcfs(graph, source, goal)
