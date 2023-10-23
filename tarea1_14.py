import io

while True:
    print("-1. Volcado\t -2.Mostrar\t -3.Salir\t")
    eleccion = input()
    if eleccion == "1":
        f = io.open("archivo1_14.txt", "w")
        f.seek(0)
        for num in range(0, 101, 2):
            f.write("%s " %(num))
    elif eleccion == "2":
        f = io.open("archivo1_14.txt", "r")
        f.seek(0)
        print(f.read())
    else:
        break

print("Programa terminado")
