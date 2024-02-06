import pickle

def guardar_estado(archivo, datos):
    with open(archivo, 'wb') as f:
        pickle.dump(datos, f)

def cargar_estado(archivo):
    with open(archivo, 'rb') as f:
        return pickle.load(f)

# Ejemplo de uso
datos = {'variable_1': 42, 'lista': [1, 2, 3], 'texto': 'Hola, mundo!'}

# Guardar el estado
guardar_estado('estado.pkl', datos)

# Modificar los datos
datos['variable_1'] = 99
datos['lista'].append(4)

# Cargar el estado guardado previamente
datos_cargados = cargar_estado('estado.pkl')

print("Datos originales:", datos)
print("Datos cargados:", datos_cargados)
