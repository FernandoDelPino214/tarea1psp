tablaStrings = [
    ["hola", "hello"],
    ["a", "somebody once told me the world is gonna roll me"]
]

def mayorYmenor(tabla):
    mayor = tabla[0][0]
    menor = tabla[0][0]
    for fila in tabla:
        for cadena in fila:
            if len(cadena) > len(mayor):
                mayor = cadena
            elif len(cadena) < len(menor):
                menor = cadena
    
    return (mayor, menor)

print(mayorYmenor(tablaStrings))
