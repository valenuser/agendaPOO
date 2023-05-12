class Persona:
    nombre = ''
    edad = 0
    email = ''
    agenda = {}

    def presentarPersona(self):
        return 'Mi nombre es',self.nombre,'y tengo',self.edad,'años'
    


class Contacto(Persona):
    def __init__(self,nombre,edad,mail,telefono,key):
        super().__init__()
        self.nombre = nombre
        self.edad = edad
        self.mail = mail
        self.telefono = telefono
        self.key = key

    def agregarContacto(self,contacto):
        self.agenda[contacto.nombre] = {'Nombre':contacto.nombre,'Edad':contacto.edad,'Mail':contacto.mail,'Telefono':contacto.telefono,'Key':contacto.key}
        print('Contacto agendado!')


    def eliminarContacto(self,contacto):
        del  self.agenda[contacto]
        print('Contacto eliminado!')

    def mostrarAgenda(self):
        return self.agenda


personas = {}

Usuario = Contacto('User',119,'user@gmail.com',639201283,0)

Carlos = Contacto('Carlos',21,'carlos@gmail.com',123456789,1)

personas['1'] = Carlos

Juan = Contacto('Juan',20,'juan@gmail.com',389756784,2)

personas['2'] = Juan

Arnau = Contacto('Arnau',18,'arnau@gmail.com',493019284,3)

personas['3'] = Arnau

Valentin = Contacto('Valentin',25,'valentin@gmail.com',890284763,4)

personas['4'] = Valentin

Abel = Contacto('Abel',28,'abel@gmail.com',856489231,5)

personas['5'] = Abel


while True:
    print('AGENDA PERSONAL -------------------')

    while True:
            ask = input('Quieres agregar o eliminar contactos? (añadir/eliminar)')
            if ask != 'añadir' and ask != 'eliminar':
                print("Escribe 'añadir' para añadir contactos a la agenda.\n Escribe 'eliminar' para eliminar contactos de la agenda.")
            else:
                break 

    if ask == 'añadir':
        for i in range(1,len(personas)+1):
                print(i,'-->',personas[str(i)].nombre)

        numeroContacto = int(input('Que contacto quieres agregar:\n'))

        Usuario.agregarContacto(personas[str(numeroContacto)])

    elif ask == 'eliminar':
        if len(Usuario.agenda) == 0:
            print('No hay contactos agendados actualmente.')
        else:
            
            for i in Usuario.agenda:
                print(i)

            numeroContacto = input('Que contacto quieres eliminar:\n')

            Usuario.eliminarContacto(numeroContacto)
    

    end = input('Deseas seguir en el programa? (y/n)\n')
    if end == 'n':
        break

print(Carlos.mostrarAgenda())