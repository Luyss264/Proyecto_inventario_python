#se define la función para agregar producto
def agregar_producto(lista_inventario, productos):
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

def mostrar_inventario(lista_inventario):
    # Verifica si hay productos y los recorre para imprimir sus datos
    if len(lista_inventario) == 0:
        print("\nAún no hay productos en el inventario")
    else:
        for item in lista_inventario:
            for nombre, datos in item.items():
                print(f"Producto:{nombre} | precio:{datos['precio']} | cantidad:{datos['cantidad']}")
                
def mostrar_estadisticas(lista_inventario):
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