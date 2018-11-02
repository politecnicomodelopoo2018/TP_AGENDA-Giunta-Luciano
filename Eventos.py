from DB import DB
import datetime
class Evento(object):
    idEventos = None

    titulo = None
    descripcion = None
    fecha = None
    idAgendas = None

    def SetEvento(self, titulo, descripcion, fecha, idag):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha
        self.idAgendas = idag

    def DeserializarEvento(self, diccionario):
        self.idAgendas = diccionario['idAgendas']
        self.titulo = diccionario['titulo']
        self.descripcion = diccionario['descripcion']
        self.fecha = diccionario['fecha']
        self.idEventos = diccionario['idEventos']

    def DeserializarDescripcion(self, diccionario):
        self.descripcion = diccionario['descripcion']

    @staticmethod
    def SelectEvento(id):
        select_cursor = DB().run("Select * from Eventos where idEventos = " + str(id) + ";")
        d = select_cursor.fetchall()
        evento = Evento()
        evento.DeserializarEvento(d[0])
        return evento

    @staticmethod
    def SelectEventoFecha(fecha):
        lista = []
        select_cursor = DB().run("Select * from Eventos where fecha = '" + str(fecha) + "';")
        for item in select_cursor:
            evento = Evento()
            evento.DeserializarEvento(item)
            lista.append(evento)
        return lista



    @staticmethod
    def SeleccionarEventos():
        lista = []
        select_cursor = DB().run("Select * from Eventos;")
        for item in select_cursor:
            evento = Evento()
            evento.DeserializarEvento(item)
            lista.append(evento)
        return lista

    def InsertEvento(self, titulo, descripcion, obj_fecha, idag):
        date = datetime.date(obj_fecha.year, obj_fecha.mes, obj_fecha.dia)
        self.SetEvento(titulo, descripcion, str(date), idag)
        insert_cursor = DB().run("Insert into Eventos values(null,'" + self.titulo + "','" + self.descripcion + "','" + self.fecha + "','" + str(self.idAgendas) + "');")

    def UpdateEvento(self, id):
        DB().run("Update Eventos set titulo = '" + self.titulo + "', descripcion = '" + self.descripcion + "', fecha = '" + self.fecha + "', idAgendas = " + str(self.idAgendas) + " where idEventos =" + str(id) + ";")

    def UpdateDescripcion(self, id):
        DB().run("Update Eventos set descripcion ='" + self.descripcion + "' where idEventos =" + str(id) + ";")

    @staticmethod
    def BorrarEvento(id):
        DB().run("Delete from Eventos where idEventos =" + str(id) + ";")