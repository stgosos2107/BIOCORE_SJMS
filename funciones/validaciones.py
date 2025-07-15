import re  # Módulo para trabajar con expresiones regulares
from datetime import datetime  # Para validar y convertir fechas
from database.conexion_mysql import conectar_mysql

def validar_admin(usuario, contrasena):
    conexion = conectar_mysql()
    cursor = conexion.cursor(dictionary=True)

    query = "SELECT * FROM administradores WHERE usuario = %s AND contrasena = %s"
    cursor.execute(query, (usuario, contrasena))
    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()
    return resultado is not None
# Valida que el correo tenga un formato correcto
def validar_correo(correo):
    """
    Valida que el correo tenga un formato correcto.
    """
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(patron, correo):
        raise ValueError("El correo electrónico no tiene un formato válido.")
    return correo
# Valida que el rol del usuario sea uno de los permitidos
def validar_rol(rol):
    roles_validos = ["admin", "técnico", "ingeniero"]
    if rol.lower() not in roles_validos:
        raise ValueError(f"Rol inválido. Debe ser uno de: {', '.join(roles_validos)}.")
    return rol.lower()
# Valida que un campo no esté vacío (ni solo espacios)
def validar_no_vacio(campo, nombre_campo):
    if not campo.strip():  # Si el campo está vacío después de quitar espacios
        raise ValueError(f"El campo '{nombre_campo}' no puede estar vacío.")  # Lanza error
    return campo.strip()  # Retorna el texto limpio

# Valida que la fecha tenga el formato correcto: AAAA-MM-DD
def validar_fecha(fecha_str):
    try:
        return datetime.strptime(fecha_str, "%Y-%m-%d")  # Intenta convertir a fecha
    except ValueError:
        raise ValueError("La fecha debe tener el formato AAAA-MM-DD.")

# Valida el formato del ID del equipo (por ejemplo ECG-001)
def validar_equipo_id(equipo_id):
    if not re.match(r"^[A-Z]{3}-\d{3}$", equipo_id):  # Expresión regular: 3 letras mayúsculas - 3 dígitos
        raise ValueError("El ID del equipo debe tener el formato ABC-123 (letras y números).")
    return equipo_id

# Valida que la duración sea un número positivo 
def validar_duracion(duracion_str):
    try:
        duracion = float(duracion_str)  # Intenta convertir a número decimal
        if duracion <= 0:
            raise ValueError  # Si es cero o negativo, lanza error
        return duracion
    except ValueError:
        raise ValueError("La duración debe ser un número mayor a cero.")

# Verifica que el estado del equipo sea uno válido
def validar_estado(estado):
    opciones_validas = ["Activo", "Inactivo", "Mantenimiento"]  # Estados permitidos
    if estado not in opciones_validas:
        raise ValueError(f"Estado inválido. Debe ser uno de: {', '.join(opciones_validas)}.")
    return estado

# Valida que el tipo de mantenimiento sea uno de los permitidos
def validar_tipo_mantenimiento(tipo):
    if tipo not in ["Preventivo", "Correctivo"]:  # Solo se aceptan estos dos tipos
        raise ValueError("Tipo de mantenimiento inválido. Debe ser 'Preventivo' o 'Correctivo'.")
    return tipo

