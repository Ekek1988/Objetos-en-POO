#Ejercicio 5

#Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona. SIRVE PARA EJERCITAR LA LOGICA DE LA HERENCIA MULTIPLE

class Universidad():
    def __init__(self, Nombre):
        self.Nombre = Nombre

class Carrera():
    def carrera(self,especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad,Carrera):
    def datos(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        print("Mi nombre es {}, tengo {} años, mi especialidad es {}.Estudio en la universidad {}".format(self.nombre, self.edad,self.especialidad,self.Nombre))

persona = Estudiante("Don Bosco")
persona.carrera("Sistemas")
persona.datos("Carlos", 20)