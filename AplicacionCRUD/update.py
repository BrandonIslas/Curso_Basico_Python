from pymongo import MongoClient
#Crear conecciones para la comunicacion con MongoDB
client = MongoClient('localhost:27017')
db=client.EmployeeData

#Funcion para Actualizar los registros en MongoDB

def update():
    try:
        criteria=input('\n Entrada de id para actualizar \n')
        name=input('\n Entrada de nombre para actualizar \n')
        age= input('\n Entrada de la edad para actualizar \n')
        country = input('\n ENtrada del pais para actualizar \n')

        db.Employees.update_one(
        {"id": criteria},
        {
            "$set":{
                "name": name,
                "age": age,
                "country": country
            }
        }
        )
        print('\n Registros actualizados correctamente \n')
    except ImportError:
        platform_specific_module=None
