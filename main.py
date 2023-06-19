from random import randint
from entities import Point, Rectangle
import coordinate_data as cd

if __name__ == "__main__":
    low_left = Point(randint(cd.CORNER1_START, cd.CORNER1_END), randint(cd.CORNER1_START, cd.CORNER1_END))
    up_right = Point(randint(cd.CORNER2_START, cd.CORNER2_END), randint(cd.CORNER2_START, cd.CORNER2_END))

    rect = Rectangle(low_left, up_right)

    print(f"Rectangle Coordinates:\nCorner 1: ({rect.corner1.x}, {rect.corner1.y})\nCorner 2: ({rect.corner2.x}, {rect.corner2.y})")
    print("Guess a coordinate that falls within the rectangle!")

    user_x = float(input("X coordinate: "))
    user_y = float(input("Y coordinate: "))
    user_area = float(input("Guess the area of the rectangle: "))
    user_point = Point(user_x, user_y)

    if user_point.falls_in_rectangle(rect):
        print("Your point was inside the rectangle!")
    else:
        print("Your point was not inside the rectangle.")

    if user_area == rect.get_area():
        print("Your area was correct!")
    else:
        difference = user_area - rect.get_area()
        if difference < 0:
            difference = difference * -1
        print(f"Your area was off by {difference}")
