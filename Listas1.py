lista=[] #DECLARACION DE LA LISTA
for k in range(10):
    lista.append(input("Introduce el "+str(k)+" valor a la lista:"))

print("Los elementos de la lista son:"+str(lista))
valor=int(input("Introduce el valor a modificar de la lista por el indice"))
nuevo=input("Introduce el nuevo valor:")
lista[valor]=nuevo#MODIFICAR VALOR DE LA LISTA
print("Los elementos de la lista son:"+str(lista))
valor=int(input("Introduce el valor en el que se insertara el nuevo valor"))
nuevo=input("Introduce el nuevo valor:")
lista.insert(valor,nuevo)#INSERTAR VALOR A LA LISTA
print("Los elementos de la lista son:"+str(lista))
nuevo=input("Introduce el valor a eliminar")
lista.remove(nuevo) #ELIMINAR VALOR DE LA LISTA
print("Los elementos de la lista son:"+str(lista))
nuevo=input("Introduce el valor de la lista que se desea buscar:")
resultado=(nuevo in lista)
if (resultado):
    print("Existe el elemento en la posicion: "+str(lista.index(nuevo)))
else:
    print("El elemento no existe en la lista ")
