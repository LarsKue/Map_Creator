"""
Map_Creator.py
Scripted by: Lars Kuehmichel
Description: Creates a map and collision map file based on image input for use in the project
"The Unmaking of Elynia", a side scroller game by Lars Kuehmichel and Thomas Rudolph.
"""

from PIL import Image

im = Image.open("empty-test.png")
RGB = list(im.getdata())
column = 0
width, height = im.size
print(RGB)          # You should check if this produced the correct results (else your image might not be RGB-coded)
print("Size: ", width, height)
im.close()
with open("empty-test.map", "w") as m, open("empty-test.cmap", "w") as c:
    for item in RGB:
        # black = air
        if item == (0, 0, 0):
            m.write("0000")
            c.write("0")
        # brown = dirt
        if item == (139, 69, 19):
            m.write("0001")
            c.write("1")
        # green = grass
        if item == (0, 200, 0):
            m.write("0002")
            c.write("1")
        # red = treasure chest
        if item == (255, 0, 0):
            m.write("0003")
            c.write("1")
        # middle grey = stone bricks
        if item == (139, 139, 139):
            m.write("0004")
            c.write("1")
        # dark grey = stone
        if item == (69, 69, 69):
            m.write("0005")
            c.write("1")
        # dark blue = animated water surface
        # note this does not yet work
        if item == (0, 51, 103):
            m.write("9003")
            c.write("0")
        # blue = standard water
        if item == (0, 126, 255):
            m.write("0100")
            c.write("0")
        # orange = lava
        if item == (255, 127, 0):
            m.write("0101")
            c.write("0")
        # white grey = marble
        if item == (208, 208, 208):
            m.write("0102")
            c.write("1")

        """
        Enter more colour coding here
        """

        """ Temporary """
        # dark red = ladder
        if item == (124, 0, 0):
            m.write("0103")
            c.write("0")

        """
        Adding commas and creating new lines
        """

        # if the column index is equal to the width, a comma needs to be placed
        if column != (width - 1):
            m.write(",")
            c.write(",")
            column += 1
        # otherwise, a new line has to begin
        else:
            m.write("\n")
            c.write("\n")
            column = 0
