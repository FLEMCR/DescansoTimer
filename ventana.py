# Modulo: ventana.py

from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)
from PySide6.QtCore import QTimer

def mostrar_ventana(mensaje):

  ventana = QWidget()
  ventana.setWindowTitle("Alarma de Descanso")

  descripcion = QLabel(mensaje, ventana)
  descripcion.move(90, 80)

  boton = QPushButton("Continuar", ventana)
  boton.move(200, 200)
  boton.clicked.connect(ventana.close)

  ventana.resize(500, 300)
  ventana.show()
