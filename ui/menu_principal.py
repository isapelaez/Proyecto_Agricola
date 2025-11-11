from crud.crear import crear_cliente, crear_factura, crear_fertilizante, crear_antibiotico, crear_control_plaga, buscar_cliente

while True:
    print("\n--- Menú Principal ---")
    print("1. Registrar cliente")
    print("2. Añadir producto")
    print("3. Crear factura")
    print("4. Buscar cliente")
    print("5. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("\nHas elegido la Opción Uno.")
        nombre = input("Digite el nombre del cliente: ")
        cedula = input("Digite el cedula del cliente: ")
        crear_cliente(nombre, cedula)
        
    elif opcion == "2":
        print("Has elegido la Opción Dos.")
        while True:
            print("\n--- Productos ---")
            print("1. Antibiotico")
            print("2. Fertilizante")
            print("3. Control de plagas")
            print("4. Salir")
            
            opcion_producto = input("Selecciona una opción: ")

            if opcion_producto == "1":
                print("\nHas elegido la Opción Uno.")
                nombre = input("Digite el nombre del antibiotico: ")
                precio = float(input("Digite el precio del antibiotico: "))
                dosis = int(input("Dosis: "))
                tipoAnimal = ("Escriba tipo de animal 'Bovinos', 'Caprinos', 'Porcinos': ")
                crear_antibiotico(nombre, precio, dosis, tipoAnimal)
                
            elif opcion_producto == "2":
                print("Has elegido la Opción Dos.")
                nombre = input("Digite el nombre del fertilizante: ")
                precio = float(input("Digite el precio del fertilizante: "))
                ICA = (input("Digite el registro ICA del fertilizante: "))
                frecuencia = int(input("Digite la frecuencia"))
                ultimaAplicacion = (input("Digite fecha de ultima aplicacion (DD/MM/AAAA): "))
                crear_fertilizante(nombre, precio, ICA, frecuencia, ultimaAplicacion)
            
            elif opcion_producto == "3":
                print("Has elegido la Opción Tres.")
                nombre = input("Digite el nombre del control de plaga: ")
                precio = float(input("Digite el precio del control de plaga: "))
                ICA = (input("Digite el registro ICA del control de plaga: "))
                frecuencia = int(input("Digite la frecuencia"))
                periodoCarencia = int(input("Digite fecha de ultima aplicacion: "))
                crear_control_plaga(nombre, precio, ICA, frecuencia, periodoCarencia)
                
            elif opcion_producto == "4":
                break
            
            else:
                print("Opción no válida. Inténtalo de nuevo.")
    
    elif opcion == "3":
        print("Has elegido la Opción Tres.")
        cedula = input("Digite el cedula del cliente a agregar factura: ")
        crear_factura(cedula)
        
        
    elif opcion == "4":
        print("Has elegido la Opción Cuatro.")
        cedula = input("Digite el cedula del cliente a consultar: ")
        busqueda = buscar_cliente(cedula)
        
        if busqueda == 0:
            print("Cliente no encontrado.")
            
        else:
            facturas = busqueda.get_facturas()

            if len(facturas) > 0:
                for factura in facturas:
                    print(f"\n🧾 Factura - Fecha: {factura.get_fecha()}")
                    print("Productos:")

                    for producto in factura.get_productos():
                        print(f" - {producto}")
            else:
                print("No hay facturas asociadas al cliente.")
            
    elif opcion == "5":
        break
    
    else:
        print("Opción no válida. Inténtalo de nuevo.")
