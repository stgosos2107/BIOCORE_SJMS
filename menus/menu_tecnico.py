#Se realiza la importación de las funciones necesarias para el funcionamiento del menu del técnico

from funciones.reportes_mongo import subir_reporte_tecnico, consultar_reportes
from funciones.mantenimientos import registrar_mantenimiento_preventivo,registrar_mantenimiento_correctivo
from funciones.equipos import ver_equipos_asignados

#Este menu permite al técnico realizar diversas acciones relacionadas con el mantenimiento de equipos y la gestión de reportes técnicos.
def menu_tecnico(tecnico_id):
   
    while True:
        print("\n--- Menú Técnico ---")
        print("1. Ver equipos asignados")
        print("2. Registrar mantenimiento preventivo")
        print("3. Registrar mantenimiento correctivo")
        print("4. Subir reporte técnico (MongoDB)")
        print("5. Consultar reportes técnicos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_equipos_asignados(tecnico_id)
        elif opcion == "2":
            registrar_mantenimiento_preventivo(tecnico_id)
        elif opcion == "3":
            registrar_mantenimiento_correctivo(tecnico_id)
        elif opcion == "4":
            subir_reporte_tecnico(tecnico_id)
        elif opcion == "5":
            consultar_reportes()
        elif opcion == "6":
            print("Sesión finalizada.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


