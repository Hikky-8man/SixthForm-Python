import pyglet
from tkinter import *
from pyglet.window import key
import random

#------------------------------------The main game------------------------------------------
#This class will contain all of the code for the main game form all the gameplay aspects
#to the sprites etc
class Main_game:
    #This is the initiation class which will start the main game
    def __init__(self):
        self.map1()
#-----------------------------------------free roam-----------------------------------------
#This meathod will contain all of the code for the free roam section of the game
    def map1(self):
        #This creates a screen and sets it to false, this is so the program can load
        #all of the data before it is show to the user, this will hopefully increase
        #the efficiency of my program
        world=pyglet.window.Window(visible=False, fullscreen=True)
#these two lines of code create the characters in_game sprite
        character_image=pyglet.resource.image("sprite_alpha.png")
        character=pyglet.sprite.Sprite(img=character_image,
                                       x=world.width//2,y=world.height//2)

        interactable_image=pyglet.resource.image("interactable_alpha.png")
        interactable=pyglet.sprite.Sprite(img=interactable_image,
                                          x=world.width//3, y=world.height//2)
        #this line of code is going to define when the switch to turn based combat happens
        #This value is a constant, so it wont change
        encounter=5
        #These lines of code clears the screen and puts the specified objects onto
        #the screen
        @world.event
        def on_draw():
            world.clear()
            character.draw()
            interactable.draw()

        pyglet.graphics.draw(2,pyglet.gl.GL_POINTS,
                             ("v2i",(10,15,30,35)))
#These lines of code work with the button inputs. When a specific key on the keyboard has
            #been pressed, a specific action will be carried out (if any)
        @world.event
        def on_key_press(symbol, modifier):
#all proceeding lines of code will deal with character movement based on specific keyboard
            #inputs and work with the boundries of the sprite.

            if symbol==key.A or symbol==key.LEFT:
                if character.x!=-12:
                    character.x-=20
                    #This is the random number that defines weather a fight is going to
                    #happen
                    fight=random.randrange(1,20)
                    #This function triggers the turn based combat section
                    if fight==encounter:
                        Main_game.combat(Main_game)
                    #This line of code (which is the same line of code on all of the other
                    #3 following input functions) deals with the conversion of the free roam
                    #area to the shop/hospital area
                if character.y==interactable.y and character.x==interactable.x-4:
                    print ("Touch")
                    Main_game.shop1(Main_game)
                    
            if symbol==key.S or symbol==key.DOWN:
                if character.y!=-8:
                    character.y-=20
                    #This is the random number that defines weather a fight is going to
                    #happen
                    fight=random.randrange(1,20)
                    #This function triggers the turn based combat section
                    if fight==encounter:
                        Main_game.combat(Main_game)
                if character.y==interactable.y and character.x==interactable.x-4:
                    Main_game.shop1(Main_game)

            if symbol==key.D or symbol==key.RIGHT:
                if character.x!=1448:
                    character.x+=20
                    #This is the random number that defines weather a fight is going to
                    #happen
                    fight=random.randrange(1,20)
                    #This function triggers the turn based combat section
                    if fight==encounter:
                        Main_game.combat(Main_game)
                if character.y==interactable.y and character.x==interactable.x-4:
                     Main_game.shop1(Main_game)

            if symbol==key.W or symbol==key.UP:
                if character.y!=772:
                    character.y+=20
                    #This is the random number that defines weather a fight is going to
                    #happen
                    fight=random.randrange(1,20)
                    #This function triggers the turn based combat section
                    if fight==encounter:
                        Main_game.combat(Main_game)
                if character.y==interactable.y and character.x==interactable.x-4:
                     Main_game.shop1(Main_game)

#These lines of code close the window after making it invisible to the user (temporary
                #emergency exit from the program
            if symbol==key.ESCAPE:
                world.set_visible(False)
                quit()
#These lines of code make the screen visible to the user and runs the pyglet code
        world.set_visible(True)
        pyglet.app.run()
#---------------------------------------shop------------------------------------
#This meathod will define a shop instance
    def shop1(self):
        #I kept it the same name so it is simple for me when I have to create the two other
        #maps and the other instances of the 'shop'
        world=pyglet.window.Window(visible=False,fullscreen=True)

        character_image=pyglet.resource.image("sprite_alpha.png")
        character=pyglet.sprite.Sprite(img=character_image,
                                       x=1448,y=world.height//2)

        door_image=pyglet.resource.image("door.png")
        door=pyglet.sprite.Sprite(img=door_image,
                                  x=1448, y=world.height//2)

        @world.event
        def on_draw():
            world.clear()
            door.draw()
            character.draw()

        @world.event
        def on_key_press(symbol, modifier):
#all proceeding lines of code will deal with character movement based on specific keyboard
            #inputs and work with the boundries of the sprite.

            if symbol==key.A or symbol==key.LEFT:
                if character.x!=-12:
                    character.x-=20
                    
            if symbol==key.S or symbol==key.DOWN:
                if character.y!=-8:
                    character.y-=20
#This line of code switches the user back to the free-roam area
            if symbol==key.D or symbol==key.RIGHT:
                if character.x==1448:
                    world.set_visible(False)
                else:
                    character.x+=20

            if symbol==key.W or symbol==key.UP:
                if character.y!=772:
                    character.y+=20
        world.set_visible(True)
        pyglet.app.run()
        
#--------------------------------------turn based combat section----------------------------
    def combat(Self):
        #This code creates the screen and makes it invisible
        screen=pyglet.window.Window(visible=False,fullscreen=True)
        #This line of code creates a text label which reads press the ESC key
        text=pyglet.text.Label("Press the ESC key",
                               x=screen.width//2,y=screen.height//2)
        #These lines of code place the text onto the screen for the user to see
        @screen.event
        def on_draw():
            screen.clear()
            text.draw()

        #These lines of code dea with specific keyboard inputs
        @screen.event
        def on_key_press(symbol,modifier):
            if symbol==key.ESCAPE:
                screen.set_visible(False)
        #This line of code makes the screen visible to the user
        screen.set_visible(True)
        #This allows the code to be exicuted and looped
        pyglet.app.run()

#----------------------------------------------------menus----------------------------------        
class Menu(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master

        self.main_menu()

    def main_menu(self):
        self.master.title("Main menu")
        self.pack(fill=BOTH,expand=1)

        start_button=Button(self,text="Start game",command=self.start_game)
        start_button.place(x=150,y=150)

        settings_button=Button(self,text="Setting", command=self.settings)
        settings_button.place(x=150,y=180)

    def start_game(self):
        root.destroy()
        Main_game()

    def settings(self):
        quit()
#----------------------------------------------configuration--------------------------------
root=Tk()
root.geometry("400x400")
app=Menu(root)
root.mainloop()
