#comenzamos lanzando un mensaje introductorio a la acción
print ("\n--Agrega un producto--\n")

#se usan "while True:" conjunto a "try" para que si llega a cumplirse "except"
#este lleve el usuario en loop al inicio y reintente usando "continue"
while True:
  
    #usuario ingresa el nombre del producto
    nombre_producto = input("Ingrese el nombre del producto: ")

    if not nombre_producto.isdigit():
        print("Agregado.")
        break
    #rompemos ciclo si se cumple
    else:
        print("Error: El nombre del producto no puede ser un número.")
        continue
    #se agrega una condición que si el usuario ingresa un número como nombre del producto, 
    #este sea invalido y devuelva al usuario a reintentar

#se usan "while True:" conjunto a "try" para que si llega a cumplirse "except"
#este lleve el usuario en loop al inicio y reintente usando "continue"  
while True:        
    try:    
        precio_producto = float(input("Ingrese el precio del producto: "))
    except:
        print("Error: Por favor ingrese un precio válido.")
        continue
    #se agrega una condición que si el número es menor que cero sea invalido y devuelva al usuario a reintentar
    if precio_producto < 0:
        print("Error: El precio no puede ser negativo.")
        continue
    
    #rompemos ciclo si se cumple
    else:        
        break    

#hacemos el mismo caso para esta petición como las anteriores
while True:
    try:       
        cantidad_producto = int(input("Ingrese la cantidad del producto: "))
    except:
        print("Error: Por favor ingrese una cantidad válida.")
        continue
    #volvemos a agregan una condicion que si el numero es menor que cero resulta invalido y reintente
    if cantidad_producto < 0:
        print("Error: La cantidad no puede ser negativa.")
        continue
    
    #rompemos ciclo si se cumple
    else:
        break

#imprimimos en consola "Producto agregado"
print("\n--Producto agregado--")

#guardamos en una variable el costo total, se hace multiplicando el precio del producto y la cantidad de productos
costo_total = precio_producto * cantidad_producto

#imprimimos usando str y variables para encancillarlos y lanzar un mensaje mostrando al usuario el costo total,
#la cantidad de productos, precio, y que producto
print(f"\nproducto: {nombre_producto} | precio: ${precio_producto} | cantidad: {cantidad_producto} | costo total: ${costo_total}")

#una vez hecho todo, lanzamos un print de finalización
print("\n--Fin del programa--")

