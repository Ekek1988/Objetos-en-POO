class FabricaTelefonos():
    def __init__(self , marca, *colores , **modelos):   ##el * significa una tupla y para diccionario se usa **
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos("Alcatel" , "Negro", "Azul", m1 = 500 , m2= 1000 )
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
telefono.memoria = 512 ##para crear un atributo temporal solamente, lo creo para un solo objeto
print(telefono.memoria) ## llamo a este unico objeto
