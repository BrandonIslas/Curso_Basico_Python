def cargar_datos():
    lista=[]
    for x in range(5):
        valor=int(input("Ingresa un valor: "))
        lista.append(valor)
    return lista

def verificar_mayor(lista):
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
    print("Mayor de la lista",may)

def verificar_suma(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    print("Suma de todos sus elementos",suma)
