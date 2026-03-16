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
# - Recorre resultados y extrae los objetos detectados
# - Elimina duplicados
# - Construye la variable linea con el formato indicado
# ─────────────────────────────────────────




# Guardar — no modificar
with open("resultados.txt", "w", encoding="utf-8") as f:
    f.writelines(lineas)

print("✅ Resultados guardados en resultados.txt")