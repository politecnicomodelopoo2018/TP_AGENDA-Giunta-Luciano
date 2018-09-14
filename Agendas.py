import pymysql
from DB import DB

class Agenda(object):
    id = None
    nombre = None
    apellido = None
    DNI = None
    grupo_sanguineo = None
    telefono = None
    celular = None
    mail = None
    direccion = None
    signo = None
    telefono_urgencia = None
    nacimiento = None
    estado_civil = None
    obra_social = None

    def SetAgenda(self, nombre, apellido, DNI, grupo_sanguineo, telefono, celular, mail, direccion, signo, telefono_urgencia, nacimiento, estado_civil, obra_social):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.telefono = telefono
        self.grupo_sanguineo = grupo_sanguineo
        self.celular = celular
        self.mail = mail
        self.direccion = direccion
        self.signo = signo
        self.telefono_urgencia = telefono_urgencia
        self.nacimiento = nacimiento
        self.estado_civil = estado_civil
        self.obra_social = obra_social

    def DeserializarAgenda(self, diccionario):
        self.id = diccionario['idAgendas']
        self.nombre = diccionario['nombre']
        self.apellido = diccionario['apellido']
        self.DNI = diccionario['DNI']
        self.telefono = diccionario['telefono']
        self.grupo_sanguineo = diccionario['grupo_sanguineo']
        self.celular = diccionario['celular']
        self.mail = diccionario['mail']
        self.direccion = diccionario['direccion']
        self.signo = diccionario['signo']
        self.telefono_urgencia = diccionario['telefono_urgencia']
        self.nacimiento = diccionario['nacimiento']
        self.estado_civil = diccionario['estado_civil']
        self.obra_social = diccionario['obra_social']

    @staticmethod
    def Select(id):

        select_cursor = DB().run("Select * from Agendas where idAgendas = " + str(id) + ";")
        d = select_cursor.fetchall()
        agenda = Agenda()
        agenda.DeserializarAgenda(d[0])

        return agenda

    def UpdateDueno(self, id):
        DB().run("Update Agendas set nombre = '" + self.nombre + "', apellido = '" + self.apellido + "', grupo_sanguineo = '" + self.grupo_sanguineo + "', telefono = '" + self.telefono + "', celular = '" + self.celular + "', mail = '" + self.mail + "', direccion ='" + self.direccion + "', signo ='" + self.signo + "', telefono_urgencia = '" + self.telefono_urgencia + "', nacimiento = '" + str(self.nacimiento) + "', estado_civil ='" + self.estado_civil + "', obra_social ='" + self.obra_social + "' where idAgendas =" + str(id) + ";")