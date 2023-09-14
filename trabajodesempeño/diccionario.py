# Creamos un diccionario para almacenar las calificaciones
calificaciones = {}

# Definimos una función para agregar una calificación
def agregarNota(asignatura, nota):
    calificaciones[asignatura] = nota

# Definimos una función para ver las calificaciones
def verNotas():
    if not calificaciones:
        print("No hay notas para mostrar")
    else:
        for asignatura, nota in calificaciones.items():
            print(f"Asignatura: {asignatura}, Nota: {nota}")

# Definimos una función para editar una calificación
def editarNota(asignatura, nuevaNota):
    if asignatura in calificaciones:
        calificaciones[asignatura] = nuevaNota
        print('La nota fue editada correctamente!')
    else:
        print('No se encontró la nota especificada')

# Definimos una función para eliminar una calificación
def eliminarNota(asignatura):
    if asignatura in calificaciones:
        del calificaciones[asignatura]
        print('La nota fue eliminada correctamente!')
    else:
        print('No se encontró la nota especificada')

# Creamos un ciclo while para interactuar con el usuario
while True:
    print('='*30)
    print('1. Agregar calificación')
    print('2. Consultar calificaciones')
    print('3. Editar calificación')
    print('4. Eliminar calificación')
    print('5. Salir')
    print('='*30)

    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        asignatura = input("Ingrese la asignatura de la nota: ")
        nota = float(input("Ingrese la calificación de la materia: "))
        agregarNota(asignatura, nota)
        print('La nota se agregó correctamente')

    elif opcion == "2":
        verNotas()

    elif opcion == "3":
        asignatura = input('Ingrese la asignatura de la calificación a editar: ')
        nuevaNota = float(input('Ingrese la nueva calificación de la asignatura: '))
        editarNota(asignatura, nuevaNota)

    elif opcion == "4":
        asignatura = input('Ingrese la asignatura de la calificación a eliminar: ')
        eliminarNota(asignatura)

    elif opcion == "5":
        break
    else:
        print('Opción inválida')

print("Fin del programa")
