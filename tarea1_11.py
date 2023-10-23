salarios = ((700, 900, 1300) , (1000, 950, 1080), (1300, 930, 1200))

empleados = ("Javier María", "Antonio Muñoz", "Isabel Allende")

index = range(len(empleados))
for i in index:
    cadena = ""
    total = 0
    jindex = range(len(salarios[i]))
    for j in jindex:
        total += salarios[i][j]
        cadena = cadena + str(salarios[i][j])
        if j < len(jindex)-1 : cadena = cadena + " + "
    print(f"{empleados[i]} -> {cadena} = {total}")
