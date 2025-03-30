import json
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# List of dataset files
dataset_files = ["data/nav_graph_1.json", "data/nav_graph_2.json", "data/nav_graph_3.json"]

# Initialize storage for merged nodes and edges
nodes = {}
edges = []
node_index = 0
robots = {}  # Store active robots and their paths
robot_count = 0  # Robot ID counter

# Function to load and merge datasets
def load_and_merge_graphs():
    global node_index

    for file in dataset_files:
        if os.path.exists(file):
            with open(file, "r") as f:
                data = json.load(f)

            # Check if "levels" and "level1" exist
            if "levels" not in data or "level1" not in data["levels"]:
                print(f"⚠️ Warning: 'level1' not found in {file}. Skipping.")
                continue  # Skip this file if "level1" is missing

            level_data = data["levels"]["level1"]
            vertices = level_data.get("vertices", [])  # Use .get() to avoid crashes
            lanes = level_data.get("lanes", [])

            local_to_global = {}

            for i, v in enumerate(vertices):
                nodes[node_index] = {
                    "x": v[0],
                    "y": v[1],
                    "name": v[2].get("name", "")
                }
                local_to_global[i] = node_index
                node_index += 1

            for lane in lanes:
                edges.append((local_to_global[lane[0]], local_to_global[lane[1]]))

# Load and merge all datasets
load_and_merge_graphs()

# Check if graph is loaded correctly
if not nodes or not edges:
    print("❌ Error: No valid graph data found. Check your JSON files.")
    exit(1)

# Plot the graph
fig, ax = plt.subplots()
ax.set_title("Fleet Management System")
ax.set_xlabel("X Coordinate")
ax.set_ylabel("Y Coordinate")

# Draw edges (lanes)
for edge in edges:
    x_values = [nodes[edge[0]]["x"], nodes[edge[1]]["x"]]
    y_values = [nodes[edge[0]]["y"], nodes[edge[1]]["y"]]
    ax.plot(x_values, y_values, "gray")

# Draw vertices (locations)
for node_id, node in nodes.items():
    ax.scatter(node["x"], node["y"], c="blue", marker="o", s=100)
    ax.text(node["x"], node["y"], f"{node_id}", fontsize=8, ha="right")

# Store robot markers
robot_markers = {}

# Function to handle click events
def on_click(event):
    global robot_count

    if event.xdata is None or event.ydata is None:
        return

    min_dist = float("inf")
    nearest_vertex = None

    for node_id, node in nodes.items():
        dist = np.sqrt((event.xdata - node["x"])**2 + (event.ydata - node["y"])**2)
        if dist < min_dist:
            min_dist = dist
            nearest_vertex = node_id

    if nearest_vertex is not None:
        print(f"Clicked near vertex: {nearest_vertex}")

        if robot_count < 5:  # Allow only 5 robots for now
            robot_count += 1
            robots[robot_count] = {
                "position": nearest_vertex,
                "path": [nearest_vertex]  # Start at spawn location
            }

            robot_markers[robot_count] = ax.scatter(
                nodes[nearest_vertex]["x"], nodes[nearest_vertex]["y"], c="red", marker="s", s=100, label=f"Robot {robot_count}"
            )

            print(f"Spawned Robot {robot_count} at vertex {nearest_vertex}")

# Function to update robot movement
def update_robots(frame):
    for robot_id, robot_data in robots.items():
        if len(robot_data["path"]) > 1:
            robot_data["position"] = robot_data["path"].pop(0)  # Move to next node
            x, y = nodes[robot_data["position"]]["x"], nodes[robot_data["position"]]["y"]
            robot_markers[robot_id].set_offsets([x, y])

# Start animation
ani = animation.FuncAnimation(fig, update_robots, interval=1000)

# Connect click event
fig.canvas.mpl_connect("button_press_event", on_click)

plt.show()
