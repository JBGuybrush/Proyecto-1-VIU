#importo este módulo a la librería porque quiero pausar unos segundos antes de que cierre el programa para que se vea el mensaje de despedida.
import time

#Vamos a emplear de las colecciones vistas en clase las listas para esta tarea. A continuación las definimos.
lista_anotaciones = []
lista_dorsales = []
lista_jugadores = []

# Función para la toma de datos del equipo, jugadores y anotaciones
def entry():
    while True:
        # Solicitamos los datos de cada jugador
        jugador = input(f"Introduce el nombre del jugador >> ").strip()
        try:
            dorsal = int(input(f"Introduce el dorsal del jugador {jugador} >> "))
        except ValueError:
            print("Lo siento, debe introducir números enteros.")
            return entry()
        try:
            canastas_de_1 = int(input(f"¿Cuántas canastas de 1 puntos ha encestado {jugador}? >> "))
        except ValueError:
            print("Lo siento, debe introducir números enteros.")
            return entry()
        try:
            canastas_de_2 = int(input(f"¿Cuántas canastas de 2 puntos ha encestado {jugador}? >> "))
        except ValueError:
            print("Lo siento, debe introducir números enteros.")
            return entry()
        try:
            canastas_de_3 = int(input(f"¿Cuántas canastas de 3 puntos ha encestado {jugador}? >> "))
        except ValueError:
            print("Lo siento, debe introducir números enteros.")
            return entry()

        # Recopilamos a continuación los datos introducidos por el usuario en las listas que tenemos creadas
        lista_jugadores.append(jugador)
        lista_dorsales.append(dorsal)
        lista_anotaciones.append(canastas_de_1 + (canastas_de_2*2) + (canastas_de_3*3))

        print("¿Quieres introducir otro jugador?")
        continuar = input("si o no:")
        if continuar.lower() != "si":
            break

# Función para imprimir las colecciones y determinar el máximo anotador
def stats():
    # Imprimir estadísticas de todos los jugadores
    for i in range(len(lista_jugadores)):
        print(f"Jugador: {lista_jugadores[i]}, Dorsal: {lista_dorsales[i]}, Anotación: [{lista_anotaciones[i]}]")

    # Determinar al jugador con la mayor anotación
    if lista_anotaciones:
        maxima_anotacion = max(lista_anotaciones)
        nombre_anotador = lista_anotaciones.index(maxima_anotacion)
        maximo_anotador = lista_jugadores[nombre_anotador]
        print(f"El máximo anotador ha sido {maximo_anotador} con {maxima_anotacion} puntos.")

# Función para el cierre o reinicio del programa
def cierre():
    reinicio = input("¿Quieres cerrar el programa? ")
    if reinicio.lower() == "y" or reinicio.lower() == "yes" or reinicio.lower() == "si" or reinicio.lower() == "s":
        print("Sayonara, baby")
        time.sleep(2) #retrasamos 2 segundos el cierre del programa para que el usuario vea el mensaje.
        quit()
    else:
        print("Okey, regresamos Doc")
        del lista_jugadores[:]
        del lista_dorsales[:]
        del lista_anotaciones[:]
        return entry(), stats(), cierre()

# Ejecución del programa
entry()
stats()
cierre()