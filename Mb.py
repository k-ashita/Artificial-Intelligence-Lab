import heapq

# Heuristic values
def heuristic(state):
    h_values = {
        "Start": 3,
        "AtBox": 2,
        "BoxUnderBanana": 1,
        "OnBox": 0,
        "Goal": 0
    }
    return h_values[state]


def astar():
    open_list = []
    heapq.heappush(open_list, (0, 0, "Start", []))
    visited = set()
    step = 1

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        print("\nStep", step)
        print("Current State:", state)
        print("g(n) =", g)
        print("h(n) =", heuristic(state))
        print("f(n) =", f)
        step += 1

        if state == "Goal":
            print("\nGoal Reached!")
            return path

        if state in visited:
            continue

        visited.add(state)

        # State transitions
        if state == "Start":
            next_state = "AtBox"
            action = "Walk to Box"

        elif state == "AtBox":
            next_state = "BoxUnderBanana"
            action = "Push Box Under Banana"

        elif state == "BoxUnderBanana":
            next_state = "OnBox"
            action = "Climb Box"

        elif state == "OnBox":
            next_state = "Goal"
            action = "Grab Banana"

        else:
            continue

        new_g = g + 1
        new_h = heuristic(next_state)
        new_f = new_g + new_h

        print("Action:", action)
        print("Next State:", next_state)
        print("New g =", new_g, " New h =", new_h, " New f =", new_f)

        heapq.heappush(open_list, (new_f, new_g, next_state, path + [action]))

    return None


# Run A*
solution = astar()

print("\nFinal Solution Path:")
for s in solution:
    print(s)
