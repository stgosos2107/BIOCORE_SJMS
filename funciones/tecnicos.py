"""
Módulo para CRUD de técnicos en la base de datos.
"""

import mysql.connector
from database.conexion_mysql import conexion
from validaciones import validar_no_vacio  # Se asume que está en validaciones.py

def agregar_tecnico(nombre, especialidad):
    """
    Agrega un técnico a la base de datos.

    Parámetros:
        nombre (str): Nombre del técnico.
        especialidad (str): Especialidad del técnico.
    """
    try:
        nombre = validar_no_vacio(nombre, "Nombre del técnico")
        especialidad = validar_no_vacio(especialidad, "Especialidad del técnico")

        conn = conexion()
        cursor = conn.cursor()
        query = "INSERT INTO tecnicos (nombre, especialidad) VALUES (%s, %s)"
        cursor.execute(query, (nombre, especialidad))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Técnico agregado con éxito.")
    except ValueError as ve:
        print(f"⚠ Error de validación: {ve}")
    except mysql.connector.Error as err:
        print(f"❌ Error al agregar técnico: {err}")


def listar_tecnicos():
    """
    Lista todos los técnicos registrados.

    Retorna:
        list: Lista de tuplas con la información de los técnicos.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tecnicos")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return datos
    except mysql.connector.Error as err:
        print(f"❌ Error al listar técnicos: {err}")
        return []


def eliminar_tecnico(tecnico_id):
    """
    Elimina un técnico de la base de datos por su ID.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tecnicos WHERE tecnico_id = %s", (tecnico_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print("🗑 Técnico eliminado con éxito.")
    except mysql.connector.Error as err:
        print(f"❌ Error al eliminar técnico: {err}")


def modificar_tecnico(tecnico_id, nuevo_nombre, nueva_especialidad):
    """
    Modifica el nombre y/o especialidad de un técnico.
    """
    try:
        nuevo_nombre = validar_no_vacio(nuevo_nombre, "Nuevo nombre del técnico")
        nueva_especialidad = validar_no_vacio(nueva_especialidad, "Nueva especialidad")

        conn = conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tecnicos SET nombre = %s, especialidad = %s WHERE tecnico_id = %s",
            (nuevo_nombre, nueva_especialidad, tecnico_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Técnico modificado con éxito.")
    except ValueError as ve:
        print(f"⚠ Error de validación: {ve}")
    except mysql.connector.Error as err:
        print(f"❌ Error al modificar técnico: {err}")