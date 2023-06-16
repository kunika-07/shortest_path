# shortest_path
This code demonstrates the implementation of the A* search algorithm on a graph representing the map of Romania. It finds the shortest path between a given source and destination city in Romania.

Requirements
To run this code, you need to have the following libraries installed:

tkinter
networkx
matplotlib
You can install the required libraries using pip:tkinter networkx matplotlib

Usage:
1.Import the necessary libraries

2.Define the Romania map graph:The graph is represented as an undirected graph with weighted edges. Each edge represents a connection between two cities in Romania, and it contains a weight (distance) and a heuristic value.

3.Define the A* search algorithm:The astar_search function takes a source city and a destination city as input and returns the shortest path between them using the A* algorithm. It uses the astar_path function from the networkx library.

4.Define a function to draw the map:The draw_map function visualizes the Romania map graph using matplotlib. It takes the graph and an optional path as input. If a path is provided, it highlights the path on the graph.

5.Implement the search function:The search function is triggered when the "Find Path" button is clicked. It retrieves the source and destination cities entered by the user, performs the A* search, displays the path, and visualizes the map with the path highlighted.

6.Create the GUI window and add the necessary elements:The GUI window contains two input fields for the source and destination cities, a "Find Path" button to initiate the search, and a label to display the result.

7.Draw the initial Romania map:The initial map without any path is displayed when the GUI window is launched.

8.Start the GUI event loop:This starts the event loop, allowing the user to interact with the GUI elements.

Running the Code:
To run the code, execute the Python script in your preferred Python environment.
Upon running the script, a GUI window titled "A*


