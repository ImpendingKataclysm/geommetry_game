from random import randint
from entities import Point, Rectangle

if __name__ == "__main__":

    low_min = 0
    low_max = 9
    up_min = 10
    up_max = 19

    low_left = Point(randint(low_min, low_max), randint(low_min, low_max))
    up_right = Point(randint(up_min, up_max), randint(up_min, up_max))

    rect = Rectangle(low_left, up_right)

    print(f"Rectangle Coordinates:\nBottom Left: ({rect.low_left.x}, {rect.low_left.y})\nTop Right: ({rect.up_right.x}, {rect.up_right.y})")
    print("Guess a coordinate that falls within the rectangle!")

    user_x = float(input("X coordinate: "))
    user_y = float(input("Y coordinate: "))
    user_point = Point(user_x, user_y)

    if user_point.falls_in_rectangle(rect):
        print("Your point was inside the rectangle!")
    else:
        print("Your point was not inside the rectangle")
