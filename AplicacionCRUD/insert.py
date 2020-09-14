from pymongo import MongoClient
#Crear conecciones para la comunicacion con MongoDB
client= MongoClient('localhost:27017')
db=client.EmployeeData

#Funcion para insertar datos en MongoDB
def insert():
    try:
        employeeid=input('Entrada Employee id:')
        employeename=input('Entrada de nombre: ')
        employeeage=input('Entrada de edad: ')
        employeecountry=input('Entrada de pais: ')
        db.Employees.insert_one(
        {
            "id": employeeid,
            "name": employeename,
            "age": employeeage,
            "country": employeecountry
        })
        print('Insercion de datos exitosa')

    except ImportError:
        platform_specific_module= None
        #print str(e)
