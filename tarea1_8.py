
tablaInput = [
    [2,5,3],
    [2,2,6],
    [6,7,1]
]

def sum(tabla):
    total = 0
    for fila in tabla:
        for num in fila:
            total += num
    
    print(total)

sum(tablaInput)
