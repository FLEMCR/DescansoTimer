# Modulo: config.py

import json
import os

ruta_configuracion = os.path.join(os.path.dirname(__file__), "configuration.json")

with open(ruta_configuracion, "r", encoding="utf-8") as f:
    datos = json.load(f)

intervalo = datos["tiempo_uso"]
intervalo_descanso = datos["tiempo_descanso"]
umbral_tiempo_final = datos["umbral_tiempo_final_previo_descanso"]
