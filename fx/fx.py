def suma(num1,num2):
    return num1+num2

sumando= lambda nur1, nur2: nur1+nur2

def restar():
    pass

if __name__=="__main__":
 print(suma(123,788))
 n1=int(input("ingrese el numero 1: ")) # capturar un numero
 n2=int(input("ingrese el numero 2: "))
print('funcion con def',suma(n1,n2))
print('funcion con lambda', sumando())