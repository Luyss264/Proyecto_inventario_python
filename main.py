from funciones import * # Importa las funciones del archivo externo

# Definición del menú principal del sistema
menuPrincipal = """
----------BIENVENIDO AL SISTEMA-----------

Por favor elija una opción:

1. -----> Agregar producto.
2. -----> Mostrar inventario.
3. -----> calcular estadísticas.
4. -----> Salir.
"""

opcion = ""

# Estructuras para almacenar los datos
lista_inventario = []
productos = {}

# Bucle principal para mantener el programa en ejecución
while opcion != "4":
    
    print(menuPrincipal)
    opcion = input("Ingrese el número de la opción que desea: ")
    
    # Llama a la función para registrar productos
    if opcion == "1":
        agregar_producto(lista_inventario, productos)
    
    # Llama a la función para ver la lista completa
    elif opcion == "2":
        mostrar_inventario(lista_inventario)
    
    # Llama a la función para ver totales y cálculos
    elif opcion == "3":
        mostrar_estadisticas(lista_inventario)
    
    # Finaliza la ejecución
    elif opcion == "4":
        print("Adiós")
        
    # Manejo de entradas incorrectas
    else:
        print("OPCIÓN NO VALIDA")