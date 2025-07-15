"""
Módulo para gestionar los registros de mantenimientos de equipos médicos.
"""

"""
Módulo para gestionar los registros de mantenimientos de equipos médicos.
"""

import mysql.connector
from database.conexion_mysql import conexion
from funciones.validaciones import (
    validar_equipo_id,
    validar_no_vacio,
    validar_tipo_mantenimiento
)  # Asumimos que tus funciones están en un módulo llamado validaciones.py

def registrar_mantenimiento(equipo_id, descripcion, tipo, tecnico_id):
    """
    Registra un mantenimiento para un equipo.

    Parámetros:
        equipo_id (str): ID del equipo (ej. ECG-001).
        descripcion (str): Descripción del mantenimiento.
        tipo (str): Tipo de mantenimiento (Preventivo o Correctivo).
        tecnico_id (int): ID del técnico responsable.
    """
    try:
        # Validaciones antes de registrar
        equipo_id = validar_equipo_id(equipo_id)
        descripcion = validar_no_vacio(descripcion, "Descripción")
        tipo = validar_tipo_mantenimiento(tipo)

        conn = conexion()
        cursor = conn.cursor()
        query = """INSERT INTO mantenimientos (equipo_id, descripcion, tipo, tecnico_id, fecha_mantenimiento)
                   VALUES (%s, %s, %s, %s, CURDATE())"""
        cursor.execute(query, (equipo_id, descripcion, tipo, tecnico_id))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Mantenimiento registrado.")
    except ValueError as ve:
        print(f"⚠ Error de validación: {ve}")
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


def actualizar_mantenimiento(mmto_id, campo, nuevo_valor):
    """
    Actualiza un campo de un mantenimiento registrado.

    Parámetros:
        mmto_id (int): ID del mantenimiento.
        campo (str): Campo a modificar ('descripcion', 'tipo', etc).
        nuevo_valor (str): Nuevo valor.
    """
    try:
        # Validaciones según el campo que se modifica
        if campo == "descripcion":
            nuevo_valor = validar_no_vacio(nuevo_valor, "Descripción")
        elif campo == "tipo":
            nuevo_valor = validar_tipo_mantenimiento(nuevo_valor)
        elif campo == "equipo_id":
            nuevo_valor = validar_equipo_id(nuevo_valor)

        conn = conexion()
        cursor = conn.cursor()
        query = f"UPDATE mantenimientos SET {campo} = %s WHERE mmto_id = %s"
        cursor.execute(query, (nuevo_valor, mmto_id))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Mantenimiento actualizado.")
    except ValueError as ve:
        print(f"⚠ Error de validación: {ve}")
    except mysql.connector.Error as err:
        print(f"❌ Error al actualizar mantenimiento: {err}")


def eliminar_mantenimiento(mmto_id):
    """
    Elimina un mantenimiento por su ID.

    Parámetros:
        mmto_id (int): ID del registro de mantenimiento.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        query = "DELETE FROM mantenimientos WHERE mantenimiento_id = %s"
        cursor.execute(query, (mmto_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Mantenimiento eliminado.")
    except mysql.connector.Error as err:
        print(f"❌ Error al eliminar mantenimiento: {err}")