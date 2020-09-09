nota1=int(input("Ingrese la 1 nota:"))
nota2=int(input("Ingrese la 2 nota:"))
nota3=int(input("Ingrese la 3 nota:"))
prom=(nota1+nota2+nota3)/3

if prom ==9 or prom==10:
    print("Excelente")
elif prom==6:
    print("Suficiente")
elif prom==5:
    print("Reprobado")
elif prom == 7 or prom== 8:
    print("Bien")
else:
    print("Reprobado")
