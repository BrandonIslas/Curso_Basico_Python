from pymongo import MongoClient
#Crear conecciones para la comunicacion con MongoDB
client=MongoClient('localhost:27017')
db=client.EmployeeData

#Funcion para leer registros de MongoDB
def read():
    try:
        empcol=db.Employees.find()
        print('\n Datos de EmployeeData de la Base de datos \n')
        for emp in empcol:
            print(emp)

    except ImportError:
        platform_specific_module=None
        #print str(e)
