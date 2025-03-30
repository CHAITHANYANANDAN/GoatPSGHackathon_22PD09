from models.robot import Robot

class FleetManager:
    def __init__(self, nav_graph):
        self.nav_graph = nav_graph
        self.robots = {}

    def spawn_robot(self, robot_id, start_position):
        if robot_id not in self.robots:
            self.robots[robot_id] = Robot(robot_id, start_position)
            return True
        return False

    def assign_path(self, robot_id, path):
        if robot_id in self.robots:
            self.robots[robot_id].assign_task(path)

    def move_robots(self):
        for robot in self.robots.values():
            robot.move()
