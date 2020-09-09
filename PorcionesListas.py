def meses_faltantes(numero):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[numero:]

#Bloque principal
#Se recupera desde el mes indicado hsta el final de la lista
print("Imprimir los nombres que faltan hasta fin de año")
numero=int(input("Ingrese el numero de mes:"))
meses_falta=meses_faltantes(numero)
print(meses_falta)
