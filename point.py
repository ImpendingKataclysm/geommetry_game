class Point:
    """
    This class describes a point on a grid, defined by its x and y coordinates.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, low_left, up_right):
        """
        Determines whether the Point falls within the coordinates of a specified
        rectangle.
        :param low_left: A tuple containing the coordinates of the rectangle's
        lower-left corner, i.e. the rectangle's minimum (x, y) values
        :param up_right: A tuple containing the coordinates of the rectangle's
        upper-right corner, i.e. the rectangle's maximum (x, y) values
        :return: True if the Point falls within the rectangle's coordinates,
        otherwise False
        """
        if low_left[0] < self.x < up_right[0] \
                and low_left[1] < self.y < up_right[1]:
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


if __name__ == "__main__":
    my_point = Point(6, 7)

    print(f"({my_point.x}, {my_point.y})")
    print(my_point.falls_in_rectangle((1, 4), (9, 10)))
    print(my_point.distance_from_point(Point(10, 25)))
