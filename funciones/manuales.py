import os
from database.conexion_mongo import conectar_mongo
from validaciones import validar_no_vacio  # Usamos la validación que ya definiste

def cargar_manual():
    """
    Carga un archivo de manual técnico a la base de datos MongoDB.
    """
    db = conectar_mongo()
    coleccion = db["manuales"]

    try:
        archivo = input("Nombre del archivo de manual (ej. manual1.txt): ")
        archivo = validar_no_vacio(archivo, "Archivo")

        ruta = os.path.join("manuales", archivo)
        if not os.path.exists(ruta):
            print("❌ Archivo no encontrado.")
            return

        with open(ruta, "r", encoding="utf-8") as file:
            contenido = file.read()

        equipo = input("Nombre del equipo asociado: ")
        equipo = validar_no_vacio(equipo, "Equipo")

        documento = {"equipo": equipo, "manual": contenido}
        coleccion.insert_one(documento)
        print("✅ Manual cargado en MongoDB.")

    except ValueError as ve:
        print(f"⚠ Error de validación: {ve}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def listar_manuales():
    """
    Lista todos los manuales almacenados en MongoDB.
    """
    db = conectar_mongo()
    coleccion = db["manuales"]

    try:
        for doc in coleccion.find():
            equipo = doc.get('equipo', 'Sin nombre')
            preview = doc.get('manual', '')[:60]
            print(f"📄 {equipo}: {preview}...")
    except Exception as e:
        print(f"❌ Error al listar manuales: {e}")


def eliminar_manual():
    """
    Elimina un manual técnico asociado a un equipo específico en MongoDB.
    """
    db = conectar_mongo()
    coleccion = db["manuales"]

    try:
        equipo = input("Nombre del equipo cuyo manual deseas eliminar: ")
        equipo = validar_no_vacio(equipo, "Equipo")

        result = coleccion.delete_one({"equipo": equipo})
        if result.deleted_count:
            print("🗑 Manual eliminado.")
        else:
            print("❌ Manual no encontrado.")

    except ValueError as ve:
        print(f"⚠ Error de validación: {ve}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")