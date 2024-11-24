#Creación de listas
lista_anotaciones = []
lista_dorsales = []
lista_jugadores = []
maxima_anotacion = 0
nombre_jugador_maxima_anotacion = ""

for jugador in range(5):
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

#imprimimos
for i in range (3):
    print(f"jugador {lista_jugadores[i]}, dorsal [{lista_dorsales[i]}, anotacion [{lista_anotaciones[i]}]")

print(f"Máximo anotador es {nombre_jugador_maxima_anotacion} con {maxima_anotacion} puntos.")

#cierre o reinicio del programa por interacción con usuario
si = True
no = False
print("¿Quieres salir de python?")
typed_answer = input("Responda si o no:")
if typed_answer == "si":
        print("Sayonara, baby")
        quit()
if typed_answer == "no":
        print("¿Quieres reiniciar el programa?")
        reinicio = input("y/n:")
        if reinicio == "y":
            print("Empecemos de nuevo")
            for jugador in range(5):
                # solicitar las anotaciones
                jugador = input(f"introduce el nombre del jugador {jugador}")
                dorsal = input(f"introduce el dorsal {jugador}")
                anotacion = int(input(f"introduce anotacion del jugador {jugador}"))
                # añadir a una lista
                lista_jugadores.append(jugador)
                lista_dorsales.append(dorsal)
                lista_anotaciones.append(anotacion)
                # el maximo anotador
                if (anotacion > maxima_anotacion):
                    maxima_anotacion = anotacion
                    nombre_jugador_maxima_anotacion = jugador
        if reinicio == "n":
            print("Sayonara, baby")
            quit()