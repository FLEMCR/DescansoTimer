# Modulo: main.py

import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

import config
import utilidades

from ventana import VentanaAlarma


app = QApplication(sys.argv)
ventana = VentanaAlarma()
timer = QTimer()


def actualizar_contador():
    horas, minutos, segundos = utilidades.convertir_tiempo(utilidades.restante)
    print(f"Tiempo restante: {horas:02}:{minutos:02}:{segundos:02}")
    utilidades.restante -= 1
    if utilidades.restante < 0:
        timer.stop()
        ventana.mostrar("Hora de descansar")

timer.timeout.connect(actualizar_contador)
timer.start(1000)


def reiniciar_contador():
    utilidades.restante = config.intervalo
    timer.start(1000)


ventana.continuar.connect(reiniciar_contador)


app.exec()
