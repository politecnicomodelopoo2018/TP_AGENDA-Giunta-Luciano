from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
Builder.load_file('mainapp.kv')

class TextInput(TextInput):
    pass

class MainApp(App):
    def build(self):
        return TextInput()


if __name__ in ("__main__", "android"):
    MainApp().run()