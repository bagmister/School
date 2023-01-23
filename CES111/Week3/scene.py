# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random

def main():

    scene_width = 800
    scene_height = 500
    canvas = start_drawing("Scene", scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3, scene_width, scene_height, width=0, fill="sky blue")
    diameter = 100
    # Draw a row of circles with
    # some of the circles missing.
    x = 800
    y = 900
    half_height = round(scene_height / .4)
    min_diam = 40
    max_diam = 80
    for i in range(50):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="white", width=1)


def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")

    # Draw a pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top, skirt_right, trunk_top, skirt_left, trunk_top, outline="gray20", width=1, fill="dark green")


main()