import os
os.environ['KIVY_GL_BACKEND'] = 'sdl2'

from kivy.core.window import Window
import kivy

kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='PUM')


if __name__ == '__main__':
    MyApp().run()