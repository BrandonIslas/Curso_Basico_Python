def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        caste=input("Ingrese palabra en castellano:")
        ing=input("Ingrese palabra en inlges:")
        diccionario[caste]=ing
        continua=input("Quiere cargar otra palabra:[s/n]")
    return diccionario

def imprimir(diccionario):
    print("Listado completo del diccionario")
    for x in diccionario:
        print(x,diccionario[x],sep="-")

def consulta_palabra(diccionario):
    pal=input("Ingrese la palabra en castellano a consultar:")
    if pal in diccionario:
        print("En inlges sognifica:",diccionario[pal])

#Bloque principal
diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)
