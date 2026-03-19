from ultralytics import YOLO
import sys

# Cargar modelo — no modificar
modelo = YOLO("yolov8n.pt")

# Analizar imagen — no modificar
imagen = sys.argv[1]
resultados = modelo(imagen)

lineas = []

etiquetas = []
for r in resultados:
    for clase_id in r.boxes.cls: 
        nombre_clase = r.names[int(clase_id)] 
        etiquetas.append(nombre_clase)

lineas.append(f"Imagen elegida: {imagen}\n")
lineas.append(f"Etiquetas detectadas: {etiquetas}\n")

# Guardar — no modificar
with open("resultados.txt", "w", encoding="utf-8") as f:
    f.writelines(lineas)

print("✅ Resultados guardados en resultados.txt")