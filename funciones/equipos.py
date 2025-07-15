"""
Módulo para realizar operaciones CRUD sobre la tabla de equipos.
"""
from database.conexion_mysql import conexion
import mysql.connector
from validaciones import validar_no_vacio, validar_estado  
def insertar_equipo(nombre, marca, modelo, ubicacion, estado, manual):
    """
    Inserta un nuevo equipo en la base de datos, validando los campos básicos.

    Parámetros:
        nombre (str): Nombre del equipo.
        marca (str): Marca del equipo.
        modelo (str): Modelo del equipo.
        ubicacion (str): Ubicación dentro del hospital.
        estado (str): Estado actual del equipo.
        manual (str): Ruta al archivo del manual (opcional).
    """
    try:
        # Validaciones
        nombre = validar_no_vacio(nombre, "Nombre")
        marca = validar_no_vacio(marca, "Marca")
        modelo = validar_no_vacio(modelo, "Modelo")
        ubicacion = validar_no_vacio(ubicacion, "Ubicación")
        estado = validar_estado(estado)

        # Inserción en base de datos
        conn = conexion()
        cursor = conn.cursor()
        query = """INSERT INTO equipos (nombre, marca, modelo, ubicacion, estado, manual, fecha_ingreso)
                   VALUES (%s, %s, %s, %s, %s, %s, CURDATE())"""
        cursor.execute(query, (nombre, marca, modelo, ubicacion, estado, manual))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Equipo registrado con éxito.")
    except ValueError as ve:
        print(f"⚠ Error de validación: {ve}")
    except mysql.connector.Error as err:
        print(f"❌ Error al insertar equipo: {err}")