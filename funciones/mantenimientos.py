"""
Módulo para gestionar los registros de mantenimientos de equipos médicos.
"""

import mysql.connector
from database.conexion_mysql import conexion

def registrar_mantenimiento(equipo_id, descripcion, tipo, tecnico):
    """
    Registra un mantenimiento para un equipo.

    Parámetros:
        equipo_id (int): ID del equipo.
        descripcion (str): Descripción del mantenimiento.
        tipo (str): Tipo de mantenimiento (preventivo o correctivo).
        tecnico (str): Nombre del técnico responsable.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        query = """INSERT INTO mantenimientos (equipo_id, descripcion, tipo, tecnico, fecha_mantenimiento)
                   VALUES (%s, %s, %s, %s, CURDATE())"""
        cursor.execute(query, (equipo_id, descripcion, tipo, tecnico))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Mantenimiento registrado.")
    except mysql.connector.Error as err:
        print(f"❌ Error al registrar mantenimiento: {err}")

def ver_mantenimientos():
    """
    Muestra todos los registros de mantenimiento.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mantenimientos")
        for fila in cursor.fetchall():
            print(fila)
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"❌ Error al consultar mantenimientos: {err}")

def actualizar_mantenimiento(mantenimiento_id, campo, nuevo_valor):
    """
    Actualiza un campo de un mantenimiento registrado.

    Parámetros:
        mantenimiento_id (int): ID del mantenimiento.
        campo (str): Campo a modificar.
        nuevo_valor (str): Nuevo valor.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        query = f"UPDATE mantenimientos SET {campo} = %s WHERE mantenimiento_id = %s"
        cursor.execute(query, (nuevo_valor, mantenimiento_id))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Mantenimiento actualizado.")
    except mysql.connector.Error as err:
        print(f"❌ Error al actualizar mantenimiento: {err}")

def eliminar_mantenimiento(mantenimiento_id):
    """
    Elimina un mantenimiento por su ID.

    Parámetros:
        mantenimiento_id (int): ID del registro de mantenimiento.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        query = "DELETE FROM mantenimientos WHERE mantenimiento_id = %s"
        cursor.execute(query, (mantenimiento_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Mantenimiento eliminado.")
    except mysql.connector.Error as err:
        print(f"❌ Error al eliminar mantenimiento: {err}")
