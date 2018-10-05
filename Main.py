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
from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import FallOutTransition
import calendar

DB().SetConection('127.0.0.1', 'root', 'alumno', 'TP_AGENDA')
Builder.load_file('screenmanagerapp.kv')

agenda = Agenda.Select(1)
root = ScreenManager()


class Calendario(BoxLayout):
    day = NumericProperty(0)
    month = NumericProperty(6)
    year = NumericProperty(2010)
    root = BoxLayout(orientation="vertical")

    def __init__(self, **kwargs):
        super(Calendario, self).__init__(**kwargs)
        self.add_widget(self.root)
        self.create_calendario()

    def create_calendario(self):
        self.day_str = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        self.month_str = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                          'October', 'November', 'December']

        self.dy = calendar.monthcalendar(self.year, self.month)
        self.title = (self.month_str[self.month - 1] + ", " + str(self.year))

        layout = GridLayout(cols=7)

        for d in self.day_str:
            b = Label(text='[b]' + d + '[/b]', markup=True)
            layout.add_widget(b)

        for wk in range(len(self.dy)):
            for d in range(0, 7):
                dateOfWeek = self.dy[wk][d]
                if not dateOfWeek == 0:
                    b = Button(text=str(dateOfWeek))
                    b.bind(on_release=self.date_selected)
                else:
                    b = Label(text='')
                layout.add_widget(b)
        if self.root:
            self.root.clear_widgets()
        self.root.add_widget(layout)
        bottombox = BoxLayout(orientation="horizontal", size_hint=(1, None), height=40)
        bottombox.add_widget(Button(text='<', on_release=self.change_month))
        bottombox.add_widget(Button(text='>', on_release=self.change_month))
        self.root.add_widget(bottombox)

    def change_month(self, event):
        if event.text == '>':
            if self.month == 12:
                self.month = 1
                self.year = self.year + 1
            else:
                self.month = self.month + 1
        elif event.text == '<':
            if self.month == 1:
                self.month = 12
                self.year = self.year - 1
            else:
                self.month = self.month - 1

    def date_selected(self, event):
        self.day = int(event.text)
        self.dismiss()

    def on_month(self, widget, event):
        self.create_calendario()

    def on_year(self, widget, event):
        self.create_calendario()

cal = Calendario(month=6, year=2014,
                        size_hint=(1, 1), size=(560, 500))
class PantallaGeneral(Screen):
    def __init__(self, **kwargs):
        super(PantallaGeneral, self).__init__(**kwargs)
        self.ids.caja_calendario.add_widget(cal)

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
        self.SetearDatosLabel()


    def SetearDatosLabel(self):

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
        self.pantallaanterior= misdatos
        self.ids.label1.text = "MIS DATOS"
        self.ids.button1.background_normal = "Faraona.jpg"
        self.ids.foto.background_normal = "Camila.jpeg"
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

    def UpdateCosas(self):
        agenda.SetAgenda(self.ids.t_nombre.text, self.ids.t_apellido.text, self.ids.t_dni.text, self.ids.t_grupo_sanguineo.text, self.ids.t_telefono.text, self.ids.t_celular.text, self.ids.t_mail.text, self.ids.t_direccion.text, self.ids.t_signo.text, self.ids.t_telefono_urgencia.text, self.ids.t_nacimiento.text, self.ids.t_estado_civil.text, self.ids.t_obra_social.text)
        agenda.UpdateDueno(1)
        self.SeleccionarNuevamente()

    def SeleccionarNuevamente(self):
        agenda = Agenda.Select(1)
        misdatos.SetearDatosLabel()


    def CambiarAnimacionMisDatos(self):
        root.transition = NoTransition()

variable = 1
lista = Contacto.SeleccionarContactos()

class Contactos(Screen):
    contactos = ListProperty()
    def __init__(self, **kwargs):
        super(Contactos, self).__init__(**kwargs)
        self.AgregarContacto()

    def AgregarContacto(self, *args):
        self.AgregarContactoLista()
        scroll = self.ids.scrollview
        scroll.clear_widgets()
        grid = GridLayout(cols=3, size_hint_y=30, spacing='15dp', id='GridDelScroll')
        for item in self.contactos:
            bnt = Button(text=item.nombre, font_size='30sp', size_hint_y=None, height=170, id=str(item.idContacto))
            bnt.bind(on_press = Contactos.CambiarScreen)
            grid.add_widget(bnt)
        scroll.add_widget(grid)

    def CambiarScreen(self,evn=None):
        root.current='DetallesContacto'
    def AgregarContactoLista(self):
        lista = Contacto.SeleccionarContactos()
        self.contactos = lista

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
        contactos.AgregarContacto()



class DetallesContacto(Screen):
    pass


class ContactosEditable(Screen):
    def __init__(self, **kwargs):
        super(ContactosEditable, self).__init__(**kwargs)
        print('hola')
    def UpdateContactos(self):
        contacto = Contacto()
        contacto.SelectContacto(1)
        contacto.SetContacto(self.nombre, self.apellido, self.mail, self.telefono, self.celular, self.idAgendas)
        contacto.UpdateContacto(1)


class Feriados(Screen):
    pass


misdatos=MisDatos(name='MisDatos')
contactos=Contactos(name='Contactos')
contactoseditables = ContactosEditable(name='ContactosEditable')
detallecontacto = DetallesContacto(name='DetallesContacto')
nuevocontacto = NuevoContacto(name='NuevoContacto')
root.add_widget(PantallaGeneral(name='PantallaGeneral'))
root.add_widget(misdatos)
root.add_widget(MisDatosEditable(name='MisDatosEditable'))
root.add_widget(contactos)
root.add_widget(Feriados(name='Feriados'))
root.add_widget(nuevocontacto)
root.add_widget(detallecontacto)
root.add_widget(contactoseditables)

class ScreenManagerApp(App):
    def build(self):
        return root

if __name__ == '__main__':
    ScreenManagerApp().run()