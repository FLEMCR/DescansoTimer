# Modulo: utilidades.py

import config

restante = config.intervalo


def convertir_tiempo(segundos_totales):
    horas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = segundos_totales % 60

    return horas, minutos, segundos
