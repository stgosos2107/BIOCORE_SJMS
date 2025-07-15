"""
Módulo para buscar equipos por ID en la base de datos MySQL.
"""

from funciones.validaciones import validar_equipo_id
from database.conexion_mysql import conexion

def buscar_equipo_por_id(equipo_id):
    """
    Busca un equipo en la base de datos MySQL usando su ID con formato ABC-123.

    Parámetros:
        equipo_id (str): ID del equipo a buscar.

    Retorna:
        dict: Información del equipo si se encuentra, None en caso contrario.
    """
    try:
        # Validar el formato del ID (ej: ECG-001)
        equipo_id = validar_equipo_id(equipo_id)

        # Conectarse a la base de datos y buscar el equipo
        conn = conexion()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM equipos WHERE equipo_id = %s"
        cursor.execute(query, (equipo_id,))
        equipo = cursor.fetchone()

        # Cerrar conexión
        cursor.close()
        conn.close()
        return equipo

    except ValueError as ve:
        print(f"⚠ Error de validación: {ve}")
        return None
