
def inventario(lista_inventario, productos):

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
            precio_producto = float(input("Ingrese el precio del producto: "))
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
    
    lista_inventario.append(productos)
    
    print("\n--Producto agregado--")


    costo_total = precio_producto * cantidad_producto


    print(f"\nproducto: {nombre_producto} | precio: ${precio_producto} | cantidad: {cantidad_producto} | costo total: ${costo_total}")


    