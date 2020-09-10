class Alumno:

    def declarar(self,nombre,dato):
        self.nombre=nombre
        self.puntuacion=dato

    def visualizar(self):
        print("Nombre: ",self.nombre)
        print("Puntuacion: ",self.puntuacion)

    def estadistica(self):
        if self.puntuacion <=5.9:
            print("Insuficiente")
        elif self.puntuacion>=6 and self.puntuacion <=7.9:
            print("Suficiente")
        elif self.puntuacion>=8:
            print("Exelente")
        else:
            print("Libre")

#Bloque principal
alumno1=Alumno()
alumno1.declarar("Diego",2)
alumno1.visualizar()
alumno1.estadistica()

alumno2=Alumno()
alumno2.declarar("Ana",10)
alumno2.visualizar()
alumno2.estadistica()     
