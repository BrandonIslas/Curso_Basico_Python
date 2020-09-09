#Ejemplo2
#retorno de lista

def cargar_lista():
    li=[]
    for x in range(5):
        valor=int(input("Introduce valor:"))
        li.append(valor)
    return li
def imprimir_mayor(li):
    print("Valores de la lista mayores a 10")
    for x in range(len(li)):
        if li[x]>10:
            print(li[x])
lista=cargar_lista()
imprimir_mayor(lista)
