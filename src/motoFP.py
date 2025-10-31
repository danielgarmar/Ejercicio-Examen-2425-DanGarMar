from typing import NamedTuple
from datetime import datetime
import csv

Piloto=NamedTuple("Piloto", [("nombre", str),("escuderia", str)])

CarreraFP=NamedTuple("CarreraFP",
    [
        ("fecha_hora", datetime), 
        ("circuito",str),                    
        ("pais",str), 
        ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado
        ("tiempo",float), 
        ("podio", list[Piloto])
    ]
)

def lee_carreras(filename: str) -> list[CarreraFP]:
    carreras: list[CarreraFP] = []
    lector = csv.DictReader(open(filename, encoding="utf-8"))
    for linea in lector:
        fecha_hora = datetime.strptime(linea["Fecha y Hora"], "%Y-%m-%d %H:%M")
        circuito = linea["Circuito"]
        pais = linea["País"]
        if asfalto := linea["Asfalto"].lower() == "seco":
            seco = True
        else:
            seco = False
        tiempo = float(linea["Tiempo de la Vuelta Rápida"])
        podio = []
        ganador = Piloto(linea["Nombre Ganador"], linea["Marca Ganador"])
        segundo = Piloto(linea["Nombre Segundo Clasificado"], linea["Marca Segundo Clasificado"])
        tercero = Piloto(linea["Nombre Tercer Clasificado"], linea["Marca Tercero Clasificado"])
        podio.extend([ganador, segundo, tercero])
        carrera = CarreraFP(fecha_hora, circuito, pais, seco, tiempo, podio)
        carreras.append(carrera)
    return carreras

def maximo_dias_sin_ganar(carreras: list[CarreraFP], nombre_piloto: str) -> int:
    max_dias = None
    ultimo_dia = None

    for carrera in carreras:
        ganador = carrera.podio[0].nombre
        fecha = carrera.fecha_hora.date()

        if ganador == nombre_piloto:
            if ultimo_dia is not None:
                dias_sin_ganar = (fecha - ultimo_dia).days
                if max_dias is None or dias_sin_ganar > max_dias:
                    max_dias = dias_sin_ganar
            ultimo_dia = fecha

    return max_dias

def piloto_mas_podios_por_circuito(carreras: list[CarreraFP]) -> dict[str,str]:
    circuito_podios = {}

    for carrera in carreras:
        circuito = carrera.circuito
        if circuito not in circuito_podios:
            circuito_podios[circuito] = {}

        for piloto in carrera.podio:
            nombre = piloto.nombre
            if nombre not in circuito_podios[circuito]:
                circuito_podios[circuito][nombre] = 0
            circuito_podios[circuito][nombre] += 1

    resultado = {}
    for circuito, podios in circuito_podios.items():
        piloto_mas_podios = max(podios, key=podios.get)
        resultado[circuito] = piloto_mas_podios

    return resultado

def escuderias_con_solo_un_piloto(carreras: list[CarreraFP]) -> list[str]:
    escuderia_pilotos = {}

    for carrera in carreras:
        for piloto in carrera.podio:
            escuderia = piloto.escuderia
            nombre = piloto.nombre
            if escuderia not in escuderia_pilotos:
                escuderia_pilotos[escuderia] = set()
            escuderia_pilotos[escuderia].add(nombre)

    resultado = [escuderia for escuderia, pilotos in escuderia_pilotos.items() if len(pilotos) == 1]

    return resultado
