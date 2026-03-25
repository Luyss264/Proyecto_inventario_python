import os


def menu():
    
    os.system('clear')
        
    menuPrincipal = """
    ----------BIENVENIDO AL SISTEMA-----------

    Por favor elija una opción:

    1. -----> Agregar producto.
    2. -----> Mostrar inventario.
    3. -----> Calcular estadísticas.
    4. -----> Buscar.
    5. -----> Actualizar.
    6. -----> Eliminar.
    7. -----> Salir.
    """
    
    print(menuPrincipal)

#se define la función para agregar producto
def agregar_producto(lista_inventario, productos):
    
    os.system('clear')
    
    print("\n--Agrega un producto--\n")
        
    # Validación del nombre: que no sea solo números
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ")
        if not nombre_producto.isdigit():
            break
        else:
            print("Error: El nombre del producto no puede ser un número.")
        
    # Validación del precio: que sea un entero positivo
    while True:        
        try:    
            precio_producto = int(input("Ingrese el precio del producto: "))
            if precio_producto >= 0: break
            print("Error: El precio no puede ser negativo.")
        except:
            print("Error: Ingrese un precio válido.")

    # Validación de cantidad: que sea un entero positivo
    while True:
        try:       
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            if cantidad_producto >= 0: break
            print("Error: La cantidad no puede ser negativa.")
        except:
            print("Error: Ingrese una cantidad válida.")

    # Guardar en el diccionario global de productos
    productos[nombre_producto] = {
        "precio": precio_producto,
        "cantidad": cantidad_producto,
    }
    
    # Agregar a la lista de inventario y confirmar
    lista_inventario.append({nombre_producto: productos[nombre_producto]})
    print("\n--Producto agregado--")

    # Cálculo y muestra del resumen del producto
    costo_total = precio_producto * cantidad_producto
    print(f"\nproducto: {nombre_producto} | precio: ${precio_producto} | cantidad: {cantidad_producto} | costo total: ${costo_total}")
    
    input("\n---Presione cualquier tecla para continuar---")
    
    


def mostrar_inventario(lista_inventario):
    
    os.system('clear')
    # Verifica si hay productos y los recorre para imprimir sus datos
    if len(lista_inventario) == 0:
        print("\nAún no hay productos en el inventario")
    else:
        for item in lista_inventario:
            for nombre, datos in item.items():
                print(f"Producto:{nombre} | precio:{datos['precio']} | cantidad:{datos['cantidad']}")

    input("\n---Presione cualquier tecla para continuar---")
                
def mostrar_estadisticas(lista_inventario):
    
    os.system('clear')
    
    total_cantidad_por_precio = 0
    total_unidades_fisicas = 0
    
    # Menú de opciones de análisis
    menuEstadisticas = "\n---Panel de estadisticas---\n1. Total Inventario\n2. Total productos registrados\n"       
    print(menuEstadisticas)
    opcionEstadisticas = input("Ingrese el número de la opción: ")
        
    # Opción 1: Calcula el valor monetario total del inventario
    if opcionEstadisticas == "1":
        for item in lista_inventario:
            for nombre, datos in item.items():
                total_cantidad_por_precio += (datos['cantidad'] * datos['precio'])
        print(f"\nEl total monetario es de: ${total_cantidad_por_precio}")
        
    # Opción 2: Calcula unidades totales y variedad de productos
    elif opcionEstadisticas == "2":
        for item in lista_inventario:
            for nombre, datos in item.items():
                total_unidades_fisicas += datos['cantidad']
        print(f"\nTotal de unidades físicas: {total_unidades_fisicas}")
        print(f"Total de tipos de productos: {len(lista_inventario)}")
        
    else:
        print("OPCIÓN NO VALIDA")
    
    
    input("\n---Presione cualquier tecla para continuar---")
        
        
def searcher_product(lista_inventario):
            
    os.system('clear')
    
    search_input = input("\nIngrese el nombre del producto que desea consultar: ")
    
    for item in lista_inventario:
        for name, datos in item.items():
            
            if name == search_input.replace(" ","").lower():
                
                print("\n----Producto encontrado----")
                print(f"\nNnombre del producto es {name}")
                print(f"el precio de {name} es: ${datos['precio']}")
                print(f"y la cantidad es de: {datos['cantidad']}")
            
            else:
                print("---El producto no existe")
    
    input("\n---Presione cualquier tecla para continuar---")
    

def data_changer(lista_inventario):
            
            os.system('clear')
    
            search_input = input("\nIngrese el nombre del producto que desea consultar: ")

            for item in lista_inventario:
                for name, datos in item.items():
                    
                    if name == search_input.replace(" ","").lower():
                        
                        peticion = input("Desea actualizar datos? Si/No: ").lower()
                        
                        if peticion == "si":
                            datos['precio'] = input("Ingrese el nuevo precio: ")
                            datos['cantidad'] = input("Ingrese la nueva cantidad: ")
                        
                        elif peticion == "no":
                            break
                            
                        else:
                            print("Ingrese un dato valido por favor")
                            continue
                    
                    else:
                        print("---El producto no existe")

            input("\n---Presione cualquier tecla para continuar---")
            
def delete_product(lista_inventario):
            
            os.system('clear')
    
            search_input = input("\nIngrese el nombre del producto que desea consultar: ")

            for item in lista_inventario:
   
                nombre_en_lista = list(item.keys())[0]
            
            
                if nombre_en_lista.lower() == search_input:
                    lista_inventario.remove(item)
                    print(f"\n--- Producto '{nombre_en_lista}' eliminado ---")


            input("\n---Presione cualquier tecla para continuar---")
            