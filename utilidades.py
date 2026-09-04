# Modulo: utilidades.py

import config

restante = config.intervalo  # Una copia de la variable "intervalo" de config.py, que se puede modificar sin afectar el valor original.

restante_descanso = config.intervalo_descanso


def convertir_tiempo(segundos_totales):
    horas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = (
        (segundos_totales % 3600) % 60
    )  # Otra forma de hacerlo: "segundos = segundos_totales % 3600 % 60" porque 3600 es multiplo de 60 y así evitamos hacer un calculo extra

    return horas, minutos, segundos
