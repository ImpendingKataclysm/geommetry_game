class Point:
    """
    Describes a point on a grid, defined by its x and y coordinates.
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
        return rectangle.min_x < self.x < rectangle.max_x and rectangle.min_y < self.y < rectangle.max_y

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


class GUIPoint(Point):
    """
    Extends the Point class to render the Point in a turtle canvas
    """

    def draw(self, canvas, size=5, color='red'):
        """
        Draws the Point in a given turtle canvas
        :param canvas: the turtle canvas on which to draw the point
        :param size: the size of the point
        :param color: the color of the point
        :return:
        """
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


class Rectangle:
    """
    Describes a rectangle in terms of its lower-left (min x, min y) and
    upper-right (max x, max y) coordinates.
    """

    def __init__(self, point1, point2):
        self.corner1 = point1
        self.corner2 = point2
        self.min_x = point1.x
        self.min_y = point1.y
        self.max_x = point2.x
        self.max_y = point2.y

        if point1.x > point2.x:
            self.min_x = point2.x
            self.max_x = point1.x

        if point1.y > point2.y:
            self.min_y = point2.y
            self.max_y = point1.y

    def get_area(self):
        """
        Calculates the area of the rectangle
        :return: the area of the rectangle
        """
        length = self.max_x - self.min_x
        height = self.max_y - self.min_y
        return length * height


class GUIRectangle(Rectangle):
    """
    Extends the Rectangle class to render the rectangle in a graphical user
    interface
    """

    def draw(self, canvas):
        """
        Draws the Rectangle on a turtle canvas.
        :param canvas: Turtle canvas on which to render the rectangles
        :return:
        """
        horizontal_distance = self.corner2.x - self.corner1.x
        vertical_distance = self.corner2.y - self.corner1.y

        # Start at certain coordinate
        canvas.penup()
        canvas.goto(self.corner1.x, self.corner1.y)

        # Move the line
        canvas.pendown()
        canvas.forward(horizontal_distance)
        canvas.left(90)
        canvas.forward(vertical_distance)
        canvas.left(90)
        canvas.forward(horizontal_distance)
        canvas.left(90)
        canvas.forward(vertical_distance)
