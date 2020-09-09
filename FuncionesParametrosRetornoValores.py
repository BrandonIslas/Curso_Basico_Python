def retornar(d1,d2):
    if d1 > d2:
        m=d1
    else:
        m=d2
    return m

d1=34
d2=56
print(retornar(d1,d2))
valor=retornar(d1,d2)
print("EL valor mayor es:",valor)
