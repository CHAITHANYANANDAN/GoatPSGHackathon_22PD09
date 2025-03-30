import tkinter as tk
from tkinter import simpledialog

class SetupGUI:
    def __init__(self, root, fleet_manager, start_simulation_callback):
        self.root = root
        self.fleet_manager = fleet_manager
        self.start_simulation_callback = start_simulation_callback
        self.robots = []
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Fleet Management Setup").pack()
        tk.Button(self.root, text="Add Robot", command=self.get_robot_details).pack()
        tk.Button(self.root, text="Start Simulation", command=self.start_simulation).pack()

    def get_robot_details(self):
        name = simpledialog.askstring("Robot Name", "Enter Robot Name:")
        start = simpledialog.askstring("Start Position", "Enter Start Position:")
        dest = simpledialog.askstring("Destination", "Enter Destination:")
        if name and start and dest:
            self.robots.append((name, start, dest))

    def start_simulation(self):
        self.start_simulation_callback(self.robots)
