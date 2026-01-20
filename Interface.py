import pyxel 

WIDTH = 30
HEIGHT = 30

def checkers():
    checkers = set()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x+y) % 2 == 0 :
                checkers.add((x,y))
    return checkers

pyxel.init(WIDTH, HEIGHT)
draw_maze(checkers())
pyxel.show()