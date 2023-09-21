#Funcion sin parametros y no devuelve nada

def FuncionConParametros():
    print("Bienvenidos a las funciones en python 😁👌")


def SaludarName(nombre):
    print(f"hola {nombre}, como amaneces hoy???")
   ## pass #se crea el pass para completar o llenar espacios vacios o bloques
   
   
def ProgamaNota(nombre, nota):
       print(f"Hola {nombre}, tienes una nota de {nota}")
       
def ProgramaDefault(nombre, nota, programa="Nuevas tecnologias"):
 print(f"Hola {nombre}, tienes una nota de {nota}, en el modulo de {programa}")
       
def Operaciones(num1,num2):
    return(num1+num2, num1*num2)
   
   #Llamar las funciones
if __name__== "__main__":
    print("="*30)
ProgamaNota("Brayan", 4.9)
ProgamaNota("felipe", 4.2) #el orden se basa en como la pongamos en los parametros
ProgramaDefault("juan", 3.2) 
resultado=Operaciones(4,34)
print (resultado) 
num1=23
num2=10

print(f"{num1}+{num2}={resultado}")
print(f"{num1}*{num2}={resultado}")
print(f"{num1}/{num2}={resultado}")
   
   # SaludarName("Brayan") 
    #user= "Arango Morales"
    #SaludarName(user)
    
    
    #saludar -- variable
    #saludar()-- funcion
    #saludar. -- metodo

    


