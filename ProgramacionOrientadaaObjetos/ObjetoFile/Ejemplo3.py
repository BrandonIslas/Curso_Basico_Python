archivo = open("archivo.txt","r+")
contenido = archivo.read()
final_de_archivo = archivo.tell()
lista=['Linea1\n','Linea2\n']

archivo.writelines(lista)
archivo.seek(final_de_archivo)


print(archivo.readline())
#Linea 1
print(archivo.readline())
#Linea 2
