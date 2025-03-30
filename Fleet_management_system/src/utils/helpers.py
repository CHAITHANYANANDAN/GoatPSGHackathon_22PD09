import json

def load_graph(filepath):
    with open(filepath, "r") as file:
        return json.load(file)
