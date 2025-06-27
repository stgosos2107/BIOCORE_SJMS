
#Importación para la conexión a MongoDB
from pymongo import MongoClient


#Función para conectar a la base de datos MongoDB en cada uno de los casos que esta se requiera
def conectar_mongo():
   
    try:
        cliente = MongoClient("mongodb://localhost:27017/")
        db = cliente["PF_Informatica1"]
        coleccion = db["reportes_tecnicos"]
        return coleccion
    
    except Exception as e:
        print(f"Error al conectar con MongoDB: {e}")
        return None