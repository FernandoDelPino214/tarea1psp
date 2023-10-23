
print("Escribe algo:")
cadena = input()
letra1 = cadena[0]
letra2 = cadena[-1]
cadena = letra2 + cadena[1:-1] + letra1

print(cadena)
