import insert
import read
import update
import delete

class Programa:
    def __init__(self):
        self.dato=1

    def menu(self):

        while self.dato:
            selecction = input("\n Selecciona una de las opciones del menu \n 1.- Insertar \n 2.- Leer \n 3.-Actualizar \n 4.-Borrar \n\n")
            if selecction=='1':
                insert.insert()
            elif selecction=='2':
                read.read()
            elif selecction=='3':
                update.update()
            elif selecction=='4':
                delete.delete()
            else:
                print("Instruccion invalida")

persona1 = Programa()
persona1.menu()
