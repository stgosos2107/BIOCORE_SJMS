import json
import os
from validaciones import validar_no_vacio  
from database.conexion_mongo import conectar_mongo

def cargar_reportes_completos_json():
    """
    Carga un archivo JSON con reportes completos a la colección 'reportes_tecnicos' de MongoDB.
    Valida que el nombre del archivo no esté vacío y que el archivo exista.
    """
    db = conectar_mongo()
    coleccion = db["reportes_tecnicos"]

    try:
        archivo = input("Nombre del archivo JSON (ej. reportes_completos.json): ")
        archivo = validar_no_vacio(archivo, "Nombre del archivo JSON")
        ruta = os.path.join("datos", archivo)

        if not os.path.exists(ruta):
            print("❌ Archivo no encontrado en la carpeta 'datos'.")
            return

        with open(ruta, "r", encoding="utf-8") as file:
            datos = json.load(file)

        if not isinstance(datos, list):
            print("⚠ El archivo debe contener una lista de objetos JSON.")
            return

        for doc in datos:
            if "reporte_id" not in doc or "Rutas" not in doc:
                print("❌ Documento inválido: falta 'reporte_id' o 'Rutas'. Revisa la estructura.")
                return

        resultado = coleccion.insert_many(datos)
        print(f"✅ {len(resultado.inserted_ids)} reportes cargados correctamente.")

    except ValueError as ve:
        print(f"Error de validación: {ve}")
    except json.JSONDecodeError:
        print("❌ Error al parsear el archivo JSON. Verifica que esté bien formateado.")