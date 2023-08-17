respuesta= 1

while respuesta==1:
    respuesta=int(input(">>>>>1. si\n2. No\nEscriba el numero para continuar<<<<<: ")) #si se utiliza el 1 se vuelve y se ejecuta el mientras si se usa el 2 se cierra el mientras 
    while respuesta !=1 and respuesta !=2: #se utiliza el ! para decir como "Diferente"
        
        print("Error, vuelva a intentarlo 🤣🤣")
        respuesta=int(input(">>>>>1. si\n2. No\nEscriba el numero para continuar<<<<<: "))
        break
        #cerramos este mientras
        
        
     
def numerodeintentos():
  # Creamos el numero de intentos solicitados..
  max_intentos = 3

#crear una contraseña
  contraseña =(123)

  # iniciamos el bucle o el ciclo while  en verdadero ya que se va cumplir y se cumplio
  while True:
    try:
      entrada_contraseña = int(input("Ingrese su contraseña👌: "))
    except ValueError:
      print("Entrada inválida.") #usamos el try cuando si no se ingresa la contraseña correcta me aparezca en pantalla entrada invalida#

   
    if entrada_contraseña == contraseña:
      print("Bienvenido contraseña correcta :).") #si ingresamos la contraseña correcta se usa el break para finalizar
      break
    else:
     
      print("Contraseña incorrecta.") # y si no que me aparezca en pantalla contraseña incorrecta ya que no cumpli el if


    max_intentos -= 1 # con esto estoy disminuyendo el numero de intentos si lo supero y llega a la condicion del ==0 se bloquea es decir se cierra el numero de intentos

    if max_intentos == 0:
      print("Ha superado el número máximo de intentos bloqueado X 24 horas <:( .")
      break

# llamamos la funcion 
numerodeintentos()