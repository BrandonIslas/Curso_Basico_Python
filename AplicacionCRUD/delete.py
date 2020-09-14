from pymongo import MongoClient
#Crear conecciones para la comunicacion con MongoDB
client = MongoClient('localhost:27017')
db=client.EmployeeData

#Funcion para borrar registros de MongoDB
def delete():
    try:
        criteria=input('\n Enter Employee id to delete \n')
        db.Employees.delete_many({"id": criteria})
        print('\n Borrado Satisfactorio \n')
    except ImportError:
        platform_specific_module=None
        #print str(e)
