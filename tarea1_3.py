import random

numRand = random.randint(0,20)
print("¿En qué número del 0 al 20 estoy pensando?")

numIntentos = 0

while True:
    respuesta = int(input())
    numIntentos += 1
    if numRand == respuesta:
        break
    elif numRand < respuesta:
        print("El número es más bajo")
    else:
        print("El número es más alto")

print(f"¿Has acertado el número en {numIntentos} intentos!")
