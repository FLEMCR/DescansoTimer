import sys
import config
import utilidades

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


def mensaje():
  h_palabra = "horas"
  if utilidades.horas == 1:
    h_palabra = "hora"
  m_palabra = "minutos"
  if utilidades.minutos == 1:
    m_palabra = "minuto"
  s_palabra = "segundos"
  if utilidades.segundos == 1:
    s_palabra = "segundo"

  mensaje = f'Ya ha pasado {utilidades.horas:02} {h_palabra}, {utilidades.minutos:02} {m_palabra} y {utilidades.segundos:02} {s_palabra}. Ahora descansa'
  if utilidades.horas == 0 and utilidades.minutos > 0:
    mensaje = f'Ya ha pasado {utilidades.minutos:02} {m_palabra} y {utilidades.segundos:02} {s_palabra}. Ahora descansa'
  elif utilidades.horas == 0 and utilidades.minutos == 0 :
    mensaje = f'Ya ha pasado {utilidades.segundos:02} {s_palabra}. Ahora descansa'
  return mensaje

def cerrar():
  ventana.close()

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Alarma de Descanso")

descripcion = QLabel(mensaje(), ventana)
descripcion.move(90, 80)


boton = QPushButton('Continuar', ventana)
boton.move(200, 200)
boton.clicked.connect(cerrar)

ventana.resize(500, 300)
ventana.show()

app.exec()
