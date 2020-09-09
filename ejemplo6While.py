#Ejercico de while

x=1
suma=0

while x<=10:
    valor=int(input("Ingrese el valor:"+str(x)))
    suma=suma+valor
    x=x+1
promedio=suma/10
print("La suma de los 10 valores es"+str(suma)+"el promedio es"+str(promedio))
