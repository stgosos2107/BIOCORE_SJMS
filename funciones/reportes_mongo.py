# Se importan las funciones necesarias para el funcionamiento del menú del técnico
# funciones/reportes_mongo.py

from database.conexion_mongo import conectar_mongo
from datetime import datetime

#Función para subir un reporte técnico a MongoDB
def subir_reporte_tecnico(tecnico_id):
    coleccion = conectar_mongo()
    if not coleccion:
        print("No se pudo acceder a la base de datos.")
        return

    try:
        mmto_id = input("ID del mantenimiento (mmto_id): ")
        equipo_id = input("ID del equipo: ")
        nombre_equipo = input("Nombre del equipo: ")
        tipo_reporte = input("Tipo de reporte (Preventivo/Correctivo): ")
        resumen = input("Resumen del mantenimiento: ")

        notas_tecnicas = []
        print("Ingrese las notas técnicas (escriba 'fin' para terminar):")
        while True:
            nota = input("→ ")
            if nota.lower() == 'fin':
                break
            notas_tecnicas.append(nota)

        estado = input("Estado del equipo tras el mantenimiento: ")

        rutas = {
            "imagen_antes": input("Ruta imagen antes: "),
            "imagen_despues": input("Ruta imagen después: "),
            "reporte_pdf": input("Ruta del PDF del reporte: "),
            "guia_pdf": input("Ruta de la guía rápida: "),
            "manual_pdf": input("Ruta del manual técnico: ")
        }

        nuevo_reporte = {
            "reporte_id": f"rep-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            "mmto_id": mmto_id,
            "equipo_id": equipo_id,
            "nombre_equipo": nombre_equipo,
            "Tipo_reporte": tipo_reporte,
            "reporte_fecha": datetime.utcnow().isoformat(),
            "tecnico_id": tecnico_id,
            "Resumen": resumen,
            "Notas_tecnicas": notas_tecnicas,
            "estado": estado,
            "Rutas": rutas
        }

        coleccion.insert_one(nuevo_reporte)
        print("Reporte técnico guardado correctamente en MongoDB.")

    except Exception as e:
        print(f"Error al subir el reporte: {e}")



#Funcion para consultar reportes técnicos en MongoDB
#Permite buscar reportes técnicos en MongoDB por palabra clave o por campo específico.
def consultar_reportes():

    coleccion = conectar_mongo()
    if not coleccion:
        print("No se pudo acceder a la base de datos.")
        return

    print("\n--- Consulta de Reportes Técnicos ---")
    print("1. Buscar por palabra clave en resumen o notas técnicas")
    print("2. Buscar por campo exacto (ej: equipo_id, estado, tipo de reporte)")
    opcion = input("Seleccione tipo de búsqueda (1 o 2): ")

    try:
        if opcion == "1":
            palabra = input("Ingrese la palabra clave que desea buscar: ").lower()
            resultados = []

            for reporte in coleccion.find():
                resumen = reporte.get("Resumen", "").lower()
                notas = [n.lower() for n in reporte.get("Notas_tecnicas", [])]

                if palabra in resumen or any(palabra in nota for nota in notas):
                    resultados.append(reporte)

        elif opcion == "2":
            campo = input("Ingrese el nombre del campo (por ejemplo: equipo_id, estado): ")
            valor = input(f"Ingrese el valor que desea buscar en '{campo}': ")

            resultados = list(coleccion.find({campo: valor}))

        else:
            print("Opción no válida.")
            return

        print("\n--- Resultados encontrados ---")
        if resultados:
            for reporte in resultados:
                print(f"Reporte ID: {reporte.get('reporte_id', 'N/A')}")
                print(f"Equipo: {reporte.get('nombre_equipo', 'N/A')} | Estado: {reporte.get('estado', 'N/A')}")
                print(f"Resumen: {reporte.get('Resumen', '')}")
                print("-" * 40)
        else:
            print("No se encontraron reportes que coincidan con la búsqueda.")

    except Exception as e:
        print(f"Error al consultar los reportes: {e}")
