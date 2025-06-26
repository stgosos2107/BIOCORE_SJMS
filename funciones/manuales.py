import os
from pymongo import MongoClient

def cargar_manuales_a_mongodb():
    """
    Lee los archivos .txt ubicados en la carpeta 'manuales/' y los guarda como documentos
    en la colección 'manuales' de la base de datos MongoDB 'PF_Informatica1'.
    Cada documento contendrá el id del equipo, el nombre del equipo y el contenido del manual.
    """
    # Ruta de la carpeta que contiene los manuales
    carpeta_manuales = "./manuales"

    # Conectar a MongoDB en localhost.
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["PF_Informatica1"]
    coleccion = db["manuales"]

    # Verificar si la carpeta existe
    if not os.path.exists(carpeta_manuales):
        print("La carpeta 'manuales/' no existe.")
        return

    archivos = [f for f in os.listdir(carpeta_manuales) if f.endswith(".txt")]

    if not archivos:
        print("No hay archivos .txt en la carpeta 'manuales/'.")
        return

    for archivo in archivos:
        ruta = os.path.join(carpeta_manuales, archivo)
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()

        # Asumimos que el nombre del archivo es: "001_Electrocardiografo.txt"
        nombre_sin_extension = os.path.splitext(archivo)[0]
        partes = nombre_sin_extension.split("_", 1)

        if len(partes) != 2:
            print(f"Nombre de archivo no válido: {archivo}")
            continue

        equipo_id = partes[0]
        nombre_equipo = partes[1].replace("_", " ")

        documento = {
            "equipo_id": equipo_id,
            "nombre_equipo": nombre_equipo,
            "manual": contenido
        }

        # Insertar en la colección
        coleccion.insert_one(documento)
        print(f"Manual '{archivo}' cargado exitosamente.")

    print("\nCarga completa de manuales a MongoDB.")