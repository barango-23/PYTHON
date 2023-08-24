"""mensaje="   Bienvenido.. al curso de python "

# Metodo len, imprime el tamaño de longitud  del string
print ("El texto original es : ", mensaje)
print("el tamaño del texto es de", len(mensaje))
print("="*10)

# Metodo strip, quita espacios al inicio y al final
sinespacios= mensaje.strip()
print("El tamaño del texto sin espacios ", sinespacios)
print("El tamaño del texto sin espacios es de ",len(sinespacios))
print("="*10)

# Metodo Upper, Mayusculas
print("Texto en MAYUSCULAS")
print("="*10)
print(sinespacios.upper())

# Metodo lower, Minusculas
print("Texto en minúscula")
print("="*10)
print(sinespacios.lower())

# Metodo Title ,inicial de cada palabra en mayúscula
print("Inicial de cada palabra en mayuscula")
print("="*10)
print(sinespacios.title())

# Metodo capitalize, Solo la primera palabra en mayúscula
print("Primera palabra en mayúscula ")
print("="*10)
print(sinespacios.capitalize())

# Metodo split, separacion de cadena de texto
sinespacios= mensaje.strip()
parrafo= sinespacios.split("...")
print(parrafo [0])
print(parrafo [1])"""



