import matplotlib.pyplot as plt

# Datos de los tiempos de ejecución para diferentes tamaños de listas
tamanios = [5, 10, 100, 1000, 10000]
tiempo_paralelo = [0.1386, 0.2590, 0.3818, 1.1569, 1.2229]
tiempo_concurrente = [0.0000, 0.0000, 0.0000, 0.0000, 0.0000]

# Calcular la diferencia en los tiempos de ejecución
diferencia_tiempo = [tiempo_paralelo[i] - tiempo_concurrente[i] for i in range(len(tamanios))]

# Crear la gráfica de barras de la diferencia de tiempos
plt.figure(figsize=(10, 6))
plt.bar(tamanios, diferencia_tiempo, color='r', width=2, label='Diferencia de tiempos (Paralelo - Concurrente)')
plt.xlabel('Tamaño de las listas')
plt.ylabel('Diferencia en tiempos de ejecución (s)')
plt.title('Diferencia en tiempos de ejecución entre enfoques Paralelo y Concurrente')
plt.xticks(tamanios)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()