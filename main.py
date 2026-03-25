from funciones import * # Importa las funciones del archivo externo

option = ""

# Estructuras para almacenar los datos
lista_inventario = []
productos = {}

# Bucle principal para mantener el programa en ejecución
while option != "7":
    
    menu()
    
    option = input("Ingrese el número de la opción que desea: ")
    
    # Llama a la función para registrar productos
    if option == "1":
        agregar_producto(lista_inventario, productos)
    
    # Llama a la función para ver la lista completa
    elif option == "2":
        mostrar_inventario(lista_inventario)
    
    # Llama a la función para ver totales y cálculos
    elif option == "3":
        mostrar_estadisticas(lista_inventario)
        
    elif option == "4":
        searcher_product(lista_inventario)
        
    elif option == "5":
        
        data_changer(lista_inventario)
        
    elif option == "6":
        
        delete_product(lista_inventario)
    
    # Finaliza la ejecución
    elif option == "7":
        print("Adiós")
        
    # Manejo de entradas incorrectas
    else:
        print("OPCIÓN NO VALIDA")