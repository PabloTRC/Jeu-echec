#Dessin des pièces 
#Pion dessin + restitution sous forme de fichier
#Piece tt desssin
#Dico de piece
#Affichage en fonction du dico
import pyxel
import pathlib
import numpy as np

import pyxel 

import sys
sys.setrecursionlimit(2000)


BLACK = 0
WHITE = 7
LINES = 8
COLUMNS = 8
SIDE = 16

class Chessboard:

#Initialisation des variables du chessboard
    def __init__(self):
        pyxel.init(LINES*SIDE,COLUMNS*SIDE + SIDE,title = "Chess")
        pyxel.load("pions.pyxres")
        pyxel.mouse(True)
        self.click1=None
        self.click2=None
        self.Nombre_coups=0
        self.first_click_done=False
        self.cases=self.cases_ini()
        self.turn = "White"
        pyxel.run(self.update, self.draw)

#fonction update du plateau qui prend en compte la réinitialisation au cas où on presse R, qui dessine etc...    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_R):
            self.click1=None
            self.click2=None
            self.Nombre_coups=0
            self.first_click_done=False
            self.cases = self.cases_ini()
            self.turn = "White"
        self.draw()
        self.interaction()

#Initialisation du dictionnaire des cases du plateau d'échecs        
    def cases_ini(self):
        cases = {(x,y):[0,'',3,0] for x in range(8) for y in range(8)} #[0 si non occupé, 1 si occupé; "nom de la pièce"; 0 si noir, 1 si blanc, 3 si pas occupé; 0 pour le nombre de fois utilisé]
        y = 1
        for x in range(LINES):
            cases[(x,y)] = [1,"p",0,0]
        y = 6
        for x in range(LINES):
            cases[(x,y)] = [1,"p",1,0]
        y=0
        for x in [0,7]:
            cases[(x,y)]=[1,"t",0,0]
        for x in [1,6]:
            cases[(x,y)]=[1,"c",0,0]
        for x in [2,5]:
            cases[(x,y)]=[1,"f",0,0]
        cases[(3,y)]=[1,"d",0,0]
        cases[(4,y)]=[1,"r",0,0]
        y=7
        for x in [0,7]:
            cases[(x,y)]=[1,"t",1,0]
        for x in [1,6]:
            cases[(x,y)]=[1,"c",1,0]
        for x in [2,5]:
            cases[(x,y)]=[1,"f",1,0]
        cases[(3,y)]=[1,"d",1,0]
        cases[(4,y)]=[1,"r",1,0]
        return cases

#Click sur les différentes cases + alternance blancs noirs pour jouer + jeu effectif si coup valide   
    def interaction(self):
        if self.Nombre_coups%2==0:     
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) :
                x,y=pyxel.mouse_x//16, pyxel.mouse_y//16
                if not self.first_click_done:
                    self.click1=(x,y)
                    self.click2=None
                    self.first_click_done=True
                else:
                    self.click2=(x,y)
                    self.first_click_done=False
            if self.click2!=None and self.cases[self.click1][2]==1:
                if self.deplacement(self.click1,self.click2) and self.coup_valide(self.click1,self.click2):
                    self.cases[self.click2]=[self.cases[self.click1][0],self.cases[self.click1][1],self.cases[self.click1][2],self.cases[self.click1][3]+1]
                    self.cases[self.click1]=[0,'',3,0]
                    self.Nombre_coups+=1
                    self.turn = "Black"
        else:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) :
                x,y=pyxel.mouse_x//16, pyxel.mouse_y//16
                if not self.first_click_done:
                    self.click1=(x,y)
                    self.click2=None
                    self.first_click_done=True
                else:
                    self.click2=(x,y)
                    self.first_click_done=False
            if self.click2!=None and self.cases[self.click1][2]==0:
                if self.deplacement(self.click1,self.click2) and self.coup_valide(self.click1,self.click2):
                    self.cases[self.click2]=[self.cases[self.click1][0],self.cases[self.click1][1],self.cases[self.click1][2],self.cases[self.click1][3]+1]
                    self.cases[self.click1]=[0,'',3,0]
                    self.Nombre_coups+=1
                    self.turn = "White"

#Manière dont se déplacent les pièces
    def deplacement(self,L,P):
        piece=self.cases[L]
        x1,y1=L[0],L[1]
        x2,y2=P[0],P[1]
        if piece[1] =='p': #A part
            if piece[2] == 0 :
                if (np.abs(x2-x1) == 1 and y2-y1==1) : 
                    if self.cases[(x2,y2)][2] == 1:
                        return True 
                    return False
            if piece[2] == 1 :
                if (np.abs(x2-x1) == 1 and y1-y2==1) : 
                    if self.cases[(x2,y2)][2] == 0:
                        return True 
                    return False
            if piece[3]==0:
                if x1!=x2:
                    return False
                if piece[2]==1 and y1<=y2:
                    return False
                if piece[2]==0 and y1>=y2:
                    return False
                if np.abs(y1-y2)>2:
                    return False
                if self.cases[(x2,y2)][0]== 1 :
                    return False 
                return True
            else: 
                if x1!=x2:
                    return False
                if piece[2]==1 and y1<=y2:
                    return False
                if piece[2]==0 and y1>=y2:
                    return False
                if np.abs(y1-y2)>1:
                    return False
                if self.cases[self.click2][0]==1:
                    return False
                return True
        if piece[1]=='t':
            if x1==x2 and y1!=y2:
                return True
            if x1!=x2 and y1==y2:
                return True
            return False
        if piece[1] == 'f':
            if np.abs(x2-x1) != np.abs(y2 - y1) :
                return False 
            return True
        if piece[1] == 'r':
            if (np.abs(x2-x1)!=0 and np.abs(x2-x1)!=1):
                return False 
            if (np.abs(y2-y1)!=0 and np.abs(y2-y1)!=1):
                return False
            return True 
        if piece[1]=='d':
            U=0
            if x1==x2 and y1!=y2:
                U+=1
            elif x1!=x2 and y1==y2:
                U+=1
            elif np.abs(x2-x1) == np.abs(y2 - y1) :
                U+=1 
            if U!=1:
                return False
            return True
        if piece[1] == "c":
            if (np.abs(x2-x1)!=1 and np.abs(x2-x1)!=2):
                return False 
            if (np.abs(y2-y1)!=1 and np.abs(y2-y1)!=2):
                return False 
            if np.abs(x2-x1)==1:
                if np.abs(y2-y1)!=2:
                          return False
            if np.abs(x2-x1)==2:
                if np.abs(y2-y1)!=1:
                          return False  
            return True

#Ne pas sauter au-dessus d'une pièce
    def coup_valide(self,L,P):
        x1,y1=L[0],L[1]
        x2,y2=P[0],P[1]
        moi=self.cases[(x1,y1)]
        pas_moi = self.cases[(x2,y2)]
        if moi[2]==pas_moi[2]:
            return False
        if moi[1]=="t" and (np.abs(y2-y1)>1 or np.abs(x2-x1)>1):
            return self.CV_T(x1,x2,y1,y2)
        if moi[1]=="f":
            return self.CV_F(x1,x2,y1,y2)
        if moi[1]=="d":
            return self.CV_D(x1,x2,y1,y2)      
        return True
    def CV_T(self,x1,x2,y1,y2):
        if y2-y1>0:
            for i in range(1,y2-y1):
                if self.cases[(x1,y1+i)][0]==1:
                    return False 
        if y1-y2>0:
            for i in range(1,y1-y2):
                if self.cases[(x1,y1-i)][0]==1:
                    return False
        if x2-x1>0:
            for i in range(1,x2-x1):
                if self.cases[(x1+i,y1)][0]==1:
                    return False 
        if x1-x2>0:
            for i in range(1,x1-x2):
                if self.cases[(x1-i,y1)][0]==1:
                    return False
        return True   
    def CV_F(self,x1,x2,y1,y2):
        if x2-x1>0:
            if y2-y1>0:
                for i in range(1,x2-x1):
                    for j in range(1,y2-y1):
                        if self.cases[((x1+i),(y1+i))][0]==1:
                            return False
                return True
            else :
                for i in range(1,x2-x1):
                    for j in range(1,y1-y2):
                        if self.cases[((x1+i),(y1-i))][0]==1:
                            return False
                return True
        elif x2-x1<0:
            if y2-y1>0:
                for i in range(1,x1-x2):
                    for j in range(1,y2-y1):
                        if self.cases[((x1-i),(y1+i))][0]==1:
                            return False
                return True
            else :
                for i in range(1,x1-x2):
                    for j in range(1,y1-y2):
                        if self.cases[((x1-i),(y1-i))][0]==1:
                            return False
                return True
        return False
    def CV_D(self,x1,x2,y1,y2):
        if self.CV_T(x1,x2,y1,y2):
            return True
        if self.CV_F(x1,x2,y1,y2):
            return True
        return False

    def coup_possibles(self,x1,y1):
        CP=[]
        for i in range(8):
                for j in range(8):
                    if i!=x1 and j!=y1:
                        if self.coup_valide((x1,y1),(i,j)) and self.deplacement((x1,y1),(i,j)):
                             CP.append((i,j))
        return CP
                             

    







#Fonction dessiner étant donné un dictionnaire des cases à l'instant t avec les pièces et les cases
    def draw(self):
        pyxel.cls(0)
        self.draw_chessboard()
        self.drawter()    
    def draw_chessboard (self):
        for line in range(LINES):
            for col in range(COLUMNS):
                if (col+line)%2==1:
                    color = BLACK
                else : 
                    color = WHITE
                pyxel.rect(line*SIDE, col*SIDE, SIDE, SIDE, color)
        pyxel.rect(0,COLUMNS*SIDE+2, LINES*SIDE, SIDE, 6)
        pyxel.rect(0,COLUMNS*SIDE,LINES*SIDE,2,0)
        pyxel.text(10,COLUMNS*SIDE+4,f"{self.turn}" "'s turn",0)
        pyxel.text(10,COLUMNS*SIDE+10,"Press R to restart",0)
        #surlignage des cases
        if self.first_click_done:
            (x1,y1)=self.click1
            pyxel.rect(x1*SIDE,y1*SIDE,5,1,8)
            pyxel.rect(x1*SIDE+11,y1*SIDE,5,1,8)
            pyxel.rect(x1*SIDE,y1*SIDE,1,5,8)
            pyxel.rect(x1*SIDE,y1*SIDE+11,1,5,8)
            pyxel.rect(x1*SIDE+15,y1*SIDE,1,5,8)
            pyxel.rect(x1*SIDE,y1*SIDE+15,5,1,8)
            pyxel.rect(x1*SIDE+11,y1*SIDE+15,5,1,8)
            pyxel.rect(x1*SIDE+15,y1*SIDE+11,1,5,8)
            CP=self.coup_possibles(x1,y1)
            for L in CP:
                 pyxel.circ(L[0]*SIDE+8,L[1]*SIDE+8,3,6)
            
            
        #mis en évidence des coups possibles
                 
    def drawter(self):
        for i in range (8):
            for j in range(8):
                Cas=self.cases[(i,j)]
                if Cas[1]!='':
                    self.drawbis(Cas[1],i,j,Cas[2]) #Nom pièce, position, couleur
    def drawbis(self,piece,x,y,Couleur):
        if piece=='p':
            if Couleur==1:
                self.draw_white_pawns(x,y)
            else:
                self.draw_black_pawns(x,y)
        if piece=='r':
            if Couleur==1:
                self.draw_white_king(x,y)
            else:
                self.draw_black_king(x,y)
        if piece=='d':
            if Couleur==1:
                self.draw_white_queen(x,y)
            else:
                self.draw_black_queen(x,y)
        if piece=='f':
            if Couleur==1:
                self.draw_white_bishop(x,y)
            else:
                self.draw_black_bishop(x,y)
        if piece=='t':
            if Couleur==1:
                self.draw_white_tower(x,y)
            else:
                self.draw_black_tower(x,y)
        if piece=='c':
            if Couleur==1:
                self.draw_white_horse(x,y)
            else:
                self.draw_black_horse(x,y)
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
        

#Lancer le jeu
if __name__ == "__main__":
    Chessboard()
