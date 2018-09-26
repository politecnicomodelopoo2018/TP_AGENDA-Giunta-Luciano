from kivy import kivy
from kivy.app import App
from DB import DB
from Contactos import Contacto
from Agendas import Agenda
kivy.require("1.8.0")
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.screenmanager import NoTransition
from kivy.properties import *
from kivy.uix.screenmanager import FallOutTransition

DB().SetConection('127.0.0.1', 'root', 'alumno', 'TP_AGENDA')
Builder.load_file('screenmanagerapp.kv')

agenda = Agenda.Select(1)
root = ScreenManager()

class PantallaGeneral(Screen):
    def __init__(self, **kwargs):
        super(PantallaGeneral, self).__init__(**kwargs)

    def CambiarAnimacionMisDatos(self):
        root.transition = NoTransition()

    def CambiarAnimacionContactos(self):
        root.transition = FallOutTransition()

class MisDatos(Screen):
    def __init__(self, **kwargs):
        super(MisDatos, self).__init__(**kwargs)
        self.ids.label1.text = "MIS DATOS"
        self.ids.button1.background_normal = "Faraona.jpg"
        self.ids.foto.background_normal = "Camila.jpeg"
        self.SetearDatosInput()

    def SetearDatosInput(self):

        self.ids.l_nombre.text = agenda.nombre
        self.ids.l_apellido.text = agenda.apellido
        self.ids.l_dni.text = str(agenda.DNI)
        self.ids.l_telefono_urgencia.text = agenda.telefono_urgencia
        self.ids.l_telefono.text = agenda.telefono
        self.ids.l_celular.text = agenda.celular
        self.ids.l_signo.text = agenda.signo
        self.ids.l_obra_social.text = agenda.obra_social
        self.ids.l_direccion.text = agenda.direccion
        self.ids.l_nacimiento.text = str(agenda.nacimiento)
        self.ids.l_estado_civil.text = agenda.estado_civil
        self.ids.l_grupo_sanguineo.text = agenda.grupo_sanguineo
        self.ids.l_mail.text = agenda.mail

    def CambiarAnimacionMisDatos(self):
        root.transition = NoTransition()

class MisDatosEditable(Screen):
    def __init__(self, **kwargs):
        super(MisDatosEditable, self).__init__(**kwargs)
        self.ids.label1.text = "MIS DATOS"
        self.ids.button1.background_normal = "Faraona.jpg"
        self.ids.foto.background_normal = "Camila.jpeg"
        self.SetearDatosInput()

    def SetearDatosInput(self):
        misdatos = MisDatos()
        misdatos.ids.label1.text = "UPDATEO"
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

    def Mostrar(self):
        misdatos = MisDatos()
        misdatos.rebind = True
    def UpdateCosas(self):
        agenda.SetAgenda(self.ids.t_nombre.text, self.ids.t_apellido.text, self.ids.t_dni.text, self.ids.t_grupo_sanguineo.text, self.ids.t_telefono.text, self.ids.t_celular.text, self.ids.t_mail.text, self.ids.t_direccion.text, self.ids.t_signo.text, self.ids.t_telefono_urgencia.text, self.ids.t_nacimiento.text, self.ids.t_estado_civil.text, self.ids.t_obra_social.text)
        agenda.UpdateDueno(1)

    def CambiarAnimacionMisDatos(self):
        root.transition = NoTransition()
class Contactos(Screen):
    pass

class NuevoContacto(Screen):
    def __init__(self, **kwargs):
        super(NuevoContacto, self).__init__(**kwargs)
        self.ids.label_nuevocontacto.text = "NUEVO CONTACTO"
    def InsertContactos(self):
        nombre = self.ids.contacto_nombre.text
        apellido = self.ids.contacto_apellido.text
        mail = self.ids.contacto_mail.text
        telefono = self.ids.contacto_telefono.text
        celular = self.ids.contacto_celular.text
        contacto = Contacto()
        contacto.InsertContacto(nombre, apellido, mail, telefono, celular, 1)


class DetallesContacto(Screen):
    def __init__(self, **kwargs):
        super(DetallesContacto, self).__init__(**kwargs)

    def UpdateContactos(self):
        contacto = Contacto()
        contacto.SelectContacto(1)
        contacto.SetContacto(self.nombre, self.apellido, self.mail, self.telefono, self.celular, self.idAgendas)
        contacto.UpdateContacto(1)
class Feriados(Screen):
    pass


root.add_widget(PantallaGeneral(name='PantallaGeneral'))
root.add_widget(MisDatos(name='MisDatos'))
root.add_widget(MisDatosEditable(name='MisDatosEditable'))
root.add_widget(Contactos(name='Contactos'))
root.add_widget(Feriados(name='Feriados'))
root.add_widget(NuevoContacto(name='NuevoContacto'))
root.add_widget(DetallesContacto(name='DetallesContacto'))

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