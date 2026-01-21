#Dessin des pièces 
#Pion dessin + restitution sous forme de fichier
import pyxel
import pathlib

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
        self.cases=self.cases_ini()
        pyxel.run(self.update, self.draw)

    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.interaction()
    def cases_ini(self):
        cases = {(x,y):[0,0,0] for x in range(8) for y in range(8)} #[0 si non occupé, 1 si occupé, "nom de la pièce", 0 si noir 1 si blanc]
        y = 1
        for x in range(LINES):
            cases[(x,y)] = [1,"p",0]
        y = 6
        for x in range(LINES):
            cases[(x,y)] = [1,"p",1]
        y=0
        for x in [0,7]:
            cases[(x,y)]=[1,"t",0]
        for x in [1,6]:
            cases[(x,y)]=[1,"c",0]
        for x in [2,5]:
            cases[(x,y)]=[1,"f",0]
        cases[(3,y)]=[1,"d",0]
        cases[(4,y)]=[1,"r",0]
        y=7
        for x in [0,7]:
            cases[(x,y)]=[1,"t",1]
        for x in [1,6]:
            cases[(x,y)]=[1,"c",1]
        for x in [2,5]:
            cases[(x,y)]=[1,"f",1]
        cases[(3,y)]=[1,"d",1]
        cases[(4,y)]=[1,"r",1]
        print(cases)
    
    def interaction(self):
        L=[]
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) :
            x1,y1=pyxel.mouse_x//16, pyxel.mouse_y//16
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) :
                x2,y2=pyxel.mouse_x//16, pyxel.mouse_y//16
                piece=self.cases[(x1,y1)]
                if coup_valid(self,piece[1],(x1,y1),(x2,y2))==1:
                    self.cases[(x1,y1)]=[0,'',0]
                    self.cases[(x2,y2)]=[1,pièce[1],pièce[2]]
    
    def coup_valid(self, piece,(x1,y1),(x2,y2)):
        if (x1,y1)==(x2,y2):
            return 0 #coup non valide
        if piece[1]=='p': #modifier en cas de mangeage
            if x2!=x1:
                return 0
            if piece[2]==1 and y2>=y1:
                return 0
            if piece[2]==0 and y2<=y1:
                return 0
            return 1



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

    def draw(self):
        for i in range (8):
            for j in range(8):
                Cas=self.cases[(i,j)]
                if Cas[2]!='':
                    drawbis(Cas[2],i,j,Cas[3]) #Nom pièce, position, couleur

    def drawbis(piece,x,y,Couleur):
        if piece=='p' and couleur==1:
            draw_white_pawns(self,x,y)
        elif piece=='p' and couleur==0:
            draw_black_pawns(self,x,y)
    
    def draw_white_pawns(self,x,y):
        pyxel.blt(x*SIDE,y*SIDE,1,0,0,SIDE,SIDE, colkey=BLACK)
    def draw_black_pawns(self,x,y):
        pyxel.blt(x*SIDE,y*SIDE,0,0,0,SIDE,SIDE, colkey=BLACK)
    def draw_white_tower(self,x,y):
        pyxel.blt(x*SIDE,y*SIDE,1,0,6*SIDE,SIDE,SIDE, colkey=BLACK)
    def draw_black_tower(self,x,y):
        pyxel.blt(x*SIDE,y*SIDE,0,0,6*SIDE,SIDE,SIDE, colkey=BLACK)
    def draw_white_horse(self,x,y):
        pyxel.blt(x*SIDE,y*SIDE,1,0,4*SIDE,SIDE,SIDE, colkey=BLACK)
    def draw_black_horse(self,x,y):
        pyxel.blt(x*SIDE,y*SIDE,0,0,4*SIDE,SIDE,SIDE, colkey=BLACK)
    def draw_white_bishop(self,x,y):
        pyxel.blt(x*SIDE,y*SIDE,1,0,2*SIDE,SIDE,SIDE, colkey=BLACK)
    def draw_black_bishop(self,x,y):
        pyxel.blt(x*SIDE,y*SIDE,0,0,2*SIDE,SIDE,SIDE, colkey=BLACK)
    def draw_white_king(self,x,y):
        pyxel.blt(x*SIDE,y*SIDE,1,2*SIDE,2*SIDE,SIDE,SIDE, colkey=BLACK)
    def draw_white_queen(self,x,y):
        pyxel.blt(x*SIDE,y*SIDE,1,2*SIDE,0,SIDE,SIDE, colkey=BLACK)
    def draw_black_king(self,x,y):
        pyxel.blt(x*SIDE,y*SIDE,0,2*SIDE,2*SIDE,SIDE,SIDE, colkey=BLACK)
    def draw_black_queen(self,x,y):
        pyxel.blt(x*SIDE,y*SIDE,0,2*SIDE,0,SIDE,SIDE, colkey=BLACK)
        

    


if __name__ == "__main__":
    Chessboard()
