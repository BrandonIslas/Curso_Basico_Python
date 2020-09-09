def presentacion():
    print("Programa para hacer operaciones aritmeticas de suma y resta de dos valores.")
    print("***************************")

def introducirDatos():
    global valor1
    global valor2
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el primer valor:"))

def suma():
    suma=valor1+valor2
    print("La suma de los valores es:",suma)

def resta():
    resta=valor1-valor2
    print("La resta de los valores es:",resta)

def finalizacion():
    print("***************************************")
    print("Final del programa")

#Programa principal
presentacion()
introducirDatos()
suma()
resta()
finalizacion()
