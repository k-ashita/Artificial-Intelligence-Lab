from collections import deque

# Goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Directions (Up, Down, Left, Right)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to find position of 0 (blank)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Convert list to tuple (for visited set)
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# BFS Algorithm
def bfs(start_state):
    queue = deque()
    visited = set()

    queue.append((start_state, []))
    visited.add(to_tuple(start_state))

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path + [current_state]

        x, y = find_zero(current_state)

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in current_state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                if to_tuple(new_state) not in visited:
                    visited.add(to_tuple(new_state))
                    queue.append((new_state, path + [current_state]))

    return None

# Example Start State
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = bfs(start)

# Print Solution
if solution:
    print("Solution Found in", len(solution) - 1, "moves\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")
