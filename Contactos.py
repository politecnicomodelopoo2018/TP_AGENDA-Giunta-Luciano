from DB import DB

class Contacto(object):
    idContacto = None
    nombre = None
    apellido = None
    mail = None
    telefono = None
    celular = None
    idAgendas = None

    def SetContacto(self, idcon, nombre, apellido, mail, telefono, celular, idag):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.telefono = telefono
        self.celular = celular
        self.idContacto = idcon
        self.idAgendas = idag

    def DeserializarContacto(self, diccionario):
        self.idAgendas = diccionario['idAgendas']
        self.nombre = diccionario['nombre']
        self.apellido = diccionario['apellido']
        self.telefono = diccionario['telefono']
        self.celular = diccionario['celular']
        self.mail = diccionario['mail']
        self.idContacto = diccionario['idContactos']

    @staticmethod
    def SelectContacto(id):
        select_cursor = DB().run("Select * from Contactos where idContactos = " + str(id) + ";")
        d = select_cursor.fetchall()
        contacto = Contacto()
        contacto.DeserializarContacto(d[0])
        return contacto




    def InsertContacto(self):

        insert_cursor = DB().run("Insert into Contactos")

    def UpdateDueno(self, id):
        DB().run("Update Contactos set nombre = '" + self.nombre + "', apellido = '" + self.apellido + "', telefono = '" + self.telefono + "', celular = '" + self.celular + "', mail = '" + self.mail + "', idAgendas = " + str(self.idAgendas) + " where idContactos =" + str(id) + ";")
