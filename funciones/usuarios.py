import mysql.connector
from database.conexion_mysql import conexion
from funciones.validaciones import validar_no_vacio, validar_correo, validar_rol


def crear_usuario():
    """
    Registra un nuevo usuario en la base de datos.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()

        nombre = validar_no_vacio(input("Nombre del usuario: "), "Nombre")
        correo = validar_correo(validar_no_vacio(input("Correo del usuario: "), "Correo"))
        rol = validar_rol(validar_no_vacio(input("Rol del usuario (admin/técnico/ingeniero): "), "Rol"))

        sql = "INSERT INTO usuarios (nombre, correo, rol) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, correo, rol))
        conn.commit()
        print("✅ Usuario registrado con éxito.")

    except ValueError as ve:
        print(f"⚠ Error de validación: {ve}")
    except mysql.connector.Error as err:
        print(f"❌ Error al registrar usuario: {err}")
    finally:
        cursor.close()
        conn.close()


def listar_usuarios():
    """
    Muestra todos los usuarios registrados en la base de datos.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        for row in cursor.fetchall():
            print(row)
    except mysql.connector.Error as err:
        print(f"❌ Error al listar usuarios: {err}")
    finally:
        cursor.close()
        conn.close()


def eliminar_usuario():
    """
    Elimina un usuario de la base de datos a partir de su ID.
    """
    try:
        id_usuario = input("ID del usuario a eliminar: ")
        if not id_usuario.isdigit() or int(id_usuario) <= 0:
            raise ValueError("El ID debe ser un número entero positivo.")

        conn = conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
        conn.commit()

        if cursor.rowcount == 0:
            print("⚠ No se encontró un usuario con ese ID.")
        else:
            print("🗑 Usuario eliminado con éxito.")

    except ValueError as ve:
        print(f"⚠ Error de validación: {ve}")
    except mysql.connector.Error as err:
        print(f"❌ Error al eliminar usuario: {err}")
    finally:
        cursor.close()
        conn.close()