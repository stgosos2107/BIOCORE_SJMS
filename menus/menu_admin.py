from funciones.tecnicos import agregar_tecnico, listar_tecnicos, modificar_tecnico, eliminar_tecnico
from funciones.busqueda_equipo import buscar_equipo_por_id
from funciones.estadisticas import generar_estadisticas
from funciones.usuarios import crear_usuario, listar_usuarios, eliminar_usuario
from funciones.manuales import cargar_manual, listar_manuales, eliminar_manual
from database.conexion_mysql import conexion

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
            agregar_tecnico()
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


def listar_tecnicos():
    conexion = conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM tecnicos")
        tecnicos = cursor.fetchall()

        if tecnicos:
            print("\n--- LISTADO DE TÉCNICOS ---")
            for t in tecnicos:
                print(f"ID: {t[0]} | Nombre: {t[1]} | Especialidad: {t[2]} | Cédula: {t[3]} | Correo: {t[4]} | Teléfono: {t[5]}")
        else:
            print("No hay técnicos registrados.")
    except Exception as e:
        print(f"❌ Error al listar técnicos: {e}")
    finally:
        cursor.close()
        conexion.close()


def modificar_tecnico():
    conexion = conexion()
    cursor = conexion.cursor()

    tecnico_id = input("ID del técnico a modificar: ")

    print("Ingresa los nuevos datos:")
    nombre = input("Nuevo nombre: ")
    especialidad = input("Nueva especialidad: ")
    cedula = input("Nueva cédula profesional: ")
    correo = input("Nuevo correo: ")
    telefono = input("Nuevo teléfono: ")

    try:
        cursor.execute("""
            UPDATE tecnicos
            SET nombre = %s, especialidad = %s, cedula_profesional = %s, correo = %s, telefono = %s
            WHERE tecnico_id = %s
        """, (nombre, especialidad, cedula, correo, telefono, tecnico_id))
        conexion.commit()
        print("✅ Técnico actualizado correctamente.")
    except Exception as e:
        print(f"❌ Error al modificar técnico: {e}")
    finally:
        cursor.close()
        conexion.close()


def eliminar_tecnico():
    conexion = conexion()
    cursor = conexion.cursor()

    tecnico_id = input("ID del técnico a eliminar: ")

    try:
        cursor.execute("DELETE FROM tecnicos WHERE tecnico_id = %s", (tecnico_id,))
        conexion.commit()
        print("✅ Técnico eliminado correctamente.")
    except Exception as e:
        print(f"❌ Error al eliminar técnico: {e}")
    finally:
        cursor.close()
        conexion.close()


def menu_ingenieros():
    """
    Menú CRUD para gestionar ingenieros biomédicos.
    """
    while True:
        print("\n--- MENÚ INGENIEROS ---")
        print("1. Registrar ingeniero")
        print("2. Listar ingenieros")
        print("3. Modificar ingeniero")
        print("4. Eliminar ingeniero")
        print("5. Volver al menú anterior")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_ingeniero()
        elif opcion == "2":
            listar_ingenieros()
        elif opcion == "3":
            modificar_ingeniero()
        elif opcion == "4":
            eliminar_ingeniero()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


def registrar_ingeniero():
    conexion = conexion()
    cursor = conexion.cursor()

    nombre = input("Nombre completo: ")
    especialidad = input("Especialidad: ")
    cedula = input("Cédula profesional (solo números): ")
    correo = input("Correo institucional (@biocore.com): ")
    telefono = input("Teléfono: ")

    try:
        cursor.execute("""
            INSERT INTO ingenieros (nombre, especialidad, cedula_profesional, correo, telefono)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, especialidad, cedula, correo, telefono))
        conexion.commit()
        print("✅ Ingeniero registrado exitosamente.")
    except Exception as e:
        print(f"❌ Error al registrar ingeniero: {e}")
    finally:
        cursor.close()
        conexion.close()


def listar_ingenieros():
    conexion = conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM ingenieros")
        ingenieros = cursor.fetchall()

        if ingenieros:
            print("\n--- LISTADO DE INGENIEROS ---")
            for i in ingenieros:
                print(f"ID: {i[0]} | Nombre: {i[1]} | Especialidad: {i[2]} | Cédula: {i[3]} | Correo: {i[4]} | Teléfono: {i[5]}")
        else:
            print("No hay ingenieros registrados.")
    except Exception as e:
        print(f"❌ Error al listar ingenieros: {e}")
    finally:
        cursor.close()
        conexion.close()


def modificar_ingeniero():
    conexion = conexion()
    cursor = conexion.cursor()

    id_ing = input("ID del ingeniero a modificar: ")

    print("Ingrese los nuevos datos:")
    nombre = input("Nuevo nombre: ")
    especialidad = input("Nueva especialidad: ")
    cedula = input("Nueva cédula profesional: ")
    correo = input("Nuevo correo: ")
    telefono = input("Nuevo teléfono: ")

    try:
        cursor.execute("""
            UPDATE ingenieros
            SET nombre = %s, especialidad = %s, cedula_profesional = %s, correo = %s, telefono = %s
            WHERE ingeniero_id = %s
        """, (nombre, especialidad, cedula, correo, telefono, id_ing))
        conexion.commit()
        print("✅ Ingeniero actualizado correctamente.")
    except Exception as e:
        print(f"❌ Error al modificar ingeniero: {e}")
    finally:
        cursor.close()
        conexion.close()


def eliminar_ingeniero():
    conexion = conexion()
    cursor = conexion.cursor()

    id_ing = input("ID del ingeniero a eliminar: ")

    try:
        cursor.execute("DELETE FROM ingenieros WHERE ingeniero_id = %s", (id_ing,))
        conexion.commit()
        print("✅ Ingeniero eliminado correctamente.")
    except Exception as e:
        print(f"❌ Error al eliminar ingeniero: {e}")
    finally:
        cursor.close()
        conexion.close()


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
        print("1. Gestionar usuarios (técnicos / ingenieros)")
        print("2. Manuales técnicos")
        print("3. Buscar equipos")
        print("4. Generar estadísticas")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            while True:
                print("\n--- Gestión de usuarios ---")
                print("1. Registrar técnico")
                print("2. Registrar ingeniero")
                print("3. Volver al menú anterior")
                subopcion = input("Selecciona una opción: ")

                if subopcion == "1":
                    menu_tecnicos()
                elif subopcion == "2":
                    menu_ingenieros()
                elif subopcion == "3":
                    break
                else:
                    print("Opción no válida.")

        elif opcion == "2":
            menu_manuales()

        elif opcion == "3":
            buscar_equipo_por_id()

        elif opcion == "4":
            generar_estadisticas()

        elif opcion == "5":
            print("Saliendo del menú administrador.")
            break

        else:
            print("Opción no válida.")
