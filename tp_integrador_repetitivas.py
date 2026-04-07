opcion_principal = ""
while opcion_principal != "6":
    print("")
    print("1) Caja del Kiosco")
    print("2) Acceso al Campus y Menú Seguro")
    print("3) Agenda de Turnos con Nombres (sin listas)")
    print("4) Escape Room: La Bóveda")
    print("5) Escape Room: La Arena del Gladiador")
    print("6) Salir")
    opcion_principal = input("Opción: ").strip()
    while (not opcion_principal.isdigit()) or (int(opcion_principal) < 1 or int(opcion_principal) > 6):
        print("Error: opción fuera de rango.")
        opcion_principal = input("Opción: ").strip()

    if opcion_principal == "1":
        cliente = input("Cliente: ").strip()
        while (cliente == "") or (not cliente.isalpha()):
            print("Error: Solo se permiten letras.")
            cliente = input("Cliente: ").strip()

        cantidad_str = input("Cantidad de productos: ").strip()
        while (not cantidad_str.isdigit()) or int(cantidad_str) <= 0:
            print("Error: ingrese un número entero positivo.")
            cantidad_str = input("Cantidad de productos: ").strip()
        cantidad = int(cantidad_str)

        total_sin_desc = 0
        total_con_desc = 0.0

        i = 1
        while i <= cantidad:
            precio_str = input(f"Producto {i} - Precio: ").strip()
            while (not precio_str.isdigit()) or int(precio_str) <= 0:
                print("Error: ingrese un número válido.")
                precio_str = input(f"Producto {i} - Precio: ").strip()
            precio = int(precio_str)

            desc = input("Descuento (S/N): ").strip().lower()
            while desc not in ("s", "n"):
                print("Error: ingrese S o N.")
                desc = input("Descuento (S/N): ").strip().lower()

            total_sin_desc += precio
            if desc == "s":
                total_con_desc += precio * 0.9
            else:
                total_con_desc += float(precio)
            i += 1

        ahorro = float(total_sin_desc) - total_con_desc
        promedio = total_con_desc / cantidad

        print(f"Total sin descuentos: ${total_sin_desc}")
        print(f"Total con descuentos: ${total_con_desc:.2f}")
        print(f"Ahorro: ${ahorro:.2f}")
        print(f"Promedio por producto: ${promedio:.2f}")

    elif opcion_principal == "2":
        usuario_correcto = "alumno"
        clave_correcta = "python123"

        intento = 1
        acceso = False
        while intento <= 3 and not acceso:
            usuario = input(f"Intento {intento}/3 - Usuario: ").strip()
            clave = input("Clave: ").strip()
            if usuario == usuario_correcto and clave == clave_correcta:
                acceso = True
                print("Acceso concedido.")
            else:
                print("Error: credenciales inválidas.")
                intento += 1

        if not acceso:
            print("Cuenta bloqueada")
        else:
            opcion = ""
            while opcion != "4":
                print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
                opcion = input("Opción: ").strip()
                if not opcion.isdigit():
                    print("Error: ingrese un número válido.")
                    continue
                op = int(opcion)
                if op < 1 or op > 4:
                    print("Error: opción fuera de rango.")
                    continue

                if opcion == "1":
                    print("Inscripto")
                elif opcion == "2":
                    cambio_exitoso = False
                    while not cambio_exitoso:
                        nueva = input("Nueva clave: ").strip()
                        if len(nueva) < 6:
                            print("Error: mínimo 6 caracteres.")
                        else:
                            conf = input("Confirmar clave: ").strip()
                            if nueva != conf:
                                print("Error: las claves no coinciden.")
                            else:
                                clave_correcta = nueva
                                cambio_exitoso = True
                                print("Clave actualizada.")
                elif opcion == "3":
                    print("Seguí practicando: la constancia gana.")
                else:
                    print("Saliendo...")

    elif opcion_principal == "3":
        operador = input("Nombre del operador: ").strip()
        while (operador == "") or (not operador.isalpha()):
            print("Error: Solo se permiten letras.")
            operador = input("Nombre del operador: ").strip()

        lunes1 = ""
        lunes2 = ""
        lunes3 = ""
        lunes4 = ""
        martes1 = ""
        martes2 = ""
        martes3 = ""

        opcion = ""
        while opcion != "5":
            print("")
            print("1) Reservar turno")
            print("2) Cancelar turno (por nombre)")
            print("3) Ver agenda del día")
            print("4) Ver resumen general")
            print("5) Cerrar sistema")
            opcion = input("Opción: ").strip()
            if not opcion.isdigit():
                print("Error: ingrese un número válido.")
                continue
            op = int(opcion)
            if op < 1 or op > 5:
                print("Error: opción fuera de rango.")
                continue

            if opcion == "1":
                dia = input("Día (1=Lunes, 2=Martes): ").strip()
                while (not dia.isdigit()) or (dia not in ("1", "2")):
                    print("Error: ingrese 1 o 2.")
                    dia = input("Día (1=Lunes, 2=Martes): ").strip()

                paciente = input("Nombre del paciente: ").strip()
                while (paciente == "") or (not paciente.isalpha()):
                    print("Error: Solo se permiten letras.")
                    paciente = input("Nombre del paciente: ").strip()

                if dia == "1":
                    repetido = False
                    if lunes1.lower() == paciente.lower() and lunes1 != "":
                        repetido = True
                    if lunes2.lower() == paciente.lower() and lunes2 != "":
                        repetido = True
                    if lunes3.lower() == paciente.lower() and lunes3 != "":
                        repetido = True
                    if lunes4.lower() == paciente.lower() and lunes4 != "":
                        repetido = True
                    if repetido:
                        print("Error: paciente repetido en Lunes.")
                    else:
                        if lunes1 == "":
                            lunes1 = paciente
                            print("Turno reservado en Lunes (Turno 1).")
                        elif lunes2 == "":
                            lunes2 = paciente
                            print("Turno reservado en Lunes (Turno 2).")
                        elif lunes3 == "":
                            lunes3 = paciente
                            print("Turno reservado en Lunes (Turno 3).")
                        elif lunes4 == "":
                            lunes4 = paciente
                            print("Turno reservado en Lunes (Turno 4).")
                        else:
                            print("No hay cupos disponibles en Lunes.")
                else:
                    repetido = False
                    if martes1.lower() == paciente.lower() and martes1 != "":
                        repetido = True
                    if martes2.lower() == paciente.lower() and martes2 != "":
                        repetido = True
                    if martes3.lower() == paciente.lower() and martes3 != "":
                        repetido = True
                    if repetido:
                        print("Error: paciente repetido en Martes.")
                    else:
                        if martes1 == "":
                            martes1 = paciente
                            print("Turno reservado en Martes (Turno 1).")
                        elif martes2 == "":
                            martes2 = paciente
                            print("Turno reservado en Martes (Turno 2).")
                        elif martes3 == "":
                            martes3 = paciente
                            print("Turno reservado en Martes (Turno 3).")
                        else:
                            print("No hay cupos disponibles en Martes.")

            elif opcion == "2":
                dia = input("Día (1=Lunes, 2=Martes): ").strip()
                while (not dia.isdigit()) or (dia not in ("1", "2")):
                    print("Error: ingrese 1 o 2.")
                    dia = input("Día (1=Lunes, 2=Martes): ").strip()

                paciente = input("Nombre del paciente a cancelar: ").strip()
                while (paciente == "") or (not paciente.isalpha()):
                    print("Error: Solo se permiten letras.")
                    paciente = input("Nombre del paciente a cancelar: ").strip()

                if dia == "1":
                    if lunes1.lower() == paciente.lower() and lunes1 != "":
                        lunes1 = ""
                        print("Turno cancelado (Lunes Turno 1).")
                    elif lunes2.lower() == paciente.lower() and lunes2 != "":
                        lunes2 = ""
                        print("Turno cancelado (Lunes Turno 2).")
                    elif lunes3.lower() == paciente.lower() and lunes3 != "":
                        lunes3 = ""
                        print("Turno cancelado (Lunes Turno 3).")
                    elif lunes4.lower() == paciente.lower() and lunes4 != "":
                        lunes4 = ""
                        print("Turno cancelado (Lunes Turno 4).")
                    else:
                        print("No se encontró el paciente en Lunes.")
                else:
                    if martes1.lower() == paciente.lower() and martes1 != "":
                        martes1 = ""
                        print("Turno cancelado (Martes Turno 1).")
                    elif martes2.lower() == paciente.lower() and martes2 != "":
                        martes2 = ""
                        print("Turno cancelado (Martes Turno 2).")
                    elif martes3.lower() == paciente.lower() and martes3 != "":
                        martes3 = ""
                        print("Turno cancelado (Martes Turno 3).")
                    else:
                        print("No se encontró el paciente en Martes.")

            elif opcion == "3":
                dia = input("Día (1=Lunes, 2=Martes): ").strip()
                while (not dia.isdigit()) or (dia not in ("1", "2")):
                    print("Error: ingrese 1 o 2.")
                    dia = input("Día (1=Lunes, 2=Martes): ").strip()
                if dia == "1":
                    print("Agenda Lunes:")
                    print("Turno 1: " + (lunes1 if lunes1 != "" else "(libre)"))
                    print("Turno 2: " + (lunes2 if lunes2 != "" else "(libre)"))
                    print("Turno 3: " + (lunes3 if lunes3 != "" else "(libre)"))
                    print("Turno 4: " + (lunes4 if lunes4 != "" else "(libre)"))
                else:
                    print("Agenda Martes:")
                    print("Turno 1: " + (martes1 if martes1 != "" else "(libre)"))
                    print("Turno 2: " + (martes2 if martes2 != "" else "(libre)"))
                    print("Turno 3: " + (martes3 if martes3 != "" else "(libre)"))

            elif opcion == "4":
                ocup_lunes = 0
                if lunes1 != "":
                    ocup_lunes += 1
                if lunes2 != "":
                    ocup_lunes += 1
                if lunes3 != "":
                    ocup_lunes += 1
                if lunes4 != "":
                    ocup_lunes += 1
                disp_lunes = 4 - ocup_lunes

                ocup_martes = 0
                if martes1 != "":
                    ocup_martes += 1
                if martes2 != "":
                    ocup_martes += 1
                if martes3 != "":
                    ocup_martes += 1
                disp_martes = 3 - ocup_martes

                print("Lunes ocupados: " + str(ocup_lunes) + " / disponibles: " + str(disp_lunes))
                print("Martes ocupados: " + str(ocup_martes) + " / disponibles: " + str(disp_martes))

                if ocup_lunes > ocup_martes:
                    print("Día con más turnos: Lunes")
                elif ocup_martes > ocup_lunes:
                    print("Día con más turnos: Martes")
                else:
                    print("Empate en cantidad de turnos.")

            else:
                print("Cerrando sistema...")

    elif opcion_principal == "4":
        energia = 100
        tiempo = 12
        cerraduras_abiertas = 0
        alarma = False
        codigo_parcial = ""
        forzar_seguidas = 0

        agente = input("Nombre del agente: ").strip()
        while (agente == "") or (not agente.isalpha()):
            print("Error: Solo se permiten letras.")
            agente = input("Nombre del agente: ").strip()

        bloqueado = False
        while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
            if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
                bloqueado = True
                break

            print("")
            print("Estado -> Energia: " + str(energia) + " | Tiempo: " + str(tiempo) + " | Cerraduras: " + str(cerraduras_abiertas) + " | Alarma: " + ("ON" if alarma else "OFF"))
            print("1) Forzar cerradura (-20 energia, -2 tiempo)")
            print("2) Hackear panel (-10 energia, -3 tiempo)")
            print("3) Descansar (+15 energia max 100, -1 tiempo)")
            opcion = input("Opción: ").strip()
            while (not opcion.isdigit()) or (int(opcion) < 1 or int(opcion) > 3):
                print("Error: ingrese 1, 2 o 3.")
                opcion = input("Opción: ").strip()

            if opcion == "1":
                forzar_seguidas += 1
                energia -= 20
                tiempo -= 2

                if forzar_seguidas >= 3:
                    alarma = True
                    print("La cerradura se trabó. Alarma activada.")
                    continue

                if energia < 40 and not alarma and energia > 0 and tiempo > 0:
                    riesgo = input("Riesgo de alarma. Elegí un número 1-3: ").strip()
                    while (not riesgo.isdigit()) or (int(riesgo) < 1 or int(riesgo) > 3):
                        print("Error: ingrese un número 1-3.")
                        riesgo = input("Riesgo de alarma. Elegí un número 1-3: ").strip()
                    if riesgo == "3":
                        alarma = True
                        print("Alarma activada.")

                if not alarma and energia > 0 and tiempo > 0:
                    cerraduras_abiertas += 1
                    print("Cerradura abierta. Total: " + str(cerraduras_abiertas))

            elif opcion == "2":
                forzar_seguidas = 0
                energia -= 10
                tiempo -= 3
                if energia <= 0 or tiempo <= 0:
                    continue
                paso = 1
                for _ in range(4):
                    print("Hackeando... paso " + str(paso) + "/4")
                    codigo_parcial = codigo_parcial + "A"
                    paso += 1
                print("Código parcial: " + codigo_parcial)
                if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                    cerraduras_abiertas += 1
                    codigo_parcial = ""
                    print("Se abrió una cerradura por hackeo. Total: " + str(cerraduras_abiertas))

            else:
                forzar_seguidas = 0
                tiempo -= 1
                energia += 15
                if energia > 100:
                    energia = 100
                if alarma:
                    energia -= 10
                print("Descanso completado.")

        if cerraduras_abiertas == 3 and energia > 0 and tiempo > 0 and not bloqueado:
            print("VICTORIA")
        else:
            if bloqueado:
                print("DERROTA (bloqueo)")
            elif energia <= 0 or tiempo <= 0:
                print("DERROTA")
            else:
                print("DERROTA")

    elif opcion_principal == "5":
        print("--- BIENVENIDO A LA ARENA ---")
        nombre = input("Nombre del Gladiador: ").strip()
        while (nombre == "") or (not nombre.isalpha()):
            print("Error: Solo se permiten letras.")
            nombre = input("Nombre del Gladiador: ").strip()

        vida_jugador = 100
        vida_enemigo = 100
        pociones = 3
        dano_pesado = 15
        dano_enemigo = 12
        turno_gladiador = True

        print("=== INICIO DEL COMBATE ===")
        while vida_jugador > 0 and vida_enemigo > 0:
            if turno_gladiador:
                print(nombre + " (HP: " + str(vida_jugador) + ") vs Enemigo (HP: " + str(vida_enemigo) + ") | Pociones: " + str(pociones))
                print("Elige acción:")
                print("1. Ataque Pesado")
                print("2. Ráfaga Veloz")
                print("3. Curar")
                opcion = input("Opción: ").strip()
                while (not opcion.isdigit()) or (int(opcion) < 1 or int(opcion) > 3):
                    print("Error: Ingrese un número válido.")
                    opcion = input("Opción: ").strip()

                if opcion == "1":
                    dano_final = float(dano_pesado)
                    if vida_enemigo < 20:
                        dano_final = dano_final * 1.5
                    vida_enemigo -= dano_final
                    print("¡Atacaste al enemigo por " + str(dano_final) + " puntos de daño!")
                elif opcion == "2":
                    print(">> ¡Inicias una ráfaga de golpes!")
                    for _ in range(3):
                        vida_enemigo -= 5
                        print("> Golpe conectado por 5 de daño")
                else:
                    if pociones > 0:
                        vida_jugador += 30
                        pociones -= 1
                        print(">> Te curaste 30 puntos.")
                    else:
                        print("¡No quedan pociones!")

                turno_gladiador = False
            else:
                vida_jugador -= dano_enemigo
                print("¡El enemigo te atacó por " + str(dano_enemigo) + " puntos de daño!")
                turno_gladiador = True

        if vida_jugador > 0:
            print("¡VICTORIA! " + nombre + " ha ganado la batalla.")
        else:
            print("DERROTA. Has caído en combate.")

    else:
        print("Fin del programa")
