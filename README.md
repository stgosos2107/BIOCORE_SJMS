# PF_Informatica1_2025
Acá está el proyecto final de informática-1 2025-1 de la Universidad de Antioquia
# BIOCORE SJMS - Sistema de Gestión de Equipos Biomédicos

Este proyecto corresponde a la entrega final del curso de Informática I. Se trata de un sistema de gestión de equipos biomédicos desarrollado en Python, que utiliza bases de datos relacionales (MySQL) y no relacionales (MongoDB) para el almacenamiento, consulta y manejo de información.

El sistema permite registrar técnicos, usuarios, equipos biomédicos, mantenimientos, manuales y reportes técnicos, diferenciando funcionalidades según el rol del usuario.

## Elaborado por: BioCore SJMS

- Sofia Henao Osorio
- Janna Valentina Castañeda Ruiz
- María José Acelas León
- Santiago Osorio Salazar

## Estructura del proyecto

BIOCORE_SJMS/
├── database/
│   ├── conexion_mysql.py
│   └── conexion_mongo.py
│
├── datos/
│   ├── equipos.csv
│   ├── mantenimientos.csv
│   ├── reportes.json
│   └── bitacoras.json
│
├── esquemas/
│
├── funciones/
│   ├── equipos.py
│   ├── mantenimientos.py
│   ├── tecnicos.py
│   ├── usuarios.py
│   ├── manuales.py
│   ├── reportes_mongo.py
│   ├── carga_json_mongo.py
│   ├── busqueda_equipo.py
│   ├── estadisticas.py
│   └── validaciones.py
│
├── menus/
│   ├── menu_admin.py
│   ├── menu_ingeniero.py
│   └── menu_tecnico.py
│
├── manuales/
│
├── main.py
└── README.md

## Requisitos del sistema

- Python 3.x instalado
- MySQL Server en funcionamiento
- MongoDB en funcionamiento

## Parámetros de conexión de las bases de datos

Nombre de la base de datos: PF_Informatica1  
Usuario: informatica1  
Contraseña: info2025_2  

Estos parámetros ya están configurados en los archivos de conexión del proyecto.

## Funcionalidades

### Funciones sobre MySQL

- Gestión de Técnicos: crear, listar, modificar y eliminar técnicos.
- Gestión de Usuarios: crear, listar y eliminar usuarios.
- Gestión de Equipos: cargar, registrar y consultar equipos biomédicos.
- Gestión de Mantenimientos: registrar y consultar mantenimientos preventivos o correctivos.

### Funciones sobre MongoDB

- Carga de manuales técnicos desde archivos `.pdf`.
- Carga masiva de reportes técnicos desde archivos `.json`.
- Almacenamiento de rutas de guías rápidas, manuales, reportes en PDF, bitácoras e imágenes antes/después de mantenimiento.
- Los documentos se asocian con un `mmto_id`.

## Instrucciones de uso

1. Verifica que el servidor MySQL y MongoDB estén activos.
2. Asegúrate de que las bases de datos con nombre PF_Informatica1 existan en ambos sistemas.
3. Ejecuta el sistema con:

   python main.py

4. Usa el menú correspondiente al rol del usuario para navegar por el sistema.

## Consideraciones finales

- Los manuales técnicos se guardan como archivos `.pdf` en la carpeta `manuales/` y se cargan a MongoDB como texto.
- Los reportes técnicos se cargan desde archivos `.json` y permiten registrar rutas asociadas a documentos reales (PDF, imágenes, etc).
- El sistema está modularizado para facilitar el mantenimiento y escalabilidad.
- Todos los datos críticos están validados mediante funciones dedicadas para mantener la integridad de la información.
