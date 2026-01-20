Hello

'''
dico pieces prises

t = [0,[0,0],0]
blanc, sa pos, en vie ou pas
'''


import numpy as np

board = [[[]for i in range 8]for j in range 8]

moves = {r:[[1,0],[1,1]], d : [[i,0] for i in range 8], f : [[i,i] for i in range 8], t : [[i,0] for i in range 8],c : [[2,1],[1,2]]}

def rev(L):
    L2 = []
    for e in L :
        L2.append(e)
        L2.append(e[0],-e[1])
        L2.append(-e[0],e[1])
    return L2

def deplac (piece,pos,coup):
    if not((np.array([pos]) + np.array([coup]))[0] >= 0 and (np.array([pos]) + np.array([coup]))[0] <= 7 and (np.array([pos]) + np.array([coup]))[1] <=7 and (np.array([pos]) + np.array([coup]))[0]>=0) :
        return False
    if piece == c or piece == r:
        if not (np.array([pos]) + np.array([coup])) in cases_prises :
            return True
        else :
            if cases_prises[(np.array([pos]) + np.array([coup]))]
            
            
    max = 1
    if coup[0] > coup[1]: 
        max = 0
    pos2 = pos.copy()
    pos2.append
    while np.array(pos2[max]) != (np.array([pos]) + np.array([coup]))[max]:
        
    
    

#coup (piece,pos)