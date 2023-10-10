import random
import datetime

combinaciones = [["00","01","02"],
                 ["10","11","12"],
                 ["20","21","22"]]
equipos = ["X", "O"]
jugadores = {}


def sumar_historial(ganador):
    with open('historial_tren_en_raya.txt', 'a') as h:
        if ganador == 'Empate':
            h.write(f'\n({datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")}) - La partida terminó en empate.')
        else:
            h.write(f'\n({datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")}) - Ganador de la partida: {ganador}.')
def ver_historial():
    with open('historial.txt', 'r') as h:
        return h.read()
def condicion(equipo):
    # Combinacion 1
    for i in range(3):
        if (combinaciones[i][0] == equipo and combinaciones[i][1] == equipo and combinaciones[i][2] == equipo) or \
           (combinaciones[0][i] == equipo and combinaciones[1][i] == equipo and combinaciones[2][i] == equipo):
            return True
    if (equipo == combinaciones[0][0] and equipo == combinaciones[1][1] and equipo == combinaciones[2][2])\
        or equipo == combinaciones[0][2] and equipo == combinaciones[1][1] and equipo == combinaciones[2][0]:
        return True
    return False
def init_game():
    print('-----------\nTRES EN RAYA\n-----------')
    input_comenzar = input("Apriete X para empezar una partida ")

    if input_comenzar.upper() == "X":
        jugadores.update({"Jugador 1":equipos[random.randrange(0,2)]})
        del equipos[equipos.index(jugadores.get("Jugador 1"))]
        jugadores.update({"Jugador 2":equipos[0]})
        return game()
def verificar_disponibilidad(posicion):
    p = list(posicion)
    if combinaciones[int(p[0])][int(p[1])] != "".join(p):
        return False
    return True
def game():
    flag = True
    movimientos = 0
    turno = "Jugador 1"
    while flag:
        print(f'\nTurno de {turno}\n')
        [print(f'{position}') for position in combinaciones]
        input_eleccion = input(f'\nElije una posicion: ')
        if verificar_disponibilidad(input_eleccion) == False:
            print("\nYa hay un elemento en esa posicion. Intentalo de nuevo")
            continue
        combinaciones[int(list(input_eleccion)[0])][int(list(input_eleccion)[1])] = jugadores.get(turno)
        if condicion(jugadores.get(turno)) == True:
            [print(f'\n{position}') for position in combinaciones]
            print(f'\nEl {turno} ganó la partida')
            return turno
        movimientos += 1
        if movimientos == 9:
            flag = False
            print("Empate. Fin del juego.")
            return "Empate"
        turno = "Jugador 2" if turno=="Jugador 1" else "Jugador 1"
        print("---------------")
