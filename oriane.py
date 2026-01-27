#[0 si non occupé/ 1 si occupé, "nom de la pièce", 0 si noir 1 si blanc 3 si pas occupé, 0 pour le nombre de fois utilisé]


moves = {"r":[(1,0),(-1,0),(1,1)(-1,1),(1,-1),(-1,-1),(0,1),(0,-1)], "d" : [[1,0]], "f" : [], "t" : [[1,0]], "c" : [[2,1],[1,2]]}

def rev(L):
        L2 = []
        for e in L :
            L2.append(e)
            L2.append(e[0],-e[1])
            L2.append(-e[0],e[1])
            L2.append(-e[0],-e[1])
        return L2

def verif_case(pos2,piece):
        pos = piece[2]
        if not (coup[0] >= 0 and coup[0] <= 7 and coup[1] <=7 and coup[0]>=0) :
            return 0
        
        if cases[(coup[0],coup[1])][0] == 0 :
            return 1
        elif :
            if cases[(coup[0],coup[1])][2] == piece[0]:
                return 2
            

def possibles(x,y):
        #si on a le temps on fera s'afficher la liste des cases possibles
        poss = {}

        if piece[0] == 'c' or piece[0] == 'r':
            for move in rev(moves[piece[0]]) :
                pos2 = np.array([pos]) + np.array([coup])
                if verif_case(pos2,piece()) >= 1 :
                    poss[pos2] = 0
        
        else :
            for dir in rev(moves[piece[0]]):
                while np.array(pos2) != (np.array([pos]) + np.array([coup])):
                    pos2 += dir
                    if verif_case(pos2,piece()) >= 1 :
                        poss[pos2] = 0
                    if verif_case(pos2,piece()) == 2 :
                        continue()
        
        return poss




def coup_valide(self):
        (x1,y1)=self.click1
        (x2,y2)=self.click2

        moi=self.cases[self.click1]
        pas_moi = self.cases[self.click2]
        
        piece = [moi[1],moi[2],[x1,y1]]

        if [x2,y2] in possibles(piece):
            return True
        else :
            return False










'''
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
'''