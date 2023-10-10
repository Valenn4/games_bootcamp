
import random
def guardar_resultados(resultados):
    with open('Historial_piedra_papel_o_tijeras.txt', 'a') as archivo:
        for resultado in resultados:
            archivo.write(resultado + '\n')
def Juego_piedra_papel_tijeras():
    
    opciones = ['piedra','papel','tijeras']
    resultados = []
    while True:
        jugador = input('Elige una opcion "Piedra", "Papel", "Tijeras" o "Salir": ').lower()
        if jugador == "salir":
            print("Hasta luego")
            break
        if jugador not in opciones:
            print("Opione invalida elige otra")
            continue
        computadora = opciones[random.randrange(0,len(opciones))]
        if jugador == computadora:
            resultado = "Empate"
        elif (jugador == "papel" and computadora == "piedra") or (jugador == "piedra" and computadora =="tijeras") or (jugador =="tijera" and computadora =="papel"):
            resultado  = "Ganas"
        else:
            resultado =  "Perdiste"
        resultados.append(resultado)
        print(f'Tú elegiste: {jugador.capitalize()}')
        print(f'Computadora eligio: {computadora.capitalize()}')
        print(f'Tu: {resultado}\n')
        return resultados

