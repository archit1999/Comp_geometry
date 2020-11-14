from point import Point


class Circle:

    def __init__(self, p1, p2, p3=None):

        if p3 is None:
            self.centre = p1.mid_pt(p2)
            self.rad = p1.dist(p2)/2

        else:
            b = [p1.x, p1.y]
            c = [p2.x, p2.y]
            d = [p3.x, p3.y]
            temp = c[0] ** 2 + c[1] ** 2
            bc = (b[0] ** 2 + b[1] ** 2 - temp) / 2
            cd = (temp - d[0] ** 2 - d[1] ** 2) / 2
            det = (b[0] - c[0]) * (c[1] - d[1]) - (c[0] - d[0]) * (b[1] - c[1])

            if abs(det) < 1.0e-10:
                return None

            else:
                cx = (bc * (c[1] - d[1]) - cd * (b[1] - c[1])) / det
                cy = ((b[0] - c[0]) * cd - (c[0] - d[0]) * bc) / det

                radius = ((cx - b[0]) ** 2 + (cy - b[1]) ** 2) ** .5
                self.centre = Point(cx, cy)
                self.rad = radius

    def check(self, p1):                    # posn of p1 in this circle
        if p1.dist(self.centre) <= self.rad:
            return True
        else:
            return False
