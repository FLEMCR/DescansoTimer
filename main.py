#Modulo: main.py

import time
import config
import utilidades

from PySide6.QtWidgets import QApplication, QWidget

def mostrar_alarma():
  print(f'Hora de Descanso {time.strftime("%H:%M:%S")}'.upper())

def contador():
  for restante in range(config.intervalo, 0, -1):
    print(f'Tiempo restante: {utilidades.minutos:02}:{utilidades.segundos:02}') #Le coloco :02 para que me muestre dos digitos y que si en caso flatan digitos me los agregue con un 0 adelante.
    time.sleep(1)

def iniciar():
  print("Iniciando...")
  while True:
    contador()
    mostrar_alarma()

# Programa Principal
iniciar()
