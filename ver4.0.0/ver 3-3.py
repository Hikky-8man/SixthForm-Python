#This ver is just putting all of the seperate screens in ver 3-1 onto one screen

import pyglet
from pyglet.window import key
from pyglet.window import mouse
import random
from tkinter import *
import time

#-----------------------------------------MONSTER CLASS-------------------------------------
class Items():
    def __init__(self):
        """self.health_potion_small=pyglet.image.load("assets\items\health_potion_;small_beta.png")
        self.mp_potion_small=pyglet.image.load("assets\items\mp_potion_small_beta.png")
        self.defence_boost_small=pyglet.image.load("assets\items\defence_boost_small_beta.png")
        self.attack_boost_small=pyglet.image.load("assets\items\attack_boost_small_beta.png")"""
    def get_effect(self,name):
        if name=="health_potion_small":
            return 10
        elif name=="mp_potion_small":
            return 10
        elif name=="defence_potion_small":
            return 10
        elif name=="attack_potion_small":
            return 10
    def get_attack_boost_image(self,flag):
        if flag==1:
            attack_boost_small=pyglet.image.load("assets\items\attack_boost_small_beta.png")
            return self.attack_boost_small
    def get_defence_boost_image(self,flag):
        if flag==1:
            defence_boost_small=pyglet.image.load("assets\items\defence_boost_small_beta.png")
            return self.defence_boost_small
    def get_health_potion_image(self,flag):
        if flag==1:
            health_potion_small=pyglet.image.load("assets\items\health_potion_;small_beta.png")
            return self.health_potion_small
    def get_mp_potion_image(self,flag):
        if flag==1:
            mp_potion_small=pyglet.image.load("assets\items\mp_potion_small_beta.png")
            return self.mp_potion_small
    
        
        
#This class handles everything to do with the monsters within the game
class Monster():
    def __init__(self,sprite_no):
        self.sprite_no=sprite_no
        
    #This meathod just gets the monster sprite and returns the sprite itself
    def get_monster_image(self,flag):
        if flag==1 or flag=="Monster1\n\
":
            monster_image=pyglet.image.load("sprites/monsters/monster_alpha_1.png")
            self.monster=pyglet.sprite.Sprite(img=monster_image,x=500,y=500)
            return self.monster
        
        if flag==2 or flag=="Monster2\n\
":
            monster_image=pyglet.image.load("sprites/monsters/monster_alpha_2.png")
            self.monster=pyglet.sprite.Sprite(img=monster_image,x=500,y=500)
            return self.monster
        
        if flag==3 or flag=="Monster3\n\
":
            monster_image=pyglet.image.load("sprites/monsters/monster_alpha_3.png")
            self.monster=pyglet.sprite.Sprite(img=monster_image,x=500,y=500)
            return self.monster
    #This meathod just returns the name of the monster that the user is using 
    def get_monster_name(self,flag):
        if flag==1:
            return "Monster1"
        elif flag==2:
            return "Monster2"
        elif flag==3:
            return "Monster3"
    
    #This meathod just gets and returns the health of the relevant monster    
    def get_monster_health(self,monster):
        def get_file(flag):
            if flag=="Monster1\n\
":
                file=open("monsters data\monster 1.txt","r")
            elif flag=="Monster2\n\
":
                file=open("monsters data\monster 2.txt","r")
            elif flag=="Monster3\n\
":
                file=open("monsters data/monster 3.txt","r")
            return file
        
        file=get_file(monster)
        count=0
        monster_health=0
        for line in file:
            count+=1
            if count==2:
                monster_health=int(line)
        return monster_health
                          
        
    
    #This meathod gets and returns the attacks of the relevant monster
    def get_monster_attacks(self,monster,attacks):
        self.monster=monster
        self.attacks=attacks
        if self.monster=="Monster1" or self.monster=="Monster1\n\
":
            file=open("monsters data/monster 1.txt","r")
        elif self.monster=="Monster2" or self.monster=="Monster2\n\
":
            file=open("monsters data/monster 2.txt","r")
        elif self.monster=="Monster3" or self.monster=="Monster3\n\
":
            file=open("monsters data/monster 3.txt","r")
        
        line_count=0
        for line in file:
            line_count+=1
            if line_count>3 and line_count<7:
                self.attacks.append(line)
        file.close()
        #print ("get monster attacks:",self.attacks)
        return self.attacks

#This class stores all the attacks in the game
class Attack():
    def __init__(self):
        self.damage=None
        self.name=None

    def catalogue(self,name):
        self.name=name

        if self.name=="scortch\n\
":
            self.damage=10
            return self.damage
        elif self.name=="burn\n\
":
            return 8
        elif self.name=="incinerate\n\
":
            return 15
        elif self.name=="cremate\n\
":
            return 20
        elif self.name=="flambe\n\
":
            return 5
        elif self.name=="cut\n\
":
            return 8
        elif self.name=="blizard\n\
":
            return 10
        elif self.name=="avalanche\n\
":
            return 15
        elif self.name=="freeze\n\
":
            return 5
        elif self.name=="ice age\n\
":
            return 20
        elif self.name=="iceicle\n\
":
            return 8
        elif self.name=="gust\n\
":
            return 8
        elif self.name=="wind sythe\n\
":
            return 15
        elif self.name=="sky wall\n\
":
            return 0
        elif self.name=="heal\n\
":
            return -10
        

#----------------------------------------ENEMY CLASS----------------------------------------
#This class will be used for boss battles, which will be different to regular battles 
class Enemy():
    def __init__(self,sprite_no):
        self.sprite_no=sprite_no#

    #These will be the getter meathods for the class
    def get_enemy_1(self):
        enemy_image=pyglet.image.load("sprites\enemy\enemy_alpha.png")
        self.enemy=pyglet.sprite.Sprite(img=enemy_image,
                                    x=100,y=500)
        self.enemy_health=50
        return self.enemy
    

    def get_enemy_2(self):
        enemy_image=pyglet.image.load("sprites\enemy\enemy_alpha_2.png")
        self.enemy=pyglet.sprite.Sprite(img=enemy_image,
                                    x=100,y=500)
        self.enemy_health=70
        return self.enemy
    
    def get_enemy_3(self):
        enemy_image=pyglet.image.load("sprites\enemy\enemy_alpha_3.png")
        self.enemy=pyglet.sprite.Sprite(img=enemy_image,
                                    x=100,y=500)
        self.enemy_health=100
        return self.enemy

    #This will get the health for each boss
    def get_enemy_health(self,enemy_no):
        if enemy_no==1:
            return 50
        elif enemy_no==2:
            return 70
        elif enemy_no==3:
            return 100
    
#-----------------------------------------SHOP CLASS----------------------------------------
#This class will handle everything to do with the shop, with the only exception being the
#method which displays the shop on the screen
class Shop():
    def __init__(self,map_no):

        self.map_no=map_no
        self.building_minimap_image=pyglet.image.load("assets/shop/building_mini_map.png")
        self.building_image=pyglet.image.load("assets/shop/building.png")
        
    #This method gets and returns the relevant assets for the shop
    def get_shop_sprite(self):
        
        if self.map_no==1:
            self.door_sprite=pyglet.sprite.Sprite(img=self.building_image,
                                                  x=680,y=140)
            return self.door_sprite

        elif self.map_no==2:
            self.door_sprite=pyglet.sprite.Sprite(img=self.building_image,
                                                  x=120,y=700)
            return self.door_sprite

        elif self.map_no==3:
            self.door_sprite=pyglet.sprite.Sprite(img=self.building_image,
                                                  x=700,y=700)
            return self.door_sprite

        elif self.map_no==4:
            self.door_sprite=pyglet.sprite.Sprite(img=self.building_image,
                                                  x=700,y=140)
            return self.door_sprite

    #These methods get the image for the shop (to be displayed on the minimap) 
    def get_shop_sprite_minimap_1(self):
        self.shop_minimap=pyglet.sprite.Sprite(img=self.building_minimap_image,
                                                   x=84,y=757)
        return self.shop_minimap
        
    def get_shop_sprite_minimap_2(self):
        self.shop_minimap=pyglet.sprite.Sprite(img=self.building_minimap_image,
                                                   x=6,y=785)
            
        return self.shop_minimap
    def get_shop_sprite_minimap_3(self):
        self.shop_minimap=pyglet.sprite.Sprite(img=self.building_minimap_image,
                                                   x=35,y=735)
        return self.shop_minimap
        
    def get_shop_sprite_minimap_4(self):
        self.shop_minimap=pyglet.sprite.Sprite(img=self.building_minimap_image,
                                                   x=85,y=707)
        return self.shop_minimap


#------------------------------------------CHARACTER CLASS----------------------------------
#This class will handle everything to do with the character
#creates a class called Character
class Character():
    #This is the initiator of the class, containing the iitial coordinates for the sprite
    def __init__(self,charx,chary,map_charx,map_chary):
        #These two lines intergrate the charx and chary variables into the object itself
        self.charx=charx
        self.chary=chary
        self.map_charx=map_charx
        self.map_chary=map_chary
        #This gets the image for the sprite
        sprite_image=pyglet.image.load("sprites\character\sprite_alpha.png")
        #This creates the sprite and sets it as an object
        self.sprite=pyglet.sprite.Sprite(img=sprite_image,x=self.charx,y=self.chary)

        map_sprite_image=pyglet.image.load("sprites\character\map_sprite_alpha.png")
        self.map_sprite=pyglet.sprite.Sprite(img=map_sprite_image,
                                             x=self.map_charx,y=self.map_chary)
    #This meathod just returns the sprite (so it can be drawn onto the screen)
    def get_sprite(self):
        return self.sprite
    def get_map_sprite(self):
        return self.map_sprite

#----------------------------------------------------------GAME CLASS-------------------------------------------
#This class will handle everything that the user is going to see, and all of the imediate
#background tasks
class Game():
    #This method generates all of the assets that the majority of methods are going to need
    #9more efficient than assigning each and every time a mea=thod is triggered)
    def __init__(self,map_no,charx,chary,map_charx,map_chary,monster1,monster2,monster3,
                 exp,currency,level,inventory):
        #This creates a 500 by 500screen
        self.window=pyglet.window.Window(800,800)

        pause_menu_image=pyglet.image.load("assets/menu/menu.png")
        self.pause_menu=pyglet.sprite.Sprite(img=pause_menu_image,x=700,y=750)
        
        self.map_no=map_no
        
        self.charx=charx
        self.chary=chary
        
        self.map_charx=map_charx
        self.map_chary=map_chary
        
        self.monster1=monster1
        self.monster2=monster2
        self.monster3=monster3

        self.exp=exp
        self.currency=currency
        self.level=level

        #MAP METHODS
        #self.char_build= Character(self.charx,self.chary,self.map_charx,self.map_chary)
        #self.shop_build=Shop(map_no)
        #self.combat_build(map_no)

        #COMBAT METHODS
        #self.enemy_build=Enemy(map_no)
        #self.monster_build=Monster(map_no)
        self.attack_build=Attack()

        self.inventory=inventory

        self.item_build=Items()
#------------------------------------------------------------MAP1------------------------------------------------
    #This method handles everything that is going to happen on map1     
    def load_map1_screen(self,charx,chary,map_charx,map_chary):
        self.map_no=1

        self.charx=charx
        self.chary=chary

        self.map_charx=map_charx
        self.map_chary=map_chary
        
        #This command changes the name of the variable self.window, to window, allowing
        #pyglets event handlers to work, allowing me to put the game onto one screen
        window=self.window

        self.char_build=Character(self.charx,self.chary,self.map_charx,self.map_chary)
        self.shop_build=Shop(1)

        exp_label=pyglet.text.Label("EXP:"+str(self.exp),
                                    x=210,y=770,
                                    font_size=20)

        currency_label=pyglet.text.Label("CURRENCY:"+str(self.currency),
                                         x=400,y=770,
                                         font_size=20)
        level_label=pyglet.text.Label("LEVEL:"+str(self.level),
                                      x=210,y=720,
                                      font_size=20)

        #This method draws things onto the window
        @window.event
        def on_draw():
            window.clear()
            #This gets the sprite from the Chaarcter class
            self.char1=self.char_build.get_sprite()
            #This places the character sprite onto the screen
            self.char1.draw()
            #THis creates the sprite that will be on the mini-map
            self.map_char1=self.char_build.get_map_sprite()
            self.map_char1.draw()

            self.shop=self.shop_build.get_shop_sprite()
            self.shop.draw()
            
            self.shop_minimap_1=self.shop_build.get_shop_sprite_minimap_1()
            self.shop_minimap_2=self.shop_build.get_shop_sprite_minimap_2()
            self.shop_minimap_3=self.shop_build.get_shop_sprite_minimap_3()
            self.shop_minimap_4=self.shop_build.get_shop_sprite_minimap_4()
            
            self.shop_minimap_1.draw()
            self.shop_minimap_2.draw()
            self.shop_minimap_3.draw()
            self.shop_minimap_4.draw()
            
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,700,0,700)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,795,95,700)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(50,795,50,700)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,750,0,750)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,795,0,795)))

            self.pause_menu.draw()

            exp_label.draw()
            currency_label.draw()
            level_label.draw()
            
            
        self.engage=random.randrange(0,20)
        
        @window.event
        def on_key_press(symbol,modifier):
            if symbol==key.I:
                self.load_inventory_screen()
        #This handles all of the arrow key inputs (so the user can hold the key instead of
        #continuously pressing the alphabetical keys to move one step at a time        
        @window.event
        #This function handles events when a key is pressed once
        def on_text_motion(motion):

            #This dictates what happens when the specified key is presses (applies to all
            #simmilar instances of this line of code)
            if (motion==key.MOTION_LEFT):

                #These lines of code create a boundary which if crossed, causes the program
                #to switch classes, which switches maps
                if self.char1.x<20:
                    #This triggers the class
                    self.load_map2_screen(680,self.chary,34,self.map_chary)

                #The else command is not needed, but is there becasue it is standard to place
                #else or elif following the use of if
                else:
                    encounter=random.randrange(0,30)
                    if encounter==self.engage:
                        self.load_combat_screen()
                    else:
                    #These lines of code move the character, and save the character
                    #coordinates (for future use)
                        self.char1.x-=20
                        self.charx-=20
                        self.map_char1.x-=1
                        self.map_charx-=1

            if (motion==key.MOTION_RIGHT):
                #This function handles the actual barriers of the screen. The pass statement
                #eans nothing happens, meaning that the sprite does not move (in this context
                if self.char1.x>680:
                    pass
                else:
                    if self.char1.x==580:
                        if self.char1.y>70 and self.char1.y<200:
                            self.load_shop_screen()
                            
                    else:
                        encounter=random.randrange(0,30)
                        if encounter==self.engage:
                            self.load_combat_screen()
                        
                    self.char1.x+=20
                    self.charx+=20
                    self.map_char1.x+=1
                    self.map_charx+=1

            if (motion==key.MOTION_UP):
                if self.char1.y==680:
                    pass
                else:
                    if self.char1.y==40:
                        if self.char1.x>610 and self.char1.x<750:
                            self.char1.y-=20
                            self.chary-=20
                            self.map_char1.y-=1
                            self.map_chary-=1
                    else:
                        encounter=random.randrange(0,30)
                        if encounter==self.engage:
                            self.load_combat_screen()
                        
                    self.char1.y+=20
                    self.chary+=20
                    self.map_char1.y+=1
                    self.map_chary+=1

            if (motion==key.MOTION_DOWN):

                if self.char1.y<20:
                    self.load_map4_screen(self.charx,680,self.map_charx,734)

                else:
                    
                    if self.char1.y==240:
                        if self.char1.x>610 and self.char1.x<750:
                            self.char1.y+=20
                            self.chary+=20
                            self.map_char1.y+=1
                            self.map_chary+=1
                    else:
                        encounter=random.randrange(0,30)
                        if encounter==self.engage:
                            self.load_combat_screen()
                        
                    self.char1.y-=20
                    self.chary-=20
                    self.map_char1.y-=1
                    self.map_chary-=1
        @window.event
        def on_mouse_press(x,y,button,modifier):
            if button==mouse.LEFT:
                if x>700 and y<800:
                    if x<800 and y<800:
                        if x>700 and y>750:
                            if x<800 and y>750:
                                self.load_menu_screen()
#--------------------------------------MENU-------------------------------------------
    #This method handles everything in the pause menu 
    def load_menu_screen(self):
        window=self.window
        quit_button_image=pyglet.image.load("assets/menu/quit_button.png")
        self.quit_button=pyglet.sprite.Sprite(img=quit_button_image,
                                                          x=0,y=600)
        #This function is the function that does the actual saving by writing all the
        #relevant data in the relevant places
        def save():
            file=open("save files/save file.txt","w")
            count=0
            while count!=13:
                count+=1
                if count==1:
                    file.write(str(self.map_no)+"\n")
                if count==2:
                    file.write(str(self.charx)+"\n")
                if count==3:
                    file.write(str(self.chary)+"\n")
                if count==4:
                    file.write(str(self.map_charx)+"\n")
                if count==5:
                    file.write(str(self.map_chary)+"\n")
                if count==6:
                    file.write(str(self.monster1))
                if count==7:
                    file.write(str(self.monster2))
                if count==8:
                    file.write(str(self.monster3))
                if count==9:
                    file.write(str(self.exp)+"\n")
                if count==10:
                    file.write(str(self.currency)+"\n")
                if count==11:
                    file.write(str(self.level)+"\n")
                if count==12:
                    file.write(str(self.inventory)+"\n")
            file.close()
                    
        @window.event
        def on_draw():
            window.clear()
            self.quit_button.draw()
            self.label=pyglet.text.Label("right click to exit the pause menu",
                                         x=100,y=400,
                                         font_size=30).draw()
        #This method handles all of the mouse inputs when the mouse is clicked
        @window.event
        def on_mouse_press(x,y,button,modifier):
            if button==mouse.LEFT:
                #This creates a box type input, where when the mouse is clicked, if all
                #of these inequalities are satisfied, the specified outcome will trigger
                #print ("x: "+str(x)+" y: "+str(y))
                if x>0 and y<800:
                    if x>0 and y>600:
                        if x<500 and y>600:
                            if x<500 and y<800:
                                print ("Saved")
                                save()
                                #This closes/kills the program
                                quit()
            if button==mouse.RIGHT:
                if self.map_no==1:
                    self.load_map1_screen(self.charx,self.chary,self.map_charx,
                                              self.map_chary)
                elif self.map_no==2:
                    self.load_map2_screen(self.charx,self.chary,self.map_charx,
                                              self.map_chary)
                elif self.map_no==3:
                    self.load_map3_screen(self.charx,self.chary,self.map_charx,
                                              self.map_chary)
                else:
                    self.load_map4_screen(self.charx,self.chary,self.map_charx,
                                              self.map_chary)
                                
                        
#------------------------------------------------------------MAP2------------------------------------------------

            
    def load_map2_screen(self,charx,chary,map_charx,map_chary):
        window=self.window

        self.charx=charx
        self.chary=chary

        self.map_charx=map_charx
        self.map_chary=map_chary

        self.map_no=2

        self.char_build=Character(self.charx,self.chary,self.map_charx,self.map_chary)
        self.shop_build=Shop(2)

        exp_label=pyglet.text.Label("EXP:"+str(self.exp),
                                    x=210,y=770,
                                    font_size=20)

        currency_label=pyglet.text.Label("CURRENCY:"+str(self.currency),
                                         x=400,y=770,
                                         font_size=20)
        
        level_label=pyglet.text.Label("LEVEL:"+str(self.level),
                                      x=210,y=720,
                                      font_size=20)

        @window.event
        def on_draw():
            window.clear()
            
            self.char1=self.char_build.get_sprite()
            self.char1.draw()
            
            self.map_char1=self.char_build.get_map_sprite()
            self.map_char1.draw()
            
            self.shop=self.shop_build.get_shop_sprite()
            self.shop.draw()
            
            self.shop_minimap_1=self.shop_build.get_shop_sprite_minimap_1()
            self.shop_minimap_2=self.shop_build.get_shop_sprite_minimap_2()
            self.shop_minimap_3=self.shop_build.get_shop_sprite_minimap_3()
            self.shop_minimap_4=self.shop_build.get_shop_sprite_minimap_4()
            
            self.shop_minimap_1.draw()
            self.shop_minimap_2.draw()
            self.shop_minimap_3.draw()
            self.shop_minimap_4.draw()
            
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,700,0,700)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,795,95,700)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(50,795,50,700)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,750,0,750)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,795,0,795)))
            
            self.pause_menu.draw()

            exp_label.draw()
            currency_label.draw()
            level_label.draw()
            
        self.engage=random.randrange(0,20)

        @window.event
        def on_key_press(symbol,modifier):
            if symbol==key.I:
                self.load_inventory_screen()
        
        @window.event
        def on_text_motion(motion):
            if (motion==key.MOTION_LEFT):
                if self.char1.x==0:
                    pass
                else:
                    if self.char1.x==220:
                        if self.char1.y>670 and self.char1.y<770:
                            self.char1.x+=20
                            self.charx+=20
                            self.map_char1.x+=1
                            self.map_charx+=1
                    else:
                        encounter=random.randrange(0,20)
                        if encounter==self.engage:
                            self.load_combat_screen()
                        
                    self.char1.x-=20
                    self.charx-=20
                    self.map_char1.x-=1
                    self.map_charx-=1
                    
            elif (motion==key.MOTION_RIGHT):
                if self.char1.x>680:
                    self.load_map1_screen(20,self.chary,51,self.map_chary)
                    
                else:
                    if self.char1.x==20:
                        if self.char1.y>650 and self.char1.y<750:
                            self.char1.x-=20
                            self.charx-=20
                            self.map_char1.x-=1
                            self.map_charx-=1
                    else:
                        encounter=random.randrange(0,20)
                        if encounter==self.engage:
                            self.load_combat_screen()
                        
                    self.char1.x+=20
                    self.charx+=20
                    self.map_char1.x+=1
                    self.map_charx+=1
                    
            elif (motion==key.MOTION_UP):
                if self.char1.y==600:
                    if self.char1.x>40 and self.char1.x<180:
                        self.load_shop_screen()
                        
                if self.char1.y==680:
                    pass
                else:
                    if self.char1.y==600:
                        if self.char1.x>70 and self.char1.x<170:
                            self.char1.y-=20
                            self.chary-=20
                            self.map_char1.y-=1
                            self.map_chary-=1
                    else:
                        encounter=random.randrange(0,20)
                        if encounter==self.engage:
                            self.load_combat_screen()
                        
                    self.char1.y+=20
                    self.chary+=20
                    self.map_char1.y+=1
                    self.map_chary+=1
            elif (motion==key.MOTION_DOWN):
                if self.char1.y<20:
                    self.load_map3_screen(self.charx,680,self.map_charx,734)
                else:
                    encounter=random.randrange(0,20)
                    if encounter==self.engage:
                        self.load_combat_screen()
                    
                self.char1.y-=20
                self.chary-=20
                self.map_char1.y-=1
                self.map_chary-=1
        @window.event
        def on_mouse_press(x,y,button,modifier):
            if button==mouse.LEFT:
                if x>700 and y<800:
                    if x<800 and y<800:
                        if x>700 and y>750:
                            if x<800 and y>750:
                                self.load_menu_screen()
#------------------------------------------------------------MAP3------------------------------------------------

                
    def load_map3_screen(self,charx,chary,map_charx,map_chary):
        window=self.window

        self.charx=charx
        self.chary=chary

        self.map_charx=map_charx
        self.map_chary=map_chary

        self.map_no=3

        self.char_build=Character(self.charx,self.chary,self.map_charx,self.map_chary)
        self.shop_build=Shop(3)

        exp_label=pyglet.text.Label("EXP:"+str(self.exp),
                                    x=210,y=770,
                                    font_size=20)

        currency_label=pyglet.text.Label("CURRENCY:"+str(self.currency),
                                         x=400,y=770,
                                         font_size=20)

        level_label=pyglet.text.Label("LEVEL:"+str(self.level),
                                      x=210,y=720,
                                      font_size=20)

        @window.event
        def on_draw():
            window.clear()
            #This gets the sprite from the Chaarcter class
            self.char1=self.char_build.get_sprite()
            #This places the character sprite onto the screen
            self.char1.draw()
            #THis creates the sprite that will be on the mini-map
            self.map_char1=self.char_build.get_map_sprite()
            self.map_char1.draw()

            self.shop=self.shop_build.get_shop_sprite()
            self.shop.draw()
            
            self.shop_minimap_1=self.shop_build.get_shop_sprite_minimap_1()
            self.shop_minimap_2=self.shop_build.get_shop_sprite_minimap_2()
            self.shop_minimap_3=self.shop_build.get_shop_sprite_minimap_3()
            self.shop_minimap_4=self.shop_build.get_shop_sprite_minimap_4()
            
            self.shop_minimap_1.draw()
            self.shop_minimap_2.draw()
            self.shop_minimap_3.draw()
            self.shop_minimap_4.draw()
            
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,700,0,700)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,795,95,700)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(50,795,50,700)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,750,0,750)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,795,0,795)))

            self.pause_menu.draw()

            exp_label.draw()
            currency_label.draw()
            level_label.draw()

        self.engage=random.randrange(0,20)

        @window.event
        def on_key_press(symbol,modifier):
            if symbol==key.I:
                self.load_inventory_screen()

        @window.event
        def on_text_motion(motion):

            if (motion==key.MOTION_LEFT):
                if self.char1.x<20:
                    pass
                else:
                    encounter=random.randrange(0,30)
                    if encounter==self.engage:
                        self.load_combat_screen()
                    
                self.char1.x-=20
                self.charx-=20
                self.map_charx-=1
                self.map_char1.x-=1
                
            elif (motion==key.MOTION_RIGHT):
                
                if self.char1.x>680:
                    self.load_map4_screen(20,self.chary,51,self.map_chary)

                else:
                    if self.char1.x==600:
                        if self.char1.y>650 and self.char1.y<750:
                            self.load_shop_screen()
                            
                    else:
                        encounter=random.randrange(0,30)
                        if encounter==self.engage:
                            self.load_combat_screen()
                    self.char1.x+=20
                    self.charx+=20
                    self.charx+=1
                    self.map_char1.x+=1
                
            elif (motion==key.MOTION_UP):

                if self.char1.y>680:
                    self.load_map2_screen(self.charx,20,self.map_charx,751)

                else:
                    if self.char1.y==600:
                        if self.char1.x>650 and self.char1.x<750:
                            self.char1.y-=20
                            self.chary-=20
                            self.map_char1.y-=1
                            self.map_chary-=1
                        else:
                            encounter=random.randrange(0,30)
                            if encounter==self.engage:
                                self.load_combat_screen()
                    self.char1.y+=20
                    self.chary+=20
                    self.map_chary+=1
                    self.map_char1.y+=1

            elif (motion==key.MOTION_DOWN):
                if self.char1.y<20:
                    pass
                else:
                    encounter=random.randrange(0,30)
                    if encounter==self.engage:
                        self.load_combat_screen()
                self.char1.y-=20
                self.chary-=20
                self.map_char1.y-=1
                self.map_chary-=1
        @window.event
        def on_mouse_press(x,y,button,modifier):
            if button==mouse.LEFT:
                if x>700 and y<800:
                    if x<800 and y<800:
                        if x>700 and y>750:
                            if x<800 and y>750:
                                self.load_menu_screen()
#------------------------------------------------------------MAP4------------------------------------------------


    def load_map4_screen(self,charx,chary,map_charx,map_chary):
        window=self.window

        self.charx=charx
        self.chary=chary

        self.map_charx=map_charx
        self.map_chary=map_chary

        self.char_build=Character(self.charx,self.chary,self.map_charx,self.map_chary)
        self.shop_build=Shop(4)

        exp_label=pyglet.text.Label("EXP:"+str(self.exp),
                                    x=210,y=770,
                                    font_size=20)

        currency_label=pyglet.text.Label("CURRENCY:"+str(self.currency),
                                         x=400,y=770,
                                         font_size=20)

        level_label=pyglet.text.Label("LEVEL:"+str(self.level),
                                      x=210,y=720,
                                      font_size=20)

        @window.event
        def on_draw():
            window.clear()
            #This gets the sprite from the Chaarcter class
            self.char1=self.char_build.get_sprite()
            #This places the character sprite onto the screen
            self.char1.draw()
            #THis creates the sprite that will be on the mini-map
            self.map_char1=self.char_build.get_map_sprite()
            self.map_char1.draw()

            self.shop=self.shop_build.get_shop_sprite()
            self.shop.draw()
            
            self.shop_minimap_1=self.shop_build.get_shop_sprite_minimap_1()
            self.shop_minimap_2=self.shop_build.get_shop_sprite_minimap_2()
            self.shop_minimap_3=self.shop_build.get_shop_sprite_minimap_3()
            self.shop_minimap_4=self.shop_build.get_shop_sprite_minimap_4()
            
            self.shop_minimap_1.draw()
            self.shop_minimap_2.draw()
            self.shop_minimap_3.draw()
            self.shop_minimap_4.draw()
            
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,700,0,700)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,795,95,700)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(50,795,50,700)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,750,0,750)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(95,795,0,795)))

            self.pause_menu.draw()

            exp_label.draw()
            currency_label.draw()
            level_label.draw()

        self.engage=random.randrange(0,20)

        @window.event
        def on_key_press(symbol,modifier):
            if symbol==key.I:
                self.load_inventory_screen()
        
        @window.event
        def on_text_motion(motion):
            
            if (motion==key.MOTION_LEFT):

                if self.char1.x<20:
                    self.load_map3_screen(680,self.chary,34,self.map_chary)

                else:
                    encounter=random.randrange(0,30)
                    if encounter==self.engage:
                        self.load_combat_screen()
                self.char1.x-=20
                self.charx-=20
                self.map_char1.x-=1
                self.map_charx-=1

            elif (motion==key.MOTION_RIGHT):
                if self.char1.x>680:
                    pass
                else:
                    if self.char1.x==600:
                        if self.char1.y>90 and self.char1.y<190:
                            self.char1.x-=20
                            self.charx-=20
                            self.map_char1.x-=1
                            self.map_charx-=1
                    else:
                        encounter=random.randrange(0,30)
                        if encounter==self.engage:
                            self.load_combat_screen()
                    self.char1.x+=20
                    self.charx+=20
                    self.map_char1.x+=1
                    self.map_charx+=1

            elif (motion==key.MOTION_UP):

                if self.char1.y>680:
                    self.load_map1_screen(self.charx,20,self.map_charx,751)

                else:
                    if self.char1.y==40:
                        if self.char1.x>650 and self.char1.x<750:
                            self.char1.y-=20
                            self.chary-=20
                            self.map_char1.y-=1
                            self.map_chary-=1
                    else:
                        encounter=random.randrange(0,30)
                        if encounter==self.engage:
                            self.load_combat_screen()
                    self.char1.y+=20
                    self.chary+=20
                    self.map_char1.y+=1
                    self.map_chary+=1

            elif (motion==key.MOTION_DOWN):
                if self.char1.y<20:
                    pass
                else:
                    if self.char1.y==240:
                        if self.char1.x>650 and self.char1.x<750:
                           self.load_shop_screen()
                    else:
                        encounter=random.randrange(0,30)
                        if encounter==self.engage:
                            self.load_combat_screen()
                    self.char1.y-=20
                    self.chary-=20
                    self.map_char1.y-=1
                    self.map_chary-=1
        @window.event
        def on_mouse_press(x,y,button,modifier):
            if button==mouse.LEFT:
                if x>700 and y<800:
                    if x<800 and y<800:
                        if x>700 and y>750:
                            if x<800 and y>750:
                                self.load_menu_screen()
#-----------------------------------------------COMBAT------------------------------------

    def load_combat_screen(self):
        window=self.window

        self.enemy_build=Enemy(1)
        self.monster_build=Monster(1)

        self.turn=True

        if self.level==0:
            self.mp=50
            self.cap=self.mp
        else:
            self.mp=self.level*100
            self.cap=self.mp
        self.monster1_health=None
        self.monster2_health=None
        self.monster3_health=None
        self.attacks=[]
        self.Type=None
        self.attack=None
        self.defence=None
        self.monster=None
        self.movelist=False
        self.attack_enemy=""
        self.multiplier=0
        self.text=1

        self.current_monster=1

        self.removed_monster=None

        self.monster_switch=False

        self.defeat=False

        self.switch1=False
        self.switch2=False

        self.selected_monster=[self.monster1,self.monster2,self.monster3]

        self.enemy_attack_name=pyglet.text.Label(""
                                                 +self.attack_enemy,
                                                 x=0,y=450,
                                                 font_size=20)
                                            
                
        self.run=pyglet.text.Label("RUN",
                                   x=600,
                                   y=90,
                                   anchor_x="center",
                                   anchor_y="center",
                                   font_size=50)
        self.attack=pyglet.text.Label("ATTACK",
                                      x=200,
                                      y=235,
                                      anchor_x="center",
                                      anchor_y="center",
                                      font_size=50)
        self.item=pyglet.text.Label("ITEM",
                                    x=200,
                                    y=85,
                                    anchor_x="center",
                                    anchor_y="center",
                                    font_size=50)
        self.capture=pyglet.text.Label("MONSTERS",
                                       x=600,
                                       y=240,
                                       anchor_x="center",
                                       anchor_y="center",
                                       font_size=50)
        self.mp_text=pyglet.text.Label("MP:"+str(self.mp)+"/"+str(self.cap),
                                       x=550,
                                       y=750,
                                       font_size=30)

        self.pick_enemy=random.randrange(1,4)

        self.enemy=None
        self.enemy_health=None
        
        def get_enemy(pick_enemy):
            self.enemy=self.monster_build.get_monster_image(pick_enemy)
            self.enemy.x=100
            self.enemy.y=500
            self.enemy_health=self.enemy_build.get_enemy_health(pick_enemy)
            self.multiplier=self.enemy_health/10


        get_enemy(self.pick_enemy)
        """self.monster=get_monster(1)"""
        #monster_image=pyglet.image.load("sprites\monsters\monster_alpha_1.png")
        #self.monster=pyglet.sprite.Sprite(img=monster_image,x=500,y=500)
        def get_monster(current_monster):
            if self.current_monster==1:
                monster=self.monster_build.get_monster_image(self.monster1)
            elif self.current_monster==2:
                monster=self.monster_build.get_monster_image(self.monster2)
            else:
                monster=self.monster_build.get_monster_image(self.monster3)
            if self.current_monster==1:
                self.selected_monster=[self.monster2,self.monster3]
            elif self.current_monster==2:
                self.selected_monster=[self.monster1,self.monster3]
            else:
                self.selected_monster=[self.monster1,self.monster2]
            #count=0

            return monster
        
        def get_monster_health_first(current_monster):
            monster_health=10
            if current_monster==1:
                monster_health=self.monster_build.get_monster_health(self.monster1)
            elif current_monster==2:
                monster_health=self.monster_build.get_monster_health(self.monster2)
            else:
                monster_health=self.monster_build.get_monster_health(self.monster3)
            return monster_health
        
        def get_monster_health(current_monster):
            health=None
            if current_monster==1:
                health=self.monster1_health
            elif current_monster==2:
                health=self.monster2_health
            else:
                health=self.monster3_health
            print (str(health))
            return health

        self.monster1_health=get_monster_health_first(1)
        self.monster2_health=get_monster_health_first(2)
        self.monster3_health=get_monster_health_first(3)
        
        self.monster_health=get_monster_health(self.current_monster)
        self.monster=get_monster(self.current_monster)

        @window.event
        def on_draw():
            window.clear()
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(400,0,400,800)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(0,300,800,300)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,(
                "v2i",(0,150,800,150)))
            self.enemy_health_text=pyglet.text.Label("HP: "+str(self.enemy_health),
                                                x=150,y=350,
                                                font_size=30)
            self.user_health_text=pyglet.text.Label("HP: "+str(self.monster_health),
                                                    x=500,y=350,
                                                    font_size=30)
            
            self.user_health_text.draw()
            self.enemy_health_text.draw()
            self.run.draw()
            self.attack.draw()
            self.item.draw()
            self.capture.draw()
            self.enemy.draw()
            self.monster.draw()
            self.enemy_attack_name.draw()
            self.mp_text.draw()
            
        
        self.up=True

        @window.event
        def on_update(dt):
            if self.up==True:
                self.monster.y+=5
                self.enemy.y-=5
                self.up=False

            elif self.up==False:
                self.monster.y-=5
                self.enemy.y+=5
                self.up=True
        pyglet.clock.schedule_interval(on_update,1.5)
        
        @window.event
        def update(dt):
            if self.text==1:
                self.attack.text="ATTACK"
                self.capture.text="MONSTERS"
                self.item.text="ITEM"
                self.run.text="RUN"
                
            elif self.text==2:
                self.attacks=[]
                self.attack.text="ACTION LIST"
                if self.current_monster==1:
                    self.monster_build.get_monster_attacks(self.monster1,
                                                                   self.attacks)
                elif self.current_monster==2:
                    self.monster_build.get_monster_attacks(self.monster2,
                                                                   self.attacks)
                else:
                    self.monster_build.get_monster_attacks(self.monster3,
                                                                   self.attacks)
                self.capture.text=self.attacks[0]
                self.item.text=self.attacks[1]
                self.run.text=self.attacks[2]
                
            elif self.text==3:
                self.attack.text="ACTION LIST"
                self.capture.text="CAPTURE"
                #if self.switch1==True or self.switch2==True:
                
                if self.current_monster==1:
                    self.item.text=str(self.monster2)
                    self.run.text=str(self.monster3)
                        #self.monster=change_slot1_monster(self.current_monster)
                        #self.monster_health=change_slot1_monster_health(self.current_monster)
                        #self.switch1=False
                elif self.current_monster==2:
                    self.item.text=str(self.monster1)
                    self.run.text=str(self.monster3)
                        #self.monster=change_slot1_monster(self.current_monster)
                        #self.monster_health=change_slot1_monster_health(self.current_monster)
                        #self.switch1=False
                    
                else:
                    self.item.text=str(self.monster1)
                    self.run.text=str(self.monster2)
                        #self.monster=change_slot2_monster(self.current_monster)
                        #self.monster_health=change_slot2_monster_health(self.current_monster)
                        #self.switch2=False
                if self.switch1==True or self.switch2==True:
                    if self.switch1==True:
                        self.monster=change_slot1_monster(self.current_monster)
                        self.monster_health=get_monster_health(self.current_monster)
                        self.monster=get_monster(self.current_monster)
                        self.switch1=False
                        print ("SLOT 1")
                    elif self.switch2==True:
                        self.monster=change_slot2_monster(self.current_monster)
                        self.monster_health=get_monster_health(self.current_monster)
                        self.monster=get_monster(self.current_monster)
                        self.switch2=False
                        print ("SLOT 2")

                    if self.current_monster==1:
                        self.attacks=[]
                        self.monster_build.get_monster_attacks(self.monster1,
                                                                   self.attacks)
                    elif self.current_monster==2:
                        self.attacks=[]
                        self.monster_build.get_monster_attacks(self.monster2,
                                                                   self.attacks)
                    else:
                        self.attacks=[]
                        self.monster_build.get_monster_attacks(self.monster3,
                                                                   self.attacks)
                    print (self.attacks)

            if self.turn==False:
                time.sleep(0.5)
                damage=self.AI_turn(self.pick_enemy)
                self.monster_health-=damage
                if self.current_monster==1:
                    self.monster1_health-=damage
                elif self.current_monster==2:
                    self.monster2_health-=damage
                else:
                    self.monster3_health-=damage
                self.turn=True
                self.enemy_attack_name.text="Enemy used the attack: "+self.attack_enemy

                self.mp+=5
                if self.mp>self.cap:
                    self.mp==self.cap
                self.mp_text.text="MP"+str(self.mp)+"/"+str(self.cap)
                
            if self.defeat==False:
                if self.monster_health<1:
                    self.defeat=True
                    self.load_game_over_screen()

                        
        pyglet.clock.schedule_interval(update,0.01)

        def change_slot1_monster(current_monster):
            monster=None
            if current_monster==1 or current_monster==3:
                current_monster=2
                monster=get_monster(2)
                print ("monster changed to 2")
            elif current_monster==2:
                current_monster=1
                monster=get_monster(1)
                print ("Monster changed to 1")
            self.current_monster=current_monster
            return monster


        def change_slot2_monster(current_monster):
            monster=None
            if current_monster==1 or current_monster==2:
                current_monster=3
                monster=get_monster(3)
                print ("monster changed to 3")
            elif current_monster==3:
                current_monster=2
                monster=get_monster(2)
                print ("monster changed to 2")
            self.current_monster=current_monster
            return monster

        @window.event
        def on_mouse_press(x,y,symbol,modifier):
            #These lines of code create a box shaped input, where only if the conditions are
            #satisfied, the event will trigger
            #attack
            if x>0 and x<400:

                if y>150 and y<300:
                    if self.text==1:
                        self.text=2
                    elif self.text==2:
                        self.text=1
                    elif self.text==3:
                        self.text=1

            #capture
            if x>400 and x<800:

                if y>150 and y<300:
                    if self.turn==True:
                        if self.text==2:
                            #if self.movelist==True:
                            #print(str(self.attack_build.catalogue(self.attacks[0])))
                            self.mp-=self.attack_build.catalogue(self.attacks[0])
                            if self.mp<0:
                                self.mp+=self.attack_build.catalogue(self.attacks[0])
                                turn=False
                            else:
                                self.enemy_health-=self.attack_build.catalogue(self.attacks[0])
                                self.mp_text.text="MP"+str(self.mp)+"/"+str(self.cap)
                                self.turn=False
                            if self.enemy_health==0 or self.enemy_health<0:        
                                self.exp+=self.multiplier
                                self.exp=int(self.exp)
                                self.load_win_screen()
                                
                        elif self.text==3:
                            print ("CAPTURE")
                        elif self.text==1:
                        #elif self.movelist==False:
                            print ("CHANGE NOW!!!")
                            #print (str(self.monster_switch))
                            self.text=3
                        elif self.text==3:
                            pass

        #items
            if x>0 and x<400:

                if y>0 and y<150:
                    if self.turn==True:
                        if self.text==3:
                            #change_slot1(self.current_monster,self.monster,self.monster_health)
                            #self.monster=change_slot1_monster(self.current_monster)
                            #self.monster_health=change_slot1_monster_health(self.current_monster)
                            self.switch1=True
                            self.turn=False
                        if self.text==2:
                        #if self.movelist==True:
                            self.mp-=self.attack_build.catalogue(self.attacks[1])
                            if self.mp<0:
                                self.mp+=self.attack_build.catalogue(self.attacks[1])
                                turn=False
                            else:
                                self.enemy_health-=self.attack_build.catalogue(self.attacks[1])
                                self.mp_text.text="MP"+str(self.mp)+"/"+str(self.cap)
                                self.turn=False

                            if self.enemy_health==0 or self.enemy_health<0:
                                print ("WIN!")
                                self.exp+=self.multiplier
                                self.exp=int(self.exp)
                                self.load_win_screen()
                                                                    
                    
                        

            #run
            if x>400 and x<800:

                if y>0 and y<150:
                    if self.turn==True:
                        if self.text==3:
                            #self.monster=change_slot2_monster(self.current_monster)
                            #self.monster_health=change_slot2_monster_health(self.current_monster)
                            self.switch2=True
                            self.turn=False

                        elif self.text==1:
                        #if self.movelist==False:

                            if self.map_no==1:
                                #Allthese lines of code do is return the sprite to where they
                                #were prior to the engagement
                                self.load_map1_screen(self.charx,self.chary,
                                                          self.map_charx,self.map_chary)
                                
                        
                            elif self.map_no==2:
                                self.load_map2_screen(self.charx,self.chary,
                                                          self.map_charx,self.map_chary)
                                
                        
                            elif self.map_no==3:
                                self.load_map3_screen(self.charx,self.chary,
                                                          self.map_charx,self.map_chary)
                                
                        
                            else:
                                self.load_map4_screen(self.charx,self.chary,
                                                          self.map_charx,self.map_chary)
                                
                        elif self.text==2:
                        #elif self.movelist==True:
                            #print (str(self.attack_build.catalogue(self.attacks[2])))
                            self.mp-=self.attack_build.catalogue(self.attacks[2])
                            if self.mp<0:
                                self.mp+=self.attack_build.catalogue(self.attacks[2])
                                turn=False
                            else:
                                self.enemy_health-=self.attack_build.catalogue(self.attacks[2])
                                self.mp_text.text="MP"+str(self.mp)+"/"+str(self.cap)
                                self.turn=False

                            if self.enemy_health==0 or self.enemy_health<0:
                                print ("WIN!")
                                self.exp+=self.multiplier
                                self.exp=int(self.exp)
                                self.load_win_screen()
                                
                            
        @window.event
        def on_mouse_motion(x,y,dx,dy):

            if x>400 and x<800:

                if y>0 and y<150:
                    #These lines of code just alter the various labels to give the suer
                    #a clear indication of which option they are on
                    self.run.font_size=60
                    self.attack.font_size=50
                    self.item.font_size=50
                    self.capture.font_size=50

            if x>0 and x<400:

                if y>150 and y<300:
                    self.run.font_size=50
                    self.attack.font_size=60
                    self.item.font_size=50
                    self.capture.font_size=50

            if x>0 and x<400:

                if y>0 and y<150:
                    self.run.font_size=50
                    self.attack.font_size=50
                    self.item.font_size=60
                    self.capture.font_size=50

            if x>400 and x<800:

                if y>150 and y<300:
                    self.run.font_size=50
                    self.attack.font_size=50
                    self.item.font_size=50
                    self.capture.font_size=60

            if y>300 or y<0:
                self.run.font_size=50
                self.attack.font_size=50
                self.item.font_size=50
                self.capture.font_size=50
#---------------------------------------AI--------------------------------------------
    def AI_turn(self,pick_enemy):
        
        def get_monster(pick_enemy):
            monster=self.monster_build.get_monster_name(pick_enemy)
            print (monster)
            return monster
        
        def get_movelist(attacks,monster):
            attacks=[]
            attacks=self.monster_build.get_monster_attacks(monster,attacks)
            print (attacks)
            return attacks
            
        monster=get_monster(pick_enemy)
        attacks=[]
        attacks=get_movelist(attacks,monster)
        pick_attack=random.randrange(1,4)
        if pick_attack==1:
            choice=self.attack_build.catalogue(attacks[0])
            print (attacks[0])
            self.attack_enemy=attacks[0]
        elif pick_attack==2:
            choice=self.attack_build.catalogue(attacks[1])
            print (attacks[1])
            self.attack_enemy=attacks[1]
        elif pick_attack==3:
            choice=self.attack_build.catalogue(attacks[2])
            #print (attacks[2])
            self.attack_enemy=attacks[2]
        choice+=10
        print (str(choice))
        return choice
#-------------------------------------INVENTORY----------------------------------------
    def load_inventory_screen(self):
        window=self.window
        
        self.items_label=pyglet.text.Label("ITEMS",
                                      x=400,y=600,
                                      anchor_x="center",
                                      anchor_y="center",
                                      font_size=80)
        
        self.monsters_label=pyglet.text.Label("MONSTERS",
                                         x=400,y=200,
                                         anchor_x="center",
                                         anchor_y="center",
                                         font_size=80)
        @window.event
        def on_draw():
            window.clear()
            self.items_label.draw()
            self.monsters_label.draw()

        @window.event
        def on_key_press(symbol,modifier):
            if symbol==key.I:
                if self.map_no==1:
                    self.load_map1_screen(self.charx,self.chary,self.map_charx,self.map_chary)
                elif self.map_no==2:
                    self.load_map2_screen(self.charx,self.chary,self.map_charx,self.map_chary)
                elif self.map_no==3:
                    self.load_map3_screen(self.charx,self.chary,self.map_charx,self.map_chary)
                else:
                    self.load_map4_screen(self.charx,self.chary,self.map_charx,self.map_chary)

        @window.event
        def on_mouse_motion(x,y,dx,dy):
            if y>400:
                self.items_label.font_size=90
                self.monsters_label.font_size=80
            elif y<400:
                self.items_label.font_size=80
                self.monsters_label.font_size=90
            elif y>800 or y<0:
                self.items_label.font_size=80
                self.monsters_label.font_size=80

        @window.event
        def on_mouse_press(x,y,symbol,modifier):
            if y>400:
                self.load_items_screen()
            elif y<400:
                self.load_monsters_screen()
#------------------------------------ITEMS---------------------------------------------
    def load_items_screen(self):
        window=self.window
        self.label=pyglet.text.Label(str(self.inventory[0]),
                                x=400,y=400)
        
        """for data in self.inventory[0]:
            if data == "health_potion_small":
                self.health_potion_small = self.inventory[0,data+1]
                print (str(self.health_potion_small))
                
            elif data == "mp_potion_small":
                self.mp_potion_small = self.inventory[0,data+1]
                print (str(self.mp_potion_small))
                
            elif data == "attack_boost_small":
                self.attack_boost_small = self.inventory[0,data+1]
                print (str(self.attack_boost_small))
                
            elif data == "defence_boost_small":
                self.defence_boost_small = self.inventory[0,data+1]
                print (str(self.defence_boost_small))"""

        #self.health_potion_small=pyglet.image.load("assets\items\health_potion_;small_beta.png")
        attack_boost_small_path="assets\items\attack_boost_small_beta.png"        
        @window.event
        def on_draw():
            window.clear()

            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,("v2i",(0,400,800,400)))

            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,("v2i",(200,0,200,800)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,("v2i",(400,0,400,800)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,("v2i",(600,0,600,800)))

            #self.health_potion_small=pyglet.image.load("assets\items\health_potion_;small_beta.png").blit(50,600)
            health_potion_small_image=pyglet.image.load("assets\items\health_potion_;small_beta.png").blit(50,600)
            mp_potion_small_image=pyglet.image.load("assets\items\mp_potion_small_beta.png").blit(250,600)
            attack_boost_small_image=pyglet.image.load(attack_boost_small_path).blit(450,600)
            defence_boost_small_image=pyglet.image.load("assets\items\defence_boost_small_beta.png").blit(650,600)
            batch.draw()
            self.label.draw()
            
            
        @window.event
        def on_key_press(symbol,modifier):
            if symbol==key.I:
                if self.map_no==1:
                    self.load_map1_screen(self.charx,self.chary,self.map_charx,self.map_chary)
                elif self.map_no==2:
                    self.load_map2_screen(self.charx,self.chary,self.map_charx,self.map_chary)
                elif self.map_no==3:
                    self.load_map3_screen(self.charx,self.chary,self.map_charx,self.map_chary)
                else:
                    self.load_map4_screen(self.charx,self.chary,self.map_charx,self.map_chary)

#------------------------------------MONSTERS------------------------------------------
    def load_monsters_screen(self):
        window=self.window
        #self.label=pyglet.text.Label(str(self.inventory[1]),
        #                        x=400,y=300)
        #count=0
        #for items in self.inventory[1]:
        #    count+=1
        #self.label=pyglet.text.Label(str(count),
        #                            x=400,y=400)
        
        
        batch=pyglet.graphics.Batch()
        monsters=[]
        x_val=20
        y_val=720
        for item in self.inventory[1]:
            #print (str(item)+" "+str(self.monster1)+","+str(self.monster2)+","+str(self.monster3))
            if str(item)==str(self.monster1):
                monsters.append(pyglet.text.Label("1: "+str(item),
                                         x=x_val,
                                         y=y_val,
                                         font_size=20,batch=batch))
                
            elif str(item)==str(self.monster2):
                monsters.append(pyglet.text.Label("2: "+str(item),
                                         x=x_val,
                                         y=y_val,
                                         font_size=20,batch=batch))
                
            elif str(item)==str(self.monster3):
                monsters.append(pyglet.text.Label("3: "+str(item),
                                         x=x_val,
                                         y=y_val,
                                         font_size=20,batch=batch))
            else:
                monsters.append(pyglet.text.Label(str(item),
                                         x=x_val,
                                         y=y_val,
                                         font_size=20,batch=batch))
            x_val+=160
            if x_val>660:
                y_val-=160
                x_val=20
                       
                                         
        @window.event
        def on_draw():
            window.clear()
            #self.label.draw()
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,("v2i",(0,640,800,640)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,("v2i",(0,480,800,480)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,("v2i",(0,320,800,320)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,("v2i",(0,160,800,160)))

            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,("v2i",(640,0,640,800)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,("v2i",(480,0,480,800)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,("v2i",(320,0,320,800)))
            pyglet.graphics.draw(2,pyglet.gl.GL_LINES,("v2i",(160,0,160,800)))

            batch.draw()
        print (str(self.monster1)+" "+str(self.monster2)+" "+str(self.monster3))
            
        @window.event
        def on_key_press(symbol,modifier):
            if symbol==key.I:
                if self.map_no==1:
                    self.load_map1_screen(self.charx,self.chary,self.map_charx,self.map_chary)
                elif self.map_no==2:
                    self.load_map2_screen(self.charx,self.chary,self.map_charx,self.map_chary)
                elif self.map_no==3:
                    self.load_map3_screen(self.charx,self.chary,self.map_charx,self.map_chary)
                else:
                    self.load_map4_screen(self.charx,self.chary,self.map_charx,self.map_chary)
        
#--------------------------------------SHOP--------------------------------------------

    def load_shop_screen(self):
        self.building_minimap_image=pyglet.image.load("assets/shop/building_mini_map.png")
        self.building_image=pyglet.image.load("assets/shop/building.png")
        self.buy_button_image=pyglet.image.load("assets/shop/buy_button.png")
        self.exit_button_image=pyglet.image.load("assets/shop/exit_button.png")
        self.buy_button_2_image=pyglet.image.load("assets/shop/buy_button_2.png")
        self.exit_button_2_image=pyglet.image.load("assets/shop/exit_button_2.png")
        map_no=self.map_no
        
        window=self.window
        self.buy_button=pyglet.sprite.Sprite(img=self.buy_button_image,
                                             x=0,y=400)
        self.exit_button=pyglet.sprite.Sprite(img=self.exit_button_image,
                                              x=0,y=0)

        

        @window.event
        def on_draw():
            window.clear()
            self.buy_button.draw()
            self.exit_button.draw()
            money=pyglet.text.Label("£"+str(self.currency),
                                    x=0,y=750,
                                    font_size=30).draw()

        @window.event
        def on_mouse_motion(x,y,dx,dy):
            if y>400:
                self.buy_button.image=self.buy_button_2_image
                self.exit_button.image=self.exit_button_image
            elif y<400:
                self.exit_button.image=self.exit_button_2_image
                self.buy_button.image=self.buy_button_image

        @window.event
        def on_mouse_press(x,y,symbol,modifier):
            if y>400:
                self.load_buy_screen()
            if y<400:
                if map_no==1:
                    self.load_map1_screen(self.charx,self.chary,self.map_charx,
                                          self.map_chary)
                elif map_no==2:
                    self.load_map2_screen(self.charx,self.chary,self.map_charx,
                                          self.map_chary)
                elif map_no==3:
                    self.load_map3_screen(self.charx,self.chary,self.map_charx,
                                          self.map_chary)
                elif map_no==4:
                    self.load_map4_screen(self.charx,self.chary,self.map_charx,
                                          self.map_chary)
    def load_buy_screen(self):
        window=self.window
        self.currency_label=pyglet.text.Label("£"+str(self.currency),
                                              x=0,y=750,
                                              font_size=30)
        self.instruction=pyglet.text.Label("Right click to exit the shop",
                                           x=0,y=50)
        @window.event
        def on_draw():
            window.clear()
            self.currency_label.draw()
            self.instruction.draw()
        @window.event
        def on_mouse_press(x,y,symbol,modifier):
            if symbol==mouse.RIGHT:
                self.load_shop_screen()
#--------------------------------------------------------GAMEOVER-------------------------

    def load_game_over_screen(self):
        window=self.window
        #self.up=True
        self.game_over=pyglet.text.Label("GAME OVER",
                                    x=400,y=400,
                                    font_size=70,
                                         anchor_x="center",
                                         anchor_y="center")
        @window.event
        def on_draw():
            window.clear()
            self.game_over.draw()

        @window.event
        def on_mouse_press(x,y,symbol,modifier):
            if symbol==mouse.LEFT:
                if self.map_no==1:
                    self.load_map1_screen(self.charx,self.chary,self.map_charx,
                                          self.map_chary)
                elif self.map_no==2:
                    self.load_map2_screen(self.charx,self.chary,self.map_charx,
                                          self.map_chary)
                elif self.map_no==3:
                    self.load_map3_screen(self.charx,self.chary,self.map_charx,
                                          self.map_chary)
                elif self.map_no==4:
                    self.load_map4_screen(self.charx,self.chary,self.map_charx,
                                          self.map_chary)
            
#---------------------------------------------WIN SCREEN----------------------------------
    def load_win_screen(self):
        window=self.window
        
        self.win_label=pyglet.text.Label("YOU WON!",
                                         x=400,y=400,
                                         font_size=50,
                                         anchor_x="center",
                                         anchor_y="center")
        gained_exp=self.multiplier
        gained_currency=self.multiplier*100
        self.currency+=int(gained_currency)
        level=self.exp
        self.level=int(level/100)
        
        

        self.exp_label=pyglet.text.Label("You have gained "+str(gained_exp)+" experience points",
                                    x=0,y=300,
                                    font_size=30)
        self.currency_label=pyglet.text.Label("You have gained "+str(gained_currency)+" currency",
                                              x=0,y=100,
                                              font_size=30)
        
        @window.event
        def on_draw():
            window.clear()
            self.win_label.draw()
            self.exp_label.draw()
            self.currency_label.draw()

        @window.event
        def on_mouse_press(x,y,symbol,modifier):
            if symbol==mouse.LEFT:
                if self.map_no==1:
                    self.load_map1_screen(self.charx,self.chary,
                                          self.map_charx,self.map_chary)
                if self.map_no==2:
                    self.load_map2_screen(self.charx,self.chary,
                                          self.map_charx,self.map_chary)
                if self.map_no==3:
                    self.load_map3_screen(self.charx,self.chary,
                                          self.map_charx,self.map_chary)
                else:
                    self.load_map4_screen(self.charx,self.chary,
                                          self.map_charx,self.map_chary)
            
#---------------------------------------MAIN MENU-------------------------------------------
#This si the class that is going to handle all of the tkinter menus in my program
class Menu(Frame):
    #This defines what is going to be inherant within all of the tkinter classes
    def __inti__(self, master=None):
        #?
        Frame.__init__(self,master)
        #This makes master apart of the object itself
        self.master=master
    #This is the meathod for the start menu. This is going to be where the user can change
    #the settings, start a new game or carry on from where they have left off.
    def main_menu(self):
        #This names the window Main Menu (purely cosmetic)
        self.master.title("Main Menu")
        #?
        self.pack(fill=BOTH, expand=1)
        #This changes the background colour of the window to black
        self.configure(background="black")

        #This creates a button and links it to the start meathod
        self.start=Button(self,text="Start",command=self.start)
        #This resizes the button
        self.start.config(height=15,width=100)
        #This placesthe button onto the tkinter window
        self.start.place(x=50,y=200)
    #This is the meathod which is going to start the game itself.
    def start(self):
        #This line of code ipens the specified file
        file=open("save files\save file.txt","r")

        #This variable is going to keep track of the line that the loop (look ahead) is on
        #This will work because the data within the text document is placed specifica;;y
        line_count=0
        #This is going to store the number of the map that is in the document
        current_map=None
        #This is going to store the x coordinate of the sprite (found in the document)
        spritex=None
        #This is going to store the y coordinate of the sprite (found in the document)
        spritey=None
        #This is going to store the x coordinate of the map sprite (found in the document)
        map_spritex=None
        #This is going to store the y coordinate of the map sprite (found in the document)
        map_spritey=None
        
        monster1=None
        monster2=None
        monster3=None

        exp=None
        currency=None
        level=None
        
        #health_potion_small=None
        #mp_potion_small=None
        #attack_boost_small=None
        #defence_boost_small=None
        inventory=[[],[]]

        #This loop kis there to read the document and record the relevant information within
        #the relevant variables
        for line in file:
            line_count+=1
            if line_count==1:
                current_map=int(line)
            if line_count==2:
                spritex=int(line)
            if line_count==3:
                spritey=int(line)
            if line_count==4:
                map_spritex=int(line)
            if line_count==5:
                map_spritey=int(line)
                
            if line_count==6:
                if line=="None":
                    pass
                else:
                    monster1=line
            if line_count==7:
                if line=="None":
                    pass
                else:
                    monster2=line
            if line_count==8:
                if line=="None":
                    pass
                else:
                    monster3=line
            if line_count==9:
                exp=int(line)
            if line_count==10:
                currency=int(line)
            if line_count==11:
                level=int(line)
        file.close()

        file=open("save files\monsters inventory.txt")
        for line in file:
            line=line.replace("\n","")
            inventory[1].append(str(line))
        file.close()

        file=open("save files\items inventory.txt")
        item_count=0
        name_temp=None

        for line in file:
            line=line.replace("\n","")
            inventory[0].append(line)        
        """for line in file:
            line=line.replace("\n","")
            #print (line)
            
            if item_count==0:
                name_temp=line
                item_count=1
                
                
            elif item_count==1:
                if name_temp=="health_potion_small":
                    print (line)
                    health_potion_small = line
                    print ("Triggered")
                    
                elif name_temp=="mp_potion_small":
                    mp_potion_small = line
                    print ("Triggered1")
                    
                elif name_temp == "attack_boost_small":
                    attack_boost_small = line
                    print ("triggered2")
                    
                elif name_temp == "defence_boost_small ":
                    defence_boost_small = line
                    print ("triggered3")
                print (line)
                item_count=0"""
                
            #inventory[0].append(str(line))
        file.close()
            
        active_screen=Game(current_map,spritex,spritey,map_spritex,map_spritey,
                               monster1,monster2,monster3,exp,currency,level,inventory)
        
        if current_map==1:
            active_screen.load_map1_screen(spritex,spritey,map_spritex,map_spritey)
        if current_map==2:
            active_screen.load_map2_screen(spritex,spritey,map_spritex,map_spritey)
        if current_map==3:
            active_screen.load_map3_screen(spritex,spritey,map_spritex,map_spritey)
        if current_map==4:
            active_screen.load_map4_screen(spritex,spritey,map_spritex,map_spritey)
            
        #This closes the tkinter window and stops the mainloop (stops tkinter from running)
        root.destroy()
        #This allows the pyglet code to be exicuted
        pyglet.app.run()
        
        
                
        
        
#----------------------------------------CONFIGURATION--------------------------------------


#This assignes the variable root 'to' tkinter
root=Tk()
#This changes the size of the tkinter window
root.geometry("800x800")
#This assignes the variable app to the class menu
app=Menu(root)
#This triggers the main menu meathod.
app.main_menu()
#This allows the tkinter code to trigger
root.mainloop()
