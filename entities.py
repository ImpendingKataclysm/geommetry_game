class Point:
    """
    This class describes a point on a grid, defined by its x and y coordinates.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        """
        Determines whether the Point falls within a given Rectangle
        :param rectangle:
        :return: True if the Point falls within the rectangle's coordinates,
        otherwise False
        """
        if rectangle.corner1.x < self.x < rectangle.corner2.x \
                and rectangle.corner1.y < self.y < rectangle.corner2.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        """
        Calculates the distance between this Point and another given Point
        :param point: the Point to which the distance is calculated
        :return: the total distance between the 2 Points
        """
        x_dist = point.x - self.x
        y_dist = point.y - self.y
        # Pythogorean Theorem
        total_dist = (x_dist ** 2 + y_dist ** 2) ** 0.5

        return total_dist


class Rectangle:
    """
    This class describes a rectangle in terms of its lower-left (min x, min y)
    and upper-right (max x, max y) coordinates.
    """
    def __init__(self, point1, point2):
        self.corner1 = point1
        self.corner2 = point2

    def get_area(self):
        length = self.corner2.x - self.corner1.x
        height = self.corner2.y - self.corner1.y
        return length * height
