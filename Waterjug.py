from collections import deque

capacity = [12,8,5,3]

start = (12,0,0,0)
goal = (6,6,0,0)

jug_names = ["12L","8L","5L","3L"]

def pour(state,i,j):

    state=list(state)

    transfer=min(state[i],capacity[j]-state[j])

    if transfer==0:
        return None

    state[i]-=transfer
    state[j]+=transfer

    return tuple(state),transfer


def bfs():

    visited=set()
    queue=deque()

    queue.append((start,[]))

    while queue:

        state,path=queue.popleft()

        if state==goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for i in range(4):
            for j in range(4):

                if i!=j:

                    result=pour(state,i,j)

                    if result:

                        new_state,amount=result

                        if new_state not in visited:

                            action=f"Pour {amount}L from {jug_names[i]} to {jug_names[j]}"

                            queue.append((new_state,path+[(state,action,new_state)]))

    return None


solution=bfs()

print("Initial State:",start)

step=1

for s in solution:

    current,action,new_state=s

    print("\nStep",step)
    print("Current State:",current)
    print("Action:",action)
    print("New State:",new_state)

    step+=1

print("\nGoal State Reached:",goal)
