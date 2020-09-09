sueldo= int(input("Introduce un sueldo: "))

if sueldo>3000:
    print("El usuario debe pagar un porcentaje en impuestos")

if sueldo <=3000:
    print("El usuario esta excento de declarar su renta")

if sueldo >6000 and sueldo <10000:
    print("El usuario tiene que pagar una bonificacion de 1000 pesos")

if sueldo==20000 or sueldo==30000:
    print("El usuario paga un 10 porciento de su sueldo")
