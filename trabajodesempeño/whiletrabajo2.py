# declaracion de variables o totales desde 0 lo mismo que con el for
total_guajira = 0
total_chicamocha = 0
total_llanos = 0
total_adultos = 0
total_ninos = 0
total_general = 0
# aqui solicitamos el numero de cotizaciones inicializandola desde 0 
num_cotizaciones = int(input("Ingrese el número de cotizaciones: ")) #el int es por que estoy pidiendo un numero obviamente 
cotizacion_actual = 0

# aqui estoy usando el ciclo while y la condicion se cumple mientras el numero de cotizaciones sea menor a cotizacion actual!
while cotizacion_actual < num_cotizaciones:
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    destino = input("Ingrese el destino (Guajira, Chicamocha o Llanos): ")
    nro_adultos = int(input("Ingrese el número de personas adultas: "))
    nro_ninos = int(input("Ingrese el número de niños: "))
    
    if destino.lower() == "guajira":
        subtotal = nro_adultos * 1450000 + nro_ninos * 870000
        total_guajira += subtotal
        cant_personasgj = nro_ninos+nro_adultos
    elif destino.lower() == "chicamocha":                              #aqui hice un elif lo mismo que en el for junto con el .lower solo como por buenas practicas trayendo lo mismo 
        subtotal = nro_adultos * 1600000 + nro_ninos * 960000
        total_chicamocha += subtotal
        cant_personascm = nro_ninos+nro_adultos
    elif destino.lower() == "llanos":
        subtotal = nro_adultos * 1200000 + nro_ninos * 720000
        total_llanos += subtotal
        cant_personasor = nro_ninos+nro_adultos
    
    total_adultos += nro_adultos
    total_ninos += nro_ninos #totalidad de cada persona y niño defini aqui con un + para que vaya acumulando entre comillas la cantidad
    total_general += subtotal #cree una variable total general para traer el  subtotal de cada uno de los destinos y num de personas y niños
    
    print("\nCotización:")
    print("Nombre Cliente:", nombre_cliente)
    print("Destino:", destino)
    print("Nro Personas Adultas:", nro_adultos) #aqui hice la impresion inicial de la cotizacion!
    print("Nro Niños:", nro_ninos)
    print("Subtotal:", subtotal)
    print("=" * 30) # con este print cree una separacion de linea como para que se vea mas practico Y lo multiplique x30 aunque puede ser por cualquier numero

    cotizacion_actual += 1 #entre vaya agregando mas cotizaciones se va acumulando de uno a uno
# Impresion final de cada totalidad 
print("\nResultados Finales:")  #segun mi logica la cantidad de personas en cada destino se calcula con el numero de adultos + niños pero no me suma 
print("Cantidad de personas que viajan para la Guajira:", cant_personasgj)
print("Cantidad de personas que viajan para Cañón del Chicamocha:", cant_personascm)
print("Cantidad de personas que viajan para los Llanos Orientales:",cant_personasor)
print("Total de dinero de los viajes para la Guajira:", total_guajira)
print("Total de dinero de los viajes para Cañón del Chicamocha:", total_chicamocha) #no le cree un break por que no lo vi necesario ya que el programa "PARA" cuando la condicion cumple 
print("Total de dinero de los viajes para los Llanos Orientales:", total_llanos)
print("Total de personas Adultas:", total_adultos)
print("Total de niños:", total_ninos)
print("Total de dinero de todos los destinos:", total_general)
