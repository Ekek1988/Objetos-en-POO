class FabricaTelefonos():
    marca = "Huawei"
    color = "Negro"
    MemoriaRam = 32
    Almacenamiento = 128
    def llamar(self , mensaje):
        return mensaje
    
    def escucharMusica(self):
        print("Estas escuchando Musica")


telefono = FabricaTelefonos()
telefono.marca
telefono.color
telefono.MemoriaRam
telefono.Almacenamiento

print(telefono.llamar("Hola , ¿Con quien hablo?"))
telefono.escucharMusica()


print(telefono.marca)
print(telefono.color)
print(telefono.MemoriaRam)
print(telefono.Almacenamiento)