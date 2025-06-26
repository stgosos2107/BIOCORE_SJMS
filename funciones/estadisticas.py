from funciones.busqueda_equipo import equipos

def generar_estadisticas():
    total = len(equipos)
    operativos = sum(1 for eq in equipos if eq["estado"].lower() == "operativo")
    en_reparacion = sum(1 for eq in equipos if eq["estado"].lower() == "en reparación")
    pendientes = total - operativos - en_reparacion

    print("\n Estadísticas de equipos:")
    print(f"Total de equipos: {total}")
    print(f"Operativos: {operativos}")
    print(f"En reparación: {en_reparacion}")
    print(f"Pendientes: {pendientes}")
