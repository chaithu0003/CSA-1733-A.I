import itertools

def tsp_brute_force(graph, start_node):
    all_nodes = list(graph.keys())
    all_nodes.remove(start_node)
    min_distance = float('inf')
    min_path = None
    
    for perm in itertools.permutations(all_nodes):
        current_path = [start_node] + list(perm) + [start_node]
        current_distance = 0
        for i in range(len(current_path) - 1):
            current_distance += graph[current_path[i]][current_path[i+1]]
        
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = current_path
    
    return min_path, min_distance

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

start_node = 'A'

min_path, min_distance = tsp_brute_force(graph, start_node)
print("Minimum Distance Path:", min_path)
print("Minimum Distance:", min_distance)
