#[0 si non occupé/ 1 si occupé, "nom de la pièce", 0 si noir 1 si blanc 3 si pas occupé, 0 pour le nombre de fois utilisé]


moves = {"r":[(1,0),(1,1)], "d" : [(1,0),(1,1)], "f" : [], "t" : [(1,0)], "c" : [(2,1),(1,2)]}

def rev(L):
        L2 = []
        for e in L :
            L2.append(e)
            L2.append((e[0],-e[1]))
            L2.append((-e[0],e[1]))
            L2.append((-e[0],-e[1]))
        return L2

def verif_case(coup,piece): #coup = (x2,y2)
        pos = piece[2]
        if not board(coup) :
            return 0
        
        if Chessboard.cases[coup][0] == 0 :
            return 1
        else :
            if Chessboard.cases[coup][2] == piece[0]:
                return 2
            
def board((x,y)):
    if x<=7 and y<=7 and x>=0 and y>=0 :
        return True
    return False

def possibles(moi,x1,y1):
        #si on a le temps on fera s'afficher la liste des cases possibles
        poss = {}
        piece = [moi[1],moi[2],(x1,y1)]

        if piece[0] == 'c' or piece[0] == 'r':
            for coup in rev(moves[piece[0]]) :
                pos2 = np.array([piece[2]]) + np.array([coup])
                if verif_case(pos2,piece()) >= 1 :
                    poss[pos2] = 0
        
        else :
            for dir in rev(moves[piece[0]]):
                pos2 = piece[2]
                while board(pos2+dir) :
                    pos2 += dir
                    if verif_case(pos2,piece) >= 1 :
                        poss[pos2] = 0
                    if verif_case(pos2,piece) == 2 :
                        continue
        
        if piece[0] == 'p':
             










        return poss


def coup_valide(self):
        (x1,y1)=self.click1
        (x2,y2)=self.click2

        moi=self.cases[self.click1]
        pas_moi = self.cases[self.click2]

        if [x2,y2] in possibles(moi,x1,y1):
            return True
        else :
            return False
        




def en_echec (couleur):    #couleur c'est 1 ou 0 selon la couelur qui est peutetre en échec
    for x in range(7):
        for y in range(7):
            essai = Chessboard.cases[(x,y)]

            if essai[1] == couleur + 1 or essai[1] == couleur - 1 :
                for pos in possibles(essai,x,y):
                    if Chessboard.cases[pos][1] == 'r':
                        return True
    
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