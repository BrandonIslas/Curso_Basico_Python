nota1=int(input("Ingrese la 1 nota:"))
nota2=int(input("Ingrese la 2 nota:"))
nota3=int(input("Ingrese la 3 nota:"))

prom=(nota1+nota2+nota3)/3

if prom>=7:
    print("Muy bien")
else:
    if prom>=6:
        print("Acredito")
    else:
        print("Reprobado")
