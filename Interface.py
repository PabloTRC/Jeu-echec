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
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.draw_chessboard()
        self.draw_white_pawns()
        self.draw_black_pawns()
        self.draw_white_tower()
        self.draw_black_tower()
        self.draw_white_horse()
        self.draw_black_horse()
        self.draw_white_bishop()
        self.draw_black_bishop()
        self.draw_white_monarchs()
        self.draw_black_monarchs()

    def draw_chessboard (self):
        for line in range(LINES):
            for col in range(COLUMNS):
                if (col+line)%2==1:
                    color = BLACK
                else : 
                    color = WHITE
                pyxel.rect(line*SIDE, col*SIDE, SIDE, SIDE, color)
    
    def draw_white_pawns(self):
        col = 6
        for line in range(LINES):
            pyxel.blt(line*SIDE,col*SIDE,1,0,0,SIDE,SIDE, colkey=BLACK)
    
    def draw_black_pawns(self):
        col = 1
        for line in range(LINES):
            pyxel.blt(line*SIDE,col*SIDE,0,0,0,SIDE,SIDE, colkey=BLACK)
    
    def draw_white_tower(self):
        col = 7
        for line in [0,7]:
            pyxel.blt(line*SIDE,col*SIDE,1,0,6*SIDE,SIDE,SIDE, colkey=BLACK)
    
    def draw_black_tower(self):
        col = 0
        for line in [0,7]:
            pyxel.blt(line*SIDE,col*SIDE,0,0,6*SIDE,SIDE,SIDE, colkey=BLACK)
    
    def draw_white_horse(self):
        col = 7
        for line in [1,6]:
            pyxel.blt(line*SIDE,col*SIDE,1,0,4*SIDE,SIDE,SIDE, colkey=BLACK)
    
    def draw_black_horse(self):
        col = 0
        for line in [1,6]:
            pyxel.blt(line*SIDE,col*SIDE,0,0,4*SIDE,SIDE,SIDE, colkey=BLACK)
        
    def draw_white_bishop(self):
        col = 7
        for line in [2,5]:
            pyxel.blt(line*SIDE,col*SIDE,1,0,2*SIDE,SIDE,SIDE, colkey=BLACK)
    
    def draw_black_bishop(self):
        col = 0
        for line in [2,5]:
            pyxel.blt(line*SIDE,col*SIDE,0,0,2*SIDE,SIDE,SIDE, colkey=BLACK)
    
    def draw_white_monarchs(self):
        col = 7
        #king
        line = 4
        pyxel.blt(line*SIDE,col*SIDE,1,2*SIDE,2*SIDE,SIDE,SIDE, colkey=BLACK)
        #queen
        line = 3
        pyxel.blt(line*SIDE,col*SIDE,1,2*SIDE,0,SIDE,SIDE, colkey=BLACK)
    
    def draw_black_monarchs(self):
        col = 0
        #king
        line = 4
        pyxel.blt(line*SIDE,col*SIDE,0,2*SIDE,2*SIDE,SIDE,SIDE, colkey=BLACK)
        #queen
        line = 3
        pyxel.blt(line*SIDE,col*SIDE,0,2*SIDE,0,SIDE,SIDE, colkey=BLACK)
        


    



if __name__ == "__main__":
    Chessboard()
