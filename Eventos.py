from DB import DB
class Evento(object):
    idEventos = None

    titulo = None
    descripcion = None
    fecha = None
    tipo_evento = None
    idAgendas = None

    def SetEvento(self, titulo, descripcion, fecha, tipo_evento, idag):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha
        self.tipo_evento = tipo_evento
        self.idAgendas = idag

    def DeserializarEvento(self, diccionario):
        self.idAgendas = diccionario['idAgendas']
        self.titulo = diccionario['titulo']
        self.descripcion = diccionario['descripcion']
        self.fecha = diccionario['fecha']
        self.tipo_evento = diccionario['tipo_evento']
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

    def InsertEvento(self, titulo, descripcion, fecha, tipo_evento, idag):
        self.SetEvento(titulo, descripcion, fecha, tipo_evento, idag)
        insert_cursor = DB().run("Insert into Eventos values(null,'" + self.titulo + "','" + self.descripcion + "','" + self.fecha + "','" + self.tipo_evento + "', " + str(self.idAgendas) + ");")

    def UpdateEvento(self, id):
        DB().run("Update Eventos set titulo = '" + self.titulo + "', descripcion = '" + self.descripcion + "', fecha = '" + self.fecha + "', tipo_evento = '" + self.tipo_evento + "', idAgendas = " + str(self.idAgendas) + " where idEventos =" + str(id) + ";")

    def UpdateDescripcion(self, id):
        DB().run("Update Eventos set descripcion ='" + self.descripcion + "' where idEventos =" + str(id) + ";")