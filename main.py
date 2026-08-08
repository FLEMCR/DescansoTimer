# Modulo: main.py

import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

import config
import utilidades
from ventana import VentanaAlarma

app = QApplication(sys.argv)
ventana = VentanaAlarma()

ventana.show()

timer = QTimer()


def actualizar_contador():
    horas, minutos, segundos = utilidades.convertir_tiempo(utilidades.restante)
    ventana.actualizar_tiempo(horas, minutos, segundos)
    utilidades.restante -= 1
    if utilidades.restante < 0:
        timer.stop()
        ventana.mostrar_final("Hora de descansar")


timer.timeout.connect(actualizar_contador)
timer.start(1000)


def reiniciar_contador():
    utilidades.restante = config.intervalo
    timer.start(1000)
    ventana.tiempo_label.show()
    ventana.boton.hide()
    ventana.descripcion.setText("")
    ventana.show()  # ← Para que la ventana vuelva a ser visible


ventana.continuar.connect(reiniciar_contador)


app.exec()
