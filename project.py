from tkinter import *
import networkx as nx
import matplotlib.pyplot as plt

# Define the Romania map graph
romania_map = nx.Graph()
romania_map.add_edges_from([
    ('Arad', 'Zerind', {'weight': 75, 'heuristic': 366}),
    ('Arad', 'Sibiu', {'weight': 140, 'heuristic': 253}),
    ('Arad', 'Timisoara', {'weight': 118, 'heuristic': 329}),
    ('Zerind', 'Oradea', {'weight': 71, 'heuristic': 380}),
    ('Oradea', 'Sibiu', {'weight': 151, 'heuristic': 253}),
    ('Sibiu', 'Fagaras', {'weight': 99, 'heuristic': 176}),
    ('Sibiu', 'Rimnicu Vilcea', {'weight': 80, 'heuristic': 193}),
    ('Rimnicu Vilcea', 'Craiova', {'weight': 146, 'heuristic': 160}),
    ('Rimnicu Vilcea', 'Pitesti', {'weight': 97, 'heuristic': 100}),
    ('Craiova', 'Pitesti', {'weight': 138, 'heuristic': 100}),
    ('Craiova', 'Drobeta', {'weight': 120, 'heuristic': 242}),
    ('Drobeta', 'Mehadia', {'weight': 75, 'heuristic': 241}),
    ('Mehadia', 'Lugoj', {'weight': 70, 'heuristic': 244}),
    ('Lugoj', 'Timisoara', {'weight': 111, 'heuristic': 329}),
    ('Fagaras', 'Bucharest', {'weight': 211, 'heuristic': 0}),
    ('Pitesti', 'Bucharest', {'weight': 101, 'heuristic': 101}),
    ('Bucharest', 'Giurgiu', {'weight': 90, 'heuristic': 77}),
    ('Bucharest', 'Urziceni', {'weight': 85, 'heuristic': 80}),
    ('Urziceni', 'Hirsova', {'weight': 98, 'heuristic': 151}),
    ('Urziceni', 'Vaslui', {'weight': 142, 'heuristic': 199}),
    ('Hirsova', 'Eforie', {'weight': 86, 'heuristic': 161}),
    ('Vaslui', 'Iasi', {'weight': 92, 'heuristic': 226}),
    ('Iasi', 'Neamt', {'weight': 87, 'heuristic': 234})
])

def astar_search(source, destination):
    path = nx.astar_path(romania_map, source, destination, weight='weight')
    return path

def draw_map(graph, path=None):
    plt.figure(figsize=(8, 8))
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=8)

    # Draw path
    if path:
        edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='red', width=2.0)

        # Draw path cost
        path_cost = sum(graph[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, 'weight'), font_color='blue',
                                     label_pos=0.3, font_size=6)
        plt.title("Final Path (Cost: {})".format(path_cost))
    else:
        # Draw heuristics
        heuristics = nx.get_node_attributes(graph, 'heuristic')
        nx.draw_networkx_labels(graph, pos, labels=heuristics, font_color='green')
        plt.title("Initial Romania Map")

    plt.axis('off')
    plt.tight_layout()
    plt.show()

def search():
    source = source_entry.get()
    destination = destination_entry.get()
    path = astar_search(source, destination)
    result_label.config(text="Path: " + ' -> '.join(path))
    draw_map(romania_map, path)

# Create the GUI window
root = Tk()
root.title("A* Search on Romania Map")

# Source and destination input fields
source_label = Label(root, text="Source:")
source_label.pack()
source_entry = Entry(root)
source_entry.pack()

destination_label = Label(root, text="Destination:")
destination_label.pack()
destination_entry = Entry(root)
destination_entry.pack()

# Find Path button
search_button = Button(root, text="Find Path", command=search)
search_button.pack()

# Result label
result_label = Label(root)
result_label.pack()

# Draw the initial Romania map
draw_map(romania_map)

# Start the GUI event loop
root.mainloop()
