#Modulo: main.py

import time
from config import intervalo

def mostrar_alarma():
  print(f'Hora de Descanso {time.strftime("%H:%M:%S")}')

def contador():
  for restante in range(intervalo, 0, -1):
    minutos = restante // 60
    segundos = restante % 60
    print(f'Tiempo restante: {minutos:02}:{segundos:02}') #Le coloco :02 para que me muestre dos digitos y que si en caso flatan digitos me los agregue con un 0 adelante.
    time.sleep(1)

def iniciar():
  print("Iniciando...")
  while True:
    contador()
    mostrar_alarma()

# Programa Principal
iniciar()
