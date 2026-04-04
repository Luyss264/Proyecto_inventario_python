from servicios import * # Importa las funciones del archivo externo

option = ""

# Estructuras para almacenar los datos
lista_inventario = []
productos = {}

# Bucle principal para mantener el programa en ejecución
while option != "9":
    #función para desplegar el menú
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

    #llama la función para buscar un producto    
    elif option == "4":
        buscar_producto(lista_inventario)
    
    #llama la función para actualizar un producto
    elif option == "5":
        
        actualizar_producto(lista_inventario)

    #llama la función para eliminar un producto    
    elif option == "6":
        
        eliminar_producto(lista_inventario)
        
    elif option == "7":
        
        guardar_csv(lista_inventario)
    
    elif option == "8":
        
        try:
            cargar_csv(lista_inventario)
        except FileNotFoundError:
            print("\n[!] Error: No se encontró el archivo 'data.csv'. Primero debes guardar datos.")
            input("\nPresione cualquier tecla para continuar...")
    
    # Finaliza la ejecución
    elif option == "9":
        print("\nAdiós")
        
    # Manejo de entradas incorrectas
    else:
        print("\nOPCIÓN NO VALIDA")
        
