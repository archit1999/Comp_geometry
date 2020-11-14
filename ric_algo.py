from point import Point
import random
from circle import Circle


def ric(x: list, y: list) -> Circle:                 # list of x and y coordinate
    points = []
    for i in range(len(x)):
        points.append(Point(x[i], y[i]))

    return ric_algo(points)


def ric_algo(points):
    random.shuffle(points)
    c1 = Circle(points[0], points[1])
    for i in range(2, len(points)):
        if c1.check(points[i]):
            continue
        else:
            c1 = disc_min_with_a_pts(points[0:i], points[i])
    return c1


def disc_min_with_a_pts(points, q):
    random.shuffle(points)
    c1 = Circle(points[0], q)
    for i in range(1, len(points)):
        if c1.check(points[i]):
            continue
        else:
            c1 = disc_min_with_2_pts(points[0:i], points[i], q)
    return c1


def disc_min_with_2_pts(points, p, q):
    c1 = Circle(p ,q)
    for i in range(len(points)):
        if c1.check(points[i]):
            continue
        else:
            c1 = Circle(p, q, points[i])
    return c1