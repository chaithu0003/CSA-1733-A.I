import heapq

class Puzzle:
    def __init__(self, board, move_count=0, previous=None):
        self.board = board
        self.move_count = move_count
        self.previous = previous

    def __lt__(self, other):
        return self.priority() < other.priority()

    def priority(self):
        return self.move_count + self.manhattan_distance()

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    x, y = divmod(self.board[i][j] - 1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def is_goal(self):
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def neighbors(self):
        neighbors = []
        x, y = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0][0]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbors.append(Puzzle(new_board, self.move_count + 1, self))
        return neighbors

    def get_path(self):
        path = []
        node = self
        while node:
            path.append((node.board, node.move_count))
            node = node.previous
        return path[::-1]

def solve_puzzle(start):
    pq = []
    heapq.heappush(pq, Puzzle(start))
    visited = set()

    while pq:
        current = heapq.heappop(pq)

        if current.is_goal():
            return current.get_path()

        visited.add(tuple(map(tuple, current.board)))

        for neighbor in current.neighbors():
            if tuple(map(tuple, neighbor.board)) not in visited:
                heapq.heappush(pq, neighbor)

def get_input():
    print("Enter the puzzle configuration row by row, with 0 representing the blank space.")
    board = []
    for i in range(3):
        row = input(f"Enter row {i + 1} (e.g., 1 2 3): ").split()
        board.append([int(num) for num in row])
    return board

def print_solution(solution):
    if solution:
        for step, cost in solution:
            for row in step:
                print(' '.join(map(str, row)))
            print(f"Cost: {cost+1}\n")
    else:
        print("No solution found.")

# Get input from the user
start = get_input()

# Solve the puzzle and print the solution
solution = solve_puzzle(start)
print_solution(solution)
