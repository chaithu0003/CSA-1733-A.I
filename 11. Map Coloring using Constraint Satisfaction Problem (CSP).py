def is_valid(graph, node, color, coloring):
    for neighbor in graph[node]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

def map_coloring(graph, colors, node, coloring):
    if node not in graph:
        return True
    
    for color in colors:
        if is_valid(graph, node, color, coloring):
            coloring[node] = color
            next_node = next(iter(graph.keys() - set(coloring.keys())), None)
            if next_node is None or map_coloring(graph, colors, next_node, coloring):
                return True
            coloring.pop(node, None)
    
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

coloring = {}
starting_node = next(iter(graph.keys()))

if map_coloring(graph, colors, starting_node, coloring):
    print("Map coloring solution:")
    for region, color in coloring.items():
        print(f"Region {region} is colored {color}")
else:
    print("No valid map coloring solution found.")