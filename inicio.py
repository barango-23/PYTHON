nombre = input("Nombre del Estudiante: ")
nota1 = float(input("Su primer nota es ---> : "))
nota2 = float(input("Su segunda nota es ---> : "))
nota3 = float(input("Su tercer nota es ---> : "))
definitiva = (nota1 + nota2 + nota3)/ 3

print("Su nombre es: " + nombre)
print("Su nota definitiva es:", definitiva)

if definitiva >= 0 and definitiva <= 2.0:
    print("Problemas de atención")
elif definitiva > 2.0 and definitiva <= 3.0:
    print("Puede recuperar")
elif definitiva > 3.0 and definitiva <= 4.0:
    print("muy bien genio")
elif definitiva > 4.0 and definitiva <= 4.5:
    print("Eres genial")
elif definitiva>4.6 :
    print ("eres el mejor :)")
else:
    print("Nota fuera de rango")

if definitiva >= 3:
    print("Aprobado")
else:
    print("Reprobado")


""""Se tiene que ejecutar con el input ya que sin el se comenta con un string en este programa estamos trayendo las notas
con el float ya que es decimal e imprimiendolas el if : else :"""
"""use el and que vendria a ser el & en programacion """
"""El trabajo constaba de calcularle las notas a un estudiante  calculando su nota definitiva y haciendole un calculo imprimiendole dependiendo de su nota si era mayor o igual"""