import pyxel 

WIDTH = 30
HEIGHT = 30
BLACK = 0
WHITE = 7

def checkers():
    checkers = set()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x+y) % 2 == 0 :
                checkers.add((x,y))
    return checkers

def display(color, pixels=None):
    if pixels is None:
        pyxel.cls(color)
    elif len(pixels) >= 1 and type(pixels[0]) == int:
        display(color, [pixels])
    else:
        for x, y in pixels:
            pyxel.pset(x, y, color)

def draw_maze(maze):
    display(BLACK)
    display(WHITE, maze)

pyxel.init(WIDTH, HEIGHT)
draw_maze(checkers())
pyxel.show()

