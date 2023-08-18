#declaracion de totales desde 0 
total_guajira = 0
total_chicamocha = 0
total_llanos = 0 
total_adultos = 0
total_ninos = 0
total_general = 0
total_adultosC=0
total_adultosL=0

# solicitamos el numero de cotizaciones en este input
num_cotizaciones = int(input("Ingrese el número de cotizaciones: "))

# aqui hicimos el ciclo for sobre  el numero de cotizaciones, declarando las variables que debiamos traer segun el ejercicio 
for _ in range(num_cotizaciones):
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    destino_turistico = input("Ingrese el destino (Guajira, Chicamocha o Llanos): ")
    numero_adultos = int(input("Ingrese el número de personas adultas: "))
    numero_ninos = int(input("Ingrese el número de niños: "))
    
    if destino_turistico.lower() == "guajira": #aqui hice un if para crear un subtotal sobre el numero o el precio de adulto y niños para cada destino
        subtotal = numero_adultos * 1450000 + numero_ninos * 870000
        total_guajira += subtotal
    elif destino_turistico.lower() == "chicamocha": # cree else if para seguir con la funcion de traer el subtotal de cada uno dependiendo de el resto de destinos
        subtotal = numero_adultos * 1600000 + numero_ninos * 960000
        total_chicamocha += subtotal
    elif destino_turistico.lower() == "llanos":
        subtotal = numero_adultos * 1200000 + numero_ninos * 720000
        total_llanos += subtotal

    total_adultosL+=numero_adultos
    total_adultosC+=numero_adultos
    total_adultos += numero_adultos
    total_ninos += numero_ninos #en este calculamos el total de cada persona X el numero 
    total_general += subtotal
    
    print("\nCotización:")
    print("Nombre Cliente:", nombre_cliente)
    print("Destino:", destino_turistico)
    print("Nro Personas Adultas:", numero_adultos)
    print("Nro Niños:", numero_ninos)
    print("Subtotal:", subtotal)
    print("=" *30)
    break

# en este le imprimo lo ultimo solicitado en el trabajo trayendo cada total de las cosas

print("\nResultados Finales:")
print("Cantidad de personas que viajan para la Guajira:", total_adultos)
print("Cantidad de personas que viajan para Cañón del Chicamocha:", total_adultosC)
print("Cantidad de personas que viajan para los Llanos Orientales:", total_adultosL)
print("Total de dinero de los viajes para la Guajira:", total_guajira)
print("Total de dinero de los viajes para Cañón del Chicamocha:", total_chicamocha)
print("Total de dinero de los viajes para los Llanos Orientales:", total_llanos)
print("Total de personas Adultas:", total_adultos)
print("Total de niños:", total_ninos)
print("Total de dinero de todos los destinos:", total_general)
