listaNums = []
for i in range(10):
    listaNums += [int(input(f"Inserte el entero nº {i+1}: "))]

i = 0
numNegativos = 0
numCeros = 0
numPositivos = 0

for i in range(10):
    if listaNums[i] < 0:
        numNegativos += 1
    elif listaNums[i] > 0:
        numPositivos += 1
    else:
        numCeros += 1

print(f"Has insertado {numPositivos} números positivos, {numNegativos} números negativos y {numCeros} ceros")