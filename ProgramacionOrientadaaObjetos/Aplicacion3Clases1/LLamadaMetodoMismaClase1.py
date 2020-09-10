class Operacion:

    def __init__(self):
        self.valor1=0
        self.valor2=0

    def sumar(self):
        suma=self.valor1+self.valor2
        print("La suma es",suma)

    def restar(self):
        resta=self.valor1-self.valor2
        print("La resta es",resta)

    def multiplicar(self):
        multiplicacion=self.valor1*self.valor2
        print("La multiplicacion es",multiplicacion)

    def dividir(self):
        divicion=self.valor1/self.valor2
        print("La divicion es",divicion)

    def intro_valores(self):
        self.valor1=int(input("Ingresa el primer valor: "))
        self.valor2=int(input("Ingresa el segundo valor: "))

    def main(self):
        self.intro_valores()
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

operacion=Operacion()
operacion.main()
