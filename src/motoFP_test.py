from motoFP import *

def lee_carreras_test(filename):
    carreras = lee_carreras(filename)
    print(f"Número de carreras leídas: {len(carreras)}")
    print("Las dos primeras carreras son:")
    for carrera in carreras[:2]:
        print(carrera)
    print("Las dos últimas carreras son:")
    for carrera in carreras[-2:]:
        print(carrera)
    
    return carreras

def test_maximo_dias_sin_ganar(carreras, nombre_piloto):
    resultado = maximo_dias_sin_ganar(carreras, nombre_piloto)
    print(f"El máximo número de días sin ganar para {nombre_piloto} es: {resultado}")
    
def test_piloto_mas_podios_por_circuito(carreras):
    resultado = piloto_mas_podios_por_circuito(carreras)
    print("Piloto con más podios por circuito:")
    for circuito, piloto in resultado.items():
        print(f"{circuito}: {piloto}")

def test_escuderias_con_solo_un_piloto(carreras):
    resultado = escuderias_con_solo_un_piloto(carreras)
    print("Escuderías con solo un piloto que ha subido al podio:")
    for escuderia in resultado:
        print(escuderia)

if __name__ == "__main__":
    carreras = lee_carreras_test("data/mundial_motofp.csv")
    #test_maximo_dias_sin_ganar(carreras, "Francesco Bagnaia")
    #test_maximo_dias_sin_ganar(carreras, "Fabio Quartararo")
    #test_piloto_mas_podios_por_circuito(carreras)
    test_escuderias_con_solo_un_piloto(carreras)
