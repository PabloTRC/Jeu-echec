import pyxel 

BLACK = 0
WHITE = 7
LINES = 8
COLUMNS = 8
SIDE = 16

class Chessboard:
    def __init__(self):
        pyxel.init(LINES*SIDE,COLUMNS*SIDE,title = "Chess")
        pyxel.load("pions.pyxres")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        for line in range(LINES):
            for col in range(COLUMNS):
                if line% 2 == 0 and col%2 == 1:
                    color = BLACK
                elif line%2==1 and col%2==0 :
                    color = BLACK
                else : 
                    color = WHITE
                pyxel.rect(line*SIDE, col*SIDE, SIDE, SIDE, color)
        #white pawns
        col = 6
        for line in range(LINES):
            pyxel.blt(line*SIDE,col*SIDE,1,0,0,SIDE,SIDE, colkey=BLACK)
        #black pawns
        col = 1
        for line in range(LINES):
            pyxel.blt(line*SIDE,col*SIDE,0,0,0,SIDE,SIDE, colkey=BLACK)



if __name__ == "__main__":
    Chessboard()
