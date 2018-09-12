from kivy import kivy
from kivy.app import App
from DB import DB
kivy.require("1.8.0")
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput

DB().SetConection('127.0.0.1', 'root', 'alumno', 'TP2')
Builder.load_file('screenmanagerapp.kv')


class PantallaGeneral(Screen):
    pass

class MisDatos(Screen):
    def __init__(self, **kwargs):
        super(MisDatos, self).__init__(**kwargs)
        self.ids.label1.text = "MIS DATOS"
        self.ids.button1.background_normal = "Faraona.jpg"
        nombre = self.ids.caja.text
        self.ids.label2.text = nombre
        print(self.ids.caja.text)
class Contactos(Screen):
    pass

class Feriados(Screen):
    pass

root = ScreenManager()
root.add_widget(PantallaGeneral(name='PantallaGeneral'))
root.add_widget(MisDatos(name='Mis Datos'))
root.add_widget(Contactos(name='Contactos'))
root.add_widget(Feriados(name='Feriados'))


'''
class PantallaSiguiente(Screen):
    pass
class PantallaAnterior(Screen):
    pass


root = ScreenManager()

root.add_widget(PantallaGeneral(name='PantallaPrincipal'))
#root.add_widget(PantallaSiguiente(name='PantallaSiguiente'))
#root.add_widget(PantallaAnterior(name='PantallaAnterior'))
'''
class ScreenManagerApp(App):

    def build(self):
        return root

if __name__ == '__main__':
    ScreenManagerApp().run()