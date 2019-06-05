import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
import kivy
kivy.require('1.11.0') # replace with your current kivy version !

from kivy.config import Config
Config.set('modules', 'cursor', '1')

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello Monty')


if __name__ == '__main__':
    MyApp().run()