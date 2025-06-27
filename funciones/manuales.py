import os
from database.conexion_mongo import conectar_mongo

def cargar_manual():
    """
    Carga un archivo de manual técnico a la base de datos MongoDB.

    Pasos que realiza:
    1. Solicita el nombre del archivo de manual ubicado en la carpeta 'manuales'.
    2. Verifica que el archivo exista.
    3. Lee el contenido del archivo en formato texto.
    4. Solicita el nombre del equipo al que pertenece el manual.
    5. Inserta el documento en la colección 'manuales' de MongoDB, con los campos:
       - 'equipo': nombre del equipo.
       - 'manual': contenido textual del archivo.

    Si el archivo no existe, se detiene y muestra un mensaje de error.
    """
    db = conectar_mongo()
    coleccion = db["manuales"]
    archivo = input("Nombre del archivo de manual (ej. manual1.txt): ")

    ruta = os.path.join("manuales", archivo)
    if not os.path.exists(ruta):
        print("❌ Archivo no encontrado.")
        return

    with open(ruta, "r", encoding="utf-8") as file:
        contenido = file.read()

    equipo = input("Nombre del equipo asociado: ")
    documento = {"equipo": equipo, "manual": contenido}
    coleccion.insert_one(documento)
    print("✅ Manual cargado en MongoDB.")

def listar_manuales():
    """
    Lista todos los manuales almacenados en MongoDB.

    Recorre la colección 'manuales' y muestra:
    - Nombre del equipo asociado.
    - Primeros 60 caracteres del contenido del manual.

    Esto permite visualizar rápidamente qué manuales están disponibles sin mostrar el contenido completo.
    """
    db = conectar_mongo()
    coleccion = db["manuales"]
    for doc in coleccion.find():
        print(f"📄 {doc['equipo']}: {doc['manual'][:60]}...")

def eliminar_manual():
    """
    Elimina un manual técnico asociado a un equipo específico en MongoDB.

    Pasos que realiza:
    1. Solicita el nombre del equipo cuyo manual se desea eliminar.
    2. Busca y elimina el documento correspondiente en la colección 'manuales'.
    3. Informa si se eliminó correctamente o si no se encontró el manual.

    Esta función se basa en que los manuales están indexados por el nombre del equipo.
    """
    db = conectar_mongo()
    coleccion = db["manuales"]
    equipo = input("Nombre del equipo cuyo manual deseas eliminar: ")
    result = coleccion.delete_one({"equipo": equipo})
    if result.deleted_count:
        print("🗑 Manual eliminado.")
    else:
        print("❌ Manual no encontrado.")