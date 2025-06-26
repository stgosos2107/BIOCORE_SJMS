tecnicos = []

def crear_tecnico():
    nombre = input("Nombre: ")
    especialidad = input("Especialidad: ")
    cedula = input("Cédula profesional: ")
    contacto = input("Datos de contacto: ")
    tecnico = {
        "nombre": nombre,
        "especialidad": especialidad,
        "cedula": cedula,
        "contacto": contacto
    }
    tecnicos.append(tecnico)
    print(" Técnico registrado con éxito.")

def listar_tecnicos():
    if not tecnicos:
        print("No hay técnicos registrados.")
        return
    print("Técnicos registrados:")
    for i, t in enumerate(tecnicos, start=1):
        print(f"{i}. {t['nombre']} - {t['especialidad']} - {t['cedula']}")

def modificar_tecnico():
    listar_tecnicos()
    idx = int(input("Número del técnico a modificar: ")) - 1
    if 0 <= idx < len(tecnicos):
        nombre = input("Nuevo nombre: ")
        especialidad = input("Nueva especialidad: ")
        cedula = input("Nueva cédula: ")
        contacto = input("Nuevo contacto: ")
        tecnicos[idx].update({
            "nombre": nombre,
            "especialidad": especialidad,
            "cedula": cedula,
            "contacto": contacto
        })
        print("Técnico modificado.")
    else:
        print("Índice no válido.")

def eliminar_tecnico():
    listar_tecnicos()
    idx = int(input("Número del técnico a eliminar: ")) - 1
    if 0 <= idx < len(tecnicos):
        eliminado = tecnicos.pop(idx)
        print(f" Técnico {eliminado['nombre']} eliminado.")
    else:
        print("Índice no válido.")

