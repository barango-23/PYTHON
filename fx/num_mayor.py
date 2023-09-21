
numero_mayor=lambda num1, num2 : num1 if num1 > num2 else num2

#corre programa



if __name__ == "__main__":
    
    numero1=int(input(" digite el numero 1 :"))
    numero2=int(input("digite el numero 2: "))
    print("el numero mayor entre los dos es :",numero_mayor(numero1,numero2))