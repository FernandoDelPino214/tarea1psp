
class Cuenta():
    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad

    def getTitular(self):
        return self.titular
    def getCantidad(self):
        return self.cantidad
    def setTitular(self, titular):
        self.titular = titular
    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def __str__(self):
        return self.toString()
    def toString(self):
        return "Titular: %s, Cantidad: %s" %(self.titular, self.cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        if self.cantidad < cantidad:
            self.cantidad = 0
        else:
            self.cantidad -= cantidad

#testing
x = Cuenta("Paco", 1000)
y = Cuenta("Elsa")

print(x)
print(y)

x.setCantidad(2500)
print(x)
x.retirar(1250)
print(x)
x.retirar(9999)
print(x)

y.setTitular("Ana")
y.ingresar(350)
print(y)
