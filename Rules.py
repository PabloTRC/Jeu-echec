import pyxel
import pathlib
import numpy as np

import pyxel 

BLACK = 0
WHITE = 7
LINES = 8
COLUMNS = 8
SIDE = 16

#Initialisation des variables du chessboard

class Rules:
    def __init__(self,deplacement,coup_valide,CV_T,CV_F,CV_D,coup_possibles):
        self.deplacement = deplacement
        self.coup_valide = coup_valide
        self.CV_T = CV_T
        self.CV_F = CV_F
        self.CV_D = CV_D
        self.coup_possibles = coup_possibles


    def deplacement(self,dico,L,P):
        piece=dico[L]
        x1,y1=L[0],L[1]
        x2,y2=P[0],P[1]
        if piece[1] =='p': #pions
            if piece[2] == 0 :
                if (np.abs(x2-x1) == 1 and y2-y1==1) : 
                    if dico[(x2,y2)][2] == 1:
                        return True 
                    return False
            if piece[2] == 1 :
                if (np.abs(x2-x1) == 1 and y1-y2==1) : 
                    if dico[(x2,y2)][2] == 0:
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
                if dico[(x2,y2)][0]== 1 :
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
                if dico[(x2,y2)][0]==1:
                    return False
                return True
        if piece[1]=='t': #tour
            if x1==x2 and y1!=y2:
                return True
            if x1!=x2 and y1==y2:
                return True
            return False
        if piece[1] == 'f': #fou
            if np.abs(x2-x1) != np.abs(y2 - y1) :
                return False 
            return True
        if piece[1] == 'r': #roi
            if (np.abs(x2-x1)!=0 and np.abs(x2-x1)!=1):
                return False 
            if (np.abs(y2-y1)!=0 and np.abs(y2-y1)!=1):
                return False
            return True 
        if piece[1]=='d': #dame
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
        if piece[1] == "c": #cavalier
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
    def coup_valide(self,dico,L,P):
        x1,y1=L[0],L[1]
        x2,y2=P[0],P[1]
        moi=dico[(x1,y1)]
        pas_moi = dico[(x2,y2)] #on peut pas manger quelqu'un de son équipe
        if moi[2]==pas_moi[2]:
            return False
        if moi[1]=="t" and (np.abs(y2-y1)>1 or np.abs(x2-x1)>1):
            return self.CV_T(dico,x1,x2,y1,y2)
        if moi[1]=="f":
            return self.CV_F(dico,x1,x2,y1,y2)
        if moi[1]=="d":
            return self.CV_D(dico,x1,x2,y1,y2)      
        return True

#coup valide pour la tour (la tour ne peut pas sauter au dessus de d'autres pièces)
    def CV_T(self,dico,x1,x2,y1,y2): 
        if y2-y1>0:
            for i in range(1,y2-y1):
                if dico[(x1,y1+i)][0]==1:
                    return False 
        if y1-y2>0:
            for i in range(1,y1-y2):
                if dico[(x1,y1-i)][0]==1:
                    return False
        if x2-x1>0:
            for i in range(1,x2-x1):
                if dico[(x1+i,y1)][0]==1:
                    return False 
        if x1-x2>0:
            for i in range(1,x1-x2):
                if dico[(x1-i,y1)][0]==1:
                    return False
        return True
    
#Coup valide pour le fou
    def CV_F(self,dico,x1,x2,y1,y2):
        if x2-x1>0:
            if y2-y1>0:
                for i in range(1,x2-x1):
                    for j in range(1,y2-y1):
                        if dico[((x1+i),(y1+i))][0]==1:
                            return False
                return True
            else :
                for i in range(1,x2-x1):
                    for j in range(1,y1-y2):
                        if dico[((x1+i),(y1-i))][0]==1:
                            return False
                return True
        elif x2-x1<0:
            if y2-y1>0:
                for i in range(1,x1-x2):
                    for j in range(1,y2-y1):
                        if dico[((x1-i),(y1+i))][0]==1:
                            return False
                return True
            else :
                for i in range(1,x1-x2):
                    for j in range(1,y1-y2):
                        if dico[((x1-i),(y1-i))][0]==1:
                            return False
                return True
        return False

#coup valide pour la dame 
    def CV_D(self,dico,x1,x2,y1,y2):
        if self.CV_T(dico,x1,x2,y1,y2):
            return True
        if self.CV_F(dico,x1,x2,y1,y2):
            return True
        return False

    def coup_possibles(self,dico,x1,y1):
        CP=[]
        for i in range(8):
            for j in range(8):
                if self.coup_valide(dico,(x1,y1),(i,j)) and self.deplacement(dico,(x1,y1),(i,j)):
                    CP.append((i,j))
        return CP