#Modulo: ventana.py

from PySide6.QtWidgets import QWidget, QLabel, QPushButton
from PySide6.QtCore import Signal


class VentanaAlarma(QWidget):
    continuar = Signal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Alarma de Descanso")

        self.descripcion = QLabel("", self)
        self.descripcion.move(90, 80)

        self.boton = QPushButton("Continuar", self)
        self.boton.move(200, 200)

        self.boton.clicked.connect(self.ocultar)

        self.resize(500, 300)

    def mostrar(self, mensaje):
        self.descripcion.setText(mensaje)
        self.show()

    def ocultar(self):
        self.hide()
        self.continuar.emit()
