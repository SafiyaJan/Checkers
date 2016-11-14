#Checkers

from Tkinter import *

class Interface(): #creating a class that will create the main Checkers Interface
    
    def __init__(self,master): #takes in the game window as a parameter

        #setting up attributes
        self.columns = 8
        self.rows = 8
        self.squaresize = 70
        self.BROWN = '#8B4513'
        self.BEIGE = '#D2B48C'
        self.master = master
        
        #defining width and height of canvas
        width = self.columns*self.squaresize
        height = self.rows*self.squaresize
        
        #creating a canvas that will house all the squares of the gameboard
        self.canvas = Canvas(master,height = height, width = width)
        self.canvas.pack()
        #calling drawCheckersBoard function that will draw the actual gameboard on the canvas
        self.drawCheckersBoard()

    def drawCheckersBoard(self): #function that draws the Checkers gameboard
        #initializing the color to be BEIGE
        color = self.BEIGE

        #iterating through entire through each row
        for i in range (self.rows):
            #following if statements interchange the colors used to fill the squares
            if color == self.BEIGE:
                color = self.BROWN
            else:
                color = self.BEIGE

            #iterating through each coloumn of each row
            for j in range (self.columns):

                #finding the x and y coordinates of the top left (x1,y1) and botton right (x2,y2) of the square to be drawn
                x1 = j*self.squaresize
                y1 = (7-i)*self.squaresize
                x2 = x1 + self.squaresize
                y2 = y1 + self.squaresize

                #drawing the square
                self.canvas.create_rectangle(x1,y1,x2,y2,fill=color,tags = str(color))

                #interchanging colors again in order to having alternating colors for each square (ie, one BEIGE square, one BROWN square, one BEIGE square and so on)
                if color == self.BEIGE:
                    color = self.BROWN
                else:
                    color = self.BEIGE

        self.drawCheckers() #calling drawCheckers function that will draw the checkers on this board

    
    def CheckerButtonPress(self,event): #calculates the coordinates at which the checker was clicked
        global prevsquare
        global turns
        item = self.canvas.find_closest(event.x,event.y)[0] 
        tags = self.canvas.gettags(item)[0]
        prevsquare.append((tags,event.x,event.y))
        turns.append(tags)


    def CheckerButtonRelease(self,event):
        global prevsquare
        global turns
        self.CheckerButtonPress(event)
        x = prevsquare
        print prevsquare
  
        if len(turns)>=4:
            if turns[len(turns)-2] == turns[len(turns)-4]:
                if turns[len(turns)-2] == "darkbrown":
                    print "Its LightBrown's Turn"
                    prevsquare = []
                    turns = []
                    return
                if turns[len(turns)-2] == "lightbrown":
                    print "Its DarkBrown's Turn"
                    prevsquare = []
                    turns = []
                    return
                
        
            elif x[0][0] == "darkbrown":

                if x[1][0] == "#D2B48C":
                    prevsquare = []
                    turns = []
                    return
                
                row = 7 - (x[1][2]/self.squaresize)
                column = x[1][1]/self.squaresize

                row1 = 7 - (x[0][2]/self.squaresize)
                column1 = x[0][1]/self.squaresize

                if column1 == column or row1 == row or row>row1 or (row1-row)>2:
                    prevsquare = []
                    turns = []
                    return

                elif (column == column1 - 2) or (row == row1 - 2) or (column == column1 + 2):
                    if column == column1 - 2:
                        prevx1 = column1*self.squaresize
                        prevy1 = (7-row1)*self.squaresize
                        prevx2 = prevx1 + self.squaresize
                        prevy2 = prevy1 + self.squaresize
                        
                        capturex1 = (column1-1)*self.squaresize
                        capturey1 = (7-(row1-1))*self.squaresize
                        capturex2 = capturex1 + self.squaresize
                        capturey2 = capturey1 + self.squaresize 

                        x1 = column*self.squaresize
                        y1 = (7-row)*self.squaresize
                        x2 = x1 + self.squaresize
                        y2 = y1 + self.squaresize
                        
                        self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                        self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = "darkbrown")
                        self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                        prevsquare = []
                        return
                    if column == column1 + 2:
                        prevx1 = column1*self.squaresize
                        prevy1 = (7-row1)*self.squaresize
                        prevx2 = prevx1 + self.squaresize
                        prevy2 = prevy1 + self.squaresize
                        
                        capturex1 = (column1+1)*self.squaresize
                        capturey1 = (7-(row1-1))*self.squaresize
                        capturex2 = capturex1 + self.squaresize
                        capturey2 = capturey1 + self.squaresize 

                        x1 = column*self.squaresize
                        y1 = (7-row)*self.squaresize
                        x2 = x1 + self.squaresize
                        y2 = y1 + self.squaresize
                        
                        self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                        self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = "darkbrown")
                        self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                        prevsquare = []
                        return
                        
                
                else:
                    x1 = column1*self.squaresize
                    y1 = (7-row1)*self.squaresize
                    x2 = x1 + self.squaresize
                    y2 = y1 + self.squaresize

                    if "darkbrown" or "lightbrown" in self.canvas.find_enclosed(x1, y1, x2, y2)[0]:
                        prevsquare = []
                        turns = []
                        return

                    else:
                        x1delete = column1*self.squaresize
                        y1delete = (7-row1)*self.squaresize
                        x2delete = x1delete + self.squaresize
                        y2delete = y1delete + self.squaresize
                        self.canvas.create_rectangle(x1delete,y1delete,x2delete,y2delete,fill="#8B4513",outline = "black",tags = "#8B4513")
                        prevsquare = []
                        return

                
            elif x[0][0] == "lightbrown":
                
                row = 7 - (x[1][2]/self.squaresize)
                column = x[1][1]/self.squaresize

                row1 = 7 - (x[0][2]/self.squaresize)
                column1 = x[0][1]/self.squaresize

                if x[1][0] == "#D2B48C":
                        prevsquare = []
                        turns = []
                        return
                
                if column1 == column or row == row1 or row<row1 or (row-row1>2):
                    prevsquare = []
                    turns = []
                    return
                
                elif (column == column1 - 2) or (row == row1 + 2) or (column == column1 + 2):
                    if column == column1 - 2:
                        prevx1 = column1*self.squaresize
                        prevy1 = (7-row1)*self.squaresize
                        prevx2 = prevx1 + self.squaresize
                        prevy2 = prevy1 + self.squaresize
                        
                        capturex1 = (column1-1)*self.squaresize
                        capturey1 = (7-(row1+1))*self.squaresize
                        capturex2 = capturex1 + self.squaresize
                        capturey2 = capturey1 + self.squaresize

                        x1 = column*self.squaresize
                        y1 = (7-row)*self.squaresize
                        x2 = x1 + self.squaresize
                        y2 = y1 + self.squaresize
                        
                        self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                        self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = "lightbrown")
                        self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                        prevsquare = []
                        return
                    
                    if column == column1 + 2:
                        prevx1 = column1*self.squaresize
                        prevy1 = (7-row1)*self.squaresize
                        prevx2 = prevx1 + self.squaresize
                        prevy2 = prevy1 + self.squaresize
                        
                        capturex1 = (column1+1)*self.squaresize
                        capturey1 = (7-(row1+1))*self.squaresize
                        capturex2 = capturex1 + self.squaresize
                        capturey2 = capturey1 + self.squaresize

                        x1 = column*self.squaresize
                        y1 = (7-row)*self.squaresize
                        x2 = x1 + self.squaresize
                        y2 = y1 + self.squaresize
                        
                        self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                        self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = "lightbrown")
                        self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                        prevsquare = []
                        return

                else:
                    x1 = column*self.squaresize
                    y1 = (7-row)*self.squaresize
                    x2 = x1 + self.squaresize
                    y2 = y1 + self.squaresize
                    self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = "lightbrown")

                    x1delete = column1*self.squaresize
                    y1delete = (7-row1)*self.squaresize
                    x2delete = x1delete + self.squaresize
                    y2delete = y1delete + self.squaresize
                    self.canvas.create_rectangle(x1delete,y1delete,x2delete,y2delete,fill="#8B4513",outline = "black",tags = "#8B4513")
                    prevsquare = []
                    return
                
        if len(turns)<4:
            if x[0][0] == "darkbrown":
                    
                    row = 7 - (x[1][2]/self.squaresize)
                    column = x[1][1]/self.squaresize

                    row1 = 7 - (x[0][2]/self.squaresize)
                    column1 = x[0][1]/self.squaresize

                    if x[1][0] == "#D2B48C":
                        prevsquare = []
                        turns = []
                        return

                    if column1 == column or row1 == row or row>row1 or (row1-row)>2:
                        prevsquare = []
                        turns = []
                        return
                    else:
                        x1 = column*self.squaresize
                        y1 = (7-row)*self.squaresize
                        x2 = x1 + self.squaresize
                        y2 = y1 + self.squaresize
                        self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = "darkbrown")

                        x1delete = column1*self.squaresize
                        y1delete = (7-row1)*self.squaresize
                        x2delete = x1delete + self.squaresize
                        y2delete = y1delete + self.squaresize
                        self.canvas.create_rectangle(x1delete,y1delete,x2delete,y2delete,fill="#8B4513",outline = "black",tags = "#8B4513")
                        prevsquare = []
                        return
            elif x[0][0] == "lightbrown":
                    
                    row = 7 - (x[1][2]/self.squaresize)
                    column = x[1][1]/self.squaresize

                    row1 = 7 - (x[0][2]/self.squaresize)
                    column1 = x[0][1]/self.squaresize

                    if x[1][0] == "#D2B48C":
                        prevsquare = []
                        turns = []
                        return
                    
                    if column1 == column or row == row1 or row<row1 or (row-row1>2):
                        prevsquare = []
                        turns = []
                        return
                    

                    else:
                        x1 = column*self.squaresize
                        y1 = (7-row)*self.squaresize
                        x2 = x1 + self.squaresize
                        y2 = y1 + self.squaresize
                        self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = "lightbrown")

                        x1delete = column1*self.squaresize
                        y1delete = (7-row1)*self.squaresize
                        x2delete = x1delete + self.squaresize
                        y2delete = y1delete + self.squaresize
                        self.canvas.create_rectangle(x1delete,y1delete,x2delete,y2delete,fill="#8B4513",outline = "black",tags = "#8B4513")
                        prevsquare = []
                        return
         
    def drawCheckers(self):

        # DRAWING THE DARK BROWN CHECKERS #
    
        k = 0
        
        '''k specifies where to start the drawing of the first checker in each row. For example,
           the fist checker on the first row was drawn on the 1st square, the first checker on the second row
           will be drawn on the second row'''
        
        #iterating through entire through each row
        for i in range (self.rows,4,-1):

            #iterating through each coloumn of each row
            for j in range (k,self.columns,2): #iterating through alternating columns

                #finding the x and y coordinates of the top left (x1,y1) and botton right (x2,y2) of the square
                x1 = j*self.squaresize
                y1 = (7-i)*self.squaresize
                x2 = x1 + self.squaresize
                y2 = y1 + self.squaresize

                '''checkers are drawn using the x and y coordinates of the top left and bottom right corners of the square in
                   in which they will drawn in'''
                #drawing the checkers
                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = "darkbrown")
                self.canvas.tag_bind("darkbrown",'<ButtonPress-1>', self.CheckerButtonPress)
                self.canvas.tag_bind("darkbrown",'<ButtonRelease-1>', self.CheckerButtonRelease)
                
                
            #alternating the value of k for each row iteration
            if k == 0:
                k=1
            else:
                k=0

        # DRAWING THE LIGHT BROWN CHECKERS #

        k = 0
        #iterating through entire through each row
        for i in range (3):
    
            #iterating through each coloumn of each row               
            for j in range (k,self.columns,2):

                #finding the x and y coordinates of the top left (x1,y1) and botton right (x2,y2) of the square
                x1 = j*self.squaresize
                y1 = (7-i)*self.squaresize
                x2 = x1 + self.squaresize
                y2 = y1 + self.squaresize

                #drawing the square
                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = "lightbrown")
                self.canvas.tag_bind("lightbrown",'<ButtonPress-1>', self.CheckerButtonPress)
                self.canvas.tag_bind("lightbrown",'<ButtonRelease-1>', self.CheckerButtonRelease)
                

            if k == 0:
                k=1
            else:
                k=0




def main():
    global Interface
    global prevsquare
    global turns
    prevsquare = []
    turns = []
    wnd = Tk()
    wnd.title("Checkers!")
    gui = Interface(wnd)
    wnd.mainloop()
if __name__=="__main__":
    main()


        
        
