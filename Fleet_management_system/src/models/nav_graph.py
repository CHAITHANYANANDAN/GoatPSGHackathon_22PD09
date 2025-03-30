import json

class NavGraph:
    def __init__(self, graph_data):
        level_key = list(graph_data["levels"].keys())[0]  # Extract first level (e.g., "level1")
        level_data = graph_data["levels"][level_key]
        
        self.vertices = level_data["vertices"]
        self.lanes = level_data["lanes"]
    
    def get_vertices(self):
        return self.vertices
    
    def get_lanes(self):
        return self.lanes
