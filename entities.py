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
        if rectangle.low_left.x < self.x < rectangle.up_right.x \
                and rectangle.low_left.y < self.y < rectangle.up_right.y:
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
    def __init__(self, low_left, up_right):
        self.low_left = low_left
        self.up_right = up_right

    def get_area(self):
        length = self.up_right.x - self.low_left.x
        height = self.up_right.y - self.low_left.y
        return length * height
