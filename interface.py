import turtle
import coordinate_data as cd
from random import randint
from entities import GUIRectangle, Point, GUIPoint

if __name__ == "__main__":
    corner1 = Point(randint(cd.CORNER1_START, cd.CORNER1_END),
                    randint(cd.CORNER1_START, cd.CORNER1_END))
    corner2 = Point(randint(cd.CORNER2_START, cd.CORNER2_END),
                    randint(cd.CORNER2_START, cd.CORNER2_END))
    gui_rect = GUIRectangle(corner1, corner2)
    rect_area = gui_rect.get_area()

    print(
        f"Rectangle Coordinates:\nCorner 1: ({gui_rect.corner1.x}, {gui_rect.corner1.y})\nCorner 2: "
        f"({gui_rect.corner2.x}, {gui_rect.corner2.y})")
    print("Guess a coordinate that falls within the rectangle!")

    user_x = float(input("X coordinate: "))
    user_y = float(input("Y coordinate: "))
    user_area = float(input("Guess the area of the rectangle: "))
    user_point = GUIPoint(user_x, user_y)

    if user_point.falls_in_rectangle(gui_rect):
        print("Your point was inside the rectangle!")
    else:
        print("Your point was not inside the rectangle.")

    if user_area == rect_area:
        print("Your area was correct!")
    else:
        difference = user_area - rect_area
        if difference < 0:
            difference = difference * -1
        print(f"Your area was off by {difference}. The area is {rect_area}")

    canvas = turtle.Turtle()
    gui_rect.draw(canvas=canvas)
    user_point.draw(canvas=canvas)

    turtle.done()
