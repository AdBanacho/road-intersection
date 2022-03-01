

class RoadIntersection:
    def __init__(self, name):
        self.name = name
        self.roads_from = []
        self.roads_to = []

    def add_road_from(self, road):
        self.roads_from.append(road)

    def add_road_to(self, road):
        self.roads_to.append(road)
