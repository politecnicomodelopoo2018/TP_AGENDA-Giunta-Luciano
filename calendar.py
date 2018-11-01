from kivy import kivy
from kivy.app import App
from DB import DB
from Agendas import Agenda
kivy.require("1.8.0")
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


DB().SetConection('127.0.0.1', 'root', '', 'TP_AGENDA')
Builder.load_file('screenmanagerapp.kv')

agenda = Agenda.Select(1)



class PantallaGeneral(Screen):
    pass

class MisDatos(Screen):
    def __init__(self, **kwargs):
        super(MisDatos, self).__init__(**kwargs)
        self.ids.label1.text = "MIS DATOS"
        self.ids.button1.background_normal = "Faraona.jpg"
        self.SetearDatosInput()

    def SetearDatosInput(self):
        self.ids.t_nombre.text = agenda.nombre
        self.ids.t_apellido.text = agenda.apellido
        self.ids.t_dni.text = str(agenda.DNI)
        self.ids.t_telefono_urgencia.text = agenda.telefono_urgencia
        self.ids.t_telefono.text = agenda.telefono
        self.ids.t_celular.text = agenda.celular
        self.ids.t_signo.text = agenda.signo
        self.ids.t_obra_social.text = agenda.obra_social
        self.ids.t_direccion.text = agenda.direccion
        self.ids.t_nacimiento.text = str(agenda.nacimiento)
        self.ids.t_estado_civil.text = agenda.estado_civil
        self.ids.t_grupo_sanguineo.text = agenda.grupo_sanguineo
        self.ids.t_mail.text = agenda.mail
    def DisabledInputs(self, evt=None):
        self.ids.t_dni.disabled = True
        self.ids.t_apellido.disabled = True
        self.ids.t_nombre.disabled = True
        self.ids.t_telefono.disabled = True
        self.ids.t_obra_social.disabled = True
        self.ids.t_mail.disabled = True
        self.ids.t_direccion.disabled = True
        self.ids.t_grupo_sanguineo.disabled = True
        self.ids.t_celular.disabled = True
        self.ids.t_nacimiento.disabled = True
        self.ids.t_estado_civil.disabled = True
        self.ids.t_telefono_urgencia.disabled = True
        self.ids.t_signo.disabled = True

    def EnableInputs(self, evt=None):
        self.ids.t_dni.disabled = False
        self.ids.t_apellido.disabled = False
        self.ids.t_nombre.disabled = False
        self.ids.t_telefono.disabled = False
        self.ids.t_obra_social.disabled = False
        self.ids.t_mail.disabled = False
        self.ids.t_direccion.disabled = False
        self.ids.t_grupo_sanguineo.disabled = False
        self.ids.t_celular.disabled = False
        self.ids.t_nacimiento.disabled = False
        self.ids.t_estado_civil.disabled = False
        self.ids.t_telefono_urgencia.disabled = False
        self.ids.t_signo.disabled = False

    def UpdateCosas(self):
        agenda.SetAgenda(self.ids.t_nombre.text, self.ids.t_apellido.text, self.ids.t_dni.text, self.ids.t_grupo_sanguineo.text, self.ids.t_telefono.text, self.ids.t_celular.text, self.ids.t_mail.text, self.ids.t_direccion.text, self.ids.t_signo.text, self.ids.t_telefono_urgencia.text, self.ids.t_nacimiento.text, self.ids.t_estado_civil.text, self.ids.t_obra_social.text)
        agenda.UpdateDueno(1)
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