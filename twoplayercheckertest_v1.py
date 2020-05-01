#Checkers

from tkinter import *

from PIL import ImageTk

import tkinter.messagebox as tkMessageBox 

# import tkMessageBox as tm
class TwoPlayer(): #creating a class that will create the main Checkers Interface
    
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
                
            #alternating the value of k for each row iteration
            if k == 0:
                k=1
            else:
                k=0

    def CheckforWin(self): #functins checks for number of dark ad light brown checkers left
        countdb = 0
        countlb = 0
        x = 105
        for j in range(8):
            for i in range(4):
                item = self.canvas.find_closest(x+(140*i),34+(70*j))[0]
                tag = self.canvas.gettags(item)[0]
                if "darkbrown" in tag:
                    countdb = countdb + 1
                if "lightbrown" in tag:
                    countlb = countlb + 1
                
            if x == 105:
                x = 34
            else:
                x = 105

        if countdb == 1:
            tkMessageBox.showinfo("Winner","Lightbrown Won!")
        if countlb == 1 :
            tkMessageBox.showinfo("Winner","Darkbrown Won!")

    
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
        # print prevsquare

        
        if len(turns)>=4:
            #checking for double turns, if last turn was played by lightbrown, next turn has to be darkbrown's
            if turns[len(turns)-2] == turns[len(turns)-4]:
                if turns[len(turns)-2] == "darkbrown":
                    tkMessageBox.showwarning("Incorrect Move","Its Lightbrown's Turn")
                    prevsquare = []
                    turns = []
                    return
                if turns[len(turns)-2] == "lightbrown":
                    tkMessageBox.showwarning("Incorrect Move","Its Darkbrowns's Turn")
                    prevsquare = []
                    turns = []
                    return
                
            elif x[0][0] == "darkbrown": #checking if the piece that was moved is darkbrown

                if x[1][0] == "#D2B48C": #checking if the square that the checker was moved to was a dark square or not
                    prevsquare = []
                    turns = []
                    return

                #calculating the row and column of the square where the checker wants to move
                row = 7 - (x[1][2]/self.squaresize)
                column = x[1][1]/self.squaresize

                #calculating the row and column of the square where the checker initially was   
                row1 = 7 - (x[0][2]/self.squaresize)
                column1 = x[0][1]/self.squaresize

                #checking for invalid moves
                if column1 == column or row1 == row or row>row1 or (row1-row)>2:
                    prevsquare = []
                    turns = []
                    return

                #if the checker wants to get a capture
                elif (column == column1 - 2) or (row == row1 - 2) or (column == column1 + 2):
                    
                    if column == column1 - 2: #capturing on the left side of the checker
                        
                        #checking if the place post move square has a checker in it or not 
                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]):
                            prevsquare = []
                            turns = []
                            return
                        else: #if not proceed with capture, delete the checker from the current square, delete the captured checkered, re draw the current checker on post square
                            #calculating coords of current square
                            prevx1 = column1*self.squaresize
                            prevy1 = (7-row1)*self.squaresize
                            prevx2 = prevx1 + self.squaresize
                            prevy2 = prevy1 + self.squaresize

                            #calculating coords of capturing square
                            capturex1 = (column1-1)*self.squaresize
                            capturey1 = (7-(row1-1))*self.squaresize
                            capturex2 = capturex1 + self.squaresize
                            capturey2 = capturey1 + self.squaresize 

                            #calculating coords of post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize

                            #draws the squares and checker on the canvas
                            self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            if row == 0:
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = "darkbrownking")
                                self.canvas.tag_bind("darkbrownking",'<ButtonPress-1>', self.CheckerButtonPress)
                                self.canvas.tag_bind("darkbrownking",'<ButtonRelease-1>', self.KingCheckerButtonRelease)
                            else:
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = "darkbrown")
                            
                            self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.CheckforWin()
                            prevsquare = []
                            return
                        
                    if column == column1 + 2: #capturing on the right side of the checker
                        
                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]): #checking if the place post move square has a checker in it or not 
                            prevsquare = []
                            turns=[]
                            return
                        else:
                            #calculating coords of current square
                            prevx1 = column1*self.squaresize
                            prevy1 = (7-row1)*self.squaresize
                            prevx2 = prevx1 + self.squaresize
                            prevy2 = prevy1 + self.squaresize

                            #calculating coords of capturing square
                            capturex1 = (column1+1)*self.squaresize
                            capturey1 = (7-(row1-1))*self.squaresize
                            capturex2 = capturex1 + self.squaresize
                            capturey2 = capturey1 + self.squaresize 

                            #calculatin coords of post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize
                            
                            #draws the squares and checker on the canvas
                            self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            if row == 0:
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = "darkbrownking")
                                self.canvas.tag_bind("darkbrownking",'<ButtonPress-1>', self.CheckerButtonPress)
                                self.canvas.tag_bind("darkbrownking",'<ButtonRelease-1>', self.KingCheckerButtonRelease)
                            else:
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = "darkbrown")
                            
                            self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.CheckforWin()
                            prevsquare = []
                            return
                        
                
                else:
                    if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]): #checking is post square has a checker in it or not
                            prevsquare = []
                            turns = []
                            return
 
                    else:
                        #calculating the post square coordinates
                        x1 = column*self.squaresize
                        y1 = (7-row)*self.squaresize
                        x2 = x1 + self.squaresize
                        y2 = y1 + self.squaresize
                        #redrawing checker at the postion
                        
                        if row == 0: #if the darkbrown checker reaches the other side of the board, it becomes king
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = "darkbrownking")
                            self.canvas.tag_bind("darkbrownking",'<ButtonPress-1>', self.CheckerButtonPress)
                            self.canvas.tag_bind("darkbrownking",'<ButtonRelease-1>', self.KingCheckerButtonRelease)
                        else:
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = "darkbrown")

                        #calculating current square coordinates
                        x1delete = column1*self.squaresize
                        y1delete = (7-row1)*self.squaresize
                        x2delete = x1delete + self.squaresize
                        y2delete = y1delete + self.squaresize
                        #drawing an empty square at the current square
                        self.canvas.create_rectangle(x1delete,y1delete,x2delete,y2delete,fill="#8B4513",outline = "black",tags = "#8B4513")
                        self.CheckforWin()
                        prevsquare = []
                        return

                
            elif x[0][0] == "lightbrown": #checking if the checker that was moved is lightbrown

                #calculating row and column of the square where checker wants to move 
                row = 7 - (x[1][2]/self.squaresize)
                column = x[1][1]/self.squaresize

                #calculating row and column of the square where the checker initially was 
                row1 = 7 - (x[0][2]/self.squaresize)
                column1 = x[0][1]/self.squaresize

                #checking if the checker has moved to a dark square or not
                if x[1][0] == "#D2B48C":
                        prevsquare = []
                        turns = []
                        return
                #checking for all invalid moves
                if column1 == column or row == row1 or row<row1 or (row-row1>2):
                    prevsquare = []
                    turns = []
                    return

                #checking for capture move
                elif (column == column1 - 2) or (row == row1 + 2) or (column == column1 + 2):
                    if column == column1 - 2:

                        #checking if the post move square has a checker in it or not 
                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]):
                            prevsquare = []
                            turns = []
                            return
                        else:
                            #calculating the coordinates of the current square
                            prevx1 = column1*self.squaresize
                            prevy1 = (7-row1)*self.squaresize
                            prevx2 = prevx1 + self.squaresize
                            prevy2 = prevy1 + self.squaresize

                            #calculating the coordinates of the capturing square 
                            capturex1 = (column1-1)*self.squaresize
                            capturey1 = (7-(row1+1))*self.squaresize
                            capturex2 = capturex1 + self.squaresize
                            capturey2 = capturey1 + self.squaresize

                            #calculating the coordinates of the post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize

                            #draws the squares and checker on the canvas
                            self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            
                            if row == 7: #if the lightbrown checker reaches the other side of the board, it becomes king
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = "4",tags = "lightbrownking")
                                self.canvas.tag_bind("lightbrownking",'<ButtonPress-1>', self.CheckerButtonPress)
                                self.canvas.tag_bind("lightbrownking",'<ButtonRelease-1>', self.KingCheckerButtonRelease)
                            else:
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = "lightbrown")
                                
                            self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.CheckforWin()
                            prevsquare = []
                            return
                    
                    if column == column1 + 2: #checking if the capturing takes place in the right of the current postion

                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]): #checking the post square is already occupied or not
                            prevsquare = []
                            turns = []
                            return
                        else:
                            #calculating the coords of the current square
                            prevx1 = column1*self.squaresize
                            prevy1 = (7-row1)*self.squaresize
                            prevx2 = prevx1 + self.squaresize
                            prevy2 = prevy1 + self.squaresize

                            #calcualting the coords of the capturing square
                            capturex1 = (column1+1)*self.squaresize
                            capturey1 = (7-(row1+1))*self.squaresize
                            capturex2 = capturex1 + self.squaresize
                            capturey2 = capturey1 + self.squaresize

                            #calculating the coords of the post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize

                            #drawing the squares and the checker
                            self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            
                            if row == 7: #if the lightbrown checker reaches the other side of the board, it becomes king (checker that moves up and down)
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = "4",tags = "lightbrownking")
                                self.canvas.tag_bind("lightbrownking",'<ButtonPress-1>', self.CheckerButtonPress)
                                self.canvas.tag_bind("lightbrownking",'<ButtonRelease-1>', self.KingCheckerButtonRelease)
                            else:
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = "lightbrown")
                                
                            self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.CheckforWin()
                            prevsquare = []
                            return

                else:
                    #checking if the post square is occupied or mnot
                    if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]): #checking the post square is already occupied or not
                            prevsquare = []
                            turns = []
                            return
                    else:
                        #calculating coordinates of post square
                        x1 = column*self.squaresize
                        y1 = (7-row)*self.squaresize
                        x2 = x1 + self.squaresize
                        y2 = y1 + self.squaresize
                        
                        if row == 7: #if the lightbrown checker reaches the other side of the board, it becomes king
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = "4",tags = "lightbrownking")
                            self.canvas.tag_bind("lightbrownking",'<ButtonPress-1>', self.CheckerButtonPress)
                            self.canvas.tag_bind("lightbrownking",'<ButtonRelease-1>', self.KingCheckerButtonRelease)
                        else:
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = "lightbrown")

                        #calculating the coords of the current square
                        x1delete = column1*self.squaresize
                        y1delete = (7-row1)*self.squaresize
                        x2delete = x1delete + self.squaresize
                        y2delete = y1delete + self.squaresize
                        self.canvas.create_rectangle(x1delete,y1delete,x2delete,y2delete,fill="#8B4513",outline = "black",tags = "#8B4513")
                        self.CheckforWin()
                        prevsquare = []
                        return
                
        if len(turns)<4: #checking if 3 or less moves have been made
            if "darkbrown" in x[0][0]:
                    #calculating row and column of the current and post square
                    row = 7 - (x[1][2]/self.squaresize)
                    column = x[1][1]/self.squaresize

                    row1 = 7 - (x[0][2]/self.squaresize)
                    column1 = x[0][1]/self.squaresize

                    #checking is move was made to a dark square
                    if x[1][0] == "#D2B48C":
                        prevsquare = []
                        turns = []
                        return

                    #checking for invalid moves
                    if column1 == column or row1 == row or row>row1 or (row1-row)>2:
                        prevsquare = []
                        turns = []
                        return
                    #checking for capture
                    elif (column == column1 - 2) or (row == row1 - 2) or (column == column1 + 2):
                        if column == column1 - 2: #capturing on the left side of the checker
                            
                            #checking if the place post move square has a checker in it or not 
                            if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]):
                                prevsquare = []
                                turns = []
                                return
                            else: #if not proceed with capture, delete the checker from the current square, delete the captured checkered, re draw the current checker on post square
                                #calculating coords of current square
                                prevx1 = column1*self.squaresize
                                prevy1 = (7-row1)*self.squaresize
                                prevx2 = prevx1 + self.squaresize
                                prevy2 = prevy1 + self.squaresize

                                #calculating coords of capturing square
                                capturex1 = (column1-1)*self.squaresize
                                capturey1 = (7-(row1-1))*self.squaresize
                                capturex2 = capturex1 + self.squaresize
                                capturey2 = capturey1 + self.squaresize 

                                #calculating coords of post square
                                x1 = column*self.squaresize
                                y1 = (7-row)*self.squaresize
                                x2 = x1 + self.squaresize
                                y2 = y1 + self.squaresize

                                #draws the squares and checker on the canvas
                                self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                                if row == 0:
                                    self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = "darkbrownking")
                                    self.canvas.tag_bind("darkbrownking",'<ButtonPress-1>', self.CheckerButtonPress)
                                    self.canvas.tag_bind("darkbrownking",'<ButtonRelease-1>', self.KingCheckerButtonRelease)
                                else:
                                    self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = "darkbrown")
                                
                                self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                                self.CheckforWin()
                                prevsquare = []
                                return
                            
                        if column == column1 + 2: #capturing on the right side of the checker
                            
                            if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]): #checking if the place post move square has a checker in it or not 
                                prevsquare = []
                                turns=[]
                                return
                            else:
                                #calculating coords of current square
                                prevx1 = column1*self.squaresize
                                prevy1 = (7-row1)*self.squaresize
                                prevx2 = prevx1 + self.squaresize
                                prevy2 = prevy1 + self.squaresize

                                #calculating coords of capturing square
                                capturex1 = (column1+1)*self.squaresize
                                capturey1 = (7-(row1-1))*self.squaresize
                                capturex2 = capturex1 + self.squaresize
                                capturey2 = capturey1 + self.squaresize 

                                #calculatin coords of post square
                                x1 = column*self.squaresize
                                y1 = (7-row)*self.squaresize
                                x2 = x1 + self.squaresize
                                y2 = y1 + self.squaresize
                                
                                #draws the squares and checker on the canvas
                                self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                                if row == 0:
                                    self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = "darkbrownking")
                                    self.canvas.tag_bind("darkbrownking",'<ButtonPress-1>', self.CheckerButtonPress)
                                    self.canvas.tag_bind("darkbrownking",'<ButtonRelease-1>', self.KingCheckerButtonRelease)
                                else:
                                    self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = "darkbrown")
                                
                                self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                                self.CheckforWin()
                                prevsquare = []
                                return
                    else:
                        #calculating coords of the post square
                        x1 = column*self.squaresize
                        y1 = (7-row)*self.squaresize
                        x2 = x1 + self.squaresize
                        y2 = y1 + self.squaresize

                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]): #checking the post square is already occupied or not
                            prevsquare = []
                            turns = []
                            return
                        else:
                            #drawing the checker on the post move quare
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = "darkbrown")
                            x1delete = column1*self.squaresize
                            y1delete = (7-row1)*self.squaresize
                            x2delete = x1delete + self.squaresize
                            y2delete = y1delete + self.squaresize
                            self.canvas.create_rectangle(x1delete,y1delete,x2delete,y2delete,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.CheckforWin()
                            prevsquare = []
                            return
                        
            elif x[0][0] == "lightbrown": #checking which checker was moved

                    #calculating thw row and column of the current and post square
                    row = 7 - (x[1][2]/self.squaresize)
                    column = x[1][1]/self.squaresize

                    row1 = 7 - (x[0][2]/self.squaresize)
                    column1 = x[0][1]/self.squaresize

                    #checking the post square is dark or not
                    if x[1][0] == "#D2B48C":
                        prevsquare = []
                        turns = []
                        return
                    #checking for invalid moves
                    if column1 == column or row == row1 or row<row1 or (row-row1>2):
                        prevsquare = []
                        turns = []
                        return
                    #checking for capture
                    elif (column == column1 - 2) or (row == row1 + 2) or (column == column1 + 2):
                        if column == column1 - 2:

                            #checking if the post move square has a checker in it or not 
                            if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]):
                                prevsquare = []
                                turns = []
                                return
                            else:
                                #calculating the coordinates of the current square
                                prevx1 = column1*self.squaresize
                                prevy1 = (7-row1)*self.squaresize
                                prevx2 = prevx1 + self.squaresize
                                prevy2 = prevy1 + self.squaresize

                                #calculating the coordinates of the capturing square 
                                capturex1 = (column1-1)*self.squaresize
                                capturey1 = (7-(row1+1))*self.squaresize
                                capturex2 = capturex1 + self.squaresize
                                capturey2 = capturey1 + self.squaresize

                                #calculating the coordinates of the post square
                                x1 = column*self.squaresize
                                y1 = (7-row)*self.squaresize
                                x2 = x1 + self.squaresize
                                y2 = y1 + self.squaresize

                                #draws the squares and checker on the canvas
                                self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                                
                                if row == 7: #if the lightbrown checker reaches the other side of the board, it becomes king
                                    self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = "4",tags = "lightbrownking")
                                    self.canvas.tag_bind("lightbrownking",'<ButtonPress-1>', self.CheckerButtonPress)
                                    self.canvas.tag_bind("lightbrownking",'<ButtonRelease-1>', self.KingCheckerButtonRelease)
                                else:
                                    self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = "lightbrown")
                                    
                                self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                                self.CheckforWin()
                                prevsquare = []
                                return
                        
                        if column == column1 + 2: #checking if the capturing takes place in the right of the current postion

                            if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]): #checking the post square is already occupied or not
                                prevsquare = []
                                turns = []
                                return
                            else:
                                #calculating the coords of the current square
                                prevx1 = column1*self.squaresize
                                prevy1 = (7-row1)*self.squaresize
                                prevx2 = prevx1 + self.squaresize
                                prevy2 = prevy1 + self.squaresize

                                #calcualting the coords of the capturing square
                                capturex1 = (column1+1)*self.squaresize
                                capturey1 = (7-(row1+1))*self.squaresize
                                capturex2 = capturex1 + self.squaresize
                                capturey2 = capturey1 + self.squaresize

                                #calculating the coords of the post square
                                x1 = column*self.squaresize
                                y1 = (7-row)*self.squaresize
                                x2 = x1 + self.squaresize
                                y2 = y1 + self.squaresize

                                #drawing the squares and the checker
                                self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                                
                                if row == 7: #if the lightbrown checker reaches the other side of the board, it becomes king (checker that moves up and down)
                                    self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = "4",tags = "lightbrownking")
                                    self.canvas.tag_bind("lightbrownking",'<ButtonPress-1>', self.CheckerButtonPress)
                                    self.canvas.tag_bind("lightbrownking",'<ButtonRelease-1>', self.KingCheckerButtonRelease)
                                else:
                                    self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = "lightbrown")
                                    
                                self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                                self.CheckforWin()
                                prevsquare = []
                                return
                    
                    else:
                        #calculating coords of the post square
                        x1 = column*self.squaresize
                        y1 = (7-row)*self.squaresize
                        x2 = x1 + self.squaresize
                        y2 = y1 + self.squaresize

                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]): #checking the post square is already occupied or not
                            prevsquare = []
                            turns = []
                            return
                        else:
                            #drawing the checker on the post square and deleting it from the current square
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = "lightbrown")
                            x1delete = column1*self.squaresize
                            y1delete = (7-row1)*self.squaresize
                            x2delete = x1delete + self.squaresize
                            y2delete = y1delete + self.squaresize
                            self.canvas.create_rectangle(x1delete,y1delete,x2delete,y2delete,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.CheckforWin()
                            prevsquare = []
                            return
                        
    def KingCheckerButtonRelease(self,event):
        global prevsquare
        global turns
        self.CheckerButtonPress(event)
        x = prevsquare
        #print x

        if turns[len(turns)-2] == turns[len(turns)-4]:
            if turns[len(turns)-2] == "darkbrownking":
                tkMessageBox.showwarning("Incorrect Move","Its Lightbrown's Turn")
                prevsquare = []
                turns = []
                return
            if turns[len(turns)-2] == "lightbrownking":
                tkMessageBox.showwarning("Incorrect Move","Its Darkbrown's Turn")
                prevsquare = []
                turns = []
                return
            
        elif x[0][0] == "darkbrownking":
                
                if x[1][0] == "#D2B48C": #checking if the square that the checker was moved to was a dark square or not
                    prevsquare = []
                    turns = []
                    return
                
                #calculating the row and column of the square where the checker wants to move
                row = 7 - (x[1][2]/self.squaresize)
                column = x[1][1]/self.squaresize

                #calculating the row and column of the square where the checker initially was   
                row1 = 7 - (x[0][2]/self.squaresize)
                column1 = x[0][1]/self.squaresize
                
                if column1 == column or row1 == row:
                    prevsquare = []
                    turns = []
                    return
                
                elif ((column == column1 - 2) or (column == column1 + 2)) and (row == row1 + 2):
                    
                    if (column == column1 - 2):#capturing on left side of current pos
                            
                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]):
                            prevsquare = []
                            turns = []
                            return
                        else: #if not proceed with capture, delete the checker from the current square, delete the captured checkered, re draw the current checker on post square

                            #calculating coords of current square
                            prevx1 = column1*self.squaresize
                            prevy1 = (7-row1)*self.squaresize
                            prevx2 = prevx1 + self.squaresize
                            prevy2 = prevy1 + self.squaresize

                            #calculating coords of capturing square
                            capturex1 = (column1-1)*self.squaresize
                            capturey1 = (7-(row1+1))*self.squaresize
                            capturex2 = capturex1 + self.squaresize
                            capturey2 = capturey1 + self.squaresize 

                            #calculating coords of post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize

                            #draws the squares and checker on the canvas
                            self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = "darkbrownking")
                            self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            prevsquare = []
                            return
                            
                    if (column == column1+2):
                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]):
                            prevsquare = []
                            turns = []
                            return
                        else: #if not proceed with capture, delete the checker from the current square, delete the captured checkered, re draw the current checker on post square

                            #calculating coords of current square
                            prevx1 = column1*self.squaresize
                            prevy1 = (7-row1)*self.squaresize
                            prevx2 = prevx1 + self.squaresize
                            prevy2 = prevy1 + self.squaresize

                            #calculating coords of capturing square
                            capturex1 = (column1+1)*self.squaresize
                            capturey1 = (7-(row1+1))*self.squaresize
                            capturex2 = capturex1 + self.squaresize
                            capturey2 = capturey1 + self.squaresize 

                            #calculating coords of post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize

                            #draws the squares and checker on the canvas
                            self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = "darkbrownking")
                            self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            prevsquare = []
                            return

                elif ((column == column1 - 2) or (column == column1 + 2)) and (row == row1 - 2):
                    
                    if (column == column1 - 2):#capturing on left side of current pos
                            
                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]):
                            prevsquare = []
                            turns = []
                            return
                        else: #if not proceed with capture, delete the checker from the current square, delete the captured checkered, re draw the current checker on post square

                            #calculating coords of current square
                            prevx1 = column1*self.squaresize
                            prevy1 = (7-row1)*self.squaresize
                            prevx2 = prevx1 + self.squaresize
                            prevy2 = prevy1 + self.squaresize

                            #calculating coords of capturing square
                            capturex1 = (column1-1)*self.squaresize
                            capturey1 = (7-(row1-1))*self.squaresize
                            capturex2 = capturex1 + self.squaresize
                            capturey2 = capturey1 + self.squaresize 

                            #calculating coords of post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize

                            #draws the squares and checker on the canvas
                            self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = "darkbrownking")
                            self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            prevsquare = []
                            return
                            
                    if (column == column1+2):
                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]):
                            prevsquare = []
                            turns = []
                            return
                        else: #if not proceed with capture, delete the checker from the current square, delete the captured checkered, re draw the current checker on post square

                            #calculating coords of current square
                            prevx1 = column1*self.squaresize
                            prevy1 = (7-row1)*self.squaresize
                            prevx2 = prevx1 + self.squaresize
                            prevy2 = prevy1 + self.squaresize

                            #calculating coords of capturing square
                            capturex1 = (column1+1)*self.squaresize
                            capturey1 = (7-(row1-1))*self.squaresize
                            capturex2 = capturex1 + self.squaresize
                            capturey2 = capturey1 + self.squaresize 

                            #calculating coords of post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize

                            #draws the squares and checker on the canvas
                            self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = "darkbrownking")
                            self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            prevsquare = []
                            return


                    
                else:
                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]): #checking is post square has a checker in it or not
                                prevsquare = []
                                turns = []
                                return

                        else:
                            #calculating the post square coordinates
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize
                            
                            #redrawing checker at the postion
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = "darkbrownking")

                            #calculating current square coordinates
                            x1delete = column1*self.squaresize
                            y1delete = (7-row1)*self.squaresize
                            x2delete = x1delete + self.squaresize
                            y2delete = y1delete + self.squaresize
                            
                            #drawing an empty square at the current square
                            self.canvas.create_rectangle(x1delete,y1delete,x2delete,y2delete,fill="#8B4513",outline = "black",tags = "#8B4513")
                            prevsquare = []
                            return
            
        elif x[0][0] == "lightbrownking":
                
                if x[1][0] == "#D2B48C": #checking if the square that the checker was moved to was a dark square or not
                    prevsquare = []
                    turns = []
                    return
                
                #calculating the row and column of the square where the checker wants to move
                row = 7 - (x[1][2]/self.squaresize)
                column = x[1][1]/self.squaresize

                #calculating the row and column of the square where the checker initially was   
                row1 = 7 - (x[0][2]/self.squaresize)
                column1 = x[0][1]/self.squaresize
                
                if column1 == column or row1 == row:
                    prevsquare = []
                    turns = []
                    return
                
                elif ((column == column1 - 2) or (column == column1 + 2)) and (row == row1 + 2):
                    
                    if (column == column1 - 2):#capturing on left side of current pos
                            
                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]):
                            prevsquare = []
                            turns = []
                            return
                        else: #if not proceed with capture, delete the checker from the current square, delete the captured checkered, re draw the current checker on post square

                            #calculating coords of current square
                            prevx1 = column1*self.squaresize
                            prevy1 = (7-row1)*self.squaresize
                            prevx2 = prevx1 + self.squaresize
                            prevy2 = prevy1 + self.squaresize

                            #calculating coords of capturing square
                            capturex1 = (column1-1)*self.squaresize
                            capturey1 = (7-(row1+1))*self.squaresize
                            capturex2 = capturex1 + self.squaresize
                            capturey2 = capturey1 + self.squaresize 

                            #calculating coords of post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize

                            #draws the squares and checker on the canvas
                            self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = "4",tags = "lightbrownking")
                            self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            prevsquare = []
                            return
                            
                    if (column == column1+2):
                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]):
                            prevsquare = []
                            turns = []
                            return
                        else: #if not proceed with capture, delete the checker from the current square, delete the captured checkered, re draw the current checker on post square

                            #calculating coords of current square
                            prevx1 = column1*self.squaresize
                            prevy1 = (7-row1)*self.squaresize
                            prevx2 = prevx1 + self.squaresize
                            prevy2 = prevy1 + self.squaresize

                            #calculating coords of capturing square
                            capturex1 = (column1+1)*self.squaresize
                            capturey1 = (7-(row1+1))*self.squaresize
                            capturex2 = capturex1 + self.squaresize
                            capturey2 = capturey1 + self.squaresize 

                            #calculating coords of post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize

                            #draws the squares and checker on the canvas
                            self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = "4",tags = "lightbrownking")
                            self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            prevsquare = []
                            return

                elif ((column == column1 - 2) or (column == column1 + 2)) and (row == row1 - 2):
                    
                    if (column == column1 - 2):#capturing on left side of current pos
                            
                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]):
                            prevsquare = []
                            turns = []
                            return
                        else: #if not proceed with capture, delete the checker from the current square, delete the captured checkered, re draw the current checker on post square

                            #calculating coords of current square
                            prevx1 = column1*self.squaresize
                            prevy1 = (7-row1)*self.squaresize
                            prevx2 = prevx1 + self.squaresize
                            prevy2 = prevy1 + self.squaresize

                            #calculating coords of capturing square
                            capturex1 = (column1-1)*self.squaresize
                            capturey1 = (7-(row1-1))*self.squaresize
                            capturex2 = capturex1 + self.squaresize
                            capturey2 = capturey1 + self.squaresize 

                            #calculating coords of post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize

                            #draws the squares and checker on the canvas
                            self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = "4",tags = "lightbrownking")
                            self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            prevsquare = []
                            return
                            
                    if (column == column1+2):
                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]):
                            prevsquare = []
                            turns = []
                            return
                        else: #if not proceed with capture, delete the checker from the current square, delete the captured checkered, re draw the current checker on post square

                            #calculating coords of current square
                            prevx1 = column1*self.squaresize
                            prevy1 = (7-row1)*self.squaresize
                            prevx2 = prevx1 + self.squaresize
                            prevy2 = prevy1 + self.squaresize

                            #calculating coords of capturing square
                            capturex1 = (column1+1)*self.squaresize
                            capturey1 = (7-(row1-1))*self.squaresize
                            capturex2 = capturex1 + self.squaresize
                            capturey2 = capturey1 + self.squaresize 

                            #calculating coords of post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize

                            #draws the squares and checker on the canvas
                            self.canvas.create_rectangle(capturex1,capturey1,capturex2,capturey2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = "4",tags = "lightbrownking")
                            self.canvas.create_rectangle(prevx1,prevy1,prevx2,prevy2,fill="#8B4513",outline = "black",tags = "#8B4513")
                            prevsquare = []
                            return


                    
                else:
                        if ("lightbrown" == x[1][0]) or ("darkbrown" == x[1][0]): #checking is post square has a checker in it or not
                                prevsquare = []
                                turns = []
                                return

                        else:
                            #calculating the post square coordinates
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize
                            
                            #redrawing checker at the postion
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = "4",tags = "lightbrownking")

                            #calculating current square coordinates
                            x1delete = column1*self.squaresize
                            y1delete = (7-row1)*self.squaresize
                            x2delete = x1delete + self.squaresize
                            y2delete = y1delete + self.squaresize
                            
                            #drawing an empty square at the current square
                            self.canvas.create_rectangle(x1delete,y1delete,x2delete,y2delete,fill="#8B4513",outline = "black",tags = "#8B4513")
                            prevsquare = []
                            return


def TwoPlayerGame(): #opens up one player game window
    twoplayer = Tk()
    twoplayer.title("Checkers! - Two Player")
    TwoPlayer(twoplayer)

def ExitProgram(): #exits the program by destroying main startup window
    global startup
    result = tkMessageBox.askyesno(title = "Exit?", message = "Would you like to exit?") 
    if result == True:
        startup.destroy()
        
def Instructions(): #creating a top level window that where an image with all the instruction is places
    howtoplay = Toplevel()
    howtoplay.title("Checkers! - How to Play")
    background = "/Users/safiyajankhan/Desktop/Instructions.gif"
    canvas = Canvas(howtoplay,width=600,height = 570)
    canvas.pack()
    background_image = ImageTk.PhotoImage(file=background) #loading image
    canvas.create_image(0,0,anchor = "nw",image=background_image) #placing image on the window
    howtoplay.mainloop()
    
def main():
    global prevsquare
    global turns
    global startup
    prevsquare = []
    turns = []

    #creating the main window
    startup = Tk()
    startup.title("Checkers!")
    
    background = "/Users/safiyajankhan/Desktop/CheckersStartup.gif"
    howtoplay = "/Users/safiyajankhan/Desktop/HowToPlay.gif"
    oneplayer = "/Users/safiyajankhan/Desktop/OnePlayer.gif"
    twoplayer = "/Users/safiyajankhan/Desktop/TwoPlayer.gif"
    exitprogram = "/Users/safiyajankhan/Desktop/Exit.gif"

    #loading images for the buttons      
    howtoplay_photo = ImageTk.PhotoImage(file=howtoplay)
    oneplayer_photo = ImageTk.PhotoImage(file=oneplayer)
    twoplayer_photo = ImageTk.PhotoImage(file=twoplayer)
    exitprogram_photo = ImageTk.PhotoImage(file=exitprogram)

    #adding a background image to the startup window
    background_image = ImageTk.PhotoImage(file=background)
    canvas = Canvas(startup,width=600,height = 600)
    canvas.pack()
    canvas.create_image(0,0,anchor = "nw",image=background_image)

    #adding buttons to the main window 
    button1 = Button(startup,width = 365,height = 60,image = howtoplay_photo, command = Instructions)
    #creating a window for the button within the main window so that image can be used as a button
    button1_window = canvas.create_window(311,162,anchor = "n",window=button1) 
    
    button2 = Button(startup,width = 365,height = 60, image = oneplayer_photo)
    button2_window = canvas.create_window(311,252,anchor = "n",window=button2)
    
    button3 = Button(startup,width = 365,height = 60, image = twoplayer_photo,command = TwoPlayerGame)
    button3_window = canvas.create_window(311,342,anchor = "n",window=button3)

    button4 = Button(startup,width = 365,height = 60, image = exitprogram_photo,command = ExitProgram)
    button4_window = canvas.create_window(311,432,anchor = "n",window=button4)

    startup.mainloop()
    
if __name__=="__main__":
    main()

