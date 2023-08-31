# Se crea el Diccionario

Agenda={
    'contacto1':{
    'nombre': 'juan',
    'telefono': '34454546',
    'ciudad': 'medellin'
    },
    'contacto2':{
    'nombre': 'Felipe',
    'telefono': '3656786',
    'ciudad': 'bogota'
},
    'contacto3':{
    'nombre':'melissa',
    'telefono': '32121122',
    'ciudad': 'bogota'

    },
    'contacto4':{
       'nombre':'brayan',
    'telefono': '3222121',
    'ciudad': 'bogota' 
    },
    'contacto5':{
        'nombre':'karen',
    'telefono': '3456777',
    'ciudad': 'barranquilla'
    },
    'contacto6':{
       'nombre':'marta',
    'telefono': '344567',
    'ciudad': 'cali' 
    },
    'contacto7':{
       'nombre':'camila',
    'telefono': '4566776',
    'ciudad': 'bogota' 
    },
    'contacto8':{
    'nombre':'dayana',
    'telefono': '34556778',
    'ciudad': 'bogota'
    },
    'contacto9':{
      'nombre':'esperanza',
    'telefono': '5565656',
    'ciudad': 'medellin'  
    },
    'contacto10':{
        'nombre':'santiago',
    'telefono': '244665',
    'ciudad': 'bogota'
    },
    'contacto11':{
        'nombre':'david',
    'telefono': '767644',
    'ciudad': 'bogota'
    },
    'contacto12':{
       'nombre':'samuel',
    'telefono': '355567',
    'ciudad': 'bogota' 
    },
    'contacto13':{
      'nombre':'enrique',
    'telefono': '5666787',
    'ciudad': 'medellin'  
    },
    'contacto14':{
      'nombre':'mathias',
    'telefono': '4643323',
    'ciudad': 'bogota'  
    },
    'contacto15':{
    'nombre':'esteban',
    'telefono': '88964545',
    'ciudad': 'cali'
    }
    # creamos los 15 contactos y los imprimimos
}
#print(Agenda) 
#Metodo para traer todos los items o contactos
print("Todos los contactos:")
for key, value in Agenda.items():
  print(f"{key}: {value}")

#USAR METODO GET PARA COGER DENTRO DE UN DICCIONARIO
nombre_cliente1=Agenda.get('contacto1',{}).get('nombre', 'no encontrado')
print(f"\ nombre  del contacto1: {nombre_cliente1}")

#Actualizar documento en el diccionario
Agenda['contacto10']['nombre']='albeiro'
print(Agenda['contacto10'])

#Metodo de mostrar solo keys del diccionario
print("\n Todas las keys o claves:")
for key in Agenda.values():
  print(key)

# agendar 15 contacto e imprimir todos los contactos usar el metodo get para acceder al valor de nombre tambien actualizar un documento en el diccionario usar tambien el metodo keys para obtener todas las  claves del diccionario y por ultimo usar el metodo items para obtener todos los pares clave-valor del diccionario en python