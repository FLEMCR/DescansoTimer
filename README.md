# DescansoTimer

Es un cronómetro de descanso que cada cierto intervalo (por defecto: 1 hora) muestra una ventana con un botón que al presionar inicia un segundo cronómetro (por defecto: 5 minutos) para poder descansar, estirarse, etc. (AFK). Después de ese tiempo aparece otra ventana para continuar con otro cronómetro (por defecto: 1 hora), repitiéndose en bucle.

El objetivo es evitar estar mucho tiempo seguido usando la computadora y tener un momento para romper la rutina.

## Origen del proyecto

Este mini proyecto fue elaborado con ayuda de la IA a modo de instructor, con el fin de aprender cómo desarrollar un proyecto de este estilo. No soy experto en el tema, así que este repositorio también sirve como registro de aprendizaje.

## Características

- Contador regresivo principal configurable.
- Icono en la bandeja del sistema con tooltip dinámico (muestra el tiempo).
- Cambio de color del icono según el estado:
  - Gris: tiempo normal.
  - Rojo: quedan menos de 5 minutos.
  - Verde: tiempo de descanso.
- Parpadeo del texto (entre blanco y rojo) de la ventana cuando queda poco tiempo (por defecto: 5 min).
- Fase de descanso con contador propio.
- Ventana de aviso con botón "Descansar" y botón "Continuar" respectivamente.
- Menú contextual en el icono de bandeja con opción "Salir".
- Clic en el icono para mostrar/ocultar la ventana.
- Configuración externa mediante archivo JSON.


## Requisitos

- Python 3.10 o superior
- PySide6

## Estructura del proyecto

```
DescansoTimer/
├── main.py
├── ventana.py
├── utilidades.py
├── config.py
├── configuration.json
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalación

### Linux (probado en Kubuntu)

```bash
# 1. Clonar el repositorio
git clone https://github.com/FLEMCR/DescansoTimer.git
cd DescansoTimer

# 2. Crear un entorno virtual
python3 -m venv .venv

# 3. Activar el entorno virtual
source .venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar
python main.py
```

### Windows

```cmd
:: 1. Clonar el repositorio
git clone https://github.com/FLEMCR/DescansoTimer.git
cd DescansoTimer

:: 2. Crear un entorno virtual
python -m venv .venv

:: 3. Activar el entorno virtual
.venv\Scripts\activate

:: 4. Instalar dependencias
pip install -r requirements.txt

:: 5. Ejecutar
python main.py
```

Si no quieres que se abra la consola en Windows, ejecuta:

```cmd
.venv\Scripts\pythonw.exe main.py
```

### macOS

```bash
# 1. Clonar el repositorio
git clone https://github.com/FLEMCR/DescansoTimer.git
cd DescansoTimer

# 2. Crear un entorno virtual
python3 -m venv .venv

# 3. Activar el entorno virtual
source .venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar
python main.py
```

## Configuración

Los tiempos se configuran en el archivo `configuration.json`:

```json
{
  "intervalo": 3600,
  "intervalo_descanso": 300,
  "umbral_tiempo_final": 300
}
```

- `intervalo`: segundos antes de que suene la alarma (por defecto 1 hora = 3600 s).
- `intervalo_descanso`: segundos que dura el descanso (por defecto 5 minutos = 300 s).
- `umbral_tiempo_final`: segundos antes del final en los que el icono se vuelve rojo (por defecto 5 minutos = 300 s).

Puedes editar este archivo con cualquier editor de texto antes de iniciar la aplicación.

## Uso

1. Ejecuta el `main.py`.
2. El programa se queda en segundo plano con un icono en la bandeja del sistema.
3. Cada segundo actualiza el tooltip con el tiempo restante.
4. Cuando falten menos de 5 minutos, el icono se pone rojo y el texto de la ventana parpadea.
5. Al llegar a 0, aparece la ventana con el botón "Descansar".
6. Al pulsar "Descansar", se inicia el descanso de 5 minutos en verde.
7. Al terminar el descanso, aparece la ventana con el botón "Continuar".
8. Al pulsar "Continuar", el ciclo vuelve a empezar.

Puedes abrir la ventana con el tiempo restante en cualquier momento haciendo doble-click en el icono de la bandeja del sistema.

## Autostart

### Kubuntu (KDE Plasma)

Crea el archivo `~/.config/autostart/descansotimer.desktop` con el siguiente contenido:

```ini
[Desktop Entry]
Type=Application
Name=DescansoTimer
Exec=/ruta/completa/al/proyecto/.venv/bin/python /ruta/completa/al/proyecto/main.py
Path=/ruta/completa/al/proyecto/
Icon=utilities-system-monitor
Terminal=false
X-GNOME-Autostart-enabled=true
```

Dale permisos de ejecución:

```bash
chmod +x ~/.config/autostart/descansotimer.desktop
```

### Windows

1. Pulsa `Win + R`, escribe `shell:startup` y pulsa Enter.
2. Crea un archivo `iniciar_descansotimer.bat`:

```bat
@echo off
cd /d "C:\ruta\a\DescansoTimer"
.venv\Scripts\pythonw.exe main.py
```

3. Crea un acceso directo a ese `.bat` y colócalo en la carpeta que se abrió.

### macOS

Añade un elemento de inicio desde **Preferencias del Sistema → Usuarios y grupos → Iniciar sesión** apuntando a un script que ejecute `python main.py`.

## Solución de problemas

### "No module named PySide6"

Asegúrate de haber activado el entorno virtual antes de instalar y ejecutar.

### La aplicación no arranca al iniciar el sistema

- En Linux: revisa que el `.desktop` tenga las rutas absolutas correctas y el nombre exacto de la carpeta del proyecto.
- En Windows: verifica que el `.bat` tenga la ruta correcta al proyecto.
