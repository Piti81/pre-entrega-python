# Sistema integral de muebles

muebles = []

while True:
    print("\n===== SISTEMA DE GESTIÓN DE MUEBLES =====")
    print("1. Agregar mueble")
    print("2. Mostrar muebles")
    print("3. Buscar mueble")
    print("4. Eliminar mueble")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # AGREGAR MUEBLE
    if opcion == "1":
        print("\n--- AGREGAR MUEBLE ---")

        nombre = input("Ingrese el nombre del mueble: ")

        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Ingrese el nombre del mueble: ")

        categoria = input("Ingrese la categoría del mueble: ")

        while categoria == "":
            print("La categoría no puede estar vacía.")
            categoria = input("Ingrese la categoría del mueble: ")

        precio = input("Ingrese el precio del mueble (sin centavos): ")

        while precio == "":
            print("El precio no puede estar vacío.")
            precio = input("Ingrese el precio del mueble (sin centavos): ")

        while not precio.isdigit():
            print("El precio debe ser un número entero positivo.")
            precio = input("Ingrese el precio del mueble (sin centavos): ")

        precio = int(precio)

        mueble = [nombre, categoria, precio]
        muebles.append(mueble)

        print("Mueble agregado correctamente.")

    # MOSTRAR MUEBLES
    elif opcion == "2":
        print("\n--- MUEBLES REGISTRADOS ---")

        if len(muebles) == 0:
            print("No hay muebles registrados.")
        else:
            for i in range(len(muebles)):
                print(
                    f"{i + 1}. Nombre: {muebles[i][0]} | "
                    f"Categoría: {muebles[i][1]} | "
                    f"Precio: ${muebles[i][2]}"
                )

    # BUSCAR MUEBLE
    elif opcion == "3":
        print("\n--- BUSCAR MUEBLE ---")

        if len(muebles) == 0:
            print("No hay muebles registrados.")
        else:
            busqueda = input("Ingrese el nombre del mueble a buscar: ")

            while busqueda == "":
                print("La búsqueda no puede estar vacía.")
                busqueda = input("Ingrese el nombre del mueble a buscar: ")

            encontrado = False

            for mueble in muebles:
                if mueble[0].lower() == busqueda.lower():
                    print("\nMueble encontrado:")
                    print(f"Nombre: {mueble[0]}")
                    print(f"Categoría: {mueble[1]}")
                    print(f"Precio: ${mueble[2]}")
                    encontrado = True

            if encontrado == False:
                print("No se encontraron muebles con ese nombre.")

    # ELIMINAR MUEBLE
    elif opcion == "4":
        print("\n--- ELIMINAR MUEBLE ---")

        if len(muebles) == 0:
            print("No hay muebles registrados.")
        else:
            for i in range(len(muebles)):
                print(
                    f"{i + 1}. Nombre: {muebles[i][0]} | "
                    f"Categoría: {muebles[i][1]} | "
                    f"Precio: ${muebles[i][2]}"
                )

            posicion = input(
                "Ingrese el número del mueble que desea eliminar: "
            )

            while not posicion.isdigit():
                print("Debe ingresar un número válido.")
                posicion = input(
                    "Ingrese el número del mueble que desea eliminar: "
                )

            posicion = int(posicion)

            if posicion >= 1 and posicion <= len(muebles):
                mueble_eliminado = muebles.pop(posicion - 1)

                print(
                    f"El mueble '{mueble_eliminado[0]}' "
                    "fue eliminado correctamente."
                )
            else:
                print("El número ingresado no corresponde a ningún mueble.")

    # SALIR
    elif opcion == "5":
        print("\nGracias por elegirnos.")
        break

    # OPCIÓN INCORRECTA
    else:
        print("Opción incorrecta. Por favor, seleccione una opción del 1 al 5.")
