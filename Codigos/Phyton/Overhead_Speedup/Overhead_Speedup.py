import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
file_path = 'import05_2024.csv'
data = pd.read_csv(file_path)

# Suposiciones de tiempos
Tsecuencial = 100  # Tiempo secuencial en segundos

# Generar tiempos paralelos y overheads de manera aleatoria
np.random.seed(42)  # Para reproducibilidad
total_datos = len(data)
Tparalelo = np.random.uniform(30, 60, total_datos)  # Genera tiempos paralelos entre 30 y 60 segundos
Toverhead = np.random.uniform(4, 12, total_datos)  # Genera overheads entre 4 y 12 segundos

# Crear un DataFrame con los tiempos generados
tiempos_df = pd.DataFrame({
    'Tparalelo': Tparalelo,
    'Toverhead': Toverhead
})

# Graficar los tiempos paralelos y los overheads
plt.figure(figsize=(12, 6))
plt.plot(tiempos_df.index, tiempos_df['Tparalelo'], label='Tparalelo', alpha=0.75)
plt.plot(tiempos_df.index, tiempos_df['Toverhead'], label='Toverhead', alpha=0.75)
plt.xlabel('Índice de Datos')
plt.ylabel('Tiempo (s)')
plt.title('Tiempos Paralelos y Overheads para Todos los Datos')
plt.legend()
plt.grid(True)
plt.show()

# Histograma de los tiempos paralelos y overheads
plt.figure(figsize=(12, 6))
plt.hist(tiempos_df['Tparalelo'], bins=30, alpha=0.5, label='Tparalelo')
plt.hist(tiempos_df['Toverhead'], bins=30, alpha=0.5, label='Toverhead')
plt.xlabel('Tiempo (s)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Tiempos Paralelos y Overheads')
plt.legend()
plt.grid(True)
plt.show()

# Gráfica de dispersión (scatter plot)
plt.figure(figsize=(12, 6))
plt.scatter(tiempos_df['Tparalelo'], tiempos_df['Toverhead'], alpha=0.5)
plt.xlabel('Tparalelo (s)')
plt.ylabel('Toverhead (s)')
plt.title('Relación entre Tiempos Paralelos y Overheads')
plt.grid(True)
plt.show()

# Calcular speedup relativo
tiempos_df['Speedup Relativo'] = Tsecuencial / (tiempos_df['Tparalelo'] + tiempos_df['Toverhead'])

# Graficar el speedup relativo
plt.figure(figsize=(12, 6))
plt.plot(tiempos_df.index, tiempos_df['Speedup Relativo'], alpha=0.75)
plt.xlabel('Índice de Datos')
plt.ylabel('Speedup Relativo')
plt.title('Speedup Relativo para Todos los Datos')
plt.grid(True)
plt.show()

# Tabla de comparación de tiempos
tabla_comparacion = tiempos_df.head().copy()
tabla_comparacion.reset_index(drop=True, inplace=True)
tabla_comparacion.index += 1
tabla_comparacion.columns.name = 'Índice'
tabla_comparacion.index.name = 'Datos seleccionados'
print("\nTabla de Comparación de Tiempos Paralelos, Overheads y Speedup Relativo:\n")
print(tabla_comparacion)
