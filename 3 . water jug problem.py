from collections import deque

def is_goal(state, target):
    return target in state

def get_successors(state, capacities):
    successors = []
    jug1, jug2 = state
    cap1, cap2 = capacities

    # Fill Jug1
    successors.append((cap1, jug2))
    # Fill Jug2
    successors.append((jug1, cap2))
    # Empty Jug1
    successors.append((0, jug2))
    # Empty Jug2
    successors.append((jug1, 0))
    # Pour Jug1 -> Jug2
    pour = min(jug1, cap2 - jug2)
    successors.append((jug1 - pour, jug2 + pour))
    # Pour Jug2 -> Jug1
    pour = min(jug2, cap1 - jug1)
    successors.append((jug1 + pour, jug2 - pour))

    return successors

def bfs(capacities, target):
    start = (0, 0)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (jug1, jug2), path = queue.popleft()

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        if is_goal((jug1, jug2), target):
            return path + [(jug1, jug2)]

        for successor in get_successors((jug1, jug2), capacities):
            queue.append((successor, path + [(jug1, jug2)]))

    return None

def main():
    cap1 = int(input("Enter capacity of Jug1: "))
    cap2 = int(input("Enter capacity of Jug2: "))
    target = int(input("Enter the target amount of water: "))

    capacities = (cap1, cap2)
    result = bfs(capacities, target)

    if result:
        for step in result:
            print(step)
    else:
        print("No solution found")

if __name__ == "__main__":
    main()
