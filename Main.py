from kivy import kivy
from kivy.app import App
from DB import DB
from Contactos import Contacto
from Agendas import Agenda
from Eventos import Evento
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
import datetime
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
        titulo = Label(text=self.month_str[self.month - 1] + ", " + str(self.year), size_hint_y=.2)

        layout = GridLayout(cols=7, size_hint_y=.8)

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

        self.root.add_widget(titulo)
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
        self.cambiarpantalla()

    def on_month(self, widget, event):
        self.create_calendario()

    def on_year(self, widget, event):
        self.create_calendario()

    def cambiarpantalla(self, evn=None):
        root.current = 'HojaAgenda'


fecha = datetime.datetime.now()
cal = Calendario(month=fecha.month, year=fecha.year,
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
        misdatos.SetearDatosLabel()


    def CambiarAnimacionMisDatos(self):
        root.transition = NoTransition()


lista = Contacto.SeleccionarContactos()
from functools import partial
contacto = Contacto()
contactoID = Contacto()
contactoID.idContacto = 1

class Contactos(Screen):
    contactos = ListProperty()
    variable = None
    def __init__(self, **kwargs):
        super(Contactos, self).__init__(**kwargs)
        self.AgregarContacto()
    def AgregarContacto(self):
        self.contactos = self.AgregarContactoLista()
        print(self.contactos[0].nombre, self.contactos[1].nombre)
        scroll = self.ids.scrollview
        scroll.clear_widgets()
        grid = GridLayout(cols=3, size_hint_y=30, spacing='15dp', id='GridDelScroll')
        for item in self.contactos:
            bnt = Button(text=item.nombre, font_size='30sp', size_hint_y=None, height=170, id=str(item.idContacto))
            buttoncallback = partial(self.GuardarId, item.idContacto)
            bnt.bind(on_press = buttoncallback)
            bnt.bind(on_press = self.CambiarScreen)

            grid.add_widget(bnt)
        scroll.add_widget(grid)

    def CambiarScreen(self, evn = None):
        root.current='DetallesContacto'


    def GuardarId(self, *args):
        contactoID.idContacto = args[0]
        detallecontacto.RellenarLabels()

    def AgregarContactoLista(self):
        lista = Contacto.SeleccionarContactos()
        return lista

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
    def __init__(self, **kwargs):
        super(DetallesContacto, self).__init__(**kwargs)

    def RellenarLabels(self):
        contacto = Contacto.SelectContacto(contactoID.idContacto)
        self.ids.l_contacto_nombre.text = contacto.nombre
        self.ids.l_contacto_apellido.text = contacto.apellido
        self.ids.l_contacto_mail.text = contacto.mail
        self.ids.l_contacto_telefono.text = contacto.telefono
        self.ids.l_contacto_celular.text = contacto.celular
        contactoseditables.ids.t_con_editable_nombre.text = contacto.nombre
        contactoseditables.ids.t_con_editable_apellido.text = contacto.apellido
        contactoseditables.ids.t_con_editable_mail.text = contacto.mail
        contactoseditables.ids.t_con_editable_telefono.text = contacto.telefono
        contactoseditables.ids.t_con_editable_celular.text = contacto.celular

class ContactosEditable(Screen):
    def __init__(self, **kwargs):
        super(ContactosEditable, self).__init__(**kwargs)


    def UpdateContactos(self):
        contacto =Contacto.SelectContacto(contactoID.idContacto)
        contacto.SetContacto(self.ids.t_con_editable_nombre.text, self.ids.t_con_editable_apellido.text,self.ids.t_con_editable_mail.text, self.ids.t_con_editable_telefono.text, self.ids.t_con_editable_celular.text, contacto.idAgendas)
        contacto.UpdateContacto(contacto.idContacto)
        self.SeleccionarNuevamente()

    def SeleccionarNuevamente(self):
        contactos.AgregarContacto()


class Feriados(Screen):
    pass

class HojaAgenda(Screen):
    def __init__(self, **kwargs):
        super(HojaAgenda, self).__init__(**kwargs)

    def AgregarEvento(self):
        self.eventos = self.AgregarEventoLista()
        print(self.eventos[0].titulo, self.eventos[1].titulo)
        scroll = self.ids.scrollview
        scroll.clear_widgets()
        grid = GridLayout(cols=1, size_hint_y=30, spacing='15dp', id='GridEventos')
        for item in self.eventos:
            bnt = Button(text=item.titulo, font_size='30sp', size_hint_y=None, height=170, id=str(item.idEvento))
            buttoncallback = partial(self.GuardarId, item.idContacto)
            bnt.bind(on_press = buttoncallback)
            bnt.bind(on_press = self.CambiarScreen)
 '''esto está pal ogt VER'''

            grid.add_widget(bnt)
        scroll.add_widget(grid)

    def AgregarEventosLista(self):
        lista = Evento.SeleccionarEventos()
        return lista


misdatos=MisDatos(name='MisDatos')
contactos=Contactos(name='Contactos')
hojaagenda = HojaAgenda(name = 'HojaAgenda')
detallecontacto = DetallesContacto(name='DetallesContacto')
nuevocontacto = NuevoContacto(name='NuevoContacto')
contactoseditables = ContactosEditable(name='ContactosEditable')
root.add_widget(PantallaGeneral(name='PantallaGeneral'))
root.add_widget(hojaagenda)
root.add_widget(misdatos)
root.add_widget(MisDatosEditable(name='MisDatosEditable'))
root.add_widget(contactos)
root.add_widget(Feriados(name='Feriados'))
root.add_widget(nuevocontacto)
root.add_widget(detallecontacto)
root.add_widget(contactoseditables)


class ScreenManagerApp(App):
    title = "Agenda"
    def build(self):
        return root

if __name__ == '__main__':
    ScreenManagerApp().run()