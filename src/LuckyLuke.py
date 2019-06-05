###################################################################################################
# These are very good documentations to start with KV:
#   - https://kivy.org/doc/stable/guide/lang.html
###################################################################################################

import os
import kivy
import time
from RPi import GPIO
from kivy.config import Config
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

###################################################################################################
#                                         Initialization
###################################################################################################

###################
### OpenGL settings
# otherwise you have segmentation faults at startup - https://github.com/kivy/kivy/issues/6007
os.environ['KIVY_GL_BACKEND'] = 'gl'

#######################
### Kivy configuration
# TODO: I dont know why I have to load it explicitly ... naming conventions should be fine?!?
kivy.require('1.11.0')              # replace with your current kivy version !
from kivy.lang import Builder
Builder.load_file("LuckyLuke.kv")

# Usually the device decides whether mouse is visible or not => this would be outside of application code.
# You could configure it in ~/.kivy/config.ini as documented here:
#    https://stackoverflow.com/questions/43588499/kivy-mouse-cursor-not-showing
# BUT: this solution working without external configuration (out-of git clone) on non-touch-displays 
#      (which is our current main use-case)
from kivy.config import Config
Config.set('modules', 'cursor', '1')

####################
### GPIO integration
#
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)

###################################################################################################
#                                         Application
###################################################################################################

class RootWidget(Widget):
    #
    # Variante 1 ... programmatic
    #    def __init__(self, **kwargs):
    #        super(RootWidget, self).__init__(**kwargs)
    #        self.add_widget(Button(text='btn 1'))
    #        self.add_widget(Button(text='btn 2'))
    #        self.add_widget(Button(text='btn 3'))

    # Variante 2 ... kv-file
    # ... nothing to do for layout UI

    newPlayerName = ObjectProperty()

    def addPlayer(self, inp):
        # TODO: add to List
        addPlayer(self.newPlayerName.text)
        
        self.newPlayerName.text = ''

        # when a new player is added the LED should blink     
        self.ledAn()

    def ledAn(self):
        GPIO.output(37, True)
        time.sleep(0.1)
        GPIO.output(37, False)

    def addPlayer(self, name):
        print(name)


class LuckyLukeApp(App):   
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    LuckyLukeApp().run()
