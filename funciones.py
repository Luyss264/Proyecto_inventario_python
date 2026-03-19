
def agregar_producto(lista_inventario, productos):
    
    print("\n--Agrega un producto--\n")
        
    while True:

        nombre_producto = input("Ingrese el nombre del producto: ")

        if not nombre_producto.isdigit():
            print("Agregado.")
            break

        else:
            print("Error: El nombre del producto no puede ser un número.")
            continue
        
    while True:        
        try:    
            precio_producto = int(input("Ingrese el precio del producto: "))
        except:
            print("Error: Por favor ingrese un precio válido.")
            continue

        if precio_producto < 0:
            print("Error: El precio no puede ser negativo.")
            continue


        else:
            break        
            
    while True:
        try:       
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))
        except:
            print("Error: Por favor ingrese una cantidad válida.")
            continue

        if cantidad_producto < 0:
            print("Error: La cantidad no puede ser negativa.")
            continue

        else:
            break

    productos[nombre_producto]={
        "precio": precio_producto,
        "cantidad": cantidad_producto,
    }
    
    lista_inventario.append({nombre_producto: productos[nombre_producto]})
    
    print("\n--Producto agregado--")


    costo_total = precio_producto * cantidad_producto


    print(f"\nproducto: {nombre_producto} | precio: ${precio_producto} | cantidad: {cantidad_producto} | costo total: ${costo_total}")


def mostrar_inventario(lista_inventario):
    if len(lista_inventario) == 0:
        print("\nAún no hay productos en el inventario")
    else:
        for item in lista_inventario:
                for nombre, datos in item.items():
                    print(f"Producto:{nombre} | precio:{datos['precio']} | cantidad:{datos['cantidad']}")
                
def mostrar_estadisticas(lista_inventario):
    
    total_cantidad_por_precio = 0
    total_unidades_fisicas =0
    
    menuEstadisticas = """
        ---Panel de estadisticas---
        
        1. ---> Total Inventario
        2. ---> Total productos registrados

        """       
        
    print(menuEstadisticas)
        
    opcionEstadisticas = input("Ingrese el número de la opción: ")
        
    if opcionEstadisticas == "1":
            
            
            for item in lista_inventario:
                for nombre, datos in item.items():
                    subtotal= datos['cantidad'] * datos['precio']
                    total_cantidad_por_precio += subtotal
            
            print(f"\nEl total monetario del inventario es de: ${total_cantidad_por_precio}")
        
    elif opcionEstadisticas == "2":
        
            for item in lista_inventario:
                for nombre, datos in item.items():
                    totalcantidad = datos['cantidad']
                    total_unidades_fisicas += totalcantidad
            
            print(f"\nEl total de productos registrados es de: {total_unidades_fisicas}")
        
    else:
            print("OPCIÓN NO VALIDA")