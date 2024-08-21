class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run_(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name
