#Vamos a emplear de las colecciones vistas en clase las listas para esta tarea. A continuación las definimos.
lista_anotaciones = []
lista_dorsales = []
lista_jugadores = []

# Función para la toma de datos del equipo, jugadores y anotaciones
def entry():
    for i in range(2):
        # Solicitamos los datos de cada jugador
        jugador = input(f"Introduce el nombre del jugador {i+1} >> ").strip()
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

        # Añadimos los datos a las listas que tenemos creadas
        lista_jugadores.append(jugador)
        lista_dorsales.append(dorsal)
        lista_anotaciones.append(canastas_de_1 + (canastas_de_2*2) + (canastas_de_3*3))

# Función para imprimir las colecciones y determinar el máximo anotador
def stats():
    # Imprimir estadísticas de todos los jugadores
    for i in range(len(lista_jugadores)):
        print(f"Jugador: {lista_jugadores[i]}, Dorsal: {lista_dorsales[i]}, Anotación: [{lista_anotaciones[i]}]")

    # Determinar al jugador con la mayor anotación
    if lista_anotaciones:
        max_anotacion = max(lista_anotaciones)
        max_index = lista_anotaciones.index(max_anotacion)
        maximo_anotador = lista_jugadores[max_index]
        print(f"El máximo anotador ha sido {maximo_anotador} con {max_anotacion} puntos.")

# Función para el cierre o reinicio del programa
def cierre():
    reinicio = input("¿Quieres cerrar el programa? ")
    if reinicio.lower() == "y" or reinicio.lower() == "yes" or reinicio.lower() == "si":
        print("Sayonara, baby")
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