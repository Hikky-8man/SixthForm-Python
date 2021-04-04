#The sorting and searching program but with a GUI
#Date created: 10/03/2021

import pyglet
from pyglet.window import key
from pyglet.window import mouse

class Window():
    def __init__(self,width,height):
        self.window=pyglet.window.Window(width,height)
        self.batch=pyglet.graphics.Batch()
        self.active=None #the current class that is using the screen
        self.size=30 #sets a common text size
        self.console=Console() #creates a new console structure

    def getConsole(self):
        return self.console
        
    def getSize(self):
        return self.size

    #changes the class which is currently using the window
    def setActive(self,active):
        self.active=active
        print ("[ACTIVE] Set to "+self.active.toString()+"\n")

    def getWidth(self):
        return self.window.width
    
    def getHeight(self):
        return self.window.height
    
    #returns the sprite batch used for drawing things on the screen
    def getBatch(self):
        return self.batch

    #empties the batch list
    def overwrite(self):
        self.batch=pyglet.graphics.Batch()

    #has to be done because of how event handlers work in pyglet
    #cant do @self.window.event
    def run(self):
        window=self.window
        @window.event
        def on_draw():
            #print("[DRAWING] \n")
            window.clear()
            #self.active.draw()
            self.batch.draw()

        #handles mouse input events for the other classes
        @window.event
        def on_mouse_press(x,y,symbol,modifier):
            #passes the mouse inputs to the relevant classes submit method
            self.active.submitMouseClick(x,y) 

        @window.event
        def on_mouse_motion(x,y,dx,dy):
            #passes the mouse inputs to the relevant classes submit method
            self.active.submitMouseHover(x,y,dx,dy)

        @window.event
        def on_key_press(symbol,modifier):
            if symbol==key.ESCAPE:
                print ("ESC")
                quit()
            else:
                #passes the key input to the relevant classes submit method
                self.active.submitKeyPress(symbol,modifier)




#---------------------Main Menu-------------------------
class MainMenu():
    def __init__(self,window):
        self.window=window #"remembers" the window
        self.window.setActive(self) #sets the active window to MM
        self.window.overwrite() #clears the window

        #retrieves the current dimensions of the screen
        self.height=self.window.getHeight()
        self.width=self.window.getWidth()

        self.quater=self.height/4 #quater of the screen

        #creates all of the label sto be used
        self.bubble=pyglet.text.Label("Bubble sort",
                          x=0,y=self.height-(self.quater),
                          anchor_x="left",anchor_y="bottom",
                          font_size=self.window.getSize(),
                          batch=self.window.getBatch())

        self.insersion=pyglet.text.Label("Insersion sort",
                          x=0,y=self.height-(self.quater*2),
                          anchor_x="left",anchor_y="bottom",
                          font_size=self.window.getSize(),
                          batch=self.window.getBatch())

        self.linear=pyglet.text.Label("Linear search",
                          x=0,y=self.quater,
                          anchor_x="left",anchor_y="bottom",
                          font_size=self.window.getSize(),
                          batch=self.window.getBatch())

        pyglet.text.Label("press the [ESC] to quit",
                          x=0,y=self.height,
                          anchor_x="left",anchor_y="top",
                          font_size=20,
                          batch=self.window.getBatch())


    def submitKeyPress(self,symbol,modifier):
        pass

    def submitMouseClick(self,x,y):
        #print ("[MOUSE PRESS] X:"+str(x)+" Y:"+str(y)+"\n")
        if y>(self.quater*3):
            bubble=BubbleSort(self.window)

    def submitMouseHover(self,x,y,dx,dy):
        #print ("[Hover]: X:"+str(x)+" Y:"+str(y)+" DX:"+str(dx)+" DY:"+str(dy)+"\n")
        if y>(self.quater*3):
            self.bubble.x=10
            self.insersion.x=0
            self.linear.x=0

        elif y<(self.quater*3) and y>(self.height/4)*2:
            self.bubble.x=0
            self.insersion.x=10
            self.linear.x=0

        elif y<(self.quater*2) and y>self.quater:
            self.bubble.x=0
            self.insersion.x=0
            self.linear.x=10

        else:
            self.bubble.x=0
            self.insersion.x=0
            self.linear.x=0
            
    def toString(self):
        return "MainMenu"

#---------------------Bubble Sort-------------------------
class BubbleSort():
    def __init__(self,window):
        self.window=window #"remembers" the window
        self.window.setActive(self) #sets the window to B.S
        self.window.overwrite() #clears the sprite batch

        self.console=self.window.getConsole() #retrieves and emembers the console
        self.console.overwrite() #clears the console
        self.input=False #Flag which enables or disables keyboard inputs (except for ESC key)
        self.inputText=">" #String which contains the text that the user entered
        
        self.array=[2,5,4,1,3]#generates a default array
        
        self.quater=self.window.getHeight()/4 #quater of the screen

        self.state=None #current state of the screen 0=menu 1=sort 2=array
        self.menuState() #sets the state of the window to menu
            
    def menuState(self):
        self.state=0
        self.window.overwrite()#emties the batch list
        
        contents=pyglet.text.Label("Current list: "+str(self.array),
                                     x=0,y=self.window.getHeight(),
                                     anchor_x="left",anchor_y="top",
                                     font_size=self.window.getSize(),
                                     batch=self.window.getBatch())
        
        self.array=pyglet.text.Label("Make a new list",
                                     x=0,y=self.quater*3,
                                     anchor_x="left",anchor_y="bottom",
                                     font_size=self.window.getSize(),
                                     batch=self.window.getBatch())
        
        self.sort=pyglet.text.Label("Sort the current array",
                                     x=0,y=self.quater*2,
                                     anchor_x="left",anchor_y="bottom",
                                     font_size=self.window.getSize(),
                                     batch=self.window.getBatch())
        
    def sortState(self):    
        self.state=1
        self.window.overwrite()
        
    def arrayState(self):
        window=self.window
        self.state=2
        self.window.overwrite()
        
        print ("[ArrayState]outputting data")
        self.console.getData(self.window.getHeight(),
                             self.window.getSize(),
                             self.window.getBatch())
        
        def _input(data):
            self.console.add(data)
            self.inputText=">"
            self.input=True
            position=0
            
        self.inputLabel=pyglet.text.Label(self.inputText,
                                          x=0,y=10,
                                          anchor_x="left",anchor_y="bottom",
                                          font_size=self.window.getSize(),
                                          batch=self.window.getBatch())
        
        _input("How long do you want the list to be?")
        
        
        
    def toString(self):
        return "BubbleSort"

    def submitKeyPress(self,symbol,modifier):
        if self.state==2: #array state
            if self.input==True:
                if symbol==key.ENTER:
                    self.console.add(self.inputText) #adds the text to the console
                    self.inputText=">" #Resets the "text field"
                    self.input=False #disables keyboard input (except for ESC)
                    #self.console.getData(self.window.getHeight,
                    #                     self.window.getSize(),
                    #                     self.window.getBatch())

                elif symbol==key.BACKSPACE:
                    if self.inputText!=">":
                        self.inputText[:-1]
                        
                elif symbol==key._0 or symbol==key.NUM_0:
                    self.inputText+="0"

                elif symbol==key._1 or symbol==key.NUM_1:
                    self.inputText+="1"
                    
                elif symbol==key._2 or symbol==key.NUM_2:
                    self.inputText+="2"

                elif symbol==key._3 or symbol==key.NUM_3:
                    self.inputText+="3"

                elif symbol==key._4 or symbol==key.NUM_4:
                    self.inputText+="4"

                elif symbol==key._5 or symbol==key.NUM_5:
                    self.inputText+="5"
                
    def submitMouseClick(self,x,y):
        if self.state==0: #Menu state
            if y>self.window.getHeight()-self.quater: #"Make a new list" option
                state=1 #array state
                self.arrayState()
    
    def submitMouseHover(self,x,y,dx,dy):
        if self.state==0: #Menu state
            if y>self.window.getHeight()-self.quater:
                self.array.x=10
                self.sort.x=0
                
            elif y<self.window.getHeight()-self.quater and y>self.quater*2:
                self.array.x=0
                self.sort.x=10

            else:
                self.array.x=0
                self.sort.x=0

#---------------------Insersion Sort----------------------

#---------------------Linear Search-----------------------
                
#---------------------Console-----------------------------
#A queue structure which contains strings
class Console:
    def __init__(self):
        self.console=[None,None,None,None,None,None,None,None,None,None]

    def length(self):
        count=0
        for item in self.console:
            if item!=None:
                count+=1
        return count
                
    def add(self,data):
        if self.length()<=10:
            print (str(self.length()))
            self.console[len(self.console)-1]=data
        else:
            count=1
            while (count!=10):
                self.console[count-1]=console[count]
                count+=1
            self.console[9]=data
        #self.getData()
        print ("[CONSOLE] '"+data+"' added")
                

    def overwrite(self):
        self.data=[]

    def getData(self,height,size,batch): #draws the contents of the console onto the screen
        if self.length()!=0:
            pos=10
            for item in self.console:
                if item!=None:
                    label=pyglet.text.Label(item,
                    x=0,y=height-pos,
                    anchor_x="left",anchor_y="bottom",
                    font_size=size,
                    batch=batch)
                    pos+=1
                    print ("[CONSOLE] YEAH")
            print ("[CONSOLE] DONE!")
        else:
            print ("[CONSOLE] Nothing to output")
            
#            |    
#            V Empty
#State flow: window -> mainMenu <->[BubbleSort, InsersionSort, LinearSearch]

#sets the window to the main menu and runs it in an inkfinite loop
print ("[CREATING] window \n")
window=Window(800,500)
print ("[CREATING] menu screen \n")
menu=MainMenu(window)
print ("[LAUNCHING] window \n")
window.run()
print ("[RUNNING] menu screen)\n")
pyglet.app.run()
