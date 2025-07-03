"""
main.py
Sistema principal de gestión de mantenimiento biomédico - BIOCORE_SJMS.

Permite seleccionar el rol del usuario y redirigir al submenú correspondiente:
Administrador, Técnico o Ingeniero.
"""

from menus.menu_admin import menu_admin
from menus.menu_tecnico import menu_tecnico
from menus.menu_ingeniero import menu_ingeniero

def main():
    while True:
        print("\n=== BIOCORE_SJMS - SISTEMA DE GESTIÓN BIOMÉDICA ===")
        print("Selecciona tu rol:")
        print("1. Administrador")
        print("2. Técnico")
        print("3. Ingeniero clínico")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            menu_admin()
        elif opcion == "2":
            menu_tecnico()
        elif opcion == "3":
            menu_ingeniero()
        elif opcion == "4":
            print("👋 Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
