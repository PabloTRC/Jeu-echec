Hello

'''
dico pieces prises

t = [0,[0,0],0]
blanc, sa pos, en vie ou pas
'''




board = [[[]for i in range 8]for j in range 8]

moves = {r:[[1,0],[1,1]], d : [[i,0] for i in range 8], f : [[i,i] for i in range 8], t : [[i,0] for i in range 8],c : [[2,1],[1,2]]}

def rev(L):
    L2 = []
    for e in L :
        L2.append(e)
        L2.append(e[0],-e[1])
        L2.append(-e[0],e[1])
    return L2

def verif (piece,pos,coup):
    if not((np.array([pos]) + np.array([coup]))[0] >= 0 and (np.array([pos]) + np.array([coup]))[0] <= 7 and (np.array([pos]) + np.array([coup]))[1] <=7 and (np.array([pos]) + np.array([coup]))[0]>=0) :
        return False
    if piece == c :
        return True
    if coup[0] > coup[1] : 
        max = 
    

#coup (piece,pos)