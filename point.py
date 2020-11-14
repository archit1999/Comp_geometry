import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rel_dist(self, p2):
        return (self.x - p2.x)**2 + (self.y - p2.y)**2

    def dist(self, p2):
        return math.sqrt(self.rel_dist(p2))

    def mid_pt(self, p2):
        x_new = (self.x + p2.y)/2
        y_new = (self.y + p2.y)/2
        return Point(x_new, y_new)

