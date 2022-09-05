class A():
    def __init__(self):
       self._contador = 0   ##Lo correcto es usar solo un _ para encapsular
       self._cuenta = 0   ##esto le va a avisar a otro prograar que no acceda a este atributo por afuera de la clase
    
    def incrementar(self):
        self._contador += 1

    def cuenta(self):
        return self._contador

a = A()
print(a._cuenta)
a.cuenta = 20
print(a._cuenta)
#print(a.cuenta)
#a.cuenta = 20
#print(a.cuenta)
