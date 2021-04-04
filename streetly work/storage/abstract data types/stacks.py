#This is code for a dynamic stack
#It has been implamented in a Object-Orientated fashon

#NOTE:
#   need to allow the user to input numbers into the stack
import pyglet
from pyglet.window import mouse
from pyglet.window import key
##########################STACK##############################

class Stack():
    def __init__(self):
        self.stack=[]

    def is_empty(self):
        if int(len(self.stack))!=0:
            return False
        else:
            return True

    def push(self,value):
        self.stack.append(value)
        return self.stack

    def pull(self):
        last_val=int(len(self.stack)-1)
        temp=self.stack.pop(last_val)
        return temp

    def get_stack(self):
        return self.stack
#############################INTERFACE#############################
class desplay():
    def __init__(self):
        self.window=pyglet.window.Window(800,500)
        self.stack_build=Stack()
        self.labels=pyglet.graphics.Batch()

    def get_screen(self):
        window=self.window
        self.labels=pyglet.graphics.Batch()
        self.stack=pyglet.text.Label(str(self.stack_build.get_stack()),
                                     x=0,y=300,
                                     font_size=40,
                                     batch=self.labels)
        
        push=pyglet.text.Label("Push",
                                    x=0,y=50,
                                    font_size=50,
                                    batch=self.labels)
        pull=pyglet.text.Label("Pull",
                               x=300,y=50,
                               font_size=50,
                               batch=self.labels)
        is_empty=pyglet.text.Label("IS_empty",
                                   x=500,y=50,
                                   font_size=50,
                                   batch=self.labels)
        @window.event
        def on_draw():
            window.clear()
            self.labels.draw()

        def update_stack(dt):
            self.stack.text=str(self.stack_build.get_stack())
            pyglet.clock.unschedule(update_stack)

        @window.event
        def on_mouse_press(x,y,symbol,modifier):
            if symbol==mouse.LEFT:
                print ("x: "+str(x)+"      y: "+str(y))
                if x>0 and x<170:
                    if y>30 and y<130:
                        self.desplay_push()
                if x>250 and x<430:
                    if y>30 and y<130:
                        self.desplay_pull()
                        pyglet.clock.schedule_interval(update_stack,0.1)
                if x>480 and x<800:
                    if y>30 and y<130:
                        self.desplay_is_empty()

    def desplay_pull(self):
        window=self.window
        self.labels=pyglet.graphics.Batch()
        label=pyglet.text.Label(str(self.stack_build.pull()),
                                font_size=50,
                                y=250,
                                batch=self.labels)
        label2=pyglet.text.Label("Back",
                                 font_size=50,
                                 x=250,y=50,
                                 batch=self.labels)

        @window.event
        def on_draw():
            window.clear()
            self.labels.draw()

        @window.event
        def on_mouse_press(x,y,symbol,modifier):
            if symbol==mouse.LEFT:
                print ("x: "+str(x)+"  y:"+str(y))
            if y<100:
                self.get_screen()

    def desplay_is_empty(self):
        window=self.window
        self.labels=pyglet.graphics.Batch()
        label=pyglet.text.Label("Back",
                                    font_size=50,
                                    anchor_x="center",
                                    anchor_y="center",
                                    x=400,y=100,
                                    batch=self.labels)
        label2=pyglet.text.Label(str(self.stack_build.is_empty()),
                                 y=250,x=0,
                                 font_size=50,
                                 batch=self.labels)
        @window.event
        def on_draw():
            window.clear()
            self.labels.draw()

        @window.event
        def on_mouse_press(x,y,symbol,modifier):
            if symbol==mouse.LEFT:
                if x<600:
                    self.get_screen()

                

    def desplay_push(self):
        window=self.window
        self.labels=pyglet.graphics.Batch()
        self.text=""
        self.input=pyglet.text.Label(self.text,
                                     x=0,y=250,
                                     font_size=80,
                                     batch=self.labels)
        enter=pyglet.text.Label("Enter",
                                anchor_x="center",
                                anchor_y="center",
                                x=400,y=100,
                                font_size=50,
                                batch=self.labels)
        @window.event
        def update_text(dt):
            self.input.text=self.text
            print (str(self.text))
        pyglet.clock.schedule_interval(update_text,0.1)

        @window.event
        def on_mouse_press(x,y,symbol,modifier):
            if symbol==mouse.LEFT:
                print ("x: "+str(x)+"      y: "+str(y))
                if y>0 and y<150:
                    if int(len(list(self.text)))!=0:
                        self.stack_build.push(self.text)
                        pyglet.clock.unschedule(update_text)
                        self.get_screen()
        @window.event
        def on_key_press(symbol,modifier):
            if symbol==key.A:
                self.text+="A"
            elif symbol==key.B:
                self.text+="B"
            elif symbol==key.C:
                self.text+="C"
            elif symbol==key.D:
                self.text+="D"
            elif symbol==key.E:
                self.text+="E"
            elif symbol==key.F:
                self.text+="F"
            elif symbol==key.G:
                self.text+="G"
            elif symbol==key.H:
                self.text+="H"
            elif symbol==key.I:
                self.text+="I"
            elif symbol==key.J:
                self.text+="J"
            elif symbol==key.K:
                self.text+="K"
            elif symbol==key.L:
                self.text+="L"
            elif symbol==key.M:
                self.text+="M"
            elif symbol==key.N:
                self.text+="N"
            elif symbol==key.O:
                self.text+="O"
            elif symbol==key.P:
                self.text+="P"
            elif symbol==key.Q:
                self.text+="Q"
            elif symbol==key.R:
                self.text+="R"
            elif symbol==key.S:
                self.text+="S"
            elif symbol==key.T:
                self.text+="T"
            elif symbol==key.U:
                self.text+="U"
            elif symbol==key.V:
                self.text+="V"
            elif symbol==key.W:
                self.text+="W"
            elif symbol==key.X:
                self.text+="X"
            elif symbol==key.Y:
                self.text+="Y"
            elif symbol==key.Z:
                self.text+="Z"
            elif symbol==key.BACKSPACE:
                self.text=""
            elif symbol==key.ENTER:
                if int(len(list(self.text)))!=0:
                        self.stack_build.push(self.text)
                        pyglet.clock.unschedule(update_text)
                        self.get_screen()
                
                
        

        @window.event
        def on_draw():
            window.clear()
            self.labels.draw()

#######################CONFIG#####################################

__main__=desplay()
__main__.get_screen()
pyglet.app.run()
"""stack=Stack()
print (stack.is_empty())
print (stack.push("eighteen"))
print (stack.push("nineteen"))
print (stack.pull())
"""
