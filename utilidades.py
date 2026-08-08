# Modulo: utilidades.py

import config

restante = config.intervalo


def convertir_tiempo(segundos_totales):
    horas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = (
        (segundos_totales % 3600) % 60
    )  # Otra forma de hacerlo: "segundos = segundos_totales % 3600 % 60" porque 3600 es multiplo de 60 y así evitamos hacer un calculo extra

    return horas, minutos, segundos
