import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FleetGUI:
    def __init__(self, nav_graph, fleet_manager, traffic_manager):
        self.nav_graph = nav_graph
        self.fleet_manager = fleet_manager
        self.traffic_manager = traffic_manager
        self.robots = {}  # Store robots with their positions

        # Initialize Tkinter window
        self.root = tk.Tk()
        self.root.title("Fleet Management System")

        # Set up GUI layout
        self.setup_ui()

    def setup_ui(self):
        """ Set up the GUI layout with the graph visualization """
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # Matplotlib figure for the navigation graph
        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().pack()

        # Draw the navigation graph
        self.draw_graph()

        # Button to spawn a robot
        self.spawn_button = tk.Button(self.root, text="Spawn Robot", command=self.spawn_robot)
        self.spawn_button.pack()

    def draw_graph(self):
        """ Draw the navigation graph using NetworkX """
        self.ax.clear()
        graph = nx.Graph()

        # Add vertices (locations)
        for i, (x, y, data) in enumerate(self.nav_graph.vertices):
            graph.add_node(i, pos=(x, y), label=data.get("name", f"V{i}"))

        # Add edges (lanes)
        for lane in self.nav_graph.lanes:
            start, end, _ = lane
            graph.add_edge(start, end)

        # Get positions and labels
        pos = nx.get_node_attributes(graph, 'pos')
        labels = nx.get_node_attributes(graph, 'label')

        # Draw the graph
        nx.draw(graph, pos, ax=self.ax, with_labels=True, labels=labels, node_size=500, node_color="lightblue")
        self.canvas.draw()

    def spawn_robot(self):
        """ Function to spawn a robot at a selected location """
        # For now, spawn at the first vertex
        start_vertex = 0
        self.robots[start_vertex] = "Robot1"
        print(f"Robot spawned at {start_vertex}")

    def run(self):
        """ Run the Tkinter main loop """
        self.root.mainloop()
