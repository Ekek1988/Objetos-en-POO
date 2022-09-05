class A():
    def __init__(self):
        self.contador = 0
    def incrementar(self):
        self.contador += 1
    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0
    def incrementar(self):
        self.__contador += 1
    def cuenta(self):
        return self.__contador   ##cuando se pone __ se encapsula el atributo dentro de la misma clase

print("Objeto 1")

a = A()
print(a.cuenta())
a.incrementar()  ## Esto le suma el valor 1 cuando vuelva a ejecutar
print(a.cuenta())
print(a.contador)

print("Objeto 2")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
print(b.__contador)