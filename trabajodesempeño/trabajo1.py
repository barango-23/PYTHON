#declaracion de totales desde 0 
total_guajira = 0
total_chicamocha = 0
total_llanos = 0 
total_adultos = 0
total_ninos = 0
total_general = 0


# solicitamos el numero de cotizaciones en este input
num_cotizaciones = int(input("Ingrese el número de cotizaciones: "))


for _ in range(3): #con este for cree un ciclo de que si añado 3 datos por ende se cerrara y me mostrara resultados finales!
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    destino_turistico = input("Ingrese el destino (Guajira, Chicamocha o Llanos): ")
    numero_adultos = int(input("Ingrese el número de personas adultas: "))
    numero_ninos = int(input("Ingrese el número de niños: "))
    
    if destino_turistico.lower() == "guajira": #aqui hice un if para crear un subtotal sobre el numero o el precio de adulto y niños para cada destino
        subtotal = numero_adultos * 1450000 + numero_ninos * 870000
        total_guajira += subtotal
        cant_personasgj = numero_ninos+numero_adultos #creacion de variable unica
    elif destino_turistico.lower() == "chicamocha": # cree else if para seguir con la funcion de traer el subtotal de cada uno dependiendo de el resto de destinos
        subtotal = numero_adultos * 1600000 + numero_ninos * 960000
        total_chicamocha += subtotal
        cant_personascm=numero_ninos+numero_adultos #creacion de variable unica
    elif destino_turistico.lower() == "llanos":
        subtotal = numero_adultos * 1200000 + numero_ninos * 720000
        total_llanos += subtotal
        cant_personasor=numero_ninos+numero_adultos #creacion de variable unica

#el .lower no es necesario pero lo use para que el caracter se me convirtiera en minusculas en pocas palabras que el texto sea en MINUSCULA 

    total_adultos += numero_adultos
    total_ninos += numero_ninos #en este calculamos el total de cada persona X el numero 
    total_general += subtotal
    
    print("\nCotización:")
    print("Nombre Cliente:", nombre_cliente) #creamos imprimision inicial 
    print("Destino:", destino_turistico)
    print("Nro Personas Adultas:", numero_adultos)
    print("Nro Niños:", numero_ninos)
    print("Subtotal:", subtotal)
    print("=" *30) #con este print creo como un tipo de linea como para hacerlo mas practico o es como un tipo de <br> por asi decirlo
    

# en este le imprimo lo ultimo solicitado en el trabajo trayendo cada total de las cosas

print("\nResultados Finales:")
print("Cantidad de personas que viajan para la Guajira:", cant_personasgj)
print("Cantidad de personas que viajan para Cañón del Chicamocha:", cant_personascm)
print("Cantidad de personas que viajan para los Llanos Orientales:",cant_personasor)# creamos una variable de cantidad de personas dentro de los IF para la cantidad de personas en cada destino 
print("Total de dinero de los viajes para la Guajira:", total_guajira)
print("Total de dinero de los viajes para Cañón del Chicamocha:", total_chicamocha)
print("Total de dinero de los viajes para los Llanos Orientales:", total_llanos)
print("Total de personas Adultas:", total_adultos)
print("Total de niños:", total_ninos)
print("Total de dinero de todos los destinos:", total_general)
