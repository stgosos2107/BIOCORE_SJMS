equipos = [
    {"id": "EQ001", "marca": "GE", "estado": "Operativo", "descripcion": "Monitor de signos vitales"},
    {"id": "EQ002", "marca": "Philips", "estado": "En reparación", "descripcion": "Ventilador mecánico"},
    {"id": "EQ003", "marca": "Siemens", "estado": "Pendiente", "descripcion": "Equipo de rayos X"}
]

def buscar_equipo():
    criterio = input("Buscar por estado, marca o palabra clave: ").lower()
    encontrados = []
    for eq in equipos:
        if (criterio in eq["marca"].lower() or
            criterio in eq["estado"].lower() or
            criterio in eq["descripcion"].lower()):
            encontrados.append(eq)
    if encontrados:
        print(" Equipos encontrados:")
        for eq in encontrados:
            print(f"- {eq['id']}: {eq['marca']} - {eq['estado']} - {eq['descripcion']}")
    else:
        print(" No se encontraron equipos con ese criterio.")
