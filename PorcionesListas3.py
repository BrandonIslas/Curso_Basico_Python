def meses_faltantes(inicio):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[:inicio]

#Bloque principal
#Se recupera desde el mes indicado hsta el final de la lista
print("Imprimir los nombres de meses compredidos entre un mes y otro")
inicio=int(input("Ingrese el numero de mes:"))
meses_falta=meses_faltantes(inicio)
print(meses_falta)
