# Advanced Vacuum Cleaner Simulation

# 1. Initially all rooms are dirty (1 = Dirty, 0 = Clean)
rooms = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

# 2. Dirty locations before cleaning (sample input given)
dirty_locations = [
    [0, 1, 0, 0],
    [1, 0, 0, 1],
    [],
    [],
    [],
    []
]

total_parts = 6 * 5   # total room parts
cleaned_parts = 0

print("INITIAL ROOM STATUS")
for room in rooms:
    print(room)

print("\nDIRTY LOCATIONS BEFORE CLEANING")
for i, loc in enumerate(dirty_locations):
    print(f"Room {i + 1}: {loc}")

print("\nCLEANING PROCESS\n")

# 3. Each room divided into Left, Center, Right
for i in range(len(rooms)):
    print(f"Room {i + 1}")

    left = rooms[i][0:2]
    center = [rooms[i][2]]
    right = rooms[i][3:5]

    # Clean all parts
    for j in range(5):
        if rooms[i][j] == 1:
            rooms[i][j] = 0
            cleaned_parts += 1

    left_status = "Cleaned"
    center_status = "Cleaned"
    right_status = "Cleaned"

    left_percent = int((2 / 5) * 100)
    center_percent = int((1 / 5) * 100)
    right_percent = int((2 / 5) * 100)

    print(f" Left   - {left_status}   - {left_percent}%")
    print(f" Center - {center_status} - {center_percent}%")
    print(f" Right  - {right_status}  - {right_percent}%\n")

# 4. All rooms cleaned
print("FINAL ROOM STATUS (0 = Clean)")
for room in rooms:
    print(room)

# 5. Performance status
performance = (cleaned_parts / total_parts) * 100


# 6. Ending message
print("\nThank you for using Vacuum Cleaner ")
