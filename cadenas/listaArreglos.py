modulos=["Logica ","Base de datos","HTML5","Moviles"]
print(modulos)
print("Elemento Inicial de la lista de arreglos es ->>>", modulos[0])
print("Elemento Final  de la lista de arreglos es ->>>", modulos[-1])
print("Numero de Elementos que contiene la lista ->>>", len(modulos) )
print("Ultimo elemento de la lista es ->>>",modulos[len(modulos)-1])
#los arreglos se calculan desde el primero en 0 , hasta los ultimos con el "-1 "

# Metodo para agregar un registro, append
print("Agregar un elemento nuevo a la lista ->>>")
modulos.append("Metodologia agiles")
print(modulos)
#print("Ultimo elemento de la lista es ->>>",modulos[len(modulos)-1])

# Metodo count, cantidad de veces que se repite un elemento en la lista
print("Cantidad de veces que aparece HTML5 ->>> ",modulos.count("HTML5"))

# Metodo sort, lista ordenada alfabeticamente
print("Lista ordenada alfabeticamente ->>> ")
modulos.sort()
#print(modulos)
i=1
for indice in modulos: #el indice es cualquier nombre
    print(indice) #desde la posicion indice hasta modulo imprima la lista ordenada
    i=1+1