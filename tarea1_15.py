import io

f = io.open("archivo1_15.txt", "r")
f.seek(0)
cadena = f.read()
cadenas = cadena.split(" ")
total = ""
for pieza in cadenas:
    total = total + pieza

print(total)
