from funciones import inventario


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
        inventario(lista_inventario, productos)
    
    elif opcion == "2":
        
        print(lista_inventario)