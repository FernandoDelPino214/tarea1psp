
texto = "holi"
tabla = [
    ["hallo", "hello", "hola", "hey"],
    ["hol", "hola", "yo", "aa"],
    ["co", "manyooo", "holi", "pavooooo"]
]

def indexContains(table, cadena):
    posicion = -1
    i = 0
    j = 0
    for fila in table:
        for dato in fila:
            if dato == cadena:  
                posicion = (i, j)
                break
            j += 1
        if posicion != -1:
            break
        i += 1
        j = 0
    return posicion

print(indexContains(tabla, texto))

