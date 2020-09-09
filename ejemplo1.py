print("Datos de la primera persona/")

nombre1=input("Ingrese nombre del producto:")
precio1= int(input("Ingrese un precio:"))
nombre2=input("Ingrese nombre del producto:")
precio2= int(input("Ingrese un precio:"))

#COMENTARIOS en line
BONIFICACION = 20

precio_compra_total = precio1 + precio2
comparar = precio1>=precio2
logico = (precio1 < precio2 and precio1==precio2)

#CONCATENAR TEXTO
cabecera ="Resultados del producto {0}. y del producto {1}.:"
print (cabecera.format(nombre1, nombre2))

print("El precio del primer valor es mayor o igual a el precio del segundo valor:")
print(comparar)
#OTRA FORMA DE CONCATENAR
print("la sume de los productos es:"+str(precio_compra_total))
print("precio1<precio2 and precio1==precio2")
print(logico)

precio_compra_total += BONIFICACION
print ("al precio total le incrementamos su valor que tiene la constante:"+str(precio_compra_total))
