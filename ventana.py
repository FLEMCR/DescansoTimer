# Modulo: ventana.py

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QAction, QColor, QIcon, QPainter, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMenu,
    QPushButton,
    QSystemTrayIcon,
    QVBoxLayout,
    QWidget,
)


class VentanaAlarma(QWidget):
    continuar = Signal()
    descansar = Signal()

    @staticmethod  # Esto es para crear una funcion sin que se requiera una instancia.
    def crear_icono(color=None):
        """Dibuja un círculo del color indicado y devuelve un QIcon.
        Si no se especifica color, usa gris."""
        if color is None:
            color = QColor("gray")

        pixmap = QPixmap(64, 64)
        pixmap.fill(QColor(0, 0, 0, 0))  # Fondo transparente

        painter = QPainter(pixmap)
        painter.setBrush(color)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(4, 4, 56, 56)
        painter.end()

        return QIcon(pixmap)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Alarma de Descanso")

        # --- Etiqueta para mostrar el tiempo restante en la ventana ---
        self.tiempo_label = QLabel("00:00:00", self)
        self.tiempo_label.setStyleSheet("font-size: 48px;")

        # --- Etiqueta de mensaje (cuando toca descansar) ---
        self.descripcion = QLabel("", self)

        # --- Botón "Descansar", oculto al principio ---
        self.boton_descansar = QPushButton("Descansar", self)
        self.boton_descansar.clicked.connect(self.ocultar_descanso)
        self.boton_descansar.hide()

        self.boton_continuar = QPushButton("Continuar", self)
        self.boton_continuar.clicked.connect(self.ocultar)
        self.boton_continuar.hide()

        # --- Layout para centrar los elementos en la ventana ---
        layout = QVBoxLayout()
        layout.addWidget(self.tiempo_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.descripcion, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.boton_descansar, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.boton_continuar, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
        self.resize(400, 200)

        # --- Configuración de la bandeja del sistema ---
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.crear_icono())

        # Menú contextual (clic derecho sobre el icono)
        salir_action = QAction("Salir", self)
        salir_action.triggered.connect(QApplication.quit)

        menu = QMenu()
        menu.addAction(salir_action)
        self.tray_icon.setContextMenu(menu)

        # Mostramos el icono en la bandeja (la ventana sigue oculta)
        self.tray_icon.show()

        self.tray_icon.activated.connect(self.muestra_ventana)

    def muestra_ventana(self, reason):
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            if self.isVisible():
                self.hide()
            else:
                self.show()

    def actualizar_tiempo(self, horas, minutos, segundos):
        """Actualiza la etiqueta del contador en la ventana."""
        self.tiempo_label.setText(f"{horas:02}:{minutos:02}:{segundos:02}")

    def actualizar_tooltip(self, horas, minutos, segundos, tipo):
        """Actualiza el texto emergente del icono de bandeja con el tiempo restante."""

        if tipo == "normal":
            self.tray_icon.setToolTip(
                f"Descanso en - {horas:02}:{minutos:02}:{segundos:02}"
            )
        elif tipo == "descanso":
            self.tray_icon.setToolTip(
                f"El descanso acaba en - {horas:02}:{minutos:02}:{segundos:02}"
            )

    def mostrar_descanso(self, mensaje):
        """
        Cambia la ventana al estado 'descanso' y la hace visible.
        Oculta el contador grande, muestra el mensaje y el botón Continuar.
        """
        self.tiempo_label.hide()
        self.descripcion.setText(mensaje)
        self.descripcion.setStyleSheet("font-size: 24px;")
        self.boton_descansar.show()
        self.boton_continuar.hide()
        self.show()

    def mostrar_continuar(self, mensaje):
        self.tiempo_label.hide()
        self.descripcion.setText(mensaje)
        self.boton_descansar.hide()
        self.boton_continuar.show()
        self.show()

    def ocultar_descanso(self):
        self.hide()
        self.descansar.emit()

    def ocultar(self):
        """
        Oculta la ventana (pero no cierra la app) y emite la señal 'continuar'
        para que main.py reinicie el contador.
        """
        self.hide()
        self.continuar.emit()

    def cambiar_color_icono(self, color):
        self.tray_icon.setIcon(self.crear_icono(QColor(color)))

    def cambiar_color_texto(self, color):
        self.tiempo_label.setStyleSheet(f"color: {color}; font-size: 48px;")
