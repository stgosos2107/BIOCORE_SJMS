#Se realiza la importación de las funciones necesarias para el funcionamiento del menu del técnico

from funciones.reportes_mongo import subir_reporte_tecnico, consultar_reportes
from funciones.mantenimientos import registrar_mantenimiento
from funciones.equipos import ver_equipos, actualizar_equipo 
from funciones.carga_json_mongo import cargar_reportes_completos_json

#Este menu permite al técnico realizar diversas acciones relacionadas con el mantenimiento de equipos y la gestión de reportes técnicos.
def menu_tecnico(tecnico_id):
   
    while True:
        print("\n--- Menú Técnico ---")
        print("1. Ver equipos asignados")
        print("2. Actualizar estado de un equipo")
        print("3. Registrar mantenimiento")
        print("4. Subir reporte técnico (MongoDB)")
        print("5. Consultar reportes técnicos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_equipos()
        elif opcion == "2":
            equipo_id = input("Ingrese el ID del equipo: ")
            campo = input("Campo a actualizar (nombre, marca, etc.): ")
            nuevo_valor = input("Nuevo valor: ")
            actualizar_equipo(equipo_id, campo, nuevo_valor)
        elif opcion == "3":
            equipo_id = input("Ingrese el ID del equipo: ")
            descripcion = input("Ingrese la descripción del mantenimiento: ")
            tipo = input("Ingrese el tipo de mantenimiento: ")
            registrar_mantenimiento(equipo_id, descripcion, tipo, tecnico_id)
        elif opcion == "4":
            print("\n--- Generar Reporte Técnico ---")
            print("\n--- Cargar archivo de reporte ---")
            opcion_reporte = input("Selecciona una opción:\n1. Subir reporte técnico\n2. Subir reporte técnico con bitácora\n")
            if opcion_reporte == "1":
                subir_reporte_tecnico(tecnico_id)
            elif opcion_reporte == "2":
                cargar_reportes_completos_json()
                print("Subiendo reporte técnico del documento json a MongoDB...")
        elif opcion == "5":
            consultar_reportes()
        elif opcion == "6":
            print("Sesión finalizada.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


