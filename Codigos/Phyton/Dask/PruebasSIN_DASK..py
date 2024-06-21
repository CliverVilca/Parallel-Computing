import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

# Función para realizar la regresión y medir tiempo y memoria con pandas
def perform_regression(csv_file, target_column, feature_columns=None, test_size=0.2, random_state=42):
    # Listas para almacenar tiempos y consumos de memoria
    tiempos = []
    consumos_memoria = []
    y_reales = []
    y_predichos = []

    # Realizar múltiples ejecuciones para obtener estadísticas
    num_ejecuciones = 5  # Puedes ajustar este número según sea necesario
    for _ in range(num_ejecuciones):
        # Medir el tiempo inicial
        start_time = time.time()

        try:
            # Cargar la data desde el archivo CSV
            data = pd.read_csv(csv_file)

            # Imprimir la cantidad total de datos
            total_data = len(data)
            print(f"Cantidad total de datos: {total_data}")

            # Validar si las columnas numéricas están presentes
            if not all(col in data.columns for col in feature_columns + [target_column]):
                raise ValueError(f"Alguna de las columnas {feature_columns + [target_column]} no está presente en el archivo CSV.")

            # Seleccionar las columnas de características e independientes
            X = data[feature_columns]
            y = data[target_column]

            # Dividir los datos en conjuntos de entrenamiento y prueba
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # Crear el modelo de regresión lineal
            model = LinearRegression()

            # Medir el uso de memoria antes de entrenar el modelo
            mem_before = memory_usage()[0]

            # Entrenar el modelo
            model.fit(X_train, y_train)

            # Medir el uso de memoria después de entrenar el modelo
            mem_after = memory_usage()[0]

            # Predecir los valores
            y_pred = model.predict(X_test)

            # Almacenar valores reales y predichos para scatter plot
            y_reales.append(y_test.values)
            y_predichos.append(y_pred)

            # Medir el tiempo final
            end_time = time.time()

            # Calcular métricas
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            # Almacenar tiempo y consumo de memoria
            tiempo_ejecucion = end_time - start_time
            tiempos.append(tiempo_ejecucion)
            consumos_memoria.append(mem_after - mem_before)

            # Imprimir los resultados de la ejecución actual
            print(f"\nEjecución {_+1}:")
            print("Mean Squared Error: ", mse)
            print("R2 Score: ", r2)
            print("Tiempo de ejecucion: {:.2f} segundos".format(tiempo_ejecucion))
            print("Consumo de memoria: {:.2f} MiB".format(mem_after - mem_before))

        except Exception as e:
            print(f"Error en la ejecución {_+1}: {e}")

    # Graficar histograma de tiempos de ejecución
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.hist(tiempos, bins=5, alpha=0.7, color='blue', edgecolor='black')
    plt.xlabel('Tiempo de Ejecución (segundos)')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Tiempos de Ejecución')

    # Graficar histograma de consumos de memoria
    plt.subplot(1, 3, 2)
    plt.hist(consumos_memoria, bins=5, alpha=0.7, color='green', edgecolor='black')
    plt.xlabel('Consumo de Memoria (MiB)')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Consumos de Memoria')

    # Graficar scatter plot de valores reales vs. predichos
    plt.subplot(1, 3, 3)
    for i in range(min(num_ejecuciones, len(y_reales))):  # Asegurar que no se exceda el número de ejecuciones válidas
        plt.scatter(y_reales[i], y_predichos[i], alpha=0.5, label=f'Ejecución {i+1}')
    plt.xlabel('Valores Reales')
    plt.ylabel('Valores Predichos')
    plt.title('Dispersión de valores reales vs. predichos')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Ejemplo de uso con el dataset proporcionado
csv_file = 'Transactions Data.csv'
target_column = 'amount'  # Variable numérica a predecir
feature_columns = ['oldbalanceOrg', 'newbalanceOrig']  # Variables numéricas como características
perform_regression(csv_file, target_column, feature_columns)
