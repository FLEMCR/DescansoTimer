# Modulo: main.py

import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

import config
import utilidades
from ventana import VentanaAlarma

app = QApplication(sys.argv)
ventana = VentanaAlarma()  # La ventana se crea, pero no se muestra (solo bandeja)

# Timer principal (cuenta regresiva normal)
timer = QTimer()

# Timer para el descanso
timer_descanso = QTimer()

# Timer para el parpadeo del texto en zona roja
timer_parpadeo = QTimer()

# Estado del color en el parpadeo
parpadeo_rojo = True


def alternar_color_parpadeo():
    """Alterna el color del texto entre gris y rojo mientras parpadea."""
    global parpadeo_rojo
    if parpadeo_rojo:
        ventana.cambiar_color_texto("gray")
    else:
        ventana.cambiar_color_texto("red")
    parpadeo_rojo = not parpadeo_rojo


timer_parpadeo.timeout.connect(alternar_color_parpadeo)


def actualizar_contador():
    """Actualiza la cuenta regresiva principal."""
    h, m, s = utilidades.convertir_tiempo(utilidades.restante)
    ventana.actualizar_tiempo(h, m, s)
    ventana.actualizar_tooltip(h, m, s, "normal")

    utilidades.restante -= 1

    if utilidades.restante < 0:
        timer.stop()
        timer_parpadeo.stop()
        ventana.mostrar_descanso("Hora de descansar")
        ventana.tray_icon.setToolTip("¿Descanso?")
        return  # Se coloca este aquí para que si es menor de 0 entonce sno ejecute los siguientes if/else (los de parpadeo en este caso)

    if utilidades.restante <= config.umbral_tiempo_final:
        ventana.cambiar_color_icono("red")
        # Iniciar parpadeo solo si no está activo
        if not timer_parpadeo.isActive():
            timer_parpadeo.start(500)
    else:
        timer_parpadeo.stop()
        ventana.cambiar_color_icono("gray")
        ventana.cambiar_color_texto("white")


def actualizar_contador_descanso():
    """Actualiza la cuenta regresiva del descanso."""
    h, m, s = utilidades.convertir_tiempo(utilidades.restante_descanso)
    ventana.actualizar_tiempo(h, m, s)
    ventana.actualizar_tooltip(h, m, s, "descanso")

    utilidades.restante_descanso -= 1

    if utilidades.restante_descanso < 0:
        timer_descanso.stop()
        ventana.mostrar_continuar("Descanso terminado")

    ventana.cambiar_color_icono("green")
    ventana.cambiar_color_texto("green")


# Conexiones iniciales
timer.timeout.connect(actualizar_contador)
timer.start(1000)

timer_descanso.timeout.connect(actualizar_contador_descanso)


def iniciar_descanso():
    """Inicia la fase de descanso."""
    timer.stop()
    timer_parpadeo.stop()
    utilidades.restante_descanso = config.intervalo_descanso
    timer_descanso.start(1000)
    ventana.tiempo_label.show()
    ventana.boton_descansar.hide()
    ventana.hide()
    ventana.descripcion.setText("")


def reiniciar_contador():
    """Reinicia la cuenta principal."""
    timer_descanso.stop()
    timer_parpadeo.stop()
    utilidades.restante = config.intervalo
    timer.start(1000)
    ventana.tiempo_label.show()
    ventana.boton_continuar.hide()
    ventana.descripcion.setText("")
    ventana.hide()


# Conexión de señales personalizadas
ventana.descansar.connect(iniciar_descanso)
ventana.continuar.connect(reiniciar_contador)

app.exec()
