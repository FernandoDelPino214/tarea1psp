
class Matriz:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0 for j in range(columns)] for i in range(rows)]#gracias stackOverflow
    
    def getNumberRows(self):
        return self.rows
    def getNumberColumns(self):
        return self.columns
    def setElement(self, i, j, element):
        self.matrix[i][j] = element
    
    def addMatrix(self, matriz):
        if (self.columns != matriz.columns) or (self.rows != matriz.rows):
            print("Las dimensiones de las matrices no coinciden")
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] += matriz.matrix[i][j]
    def multMatrix(self, matriz):
        if (self.columns != matriz.columns) or (self.rows != matriz.rows):
            print("Las dimensiones de las matrices no coinciden")
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    self.matrix[i][j] *= matriz.matrix[i][j]

#testing
x = Matriz(2, 2)
y = Matriz(2, 2)
z = Matriz(4, 5)

x.setElement(0,0,2)
x.setElement(0,1,2)
x.setElement(1,0,2)
x.setElement(1,1,2)
y.setElement(0,0,2)
y.setElement(0,1,2)
y.setElement(1,0,2)
y.setElement(1,1,2)

y.multMatrix(x)

for i in range(len(y.matrix)):
    print("%s  %s" %(y.matrix[i][0], y.matrix[i][1]))

x.addMatrix(y)

for i in range(len(x.matrix)):
    print("%s  %s" %(x.matrix[i][0], x.matrix[i][1]))
