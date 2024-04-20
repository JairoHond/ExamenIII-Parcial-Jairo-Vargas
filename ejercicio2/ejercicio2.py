import json
import os

# Obtener la ruta completa al archivo JSON
ruta_archivo = os.path.join("C:\\Users\\jairo\\Desktop\\ExamenIII-Parcial\\ejercicio2", 'archivo.json')

# Cargar el archivo JSON
with open(ruta_archivo, 'r') as f:
    data = json.load(f)

# Modificar los valores según sea necesario
data['name'] = 'Andres Iniesta Perez'
# Si es un nuevo club, agregarlo a la lista de clubs
data['clubs'].append({
    "name": "Motagua FC",
    "period": "2024-present"
})

# Guardar el archivo JSON modificado
with open(ruta_archivo, 'w') as f:
    json.dump(data, f, indent=4)

print("Archivo modificado y guardado exitosamente.")
