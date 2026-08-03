# Modulo: main.py

import time, sys
import config, utilidades, ventana

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication


timer = QTimer()


def actualizar_contador():
  horas, minutos, segundos = utilidades.convertir_tiempo(utilidades.restante)
  print(f"Tiempo restante: {horas:02}:{minutos:02}:{segundos:02}")
  utilidades.restante -= 1
  if utilidades.restante <= 0:
    ventana.mostrar_ventana("Hora de descansar.")
    utilidades.restante = config.intervalo


def iniciar():
  app = QApplication(sys.argv)
  timer.timeout.connect(actualizar_contador)
  timer.start(1000)
  app.exec()


iniciar()
