from funciones import *


menuPrincipal = """
----------BIENVENIDO AL SISTEMA-----------

Por favor elija una opción:

1. -----> Agregar producto.
2. -----> Mostrar inventario.
3. -----> calcular estadísticas.
4. -----> Salir.
"""

opcion = ""

lista_inventario = []

productos = {}

while opcion != "4":
    
    print(menuPrincipal)
    
    opcion = input("Ingrese el número de la opción que desea: ")
    
    if opcion == "1":
        
        agregar_producto(lista_inventario, productos)
    
    elif opcion == "2":
        
        mostrar_inventario(lista_inventario)
    
    elif opcion == "3":
        
        mostrar_estadisticas(lista_inventario)
    
    elif opcion == "4":
        print("Adiós")
        
    else:
        print("OPCIÓN NO VALIDA")