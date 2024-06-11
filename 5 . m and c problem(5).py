from collections import deque
MAX_MISSIONARIES = 3
MAX_CANNIBALS = 3
BOAT_CAPACITY = 2

def is_valid_state(state):
    m_on_left, c_on_left, _ = state
    if m_on_left < 0 or m_on_left > MAX_MISSIONARIES:
        return False
    if c_on_left < 0 or c_on_left > MAX_CANNIBALS:
        return False
    return True

def is_goal_state(state):
    return state == (0, 0, 0)

def get_successors(state):
    m_on_left, c_on_left, boat_position = state
    successors = []

    if boat_position == 1:  # Boat on the left side
        for m in range(BOAT_CAPACITY + 1):
            for c in range(BOAT_CAPACITY - m + 1):
                if m + c > 0 and m + c <= BOAT_CAPACITY:
                    successors.append((m_on_left - m, c_on_left - c, 0))
    else:  # Boat on the right side
        for m in range(BOAT_CAPACITY + 1):
            for c in range(BOAT_CAPACITY - m + 1):
                if m + c > 0 and m + c <= BOAT_CAPACITY:
                    successors.append((m_on_left + m, c_on_left + c, 1))

    return [state for state in successors if is_valid_state(state)]

def bfs():
    start_state = (3, 3, 1)
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if is_goal_state(state):
            return path + [state]

        if state not in visited:
            visited.add(state)
            for successor in get_successors(state):
                queue.append((successor, path + [state]))

    return None

def main():
    solution = bfs()
    if solution:
        print("Solution found:")
        for i, state in enumerate(solution):
            m_on_left, c_on_left, boat_position = state
            print(f"Step {i + 1}: {m_on_left} missionaries, {c_on_left} cannibals, boat {'left' if boat_position == 1 else 'right'}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
