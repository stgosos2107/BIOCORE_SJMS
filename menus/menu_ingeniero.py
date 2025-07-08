
# menu_ingeniero
# Este módulo define el menú para el rol de ingeniero, permitiendo ver equipos, mantenimientos, reportes y bitácoras.
from funciones.equipos import ver_equipos
from funciones.mantenimientos import ver_mantenimientos
from funciones.reportes_mongo import consultar_reportes
# Función para mostrar el menú del ingeniero
# y permitirle interactuar con las funcionalidades del sistema.


def menu_ingeniero():
    while True:
        print("\n--- Menú Ingeniero ---")
        print("1. Ver Equipos")   
        print("2. Ver Mantenimientos")
        print("3. Ver Reportes")
        print("4. Cerrar Sesión")                                                                                                                                                                                                                                                                                                                                 
        opcion = input("Elija una opción: ")

        if opcion == "1":
            ver_equipos()
        elif opcion == "2":
            ver_mantenimientos()
        elif opcion == "3":
            consultar_reportes()
        elif opcion == "4":
            print("Cerrando sesión...")
            break
            
        


