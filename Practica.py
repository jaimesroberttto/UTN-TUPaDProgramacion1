habitaciones = []
estados = []
while True:
    print("\n--- MENÚ HOTEL ---")
    print("1. Ingresar números de habitación")
    print("2. Ingresar estados (0=Libre / 1=Ocupada)")
    print("3. Mostrar estado general")
    print("4. Consultar estado de una habitación")
    print("5. Listar habitaciones libres u ocupadas")
    print("6. Agregar habitación")
    print("7. Cambiar estado de una habitación")
    print("8. Salir")
    opcion = input("que desea hacer:")
    match opcion:
        case "1":
            cargar = input("cuantas habitaciones deseas cargar: ")
            if not cargar.isnumeric():
                print("numero no valido")
            else:
                cargar = int(cargar)
            for i in range(cargar):
                nuevahabitacion = input("numero de la nueva habitacion: ")
                if not nuevahabitacion.isnumeric():
                    print("numero invalido")
                else:
                    nuevahabitacion = int(nuevahabitacion)
                    habitaciones.append(nuevahabitacion)
                    estados.append(0)
        case "2":       
            if not habitaciones:
                print("Error: Primero debe registrar las habitaciones en la Opción 1.")
            else:
                print(f"\n--- Registro de Estados (Total: {len(habitaciones)} habitaciones) ---")                
                estados = []                
                for i in range(len(habitaciones)):
                    while True:
                        try:
                            estado = int(input(f"Ingrese estado para la habitación {habitaciones[i]} (0=Libre / 1=Ocupada): "))
                            if estado in [0, 1]:
                                estados.append(estado)
                                break
                            else:
                                print("Valor inválido. Por favor ingrese 0 o 1.")
                        except ValueError:
                            print("Error: Debe ingresar un número entero (0 o 1).")
                            
                print("Estados registrados exitosamente.")            
        case "3":
            for x in range(len(habitaciones)):
                if estados[x] == 0:
                    print(f"la habitacion {habitaciones[x]} y esta libre")
                elif estados[x] == 1:
                    print(f"la habitacion {habitaciones[x]} y esta ocupada")
        case "4":
            buscar = input("habitacion a consultar: ")
            if not buscar.isnumeric():
                print("habitacion invalida")
            else:
                buscar = int(buscar)
                for i in habitaciones:
                    if buscar == habitaciones[i]:
                        if estados[i] == 0:
                            print(f"la habitacion {habitaciones[i]} esta libre")
                        else:
                            print(f"la habitacion {habitaciones[i]} esta ocupada")
        case "5":
            if not habitaciones or not estados:
                print("Error: No hay datos registrados.")
            else:
                print("\n--- Listar por Estado ---")
                print("0. Ver habitaciones LIBRES")
                print("1. Ver habitaciones OCUPADAS")
                
                opcion_filtro = int(input("¿Qué desea listar? (0/1): "))
                
                if opcion_filtro == 0:
                    print("Habitaciones LIBRES:")
                    encontrado = False
                    for i in range(len(habitaciones)):
                        if estados[i] == 0:
                            print(f"- Habitación {habitaciones[i]}")
                            encontrado = True
                    if not encontrado:
                        print("No hay habitaciones libres actualmente.")
                        
                elif opcion_filtro == 1:
                    print("Habitaciones OCUPADAS:")
                    encontrado = False
                    for i in range(len(habitaciones)):
                        if estados[i] == 1:
                            print(f"- Habitación {habitaciones[i]}")
                            encontrado = True
                    if not encontrado:
                        print("No hay habitaciones ocupadas actualmente.")
                else:
                    print("Opción inválida.")
        case "6":
            nombre = input("numero de la nueva habitacion: ")
            if not nombre.isnumeric():
                print("numero no valido")
            else:
                nombre = int(nombre)
                estado = input("estado de la nueva habitacion: ")
                if estado.isnumeric():
                    if int(estado) > 1:
                        print("numero invalido")
                    elif 0 > int(estado):
                        print("numero invalido")
                    else:
                        estado = int(estado)
                        habitaciones.append(nombre)
                        estados.append(estado)
        case "7":
            buscar = input("habitacion a cambiar estado: ")
            if not buscar.isnumeric():
                print("habitacion invalida")
            else:
                buscar = int(buscar)
                for i in range(len(habitaciones)):
                    if buscar == habitaciones[i]:
                        if estados[i] == 0:
                            print(f"la habitacion {habitaciones[i]} ahora estara ocupada")
                            estados[i] = 1
                        else:
                            print(f"la habitacion {habitaciones[i]} ahora estara libre")
                            estados[i] = 0
        case "8":
            print("adios")
            break