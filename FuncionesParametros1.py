def mostrar_mensaje(mensaje):
    #Funciones con parametro simple
    print("**************************")
    print(mensaje)
    print("**************************")

def cargar_suma():
    valor1=int(input("Ingresa el valor:"))
    valor2=int(input("Ingresa el valor:"))
    suma=valor1+valor2
    print("La suma es:",suma)
mostrar_mensaje("Calculo de suma de dos valores")
cargar_suma()
