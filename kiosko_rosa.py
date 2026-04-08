nombres_prod=[]
strock_prod=[]
precios_prod=[]

while True:
        print("Bienvenida Doña Rosa, seleccione que tipo de movimiento desea hacer:\n" \
            "-1. Cargar un solo producto\n" \
            "-2. Cargar varios productos\n" \
            "-3. Eliminar un producto\n" \
            "-4. consultar por un producto\n" \
            "-5. Venta o Reposicion\n" \
            "-6. productos agotados\n" \
            "-7. Lista general\n" \
            "-8. salir")
        opcion=input("Ingrese su opcion: ")
        match opcion:
            case "1":
                print("Cargar un solo producto")                                
                while True:
                        carga_producto=input("Ingrese el nombre del producto: ").strip().capitalize()
                        if carga_producto.replace(" ","").isalpha():
                            nombres_prod.append(carga_producto)
                            break
                        else:
                            print("El nombre del producto solo puede contener letras")                
                while True:
                        carga_stock=input("Ingrese el stock del producto: ")
                        if carga_stock.isdigit():
                            strock_prod.append(int(carga_stock))
                            break
                        else:
                            print("El stock solo puede contener numeros")
                while True:
                        carga_precio=input("Ingrese el precio del producto: ")
                        if carga_precio.replace(",", "").replace(".","").isdigit():                            
                            carga_precio_num=float(carga_precio.replace(",", "."))
                            precios_prod.append(carga_precio_num)
                            break
                        else:
                            print("El precio solo puede contener numeros o decimales")                            
                print("Producto cargado con exito")
                print(nombres_prod)
                print(strock_prod)
                print(precios_prod)
            case "2":                
                while True:
                            cantidad_cargas=input("Ingrese la cantidad de productos a cargar: ")
                            if cantidad_cargas.isdigit():
                                cantidad_cargas=int(cantidad_cargas)
                                break
                            else:
                                print("La cantidad de productos solo puede ser un numero")                                
                for i in range(cantidad_cargas):
                            while True:
                                    carga_producto=input("Ingrese el nombre del producto: ").strip().capitalize()
                                    if carga_producto in nombres_prod:
                                        print("El nombre del producto ya existe")
                                        print("P. Para Modificar Precio")
                                        print("M. Para Modificar Stock")
                                        print("S. Para Salir")
                                        accion = input("Ingrese que desea hacer: ")                                        
                                        while True:
                                                match accion:
                                                    case "P":
                                                        print("Modificar Precio")                                                
                                                        for i in range(cantidad_cargas):
                                                            if nombres_prod[i]==carga_producto:                                                        
                                                                while True:
                                                                    carga_precio_num=input("Ingrese el nuevo precio del producto: ")
                                                                    if carga_precio_num.replace(",", "").replace(".","").isdigit():
                                                                        precios_prod[i]=float(carga_precio_num.replace(",", "."))
                                                                        break
                                                                    else:
                                                                        print("El precio solo puede contener numeros o decimales")                                                        
                                                                break
                                                        break
                                                    case "M":
                                                        print(" Stock")                                                        
                                                        for i in range(cantidad_cargas):
                                                            if nombres_prod[i]==carga_producto:
                                                                while True:
                                                                    carga_stock=input("Ingrese el nuevo stock del producto: ")
                                                                    if carga_stock.isdigit():
                                                                        strock_prod[i]=int(carga_stock)
                                                                        break
                                                                    else:
                                                                        print("El stock solo puede contener numeros")                                                        
                                                                break
                                                    case "S":
                                                        print("Salir")
                                                        break
                                                    case _:
                                                        print("Ingrese una opcion valida")                                                        
                                    if carga_producto.replace(" ","").isalpha():
                                            nombres_prod.append(carga_producto)
                                            break
                                    else:
                                            print("El nombre del producto solo puede contener letras")                
                            while True:
                                    carga_stock=input("Ingrese el stock del producto: ")
                                    if carga_stock.isdigit():
                                        strock_prod.append(int(carga_stock))
                                        break
                                    else:
                                        print("El stock solo puede contener numeros")
                            while True:
                                    carga_precio=input("Ingrese el precio del producto: ")
                                    if carga_precio.replace(",", "").replace(".","").isdigit():                            
                                        carga_precio_num=float(carga_precio.replace(",", "."))
                                        precios_prod.append(carga_precio_num)
                                        break
                                    else:
                                        print("El precio solo puede contener numeros o decimales")                                                        
            case "3":
                eliminar_uno()
            case "4":
                consultar_uno()
            case "5":
                venta_reposicion()
            case "6":
                salir()
            case "7":
                lista_general()
            case "8":
                print("Gracias por usar el kiosko Rosa")
                break
            case _:
                print("Opcion invalida")
               
