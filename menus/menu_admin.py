from funciones.tecnicos import crear_tecnico, listar_tecnicos, modificar_tecnico, eliminar_tecnico
from funciones.busqueda_equipo import buscar_equipo
from funciones.estadisticas import generar_estadisticas
from funciones.usuarios import crear_usuario, listar_usuarios, eliminar_usuario
from funciones.manuales import cargar_manual, listar_manuales, eliminar_manual

def menu_tecnicos():
    """
    Despliega el submenú para gestionar técnicos con opciones CRUD.
    """
    while True:
        print("\n--- GESTIÓN DE TÉCNICOS ---")
        print("1. Registrar técnico")
        print("2. Listar técnicos")
        print("3. Modificar técnico")
        print("4. Eliminar técnico")
        print("5. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_tecnico()
        elif opcion == "2":
            listar_tecnicos()
        elif opcion == "3":
            modificar_tecnico()
        elif opcion == "4":
            eliminar_tecnico()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

def menu_usuarios():
    """
    Despliega el submenú para crear, listar o eliminar usuarios.
    """
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Eliminar usuario")
        print("4. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def menu_manuales():
    """
    Despliega el submenú para gestionar los manuales técnicos.
    """
    while True:
        print("\n--- MANUALES TÉCNICOS ---")
        print("1. Cargar manual")
        print("2. Listar manuales")
        print("3. Eliminar manual")
        print("4. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            cargar_manual()
        elif opcion == "2":
            listar_manuales()
        elif opcion == "3":
            eliminar_manual()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def menu_admin():
    """
    Menú principal del administrador. Accede a las diferentes funciones del sistema.
    """
    while True:
        print("\n=== MENÚ ADMINISTRADOR ===")
        print("1. Gestionar técnicos")
        print("2. Gestionar usuarios")
        print("3. Manuales técnicos")
        print("4. Buscar equipos")
        print("5. Generar estadísticas")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            menu_tecnicos()
        elif opcion == "2":
            menu_usuarios()
        elif opcion == "3":
            menu_manuales()
        elif opcion == "4":
            buscar_equipo()
        elif opcion == "5":
            generar_estadisticas()
        elif opcion == "6":
            print("Saliendo del menú administrador.")
            break
        else:
            print("Opción no válida.")