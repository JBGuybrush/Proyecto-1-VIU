#Vamos a emplear de las colecciones vistas en clase las listas para esta tarea. A continuación las definimos.

lista_anotaciones = []
lista_dorsales = []
lista_jugadores = []

#Función para la toma de datos del equipo, jugadores y anotaciones.
def entry(maxima_anotacion=0):
    for jugador in range(2):
    #solicitar datos de partido
        jugador = str(input(f"introduce el nombre del jugador {jugador} >> "))
        try:
            dorsal = int(input(f"introduce el dorsal {jugador} >> "))
        except ValueError:
            print ("lo siento, debe introducir números enteros")
            return entry(maxima_anotacion)
        try:
            anotacion = int(input(f"introduce anotacion del jugador {jugador} >> "))
        except ValueError:
            print ("lo siento, debe introducir números enteros")
            return entry(maxima_anotacion)
    #añadir a una lista
        lista_jugadores.append(jugador)
        lista_dorsales.append(dorsal)
        lista_anotaciones.append(anotacion)
    #el maximo anotador
        maxima_anotacion = max(lista_anotaciones)


#Función para imprimir las colecciones
def stats():
    for i in range (2):
            print(f"jugador {lista_jugadores[i]}, dorsal {lista_dorsales[i]}, anotacion [{lista_anotaciones[i]}]")

    print(f"Máximo anotador es", max(lista_jugadores), "con", max(lista_anotaciones), "puntos.")

#Función para el cierre o reinicio del programa por interacción con usuario
def cierre():
    reinicio = input("¿Quieres cerrar el programa? ")
    if reinicio == "y" or reinicio == "yes" or reinicio == "si":
        print("Sayonara, baby")
        quit()
    else:
        print("Okey, reiniciamos")
        del lista_jugadores[:]
        del lista_dorsales[:]
        del lista_anotaciones[:]
        return entry(maxima_anotacion=0), stats(), cierre()

entry(maxima_anotacion=0)
stats()
cierre()
