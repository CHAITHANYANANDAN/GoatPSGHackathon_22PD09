class TrafficManager:
    def __init__(self, nav_graph):
        self.nav_graph = nav_graph
        self.occupied_positions = set()

    def is_position_free(self, position):
        return position not in self.occupied_positions

    def update_occupancy(self, robot, new_position):
        if robot.position in self.occupied_positions:
            self.occupied_positions.remove(robot.position)
        self.occupied_positions.add(new_position)
