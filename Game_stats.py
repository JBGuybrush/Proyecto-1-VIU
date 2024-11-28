#Vamos a emplear de las colecciones vistas en clase las listas para esta tarea. A continuación las definimos.
lista_anotaciones = []
lista_dorsales = []
lista_jugadores = []
nombre_jugador_maxima_anotacion = ""

#Función para la toma de datos del equipo, jugadores y anotaciones.
def entry(maxima_anotacion=0):
    for jugador in range(1):
    #solicitar las anotaciones
        jugador = input(f"introduce el nombre del jugador {jugador}")
        dorsal = input(f"introduce el dorsal {jugador}")
        anotacion = int(input(f"introduce anotacion del jugador {jugador}"))
    #añadir a una lista
        lista_jugadores.append(jugador)
        lista_dorsales.append(dorsal)
        lista_anotaciones.append(anotacion)
    #el maximo anotador
    if(anotacion>maxima_anotacion):
        maxima_anotacion = anotacion
        nombre_jugador_maxima_anotacion = jugador

#Función para imprimir las colecciones
def stats(maxima_anotacion=0):
    for i in range (1):
        print(f"jugador {lista_jugadores[i]}, dorsal {lista_dorsales[i]}, anotacion [{lista_anotaciones[i]}]")
        print(f"Máximo anotador es {nombre_jugador_maxima_anotacion} con {maxima_anotacion} puntos.")

#Función para el cierre o reinicio del programa por interacción con usuario
def cierre():
    reinicio = input("¿Quieres cerrar el programa?")
    if reinicio == "y" or reinicio == "yes" or reinicio == "si":
        print("Sayonara, baby")
        quit()
    else:
        print("Okey")
        entry(maxima_anotacion=0)
        stats(maxima_anotacion=0)
        cierre()

entry(maxima_anotacion=0)
stats(maxima_anotacion=0)
cierre()
