#Ejercicio while 2
cantidad=0
x=1
n=int(input("Cuantas piezas cargara:"))
while x<=n:
    largo=float(input("Ingrese la medida de la ( " +str(x) +" ) pieza"))
    if largo>=1.2 and largo<=1.3:
        cantidad=cantidad+1
    x=x+1
print("La cantidad de piezas aptas son"+str(cantidad))
