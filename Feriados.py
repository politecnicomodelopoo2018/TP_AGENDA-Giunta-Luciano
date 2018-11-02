from DB import DB
import datetime

class Feriado(object):
    idFeriado = None
    titulo = None
    fecha = None
    descripcion = None
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
    def SelectFeriadoMes(mes):
        lista = []
        select_cursor = DB().run("Select * from Feriados where mes = '" + str(mes) + "';")
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
            feriado = Feriado()
            feriado.DeserializarFeriado(item)
            lista.append(feriado)
        return lista
    def InsertEvento(self, titulo, obj_fecha, descripcion, pais, idag):
        date = datetime.date(obj_fecha.year, obj_fecha.mes, obj_fecha.dia)
        self.SetFeriado(titulo, str(date), descripcion, idag)
        mes = obj_fecha.mes
        insert_cursor = DB().run("Insert into Feriados values(null,'" + self.titulo + "','" + self.fecha + "','" + self.descripcion + "','" + self.pais + "'," + str(self.idAgendas) + "'," + mes + "');")

    def UpdateFeriado(self, id, obj_fecha):
        date = datetime.date(obj_fecha.year, obj_fecha.mes, obj_fecha.dia)
        DB().run("Update Eventos set titulo = '" + self.titulo + "', fecha = '" + date + "', descripcion = '" + self.descripcion + "', pais = "'' + str(self.pais) + "', idAgendas = " + str(self.idAgendas) + ", mes = '"+ obj_fecha.mes + "' where idEventos =" + str(id) + ";")
