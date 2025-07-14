"""
Módulo para mostrar estadísticas básicas de los equipos registrados.
"""

import mysql.connector
from database.conexion_mysql import conexion

def total_equipos():
    """
    Devuelve la cantidad total de equipos registrados en la base de datos.

    Retorna:
        int: Número total de equipos.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM equipos")
        total = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return total
    except mysql.connector.Error as err:
        print(f"Error al obtener estadísticas: {err}")
        return 0

def total_por_marca():
    """
    Devuelve el total de equipos agrupados por marca.

    Retorna:
        list: Lista de tuplas con marca y cantidad.
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT marca, COUNT(*) FROM equipos GROUP BY marca")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return datos
    except mysql.connector.Error as err:
        print(f"Error al obtener estadísticas por marca: {err}")
        return[]
    
def generar_estadisticas():
    """
    Muestra estadísticas básicas de los equipos registrados.
    """
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---\n")

    total = total_equipos()
    print(f"Total de equipos registrados: {total}")

    marcas = total_por_marca()
    print("\nEquipos por marca:")
    for marca, cantidad in marcas:
        print(f"- {marca}: {cantidad} equipos")
