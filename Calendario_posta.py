import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout
import calendar



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


