import mysql.connector
from database.conexion_mysql import conectar_mysql

def crear_usuario():
    """
    Registra un nuevo usuario en la base de datos.

    Solicita al usuario por consola el nombre, correo y rol (admin, técnico o ingeniero).
    Luego inserta estos datos en la tabla usuarios.

    Campos requeridos:
    - nombre: Nombre del usuario.
    - correo: Correo electrónico del usuario.
    - rol: Rol que tendrá en el sistema (admin/técnico/ingeniero).

    La conexión a la base de datos se realiza mediante conectar_mysql().
    """
    conn = conectar_mysql()
    cursor = conn.cursor()
    nombre = input("Nombre del usuario: ")
    correo = input("Correo del usuario: ")
    rol = input("Rol del usuario (admin/técnico/ingeniero): ")

    sql = "INSERT INTO usuarios (nombre, correo, rol) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, correo, rol))
    conn.commit()
    print("✅ Usuario registrado con éxito.")
    cursor.close()
    conn.close()

def listar_usuarios():
    """
    Muestra todos los usuarios registrados en la base de datos.

    Recupera los registros de la tabla usuarios y los imprime línea por línea.
    """
    conn = conectar_mysql()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def eliminar_usuario():
    """
    Elimina un usuario de la base de datos a partir de su ID.

    Solicita por consola el ID del usuario a eliminar y ejecuta un comando SQL DELETE.
    
    Requiere que el usuario exista en la tabla usuarios.
    """
    conn = conectar_mysql()
    cursor = conn.cursor()
    id_usuario = input("ID del usuario a eliminar: ")
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
    conn.commit()
    print("🗑 Usuario eliminado.")
    cursor.close()
    conn.close()