"""
Módulo para realizar operaciones CRUD sobre la tabla de equipos.
"""

import mysql.connector
from database.conexion_mysql import conexion
from validaciones import (
    validar_no_vacio,
    validar_estado,
    validar_id_numerico
)

def insertar_equipo(nombre, marca, modelo, ubicacion, estado, manual):
    """
    Inserta un nuevo equipo en la base de datos.
    """
    try:
        # Validaciones
        nombre = validar_no_vacio(nombre, "Nombre del equipo")
        marca = validar_no_vacio(marca, "Marca")
        modelo = validar_no_vacio(modelo, "Modelo")
        ubicacion = validar_no_vacio(ubicacion, "Ubicación")
        estado = validar_estado(estado)
        manual = manual.strip() if manual else None  # Manual puede ser opcional

        conn = conexion()
        cursor = conn.cursor()
        query = """INSERT INTO equipos (nombre, marca, modelo, ubicacion, estado, manual, fecha_ingreso)
                   VALUES (%s, %s, %s, %s, %s, %s, CURDATE())"""
        cursor.execute(query, (nombre, marca, modelo, ubicacion, estado, manual))
        conn.commit()
        print("✅ Equipo registrado con éxito.")
    except ValueError as ve:
        print(f"⚠ Error de validación: {ve}")
    except mysql.connector.Error as err:
        print(f"❌ Error al insertar equipo: {err}")
    finally:
        cursor.close()
        conn.close()


def ver_equipos():
    """
    Muestra todos los equipos registrados en la base de datos.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM equipos")
        for fila in cursor.fetchall():
            print(fila)
    except mysql.connector.Error as err:
        print(f"❌ Error al consultar equipos: {err}")
    finally:
        cursor.close()
        conn.close()


def actualizar_equipo(equipo_id, campo, nuevo_valor):
    """
    Actualiza un campo específico de un equipo.
    """
    try:
        equipo_id = validar_id_numerico(str(equipo_id), "ID del equipo")

        conn = conexion()
        cursor = conn.cursor()
        query = f"UPDATE equipos SET {campo} = %s WHERE equipo_id = %s"
        cursor.execute(query, (nuevo_valor, equipo_id))
        conn.commit()
        print("✅ Equipo actualizado.")
    except ValueError as ve:
        print(f"⚠ Error de validación: {ve}")
    except mysql.connector.Error as err:
        print(f"❌ Error al actualizar equipo: {err}")
    finally:
        cursor.close()
        conn.close()


def eliminar_equipo(equipo_id):
    """
    Elimina un equipo de la base de datos.
    """
    try:
        equipo_id = validar_id_numerico(str(equipo_id), "ID del equipo")

        conn = conexion()
        cursor = conn.cursor()
        query = "DELETE FROM equipos WHERE equipo_id = %s"
        cursor.execute(query, (equipo_id,))
        conn.commit()
        if cursor.rowcount:
            print("✅ Equipo eliminado.")
        else:
            print("⚠ No se encontró ningún equipo con ese ID.")
    except ValueError as ve:
        print(f"⚠ Error de validación: {ve}")
    except mysql.connector.Error as err:
        print(f"❌ Error al eliminar equipo: {err}")
    finally:
        cursor.close()
        conn.close()