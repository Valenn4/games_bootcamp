import piedra_papel_tijera.p_p_t as p_p_t
import tres_en_raya.tres_en_raya

def inicio():
    option = input("Bienvendido, ¿que deseas jugar?, elige una opcion \n1-Tres en linea \n2-Piedra, papel o tijeras\nElija un juego: ")
    if option == "1":
        result = tres_en_raya.tres_en_raya.init_game()
        tres_en_raya.tres_en_raya.sumar_historial(result)
        inicio()
    elif option == '2':
        result = p_p_t.Juego_piedra_papel_tijeras()
        p_p_t.guardar_resultados(result)
        inicio()

inicio()