"""An example program using turtle to draw different shapes"""

import turtle

# --------- EDIT AREA ---------
CORNERS = 5           # default: 5
SIDE_LEN = 100        # default: 100
PEN_COLOR = "blue"    # default: "black
PEN_SIZE = 10         # default: 1
FILL_COLOR = "red"    # default: "white"
SHAPE = "arrow"       # default: "turtle"
# See https://trinket.io/docs/colors for color names
# --------- END EDIT  ---------


BOB = turtle.Turtle()
BOB.pen(pencolor=PEN_COLOR, fillcolor=FILL_COLOR, pensize=PEN_SIZE)

BOB.begin_fill()
for _ in range(CORNERS):
    BOB.forward(SIDE_LEN)
    BOB.left(360/CORNERS)
BOB.end_fill()

turtle.done()
