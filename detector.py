from ultralytics import YOLO
import sys

# Cargar modelo — no modificar
modelo = YOLO("yolov8n.pt")

# Analizar imagen — no modificar
imagen = sys.argv[1]
resultados = modelo(imagen)

lineas = []

# ─────────────────────────────────────────
# TU CÓDIGO VA AQUÍ
# El archivo resultados.txt debe quedar así:
#
# Imagen elegida: image1.jpeg
# Etiquetas detectadas: ['car', 'person', 'bus']
# ─────────────────────────────────────────

# Guardar — no modificar
with open("resultados.txt", "w", encoding="utf-8") as f:
    f.writelines(lineas)

print("✅ Resultados guardados en resultados.txt")