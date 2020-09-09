def proceso(cadena):
    indice=-1
    iguales=0
    for x in range(0,len(cadena)//2):
        if cadena[x]==cadena[indice]:
            iguales=iguales+1
        indice=indice-1
    print(cadena)
    if iguales==(len(cadena)//2):
        print("Es capicua")
    else:
        print("No es capicua")

#Bloque principal
#podemos utilizar valores negativos para acceder a valores de las estructuras de datos
#para accedes al ultimo valor ponderemos el indice -1, para el penultimo -2 y asi hasta el primero
#lista =[1,2,3] print(lista[-1]) accedemos al valor 3 y asi sucesivamente

proceso("1331")
