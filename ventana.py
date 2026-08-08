# Modulo: ventana.py

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class VentanaAlarma(QWidget):
    continuar = Signal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Alarma de Descanso")

        # --- Etiqueta para mostrar el tiempo restante ---
        # La creamos con texto inicial "00:00:00", luego se actualizará.
        self.tiempo_label = QLabel("00:00:00", self)
        # Le damos un tamaño de fuente grande para que destaque.
        self.tiempo_label.setStyleSheet("font-size: 48px;")

        # --- Etiqueta de mensaje (ya existente) ---
        self.descripcion = QLabel("", self)
        # Eliminamos margin: auto porque no funciona en Qt; el layout centrará.

        # --- Botón "Continuar" ---
        self.boton = QPushButton("Continuar", self)
        self.boton.clicked.connect(self.ocultar)
        # Lo ocultamos desde el principio; solo se verá al finalizar la cuenta.
        self.boton.hide()

        # --- Layout vertical para centrar los widgets ---
        layout = QVBoxLayout()
        # Añadimos los widgets en orden: tiempo, descripción, botón.
        # alignment=Qt.AlignCenter los centra tanto horizontal como verticalmente.
        layout.addWidget(self.tiempo_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.descripcion, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.boton, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)
        # Damos un tamaño inicial a la ventana para que el centrado sea visible.
        self.resize(500, 300)

    def actualizar_tiempo(self, horas, minutos, segundos):
        """Actualiza la etiqueta del contador con el tiempo restante."""
        self.tiempo_label.setText(f"{horas:02}:{minutos:02}:{segundos:02}")

    def mostrar_final(self, mensaje):
        """
        Cambia la ventana al estado de 'descanso':
        - Oculta la etiqueta del contador.
        - Muestra el mensaje (ej. 'Hora de descansar').
        - Muestra el botón 'Continuar'.
        """
        self.tiempo_label.hide()
        self.descripcion.setText(mensaje)
        self.boton.show()

    def ocultar(self):
        """
        Oculta la ventana y emite la señal 'continuar'
        para que main.py reinicie el contador.
        """
        self.hide()
        self.continuar.emit()
