
'''
dico pieces prises

t = [c,0,0]
cavalier,couleur,pos, en vie ou pas
'''


import numpy as np

#moves
moves = {"r":[(1,0),(-1,0),(1,1)(-1,1),(1,-1),(-1,-1),(0,1),(0,-1)], "d" : [[1,0]], "f" : [], "t" : [[1,0]], "c" : [[2,1],[1,2]]}

def rev(L):
        L2 = []
        for e in L :
            L2.append(e)
            L2.append(e[0],-e[1])
            L2.append(-e[0],e[1])
            L2.append(-e[0],-e[1])
        return L2


    #avant de lancer deplac on verifie que le coup est dans possibles
def deplac(piece,coup):
        if coup in verif_case(pos,piece):
            cases_prises[coup] = piece
            del cases_prises[piece[2]]


def verif_case(pos2,piece):
        pos = piece[2]
        if not (coup[0] >= 0 and coup[0] <= 7 and coup[1] <=7 and coup[0]>=0) :
            return 0
        
        if not coup in cases_prises :
            return 1
        elif :
            if cases_prises[coup][0] == piece[0]:
                return 2


def possibles(piece):

        poss = []

        if piece[0] == 'p':
            if piece[1] == 0 :
                
                if piece[2][1] == 6 :
                     

        if piece[0] == 'c' or piece[0] == 'r':
            for move in rev(moves[piece[0]]) :
                pos2 = np.array([pos]) + np.array([coup])
                if verif_case(pos2,piece()) >= 1 :
                    poss.append(pos2)
        
        else :
            for dir in rev(moves[piece[0]]):
                while np.array(pos2) != (np.array([pos]) + np.array([coup])):
                    pos2 += dir
                    if verif_case(pos2,piece()) >= 1 :
                        poss.append(pos2)
                    if verif_case(pos2,piece()) == 2 :
                        continue()




def coup_valide(self):
        (x1,y1)=self.click1
        (x2,y2)=self.click2
        moi=self.cases[self.click1]
        pas_moi = self.cases[self.click2]
        if moi[1]=="t" and (np.abs(y2-y1)>1 or np.abs(x2-x1)>1):
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
        if moi[2]==pas_moi[2]:
            return False
        return True 


helloo