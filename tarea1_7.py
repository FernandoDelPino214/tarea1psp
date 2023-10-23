
print("Escribe algo:")
cadena = input() + ""

print("AL REVÉS!")

cadena2 = ""
for i in range(len(cadena)):
    cadena2 = cadena2 + cadena[-(i+1)]

print(cadena2)
