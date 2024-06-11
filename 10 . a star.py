# Python program for A* algorithm
from queue import PriorityQueue

def a_star(graph, start, goal, h):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_list.empty():
        current_cost, current_node = open_list.get()

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1], g_score[goal]

        for neighbor, cost in graph[current_node].items():
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + h[neighbor]
                open_list.put((f_score, neighbor))

    return None

# Sample graph with heuristic
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

h = {'A': 7, 'B': 6, 'C': 2, 'D': 1}  # Heuristic values

# Sample output
path, cost = a_star(graph, 'A', 'D', h)
print("A* Path:", path)
print("Total cost:", cost)
