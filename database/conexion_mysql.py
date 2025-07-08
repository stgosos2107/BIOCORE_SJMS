"""
Módulo de conexión a la base de datos MySQL para el sistema BIOCORE_SMJS.

Este archivo define una función para establecer la conexión con la base de datos
`PF_Informatica1`, utilizando el conector mysql.connector. También incluye una 
prueba directa de conexión que puede ejecutarse como script principal.
"""

import mysql.connector
from mysql.connector import Error

def conexion():
    """
    Establece una conexión con la base de datos MySQL del proyecto.

    Returns:
        mysql.connector.connection.MySQLConnection:
            Objeto de conexión si es exitosa.
        None:
            Si ocurre un error durante la conexión.

    Lanza:
        Error: Si no es posible conectar con la base de datos.
    """
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='informatica1',
            password='info2025_2',
            database='PF_Informatica1'
        )
        if conexion.is_connected():
            print("✅ Conexión exitosa a MySQL.")
            return conexion
    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None

# Prueba directa de conexión al ejecutar este archivo
if __name__ == "__main__":
    """
    Prueba de ejecución directa para verificar que la conexión a la base de datos 
    se establece correctamente.
    """
    conexion = conexion()
    if conexion:
        conexion.close()
