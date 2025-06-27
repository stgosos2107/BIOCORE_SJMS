#Se realiza la importación de las funciones necesarias para el funcionamiento del menu del técnico

from funciones.reportes_mongo import subir_reporte_tecnico, consultar_reportes
from funciones.mantenimientos import registrar_mantenimeinto
from funciones.equipos import ver_equipos, actualizar_equipo 

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
            actualizar_equipo(equipo_id,campo,nuevo_valor)
        elif opcion == "3":
            registrar_mantenimiento(equipo_id,descripcion,tipo,tecnico_id)
        elif opcion == "4":
            subir_reporte_tecnico(tecnico_id)
        elif opcion == "5":
            consultar_reportes()
        elif opcion == "6":
            print("Sesión finalizada.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


