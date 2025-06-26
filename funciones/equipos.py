"""
Módulo para realizar operaciones CRUD sobre la tabla de equipos.
"""

import mysql.connector
from database.conexion_mysql import conexion

def insertar_equipo(nombre, marca, modelo, ubicacion, estado, manual):
    """
    Inserta un nuevo equipo en la base de datos.

    Parámetros:
        nombre (str): Nombre del equipo.
        marca (str): Marca del equipo.
        modelo (str): Modelo del equipo.
        ubicacion (str): Ubicación dentro del hospital.
        estado (str): Estado actual del equipo.
        manual (str): Ruta al archivo del manual (opcional).
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        query = """INSERT INTO equipos (nombre, marca, modelo, ubicacion, estado, manual, fecha_ingreso)
                   VALUES (%s, %s, %s, %s, %s, %s, CURDATE())"""
        cursor.execute(query, (nombre, marca, modelo, ubicacion, estado, manual))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Equipo registrado con éxito.")
    except mysql.connector.Error as err:
        print(f"❌ Error al insertar equipo: {err}")

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
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"❌ Error al consultar equipos: {err}")

def actualizar_equipo(equipo_id, campo, nuevo_valor):
    """
    Actualiza un campo específico de un equipo.

    Parámetros:
        equipo_id (int): ID del equipo a actualizar.
        campo (str): Nombre del campo a modificar.
        nuevo_valor (str): Nuevo valor que se asignará.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        query = f"UPDATE equipos SET {campo} = %s WHERE equipo_id = %s"
        cursor.execute(query, (nuevo_valor, equipo_id))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Equipo actualizado.")
    except mysql.connector.Error as err:
        print(f"❌ Error al actualizar equipo: {err}")

def eliminar_equipo(equipo_id):
    """
    Elimina un equipo de la base de datos.

    Parámetros:
        equipo_id (int): ID del equipo a eliminar.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        query = "DELETE FROM equipos WHERE equipo_id = %s"
        cursor.execute(query, (equipo_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Equipo eliminado.")
    except mysql.connector.Error as err:
        print(f"❌ Error al eliminar equipo: {err}")
