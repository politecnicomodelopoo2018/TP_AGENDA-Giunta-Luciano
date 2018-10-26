from DB import DB
import datetime

class Feriados(object):
    idFeriado = None
    Titulo = None
    Fecha = None
    Descripcion = None
    pais = None

    def SetFeriado(self, idFeriado, titulo, fecha, descripcion, pais):
        self.idFeriado = idFeriado
        self.descripcion = descripcion
        self.fecha = fecha
        self.titulo = titulo
        self.pais = pais

    def DeserializarFeriado(self, diccionario):
        self.idFeriado = diccionario['idFeriados']
        self.descripcion = diccionario['descripcion']
        self.fecha = diccionario['fecha']
        self.titulo = diccionario['titulo']
        self.pais = diccionario['pais']

    def DeserializarDescripcion(self, diccionario):
        self.descripcion = diccionario['descripcion']

    @staticmethod
    def SelectFeriado(id):
        select_cursor = DB().run("Select * from Feriados where idFeriado = " + str(id) + ";")
        d = select_cursor.fetchall()
        feriado = Feriados()
        feriado.DeserializarFeriado(d[0])
        return feriado

    @staticmethod
    def SelectFeriadoFecha(fecha):
        lista = []
        select_cursor = DB().run("Select * from Feriados where fecha = '" + str(fecha) + "';")
        for item in select_cursor:
            feriado = Feriados()
            feriado.DeserializarFeriado(item)
            lista.append(feriado)
        return lista



    @staticmethod
    def SeleccionarFeriados():
        lista = []
        select_cursor = DB().run("Select * from Feriados;")
        for item in select_cursor:
            feriado = Feriados()
            feriado.DeserializarFeriado(item)
            lista.append(feriado)
        return lista

    def InsertEvento(self, titulo, descripcion, obj_fecha, idag):
        date = datetime.date(obj_fecha.year, obj_fecha.mes, obj_fecha.dia)
        self.SetFeriado(titulo, descripcion, str(date), idag)
        insert_cursor = DB().run("Insert into Feriados values(null,'" + self.titulo + "','" + self.fecha + "','" + self.descripcion + "','" + str(self.idAgendas) + "');")

    def UpdateEvento(self, id):
        DB().run("Update Eventos set titulo = '" + self.titulo + "', descripcion = '" + self.descripcion + "', fecha = '" + self.fecha + "', idAgendas = " + str(self.idAgendas) + " where idEventos =" + str(id) + ";")

    def UpdateDescripcion(self, id):
        DB().run("Update Eventos set descripcion ='" + self.descripcion + "' where idEventos =" + str(id) + ";")