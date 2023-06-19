import turtle
import coordinate_data as cd
from random import randint
from entities import GUIRectangle, Point

if __name__ == "__main__":
    corner1 = Point(randint(cd.CORNER1_START, cd.CORNER1_END),
                    randint(cd.CORNER1_START, cd.CORNER1_END))
    corner2 = Point(randint(cd.CORNER2_START, cd.CORNER2_END),
                    randint(cd.CORNER2_START, cd.CORNER2_END))
    gui_rect = GUIRectangle(corner1, corner2)
    canvas = turtle.Turtle()
    gui_rect.draw(canvas=canvas)

    turtle.done()
