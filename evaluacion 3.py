asiento=['Asiento Comun', 'Asiento con espacio para piernas', 'Asiento que no reclina']
asiento_comun= 60000
asiento_con_espacio=80000
asiento_sin_reclinacion= 50000


pasajeros=[]
while True:
    print("Bienvenido a la línea aérea “Flash”")
    print("1. Comprar pasajes")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Mostrar Listado de pasajeros")
    print("4. Buscar pasajeros")
    print("5. Reasignar asiento")
    print("6. Mostrar ganancias totales")
    print("7. Salir")

    opcion=int(input("Elija una opción "))
    if opcion==1:
        pasajes=int(input("Ingrese cantidad de pasajes "))
        asiento=input("Escoga un tipo de asiento \n 1.Asiento Común\n2.Asiento con espacio para piernas\n3.Asiento que no relina ")
    elif opcion ==3:
        def lista_pasajeros(pasajeros):
            print(pasajeros)
    elif opcion==4:
        rut=int(input("Ingrese Rut "))
        if rut not in pasajeros:
            print("Rut no valido")
        rut=int(input("Ingrese Rut "))
    elif opcion==5:
        int(input("Ingrese Rut del pasajero "))
        asiento=input("Escoga un tipo de asiento \n 1.Asiento Común\n2.Asiento con espacio para piernas\n3.Asiento que no relina ")
    elif opcion==6:
        print()

    elif opcion == 7:
        break