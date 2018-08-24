from kivy import kivy
from kivy.app import App


kivy.require("1.8.0")
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class Box01(BoxLayout):
    None

class MainApp(App):
    title = "Agenda, pagina 1"
    def build(self):
        return Box01()


if __name__ == "__main__":
    MainApp().run()
