import pyxel 
from Interface import Chessboard


class Pieces(Chessboard):

    def dico_pieces():
        pieces = {}
        pieces["p",0] = [(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]
        pieces["t",0] = [()]


class Interaction(Chessboard):
    
    def __click__(self):
         self.click1 = None 
         self.click2 = None
         self.first_click_done = False 

    def two_clicks(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            x, y = pyxel.mouse_x, pyxel.mouse_y
            if not self.first_click_done:
                # First click: store position
                self.click1 = (x, y)
                self.first_click_done = True
            else:
                # Second click: store position and reset state
                self.click2 = (x, y)
                self.first_click_done = False
                # Now you can use both click1 and click2
                print(self.click1,self.click2)
        self.interaction()

    #def coup_valid(self, piece,x1,y1,x2,y2):
            #if (x1,y1)==(x2,y2):
            #    return 0 #coup non valide
           # if piece[1]=='p': #modifier en cas de mangeage
             #   if x2!=x1:
             #       return 0
             #   if piece[2]==1 and y2>=y1:
             #       return 0
             #   if piece[2]==0 and y2<=y1:
             #       return 0
             #   return 1
    
    def interaction(self):
        x1,y1 = self.click1
        x2,y2 = self.click2
        print(x1,y1,x2,y2)
        piece=self.cases[(x1,y1)]
        #if self.coup_valid(self,piece,x1,y1,x2,y2)==1:
        self.cases[(x1,y1)]=[0,'',0]
        self.cases[(x2,y2)]=[1,piece[1],piece[2]]

if __name__ == "__main__":
    Interaction()