#Hacer tabla de multiplicar
num=int (input("Numero a X >>> "))
for i in range(1,11): #Con esto hacemos un rango de hasta donde va multiplicar el numero y el 11 es para que termine en 10
    print(f"{i} * {num}= {i*num} ")#imprimir interpolando llamando ciertas variables junto con su ciclo