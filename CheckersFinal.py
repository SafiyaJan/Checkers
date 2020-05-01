## Safiya Jan - 15112 Fall 2016 - Final Project ##

#libraries used
# from Tkinter import *
# import tkinter as tk
from tkinter import *
from PIL import ImageTk
# import tkMessageBox as tm
import tkinter.messagebox as tm
import re
import random
import math 


''' Functions Used in Two Player Class '''

''' drawCheckersBoard(self) : This function creates the actual gameboard, labeling each square with a tag so that it can be identified. Then calls drawChecker function
                              after gameboard is made

    drawCheckers(self) : This takes in the gameboard and draws the checkers on the board. Each checker is tagged with a label and binded with a button press and button
                         release event

    CheckerButtonPress(self,event) : This function takes in the button press event and finds the item (checker) that was clicked and its position in coordinates. The
                                     function then appends this to a list named prevsquare that saves the checker and its postion on the board. Function also keeps track
                                     of turns, ie 1st move was made by darkbrown, the next by lightbrown and so on

    CheckerButtonRelease(self,event) : This is the main part of the class. This function takes in the button release event and makes the appropriate move. This function
                                      contains all the conditions of possible moves and conditions for illegal moves. Depending on which move is made, function calculates
                                      it legality of the move and acts accordingly (make the move if legel, dont do anything if illegal)

    KingCheckerButtonRelease(self,event) : This function is especially for kings that are made. It has the same functionality of the CheckerButtonRelease function, but
                                          contains conditons specially for the kings since they can make moves in any direction. The function takes in the button release
                                          event and makes the appropriate move according to the moves legality.
                                          
    CheckForWin(self) : This function checks for a winner. The function loops through each square of the gameboard and checks if there are any darkbrown or lightbrown
                       checkers. If there are no lightbrown checkers left, a messagebox opens stating that darkbrown won and vice versa.

'''

''' Functions Used in One Player Class '''

''' drawCheckersBoard(self) : This function creates the actual gameboard, labeling each square with a tag so that it can be identified. Then calls drawChecker
                            function after gameboard is made

    drawCheckers(self) : This takes in the gameboard and draws the checkers on the board. Each checker is tagged with a uniqe label and binded with a button
                         press and button release event

    CheckerButtonPress(self,event) : This function takes in the button press event and finds the item (checker) that was clicked and its position in coordinates. The
                                     function then appends this to a list named prevsquare that saves the checker and its postion on the board. Function also keeps track
                                     of turns, ie 1st move was made by darkbrown, the next by lightbrown and so on

    CheckerButtonRelease(self,event) : This is the main part of the class. This function takes in the button release event and makes the appropriate move. This function
                                      contains all the conditions of possible moves and conditions for illegal moves. Depending on which move is made, function calculates
                                      it legality of the move and acts accordingly (make the move if legel, dont do anything if illegal). This function only looks at the
                                      moves made by darkbrown checker, since the lightbrown checker is the AI.
                                      
    KingCheckerButtonRelease(self,event) : This function is especially for kings that are made. It has the same functionality of the CheckerButtonRelease function, but
                                          contains conditons specially for the kings since they can make moves in any direction. The function takes in the button release
                                          event and makes the appropriate move according to the moves legality. Again this function only looks at the darkbrown kings,
                                          since the AI makes the lightbrown kings

    GetAIMove(self,x,y) : This function takes in the coordinates of the move made by the darkbrown checker. The function then loops through each dark square of the
                          gameboard, looking for lightbrown checkers. The function then saves all the positions of these checkers in a list named location where each
                          element contains the tag of the checker and its position in row,column. The function then calculates the the possible moves and all possible
                          captures that can be done for each checker and saves this info in two lists named possiblemoves and possiblecapture. The possiblemoves contains
                          in element the checker tag and row,column of the move it can make to. The possiblecaptures list contains in each element, the name of the checker
                          that can be moved and the piece it can capture and the row,column of the move it can make to. The function then calls the MakeAIMove()

    MakeAIMove(self,possiblecaptures,possiblemoves) : So this function takes in the two lists created in the last function as inputs. Then checks if there are any possible
                                                      captures, if there are, then the function makes the move. If there are none then make a random move from the
                                                      possiblemoves list. If the king is made, the king is then tagged with a unique name
    
    CheckForWin(self) : This function checks for a winner. The function loops through each square of the gameboard and checks if there are any darkbrown or lightbrown
                       checkers. If there are no lightbrown checkers left, a messagebox opens stating that darkbrown won and vice versa.
    
'''

''' Other Main functions '''

''' OnePlayer() - Creates a new window and calls the One Player Class and creates the game.
    TwoPlayer() - Creates a new window and calls the Two Player Class and creates the game.
    ExitProgram() - This function closes the entire program
    Instructions() - This function creates a window that displays all the instructions
    Main() - This function creates the main window startup of the program. The function also creates the buttons which directs the player to the appropriate game/option.
             The function also loads up the images for the main window using PIL. Also create global variables that are needed for the functions in the classes. '''





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
            tm.showinfo("Winner","Lightbrown Won!")
        if countlb == 1 :
            tm.showinfo("Winner","Darkbrown Won!")

    
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
        # print (prevsquare)

        
        if len(turns)>=4:
            #checking for double turns, if last turn was played by lightbrown, next turn has to be darkbrown's
            if turns[len(turns)-2] == turns[len(turns)-4]:
                if turns[len(turns)-2] == "darkbrown":
                    tm.showwarning("Incorrect Move","Its Lightbrown's Turn")
                    prevsquare = []
                    return
                if turns[len(turns)-2] == "lightbrown":
                    tm.showwarning("Incorrect Move","Its Darkbrowns's Turn")
                    prevsquare = []
                    return
                
            elif x[0][0] == "darkbrown": #checking if the piece that was moved is darkbrown

                if x[1][0] == "#D2B48C": #checking if the square that the checker was moved to was a dark square or not
                    prevsquare = []
                    turns = []
                    return

                #calculating the row and column of the square where the checker wants to move
                row = math.floor(7 - (x[1][2]/self.squaresize))+1
                column = math.floor(x[1][1]/self.squaresize)

                #calculating the row and column of the square where the checker initially was   
                row1 = math.floor(7 - (x[0][2]/self.squaresize))+1
                column1 = math.floor(x[0][1]/self.squaresize)

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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print (tags)

                            #checking if capture square has a darkbrown checker in it or if the square is empty
                            if "darkbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                turns = []
                                prevsquare = []
                                return
                                
                            else:
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
                                self.CheckforWin() #checking if any player won or not
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]

                            if "darkbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                turns = []
                                prevsquare = []
                                return

                            else:    
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

                #calculating the row and column of the square where the checker wants to move
                row = math.floor(7 - (x[1][2]/self.squaresize))+1
                column = math.floor(x[1][1]/self.squaresize)

                #calculating the row and column of the square where the checker initially was   
                row1 = math.floor(7 - (x[0][2]/self.squaresize))+1
                column1 = math.floor(x[0][1]/self.squaresize)

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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print (tags)
                            
                            if "lightbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                turns = []
                                prevsquare = []
                                return

                            else:#calculating the coordinates of the post square
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print (tags)
                            
                            if "lightbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                turns = []
                                prevsquare = []
                                return
                            else:
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
            if turns[0][0] == turns[0][1]:
                if turns[0] == "darkbrown":
                    tm.showwarning("Incorrect Move","Its Lightbrown's Turn")
                    prevsquare = []
                    turns = []
                    return
                if turns[0] == "lightbrown":
                    tm.showwarning("Incorrect Move","Its Darkbrowns's Turn")
                    prevsquare = []
                    turns = []
                    return
            if "darkbrown" in x[0][0]:
                    #calculating the row and column of the square where the checker wants to move
                    row = math.floor(7 - (x[1][2]/self.squaresize))+1
                    column = math.floor(x[1][1]/self.squaresize)

                    #calculating the row and column of the square where the checker initially was   
                    row1 = math.floor(7 - (x[0][2]/self.squaresize))+1
                    column1 = math.floor(x[0][1]/self.squaresize)

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

                                item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                                tags = self.canvas.gettags(item)[0]

                                if "darkbrown" in tags:
                                       prevsquare = []
                                       turns =[]
                                       return
                                if "#8B4513" in tags:
                                    turns = []
                                    prevsquare = []
                                    return                                   

                                else:#calculating coords of post square
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

                                item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                                tags = self.canvas.gettags(item)[0]
                                
                                if "darkbrown" in tags:
                                    prevsquare = []
                                    turns=[]
                                    return
                                
                                if "#8B4513" in tags:
                                    turns = []
                                    prevsquare = []
                                    return
                                else:#calculatin coords of post square
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

                    #calculating the row and column of the square where the checker wants to move
                    row = math.floor(7 - (x[1][2]/self.squaresize))+1
                    column = math.floor(x[1][1]/self.squaresize)

                    #calculating the row and column of the square where the checker initially was   
                    row1 = math.floor(7 - (x[0][2]/self.squaresize))+1
                    column1 = math.floor(x[0][1]/self.squaresize)

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

                                item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                                tags = self.canvas.gettags(item)[0]
                                # print tags
                              
                            if "lightbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                    turns = []
                                    prevsquare = []
                                    return

                            else:
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

                                item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                                tags = self.canvas.gettags(item)[0]
                                # print tags
                            
                            if "lightbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                    turns = []
                                    prevsquare = []
                                    return

                            else:
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
    

        if turns[len(turns)-2] == turns[len(turns)-4]:
            if turns[len(turns)-2] == "darkbrownking":
                tm.showwarning("Incorrect Move","Its Lightbrown's Turn")
                prevsquare = []
                return
            if turns[len(turns)-2] == "lightbrownking":
                tm.showwarning("Incorrect Move","Its Darkbrown's Turn")
                prevsquare = []
                return
            
        elif x[0][0] == "darkbrownking":
                
                if x[1][0] == "#D2B48C": #checking if the square that the checker was moved to was a dark square or not
                    prevsquare = []
                    turns = []
                    return
                
                #calculating the row and column of the square where the checker wants to move
                row = math.floor(7 - (x[1][2]/self.squaresize))+1
                column = math.floor(x[1][1]/self.squaresize)

                #calculating the row and column of the square where the checker initially was   
                row1 = math.floor(7 - (x[0][2]/self.squaresize))+1
                column1 = math.floor(x[0][1]/self.squaresize)
                
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print tags
                            
                            if "darkbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            
                            if "#8B4513" in tags:
                                    turns = []
                                    prevsquare = []
                                    return


                            else:#calculating coords of post square
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print tags
                            
                            if "darkbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                    turns = []
                                    prevsquare = []
                                    return
                            else:
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print tags
                            
                            if "darkbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                    turns = []
                                    prevsquare = []
                                    return

                            else:#calculating coords of post square
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print tags
                            
                            if "darkbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                    turns = []
                                    prevsquare = []
                                    return

                            else:#calculating coords of post square
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
                row = math.floor(7 - (x[1][2]/self.squaresize))+1
                column = math.floor(x[1][1]/self.squaresize)

                #calculating the row and column of the square where the checker initially was   
                row1 = math.floor(7 - (x[0][2]/self.squaresize))+1
                column1 = math.floor(x[0][1]/self.squaresize)
                
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print tags
                            
                            if "lightbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                    turns = []
                                    prevsquare = []
                                    return

                            else:
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print tags
                            
                            if "lightbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                    turns = []
                                    prevsquare = []
                                    return

                            else:#calculating coords of post square
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print tags
                            
                            if "lightbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                    turns = []
                                    prevsquare = []
                                    return

                            else:#calculating coords of post square
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print tags
                            
                            if "lightbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                    turns = []
                                    prevsquare = []
                                    return

                            else:#calculating coords of post square
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
class OnePlayer():
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
        lb = []
        db = []
        # DRAWING THE DARK BROWN CHECKERS #
    
        k = 0
        
        '''k specifies where to start the drawing of the first checker in each row. For example,
           the fist checker on the first row was drawn on the 1st square, the first checker on the second row
           will be drawn on the second row'''
        count = -4
        #iterating through entire through each row
        for i in range (self.rows,4,-1):
            
            #iterating through each coloumn of each row
            for j in range (k,self.columns,2): #iterating through alternating columns
                count = count + 1
                #finding the x and y coordinates of the top left (x1,y1) and botton right (x2,y2) of the square
                x1 = j*self.squaresize
                y1 = (7-i)*self.squaresize
                x2 = x1 + self.squaresize
                y2 = y1 + self.squaresize

                '''checkers are drawn using the x and y coordinates of the top left and bottom right corners of the square in
                   in which they will drawn in'''
                #drawing the checkers
                db.append(self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = "darkbrown"+str(count)))
                self.canvas.tag_bind("darkbrown"+str(count),'<ButtonPress-1>', self.CheckerButtonPress)
                self.canvas.tag_bind("darkbrown"+str(count),'<ButtonRelease-1>', self.CheckerButtonRelease)
                
                
            #alternating the value of k for each row iteration
            if k == 0:
                k=1
            else:
                k=0

        # DRAWING THE LIGHT BROWN CHECKERS #
        count = 0
        k = 0
        #iterating through entire through each row
        for i in range (3):
        
            #iterating through each coloumn of each row               
            for j in range (k,self.columns,2):
                count = count + 1
                #finding the x and y coordinates of the top left (x1,y1) and botton right (x2,y2) of the square
                x1 = j*self.squaresize
                y1 = (7-i)*self.squaresize
                x2 = x1 + self.squaresize
                y2 = y1 + self.squaresize

                #drawing the square
                lb.append(self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = "lightbrowncomputer" + str(count)))

                
            #alternating the value of k for each row iteration
            if k == 0:
                k=1
            else:
                k=0
                
    def CheckforWin(self): #functins checks for number of dark ad light brown checkers left
        countdb = 0
        countlb = 0
        x = 105
        #looping through  each dark square of the board checking for pieces
        for j in range(8):
            for i in range(4):
                item = self.canvas.find_closest(x+(140*i),34+(70*j))[0]
                tag = self.canvas.gettags(item)[0]
                if "darkbrown" in tag: #if darkbown checker found, increase the count by 2
                    countdb = countdb + 1
                if "lightbrown" or "lb" in tag:
                    countlb = countlb + 1 #if darkbown checker found, increase the count by 2
                
            if x == 105:
                x = 34
            else:
                x = 105

        if countdb == 1:
            tm.showinfo("Winner","Lightbrown Won!")
        if countlb == 1 :
            tm.showinfo("Winner","Darkbrown Won!")



    def getAIMove(self,x,y):

        location = [] #location of all lightbrown checkers on the board
        
        a = 105
        for j in range(8):
            for i in range(4):
                item = self.canvas.find_closest(a+(140*i),34+(70*j))[0]
                tag = self.canvas.gettags(item)[0]
                #print tag
                if ("lightbrown") in tag or ("lb" in tag):
                    #print tag
                    coords = self.canvas.coords(tag)
                    row = math.floor(7 - int(coords[1])/self.squaresize) + 1
                    column = math.floor(int(coords[0])/self.squaresize)


                    #print row,column
                    location.append((tag,row,column)) #appending to location, name of checker and row and column of checker postion
                    

            if a == 105:
                a = 34
            else:
                a = 105
                
        #print location
        possiblemoves = []
        possiblecapture = []

        for k in range(len(location)):
            #for loop checks for all possible moves
            if 'lb' in location [k][0]:
                row = location[k][1]
                column = location[k][2]
                moverow1 = row + 1
                moverow2 = row - 1
                movecolumn1 = column - 1
                movecolumn2 = column + 1

                #row up
                move1_x1 = movecolumn1*self.squaresize + 30
                move1_y1 = (7-moverow1)*self.squaresize + 30

                move2_x1 = movecolumn2*self.squaresize + 30
                move2_y1 = (7-moverow1)*self.squaresize + 30

                #row down

                move3_x1 = movecolumn1*self.squaresize + 30
                move3_y1 = (7-moverow2)*self.squaresize + 30
                
                move4_x1 = movecolumn2*self.squaresize + 30
                move4_y1 = (7-moverow2)*self.squaresize + 30

                #appending all the possible moves to list of possiblemoves
                
                item = self.canvas.find_closest(move1_x1,move1_y1)[0]
                tag = self.canvas.gettags(item)[0]
                if ("darkbrown" not in tag) and ("lightbrown" not in tag) and ("lb" not in tag) :
                    if (movecolumn1 > 0) and (moverow1 > 0) and (moverow1 < 8): #column and row number cannot exceed 8 and cannot be lower than 0
                        possiblemoves.append((location[k][0],moverow1,movecolumn1))

                item = self.canvas.find_closest(move3_x1,move3_y1)[0]
                tag = self.canvas.gettags(item)[0]
                if ("darkbrown" not in tag) and ("lightbrown" not in tag) and ("lb" not in tag) :
                    if (movecolumn1 > 0) and (moverow1 > 0) and (moverow2 < 8):
                        possiblemoves.append((location[k][0],moverow2,movecolumn1))
                
                item = self.canvas.find_closest(move2_x1,move2_y1)[0]
                tag = self.canvas.gettags(item)[0]
                if ("darkbrown" not in tag) and ("lightbrown" not in tag) and ("lb" not in tag):
                    if (movecolumn2 > 0) and (movecolumn2 < 8) and (moverow1 > 0) and (moverow1 < 8):
                       possiblemoves.append((location[k][0],moverow1,movecolumn2))

                item = self.canvas.find_closest(move4_x1,move4_y1)[0]
                tag = self.canvas.gettags(item)[0]
                if ("darkbrown" not in tag) and ("lightbrown" not in tag) and ("lb" not in tag):
                    if (movecolumn2 > 0) and (movecolumn2 < 8) and (moverow2 > 0) and (moverow2 < 8):
                       possiblemoves.append((location[k][0],moverow2,movecolumn2))

            else:               
                row = location[k][1]
                column = location[k][2]
                moverow1 = row + 1
                movecolumn1 = column - 1
                movecolumn2 = column + 1

                move1_x1 = movecolumn1*self.squaresize + 30
                move1_y1 = (7-moverow1)*self.squaresize + 30

                move2_x1 = movecolumn2*self.squaresize + 30
                move2_y1 = (7-moverow1)*self.squaresize + 30

                item = self.canvas.find_closest(move1_x1,move1_y1)[0]
                tag = self.canvas.gettags(item)[0]
                #print tag
                if ("darkbrown" not in tag) and ("lightbrown" not in tag) and ("lb" not in tag) :
                    if (movecolumn1 > 0) and (moverow1 > 0) and (moverow1 < 8):
                        possiblemoves.append((location[k][0],moverow1,movecolumn1))

                item = self.canvas.find_closest(move2_x1,move2_y1)[0]
                tag = self.canvas.gettags(item)[0]
                if ("darkbrown" not in tag) and ("lightbrown" not in tag) and ("lb" not in tag):
                    if (movecolumn2 > 0) and (movecolumn2 < 8) and (moverow1 > 0) and (moverow1 < 8):
                       possiblemoves.append((location[k][0],moverow1,movecolumn2))

        for k in range(len(location)):
            
            #this for loop checks for all possible captures
            row = location[k][1]
            column = location[k][2]
            moverow1 = row + 2
            moverow_capture = row + 1
            
            #capturing left side
            
            movecolumn1 = column - 2
            movecolumn1_capture = column - 1

            capture1_x1 = movecolumn1_capture*self.squaresize + 20 
            capture1_y1 = (7 - moverow_capture)*self.squaresize + 20

            move1_x1 = movecolumn1*self.squaresize + 20
            move1_y1 = (7-moverow1)*self.squaresize + 20

            item1 = self.canvas.find_closest(move1_x1,move1_y1)[0] #checking for items at post square
            tag1 = self.canvas.gettags(item1)[0]

            item2 = self.canvas.find_closest(capture1_x1,capture1_y1)[0] #checking for items at capture square
            tag2 = self.canvas.gettags(item2)[0]
            

            if ("darkbrown" in tag2) and ("darkbrown" not in tag1) and ("lightbrown" not in tag1) and ("lb" not in tag1):
                if (movecolumn1_capture > 0) and (moverow_capture < 8) and (movecolumn1 > 0) and (moverow1 < 8):
                    possiblecapture.append((location[k][0],moverow1,movecolumn1,tag2))

            #capturing on right side

            movecolumn2 = column + 2
            movecolumn2_capture = column + 1

            capture2_x1 = movecolumn2_capture*self.squaresize + 20 
            capture2_y1 = (7 - moverow_capture)*self.squaresize + 20

            move2_x1 = movecolumn2*self.squaresize + 20
            move2_y1 = (7-moverow1)*self.squaresize + 20

            item3 = self.canvas.find_closest(move2_x1,move2_y1)[0] #checking for items at post square
            tag3 = self.canvas.gettags(item3)[0]

            item4 = self.canvas.find_closest(capture2_x1,capture2_y1)[0] #checking for items at capture square
            tag4 = self.canvas.gettags(item4)[0]

            if ("darkbrown" in tag4) and ("darkbrown" not in tag3) and ("lightbrown" not in tag3) and ("lb" not in tag3):
                if (movecolumn2_capture < 8) and (moverow_capture < 8) and (movecolumn2 < 8) and (moverow1 < 8):
                    possiblecapture.append((location[k][0],moverow1,movecolumn2,tag4))

            if "lb" in location[k][0]:
                #capturing below, to the left and right
                row = location[k][1]
                column = location[k][2]
                moverow1 = row - 2
                moverow_capture = row - 1

                #capturing left side
            
                movecolumn1 = column - 2
                movecolumn1_capture = column - 1

                capture1_x1 = movecolumn1_capture*self.squaresize + 20 
                capture1_y1 = (7 - moverow_capture)*self.squaresize + 20

                move1_x1 = movecolumn1*self.squaresize + 20
                move1_y1 = (7-moverow1)*self.squaresize + 20

                item1 = self.canvas.find_closest(move1_x1,move1_y1)[0] #checking for items at post square
                tag1 = self.canvas.gettags(item1)[0]

                item2 = self.canvas.find_closest(capture1_x1,capture1_y1)[0] #checking for items at capture square
                tag2 = self.canvas.gettags(item2)[0]
                

                if ("darkbrown" in tag2) and ("darkbrown" not in tag1) and ("lightbrown" not in tag1) and ("lb" not in tag1):
                    if (movecolumn1_capture > 0) and (moverow_capture < 8) and (movecolumn1 > 0) and (moverow1 < 8):
                        possiblecapture.append((location[k][0],moverow1,movecolumn1,tag2))

                #capturing on right side

                movecolumn2 = column + 2
                movecolumn2_capture = column + 1

                capture2_x1 = movecolumn2_capture*self.squaresize + 20 
                capture2_y1 = (7 - moverow_capture)*self.squaresize + 20

                move2_x1 = movecolumn2*self.squaresize + 20
                move2_y1 = (7-moverow1)*self.squaresize + 20

                item3 = self.canvas.find_closest(move2_x1,move2_y1)[0] #checking for items at post square
                tag3 = self.canvas.gettags(item3)[0]

                item4 = self.canvas.find_closest(capture2_x1,capture2_y1)[0] #checking for items at capture square
                tag4 = self.canvas.gettags(item4)[0]

                if ("darkbrown" in tag4) and ("darkbrown" not in tag3) and ("lightbrown" not in tag3) and ("lb" not in tag3):
                    if (movecolumn2_capture < 8) and (moverow_capture < 8) and (movecolumn2 < 8) and (moverow1 < 8):
                        possiblecapture.append((location[k][0],moverow1,movecolumn2,tag4))                

        self.makeAIMove(possiblemoves,possiblecapture) #calling function that will perform the checker move

    def makeAIMove(self,possiblemoves, possiblecapture):
        if len(possiblemoves) == 0: #if there are no possible moves, then that means that all darkbrown checkers are blocked, darkbrown then wins
            tm.showinfo("Winner","Darkbrown Won!")
            return
            
        elif len(possiblecapture) == 0: #if no possible possible captures, choose a random move from the possible moves and move the checker
            move = random.choice(possiblemoves)
            index = re.search("\d+",move[0])
            checkernumber = move[0][index.start():index.end()] #finding checker number to create a uniquely named king checker
            self.canvas.delete(move[0])
            
            x1 = move[2]*self.squaresize
            y1 = (7-move[1])*self.squaresize
            x2 = x1 + self.squaresize
            y2 = y1 + self.squaresize

            #drawing the checkers
            if "lb" in move[0]:
                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = 4,tags = move[0])
                self.CheckforWin()
                return
            if move[1] == 7: #if checker reaches the top row, it becames a king
                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = 4,tags = "lbking"+str(checkernumber))
                self.CheckforWin()
                return
            else:
                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = move[0])
                self.CheckforWin()
                return
        else:
            #perform the capture
            move = random.choice(possiblecapture)
            
            index = re.search("\d+",move[0])
            checkernumber = move[0][index.start():index.end()]
            
            self.canvas.delete(move[0])
            self.canvas.delete(move[3]) #delete the captured checker
            x1 = move[2]*self.squaresize
            y1 = (7-move[1])*self.squaresize
            x2 = x1 + self.squaresize
            y2 = y1 + self.squaresize

            #drawing the checkers
            if "lb" in move[0]:
                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = 4,tags = move[0])
                self.CheckforWin()
                return
                
            if move[1] == 7:
                
                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "red",width = 4,tags = "lbking" + str(checkernumber))
                self.CheckforWin()
                return
                                              
            else:
                
                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#DEB887",outline = "black",tags = move[0])
                self.CheckforWin()
                return
                
            
            



    def CheckerButtonPress(self,event): #this function calculates which object was pressed and saves its name + position in prevsquare
        global prevsquare
        item = self.canvas.find_closest(event.x,event.y)[0] #finding item clicked
        tags = self.canvas.gettags(item)[0] #finding tag of the item
        prevsquare.append((tags,event.x,event.y))
        


    def CheckerButtonRelease(self,event):
        global turns
        global prevsquare
        
        self.CheckerButtonPress(event) #calling checkerbuttonpress function
        
        x = prevsquare
        # print x

        if "darkbrown" in x[0][0]:
            if x[1][0] == "#D2B48C": #cannot move to a light square
                prevsquare = []
                turns = []

            #calculating the row and column of the square where the checker wants to move
            row = math.floor(7 - (x[1][2]/self.squaresize))+1
            column = math.floor(x[1][1]/self.squaresize)

            #calculating the row and column of the square where the checker initially was   
            row1 = math.floor(7 - (x[0][2]/self.squaresize))+1
            column1 = math.floor(x[0][1]/self.squaresize)

            #checking for invalid moves
            if column1 == column or row1 == row or row>row1 or (row1-row)>2:
                prevsquare = []
                turns = []
                return

            #if the checker wants to get a capture
            elif (column == column1 - 2) or (row == row1 - 2) or (column == column1 + 2):
                
                if column == column1 - 2: #capturing on the left side of the checker
        
                    #checking if the place post move square has a checker in it or not 
                    if ("lightbrowncomputer" in x[1][0]) or ("darkbrown" in x[1][0]):
                        prevsquare = []
                        turns = []
                        return
                    else: #if not proceed with capture, delete the checker from the current square, delete the captured checkered, re draw the current checker on post square

                        #calculating coords of capturing square
                        capturex1 = (column1-1)*self.squaresize + 20
                        capturey1 = (7-(row1-1))*self.squaresize + 20

                        #finding the checker at the capturing square
                        item = self.canvas.find_closest(capturex1,capturey1)[0]
                        tags = self.canvas.gettags(item)[0]

                        #finding checker number to create a uniquely named king checker
                        index = re.search("\d+",x[0][0])
                        checkernumber = x[0][0][index.start():]
                        

                        if "darkbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                        if "#8B4513" in tags:
                                turns = []
                                prevsquare = []
                                return
                            
                        else: #calculating coords of post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize

                            #draws the squares and checker on the canvas
                            #deleting captred checker and current checker and drawing the checker again
                            self.canvas.delete(tags)
                            self.canvas.delete(x[0][0])
                            if row == 0:
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = "darkbrownking"+ str(checkernumber))
                                self.canvas.tag_bind("darkbrownking"+ str(checkernumber),'<ButtonPress-1>', self.CheckerButtonPress)
                                self.canvas.tag_bind("darkbrownking"+ str(checkernumber),'<ButtonRelease-1>', self.KingCheckerButtonRelease)
                            else:
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = x[0][0])
        
                            prevsquare = []
                            
                            #getting AI move
                            self.CheckforWin()
                            self.getAIMove(x[1][1],x[1][2])
                            self.CheckforWin()
                            return
                    
                if column == column1 + 2: #capturing on the right side of the checker
                    
                    if ("lightbrown" in x[1][0]) or ("darkbrown" in x[1][0]): #checking if the place post move square has a checker in it or not 
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
                        capturex1 = (column1+1)*self.squaresize + 20
                        capturey1 = (7-(row1-1))*self.squaresize + 20
                        
                        item = self.canvas.find_closest(capturex1,capturey1)[0]
                        tags = self.canvas.gettags(item)[0]

                        #finding checker number to create a uniquely named king checker
                        index = re.search("\d+",x[0][0])
                        checkernumber = x[0][0][index.start()]
                        

                        if "darkbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                        if "#8B4513" in tags:
                                turns = []
                                prevsquare = []
                                return
                        
                        else:#calculatin coords of post square
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize
                            
                            #draws the squares and checker on the canvas
                            self.canvas.delete(x[0][0])
                            self.canvas.delete(tags)
                            if row == 0:
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = "darkbrownking"+ str(checkernumber))
                                self.canvas.tag_bind("darkbrownking"+ str(checkernumber),'<ButtonPress-1>', self.CheckerButtonPress)
                                self.canvas.tag_bind("darkbrownking"+ str(checkernumber),'<ButtonRelease-1>', self.KingCheckerButtonRelease)
                            else:
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = x[0][0])
                            prevsquare = []
                            
                            self.CheckforWin()
                            self.getAIMove(x[1][1],x[1][2])
                            self.CheckforWin()
                            return
            else:
                    if ("lightbrown" in x[1][0]) or ("darkbrown" in x[1][0]): #checking is post square has a checker in it or not
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

                        item = self.canvas.find_closest(x1,y1)[0]
                        tags = self.canvas.gettags(item)[0]

                        #finding checker number to create a uniquely named king checker
                        index = re.search("\d+",x[0][0])
                        checkernumber = x[0][0][index.start()]
                        

                        if "darkbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                        if "#8B4513" in tags:
                                turns = []
                                prevsquare = []
                                return

                        self.canvas.delete(x[0][0]) #deleting current piece
                      
                        
                        if row == 0: #if the darkbrown checker reaches the other side of the board, it becomes king
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = "darkbrownking"+ str(checkernumber))
                            self.canvas.tag_bind("darkbrownking"+ str(checkernumber),'<ButtonPress-1>', self.CheckerButtonPress)
                            self.canvas.tag_bind("darkbrownking"+ str(checkernumber),'<ButtonRelease-1>', self.KingCheckerButtonRelease)
                        else:
                           
                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "black",tags = x[0][0])
                        prevsquare = []
                        self.CheckforWin()
                        self.getAIMove(x[1][1],x[1][2])
                        self.CheckforWin()
                        return
                    
    def KingCheckerButtonRelease(self,event):
        global prevsquare
        global turns
        self.CheckerButtonPress(event)
        x = prevsquare
        # print x

            
        if "darkbrownking" in x[0][0]:
                
                if x[1][0] == "#D2B48C": #checking if the square that the checker was moved to was a dark square or not
                    prevsquare = []
                    turns = []
                    return
                
                #calculating the row and column of the square where the checker wants to move
                row = math.floor(7 - (x[1][2]/self.squaresize))+1
                column = math.floor(x[1][1]/self.squaresize)

                #calculating the row and column of the square where the checker initially was   
                row1 = math.floor(7 - (x[0][2]/self.squaresize))+1
                column1 = math.floor(x[0][1]/self.squaresize)
                
                if column1 == column or row1 == row:
                    prevsquare = []
                    turns = []
                    return
                
                elif ((column == column1 - 2) or (column == column1 + 2)) and (row == row1 + 2):
                    
                    if (column == column1 - 2):#capturing on left side of current pos
                            
                        if ("lightbrown" in x[1][0]) or ("darkbrown" in x[1][0]):
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print tags

                            #checking if capture square is empty or has a darkbrown checker in it
                            if "darkbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                turns = []
                                prevsquare = []
                                return


                            else:#calculating coords of post square
                                x1 = column*self.squaresize
                                y1 = (7-row)*self.squaresize
                                x2 = x1 + self.squaresize
                                y2 = y1 + self.squaresize

                                self.canvas.delete(tags)
                                self.canvas.delete(x[0][0])

                                #draws the squares and checker on the canvas)
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = x[0][0])
                                prevsquare = []
                                self.CheckforWin()
                                self.getAIMove(x[1][1],x[1][2])
                                self.CheckforWin()
                                return
                            
                    if (column == column1+2):
                        if ("lightbrown" in x[1][0]) or ("darkbrown" in x[1][0]):
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print tags
                            
                            if "darkbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                turns = []
                                prevsquare = []
                                return
                            

                            else:
                                #calculating coords of post square
                                x1 = column*self.squaresize
                                y1 = (7-row)*self.squaresize
                                x2 = x1 + self.squaresize
                                y2 = y1 + self.squaresize

                                self.canvas.delete(tags)
                                self.canvas.delete(x[0][0])

                                #draws the squares and checker on the canvas
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = x[0][0])
                                prevsquare = []
                                
                                self.CheckforWin()
                                self.getAIMove(x[1][1],x[1][2])
                                self.CheckforWin()
                                return

                elif ((column == column1 - 2) or (column == column1 + 2)) and (row == row1 - 2):
                    
                    if (column == column1 - 2):#capturing on left side of current pos
                            
                        if ("lightbrown" in x[1][0]) or ("darkbrown" in x[1][0]):
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print tags
                            
                            if "darkbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                turns = []
                                prevsquare = []
                                return


                            else:#calculating coords of post square
                                x1 = column*self.squaresize
                                y1 = (7-row)*self.squaresize
                                x2 = x1 + self.squaresize
                                y2 = y1 + self.squaresize

                                self.canvas.delete(tags)
                                self.canvas.delete(x[0][0])

                                #draws the squares and checker on the canvas
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = x[0][0])

                                prevsquare = []

                                self.CheckforWin()
                                self.getAIMove(x[1][1],x[1][2])
                                self.CheckforWin()
                                return
                            
                    if (column == column1+2):
                        if ("lightbrown" in x[1][0]) or ("darkbrown" in x[1][0]):
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

                            item = self.canvas.find_closest(capturex1 + 20,capturey1+20)[0]
                            tags = self.canvas.gettags(item)[0]
                            # print tags
                            
                            if "darkbrown" in tags:
                                turns = []
                                prevsquare = []
                                return
                            if "#8B4513" in tags:
                                turns = []
                                prevsquare = []
                                return

                            else:#calculating coords of post square
                                x1 = column*self.squaresize
                                y1 = (7-row)*self.squaresize
                                x2 = x1 + self.squaresize
                                y2 = y1 + self.squaresize

                                self.canvas.delete(tags)
                                self.canvas.delete(x[0][0])


                                #draws the checker on the canvas
                                self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = x[0][0])
                                
                                prevsquare = []
                                self.CheckforWin()
                                self.getAIMove(x[1][1],x[1][2])
                                self.CheckforWin()
                                return
                    
                else:
                        if ("lightbrown" in x[1][0]) or ("darkbrown" in x[1][0]) or ("lb" in x[1][0]): #checking is post square has a checker in it or not
                                prevsquare = []
                                turns = []
                                return

                        else:
                            #calculating the post square coordinates
                            x1 = column*self.squaresize
                            y1 = (7-row)*self.squaresize
                            x2 = x1 + self.squaresize
                            y2 = y1 + self.squaresize

                            item = self.canvas.find_closest(x1 + 20,y1+20)[0]
                            tags = self.canvas.gettags(item)[0]

                            #calculating current square coordinates
                            x1delete = column1*self.squaresize
                            y1delete = (7-row1)*self.squaresize
                            x2delete = x1delete + self.squaresize
                            y2delete = y1delete + self.squaresize

                            item = self.canvas.find_closest(x1delete + 20,y1delete+20)[0]
                            tags = self.canvas.gettags(item)[0]

                            #deleting and redrawing the checkers
                            self.canvas.delete(tags)
                            self.canvas.delete(x[0][0])

                            self.canvas.create_oval(x1+5,y1+5,x2-5,y2-5,fill="#331900",outline = "red",width = "4",tags = x[0][0])
                            prevsquare = []
                            self.CheckforWin()
                            self.getAIMove(x[1][1],x[1][2])
                            self.CheckforWin()
                            return


def OnePlayerGame():
    oneplayer = Tk()
    oneplayer.title("Checkers! - One Player")
    OnePlayer(oneplayer)
    tm.showinfo("Information", "You will be the using the DarkBrown checkers.\nThe computer will be playing with the Lightbrown Checkers.\nHave fun!")

def TwoPlayerGame(): #opens up one player game window
    twoplayer = Tk()
    twoplayer.title("Checkers! - Two Player")
    TwoPlayer(twoplayer)
    tm.showinfo("Information", "Decide between you and your opponent which checkers you would like to use.\nWhosoever chooses the Darkbrown Checker, they make the first move.")

def ExitProgram(): #exits the program by destroying main startup window
    global startup
    result = tm.askyesno(title = "Exit?", message = "Would you like to exit?") 
    if result == True:
        startup.destroy()
        
def Instructions(): #creating a top level window that where an image with all the instruction is places
    howtoplay = Toplevel()
    howtoplay.title("Checkers! - How to Play")
    background = "Instructions.gif"
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

    #These images have files paths pertaining to my OS, if you would like to use the images, download them from 
    #my github repository and change the file names below
    background = "CheckersStartup.gif" 
    howtoplay = "HowToPlay.gif"
    oneplayer = "OnePlayer.gif"
    twoplayer = "TwoPlayer.gif"
    exitprogram = "Exit.gif"

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
    
    button2 = Button(startup,width = 365,height = 60, image = oneplayer_photo, command = OnePlayerGame)
    button2_window = canvas.create_window(311,252,anchor = "n",window=button2)
    
    button3 = Button(startup,width = 365,height = 60, image = twoplayer_photo,command = TwoPlayerGame)
    button3_window = canvas.create_window(311,342,anchor = "n",window=button3)

    button4 = Button(startup,width = 365,height = 60, image = exitprogram_photo,command = ExitProgram)
    button4_window = canvas.create_window(311,432,anchor = "n",window=button4)

    startup.mainloop()
    
if __name__=="__main__":
    main()
