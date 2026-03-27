import csv
import os

DATA_CSV = os.path.join('data', 'data.csv')



def limpiar_pantalla():
    print("\033[H\033[J", end="")
    

def menu():
    
    limpiar_pantalla()
        
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
    
    limpiar_pantalla()
    
    print("\n--Agrega un producto--\n")
        
    # Validación del nombre: que no sea solo números
    while True:
        nombre_producto = input("Ingrese el nombre del producto: ").lower()

        for item in lista_inventario:
             if nombre_producto == item['nombre']:
                  print('\nEste producto ya existe')
                  continue
             
        if not nombre_producto.isdigit():
            break
        else:
            print("\nError: El nombre del producto no puede ser un número.")
        
    # Validación del precio: que sea un entero positivo
    while True:        
        try:    
            precio_producto = int(input("\nIngrese el precio del producto: "))
            if precio_producto >= 0: 
                break

        except:
            print("\nError: Ingrese un precio válido.")

    # Validación de cantidad: que sea un entero positivo
    while True:
        try:       
            cantidad_producto = int(input("\nIngrese la cantidad del producto: "))
            if cantidad_producto >= 0: 
                break
        except:
            print("\nError: Ingrese una cantidad válida.")

    # Guardar en el diccionario global de productos
    productos = {
        "nombre": nombre_producto,
        "precio": precio_producto,
        "cantidad": cantidad_producto,
    }
    
    # Agregar a la lista de inventario y confirmar
    lista_inventario.append(productos)
    print("\n--Producto agregado--")
    
    guardar_csv(lista_inventario)

    # Cálculo y muestra del resumen del producto
    costo_total = precio_producto * cantidad_producto
    print(f"\nproducto: {nombre_producto} | precio: ${precio_producto} | cantidad: {cantidad_producto} | costo total: ${costo_total}")
    
    input("\n---Presione cualquier tecla para continuar---")

    return lista_inventario
    
def guardar_csv(lista_inventario):

    with open(DATA_CSV, 'w', newline='', encoding='utf-8') as f:
        campos =['nombre', 'precio', 'cantidad']
        write = csv.DictWriter(f, fieldnames=campos)
        write.writeheader()
        for i in lista_inventario:
                var = {'nombre': i['nombre'], 'precio': i['precio'], 'cantidad': i['cantidad']}
                write.writerow(var)




def mostrar_inventario(lista_inventario):
    
    limpiar_pantalla()
    # Verifica si hay productos y los recorre para imprimir sus datos
    if len(lista_inventario) == 0:
        print("\nAún no hay productos en el inventario")
    else:
        for i in lista_inventario:
                print(f"Producto: {i['nombre']} | precio:{i['precio']} | cantidad:{i['cantidad']}")

    input("\n---Presione cualquier tecla para continuar---")
                
def mostrar_estadisticas(lista_inventario):
    
    limpiar_pantalla()
    
    total_cantidad_por_precio = 0
    total_unidades_fisicas = 0
    
    # Menú de opciones de análisis
    menuEstadisticas = "\n---Panel de estadisticas---\n1. Total Inventario\n2. Total productos registrados\n3. Producto con mayor precio"       
    print(menuEstadisticas)
    opcionEstadisticas = input("Ingrese el número de la opción: ")
        
    # Opción 1: Calcula el valor monetario total del inventario
    if opcionEstadisticas == "1":
        for item in lista_inventario:
                total_cantidad_por_precio = total_cantidad_por_precio + (item['cantidad'] * item['precio'])
        print(f"\nEl total monetario es de: ${total_cantidad_por_precio}")
        
    # Opción 2: Calcula unidades totales y variedad de productos
    elif opcionEstadisticas == "2":
        for item in lista_inventario:
                total_unidades_fisicas += item['cantidad']
        print(f"\nTotal de unidades físicas: {total_unidades_fisicas}")
        print(f"Total de tipos de productos: {len(lista_inventario)}")

   
    else:
        print("OPCIÓN NO VALIDA")
    
    
    input("\n---Presione cualquier tecla para continuar---")
        
        
def buscar_producto(lista_inventario):
            
    limpiar_pantalla()
    
    search_input = input("\nIngrese el nombre del producto que desea consultar: ")
    encontrado = False
    
    for item in lista_inventario:

            if item['nombre'] == search_input.replace(" ","").lower():
                
                print("\n----Producto encontrado----")
                print(f"\nNombre del producto es {item['nombre']}")
                print(f"el precio de {item['nombre']} es: ${item['precio']}")
                print(f"y la cantidad es de: {item['cantidad']}")
                encontrado = True
                break
            
    if encontrado == False:
        print("\n---El producto no existe---")
    
    input("\n---Presione cualquier tecla para continuar---")
    

def actualizar_producto(lista_inventario):
            
    limpiar_pantalla()
    encontrado = False
    search_input = input("\nIngrese el nombre del producto que desea consultar: ")

    for item in lista_inventario:
            
            if item['nombre'] == search_input.replace(" ","").lower():
                
                encontrado = True
                
                while True:
                    
                    try:
                        peticion = input("\nDesea actualizar datos? Si/No: ").lower()
                        break
                    except:
                        print("\nDato invalido")
                        continue
                    
                if peticion == "si":
                        while True:
                            try:
                                item['precio'] = float(input("\nIngrese el nuevo precio: "))
                            except:
                                print("\nDato invalido")
                                continue
                            if item['precio'] < 0:
                                print("\nNo puede valer menos que 0")
                                continue
                            else:
                                print("\nPrecio actualizado")
                                break

                        while True:
                            try:
                                item['cantidad'] = int(input("\nIngrese la nueva cantidad: "))
                            except:
                                print("\nDato invalido")
                                continue
                            if item['precio'] < 0:
                                print("\nNo puede haber menos que 0")
                                continue
                            else:
                                print("\ncantidad actualizada")
                                break
                    
                elif peticion == "no":
                    break
                        
                else:
                    print("\nIngrese un dato valido por favor")
                    continue
            
    if encontrado == False:
        print("\n---El producto no existe---")    

    input("\n---Presione cualquier tecla para continuar---")
    
def eliminar_producto(lista_inventario):
            
    limpiar_pantalla()
    encontrado = False
    search_input = input("\nIngrese el nombre del producto que desea consultar: ").lower()

    for item in lista_inventario:
    
            if item['nombre'] == search_input:

                lista_inventario.remove(item)
                encontrado = True
                print(f"\n--- Producto '{item['nombre']}' eliminado ---")
                break
    
    if encontrado == False:
        print("\n---El producto no existe---")

    input("\n---Presione cualquier tecla para continuar---")
    