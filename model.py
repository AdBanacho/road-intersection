from RoadIntersection import RoadIntersection
from Road import SingleRoad


class Model:
    def __init__(self):
        self.road_A = RoadIntersection("A")
        self.initialization_road_A()
        self.road_B = RoadIntersection("B")
        self.initialization_road_B()
        self.road_C = RoadIntersection("C")
        self.initialization_road_C()
        self.road_D = RoadIntersection("D")
        self.initialization_road_D()
        self.roads = [self.road_A, self.road_B, self.road_C, self.road_D]

    def initialization_road_A(self):
        self.road_A.add_road_from(SingleRoad(direction=[0, 1, 1, 0]))
        self.road_A.add_road_from(SingleRoad(direction=[0, 0, 0, 1]))
        self.road_A.add_road_to(SingleRoad(direction=None))

    def initialization_road_B(self):
        self.road_B.add_road_from(SingleRoad(direction=[1, 0, 0, 1]))
        self.road_B.add_road_from(SingleRoad(direction=[0, 0, 1, 0]))
        self.road_B.add_road_to(SingleRoad(direction=None))

    def initialization_road_C(self):
        self.road_C.add_road_from(SingleRoad(direction=[1, 1, 0, 1]))
        self.road_C.add_road_to(SingleRoad(direction=None))

    def initialization_road_D(self):
        self.road_D.add_road_from(SingleRoad(direction=[0, 1, 1, 0]))
        self.road_D.add_road_from(SingleRoad(direction=[1, 0, 0, 0]))
        self.road_D.add_road_to(SingleRoad(direction=None))


