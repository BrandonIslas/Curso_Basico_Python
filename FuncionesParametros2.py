#Ejemplo 2 retorno de introducirDatos
#retorno de datos se devuelven a la llamada de la funcion que recoge los introducirDatos

def retorno_superficie(lado):
    sup=lado*lado
    return sup #con la instruccion return se retorna los datos de la Funciones

va=int(input("Introduce el valor del cuadrado:"))
superficie=retorno_superficie(va)
print("Al algoritmo del cuadrado es:",superficie)
