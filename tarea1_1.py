#Implementa un programa Python que PREGUNTE al usuario por dos números enteros (x, y) y muestre por pantalla la suma, resta, multiplicación,
#división y resto de ambos, con el siguiente formato:

print("Introduce dos números enteros: \n")
x = int(input("x = "))
y = int(input("y = "))

print(f"x + y = {x+y}")
print(f"x - y = {x-y}")
print(f"x * y = {x*y}")
print(f"x / y = {x/y}")
print(f"x % y = {x%y}")