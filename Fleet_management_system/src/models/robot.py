class Robot:
    def __init__(self, robot_id, start_position):
        self.id = robot_id
        self.position = start_position
        self.path = []
        self.status = "idle"

    def assign_task(self, path):
        if path:
            self.path = path
            self.status = "moving"

    def move(self):
        if self.path:
            self.position = self.path.pop(0)
            if not self.path:
                self.status = "idle"
