inventario = {}

def mostrar_inventario():
    print("\nInventario actual:")
    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto, (cantidad, precio) in inventario.items():
            print(f"Producto: {producto}, Cantidad: {cantidad}, Precio: ${precio:.2f}")

def agregar_producto(producto, cantidad, precio):
    if producto in inventario:
        inventario[producto] = (inventario[producto][0] + cantidad, precio)
    else:
        inventario[producto] = (cantidad, precio)
    print(f"Producto '{producto}' agregado/actualizado en el inventario.")

def eliminar_producto(producto):
    if producto in inventario:
        del inventario[producto]
        print(f"Producto '{producto}' eliminado del inventario.")
    else:
        print(f"Producto '{producto}' no encontrado en el inventario.")

def informar_bajo_stock():
    print("\nProductos con cantidad menor a 5:")
    bajo_stock = {producto: cantidad for producto, (cantidad, _) in inventario.items() if cantidad < 5}
    if not bajo_stock:
        print("No hay productos con cantidad menor a 5.")
    else:
        for producto, cantidad in bajo_stock.items():
            print(f"Producto: {producto}, Cantidad: {cantidad}")

def menu():
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Mostrar inventario")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Informar bajo stock")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_inventario()
        elif opcion == '2':
            producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            agregar_producto(producto, cantidad, precio)
        elif opcion == '3':
            producto = input("Ingrese el nombre del producto a eliminar: ")
            eliminar_producto(producto)
        elif opcion == '4':
            informar_bajo_stock()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
