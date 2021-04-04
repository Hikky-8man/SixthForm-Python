import pyglet
from tkinter import *
from pyglet.window import key

#--------------------The main game--------------------------
#This class will contain all of the code for the main game form all the gameplay aspects
#to the sprites etc
class Main_game:
    #This is the initiation class which will start the main game
    def __init__(self):
        self.free_roam()
#This meathod will contain all of the code for the free roam section of the game
    def free_roam(self):
        #This creates a screen and sets it to false, this is so the program can load
        #all of the data before it is show to the user, this will hopefully increase
        #the efficiency of my program
        world=pyglet.window.Window(visible=False, fullscreen=True)
#these two lines of code create the characters in_game sprite
        character_image=pyglet.resource.image("sprite_alpha.png")
        character=pyglet.sprite.Sprite(img=character_image,
                                       x=world.width//2,y=world.height//2)
        #These lines of code clears the screen and puts the specified objects onto
        #the screen
        @world.event
        def on_draw():
            world.clear()
            character.draw()
#These lines of code work with the button inputs. When a specific key on the keyboard has
            #been pressed, a specific action will be carried out (if any)
        @world.event
        def on_key_press(symbol, modifier):
#all proceeding lines of code will deal with character movement based on specific keyboard
            #inputs

            if symbol==key.A or symbol==key.LEFT:
                if character.x!=0:
                    character.x-=20
                else:
                    pass
                
            if symbol==key.S or symbol==key.DOWN:
                if character.y!=0:
                    character.y-=20
                else:
                    pass

            if symbol==key.D or symbol==key.RIGHT:
                if character.x!=world.width:
                    character.x+=20
                else:
                    pass

            if symbol==key.W or symbol==key.UP:
                if character.y!=world.height:
                    character.y+=20
                else:
                    pass

#These lines of code close the window after making it invisible to the user (temporary
                #emergency exit from the program
            if symbol==key.ESCAPE:
                world.set_visible(False)
                quit()
#These lines of code make the screen visible to the user and runs the pyglet code
        world.set_visible(True)
        pyglet.app.run()

#This line of code runs the Main_game class, which basically starts the game
Main_game()
