# GoatPSGHackathon_22PD09
# **Fleet Management System**  

This project is a **robot fleet management system** that allows users to **spawn robots, assign tasks, and visualize movement** on a predefined map. The system reads multiple **navigation graphs**, processes them, and ensures **collision-free** robot movement.  

---

## **What This Project Does**  

**Loads multiple graph datasets** (`nav_graph_1.json`, `nav_graph_2.json`, `nav_graph_3.json`) and merges them.  
**Displays locations and lanes** clearly on a map.  
**Allows spawning robots** at any vertex by clicking.  
**Assigns tasks to robots** so they move to a destination.  
**Implements pathfinding (Dijkstra/A*)** to find the best route.  
**Prevents collisions** by making robots wait at occupied paths.  
**Logs all actions** (spawning, movements, and waiting) for debugging.  

---

## **Project Structure**  

```
Fleet_management_system/
│── data/
│   ├── nav_graph_1.json  # First navigation graph
│   ├── nav_graph_2.json  # Second navigation graph
│   ├── nav_graph_3.json  # Third navigation graph
│── src/
│   ├── main.py           # Runs the fleet management system
│   ├── pathfinding.py    # Handles shortest path logic
│   ├── visualization.py  # Handles graph and robot display
│   ├── simulation.py     # Controls robot movement
│── fleet_logs.txt        # Stores all robot actions
│── README.md             # This file
```

---

## **How to Set Up & Run**  

1️⃣ **Install Python (3.8+)** if not installed.  
2️⃣ **Install dependencies:**  
```sh
pip install matplotlib numpy
```
3️⃣ **Run the system:**  
```sh
python src/main.py
```

---

## **How It Works**  

### **1. Viewing the Graph**  
- The system loads a **map with nodes and paths**.  
- **Nodes (blue points)** represent locations where robots can be spawned.  
- **Edges (gray lines)** represent the paths robots can take.  

### **2. Spawning Robots**  
- Click on any **node** to **spawn a robot** at that location.  
- Each robot gets a **unique color** for easy identification.  

### **3. Assigning a Task**  
- Click on a **robot** to select it.  
- Click on a **destination node** to assign a navigation task.  
- The robot will **calculate the shortest path and start moving**.  

### **4. Collision Avoidance**  
- If a robot detects another in its path, it will **wait instead of crashing**.  
- Robots **queue at intersections** and **take turns moving**.  

---

## **How the Data is Structured**  

The navigation graphs are stored in JSON files like this:  

```json
{
  "levels": {
    "level1": {
      "lanes": [ [0, 4], [4, 5], [5, 11] ],
      "vertices": [
        [6.73, -1.18, { "name": "m2", "is_charger": true }],
        [3.61, -1.98, { "name": "m1" }]
      ]
    }
  },
  "building_name": "new_site"
}
```

- **Vertices (nodes):** Locations (x, y coordinates)  
- **Lanes (edges):** Paths connecting locations  

---

## **How Robots Move**  

1 **Pathfinding** – Uses **Dijkstra’s Algorithm** (or **A* search**) to find the **fastest path**.  
2 **Smooth Movement** – Robots move step by step using **matplotlib animation**.  
3️ **Traffic Management** – Robots **wait** if a lane is occupied to avoid crashes.  

---

## **Logging & Debugging**  

- All robot actions are logged in `fleet_logs.txt` for debugging:  
  ```
  [10:05:21] Robot 1 spawned at vertex 5
  [10:05:25] Robot 1 assigned destination vertex 12
  [10:05:30] Robot 1 moving: Path [5 → 11 → 12]
  [10:05:40] Robot 1 reached destination 12
  ```
- Helps **track movements, waiting times, and task completions**.  

---

## **What’s Next? (Possible Improvements)**  

🔹 Add **UI buttons** to control robot behavior  
🔹 Implement **real-time obstacle detection**  
🔹 Add **speed variations for different robots**  
🔹 Allow **multi-floor navigation**  

---

## **Final Thoughts**  

This **Fleet Management System** simulates **robot movement and navigation** in a mapped space. It handles **pathfinding, traffic control, and dynamic interactions**. Hope this helps! 