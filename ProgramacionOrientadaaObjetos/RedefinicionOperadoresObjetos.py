class Operadores:

    def __init__(self,lista):
        self.lista=lista

    def visualizar(self):
        print(self.lista)

    def __add__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]+entero)
        return nueva

    def __sub__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]-entero)
        return nueva

    def __mul__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]*entero)
        return nueva

    def __floordiv__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]/entero)
        return nueva

operaciones=Operadores([19,23,58])
operaciones.visualizar()
print(operaciones+2)
print(operaciones-3)
print(operaciones*4)
print(operaciones//2)
