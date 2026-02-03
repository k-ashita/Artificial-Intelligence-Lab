def vacuum_cleaner(loc,state):
  if state[loc] == 'Dirty':
        print(f"Room {loc} is Dirty")
        print("Suck")
        state[loc] = 'Clean'
  else:
        print(f"Room {loc} is Clean")
        print("Move Right")

        if loc == 'A':
            loc = 'B'
        else:
            loc = 'A'

  return loc, state

location = 'A'
state = {
    'A': 'Dirty',
    'B': 'Dirty'
}

for step in range(4):
    print(f"\nStep {step + 1}")
    location, state = vacuum_cleaner(location, state)
    print("Current State:", state)
