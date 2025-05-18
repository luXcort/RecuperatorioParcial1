print("Bienvenido al sistema de gestión de stock")

# Listas para productos y cantidades
productos = []
cantidades = []

while True:
    print("Menú de opciones:")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        producto = input("Producto: ").strip()
        try:
            cantidad = int(input("Cantidad: ").strip())
            productos.append(producto)
            cantidades.append(max(0, cantidad))  # Evitar negativos
            print("Producto agregado correctamente.")
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")

    elif opcion == "2":
        print("\nProductos agotados:")
        agotados = False
        for i in range(len(productos)):
            if cantidades[i] == 0:
                print("-", productos[i])
                agotados = True
        if not agotados:
            print("No hay productos agotados.")

    elif opcion == "3":
        producto = input("Producto a actualizar: ").strip()
        if producto in productos:
            try:
                nueva_cantidad = int(input("Nueva cantidad: ").strip())
                cantidades[productos.index(producto)] = max(0, nueva_cantidad)
                print("Stock actualizado correctamente.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        print("\nListado de Stock:")
        if productos:
            for i in range(len(productos)):
                print("-", productos[i], "-", cantidades[i], "unidades")
        else:
            print("No hay productos registrados.")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
