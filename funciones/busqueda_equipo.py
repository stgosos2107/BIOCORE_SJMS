"""
Módulo para buscar equipos por ID en la base de datos MySQL.
"""

import mysql.connector
from database.conexion_mysql import conexion

def buscar_equipo_por_id(equipo_id):
    """
    Busca un equipo en la base de datos MySQL usando su ID.

    Parámetros:
        equipo_id (int): ID del equipo a buscar.

    Retorna:
        dict: Información del equipo si se encuentra, None en caso contrario.
    """
    try:
        conn = conexion()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM equipos WHERE equipo_id = %s"
        cursor.execute(query, (equipo_id,))
        equipo = cursor.fetchone()
        cursor.close()
        conn.close()
        return equipo
    except mysql.connector.Error as err:
        print(f"Error al buscar equipo: {err}")
        return None
