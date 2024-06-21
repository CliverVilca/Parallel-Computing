from dask.distributed import Client
import dask.dataframe as dd
from dask_ml.model_selection import train_test_split
from dask_ml.linear_model import LinearRegression
from dask_ml.metrics import mean_squared_error, r2_score
import time
import matplotlib.pyplot as plt

def perform_regression_dask(csv_file, target_column, feature_columns=None, test_size=0.2, random_state=42):
    # Iniciar el cliente Dask
    client = Client()
    print(client)  # Esto imprimirá la URL del dashboard

    # Medir el tiempo inicial
    start_time = time.time()

    # Cargar la data desde el archivo CSV usando Dask
    data = dd.read_csv(csv_file)

    # Seleccionar las columnas de características e independientes
    if feature_columns is None:
        # Si no se especifican las columnas de características, se usan todas excepto la de target
        X = data.drop(columns=[target_column])
    else:
        X = data[feature_columns]
    y = data[target_column]

    # Dividir los datos en conjuntos de entrenamiento y prueba usando Dask
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, shuffle=True)

    # Convertir dask.dataframe a dask.array
    X_train_array = X_train.to_dask_array(lengths=True)
    X_test_array = X_test.to_dask_array(lengths=True)
    y_train_array = y_train.to_dask_array(lengths=True)
    y_test_array = y_test.to_dask_array(lengths=True)

    # Crear el modelo de regresión lineal usando Dask
    model = LinearRegression()

    # Entrenar el modelo
    model.fit(X_train_array, y_train_array)

    # Predecir los valores
    y_pred = model.predict(X_test_array)

    # Calcular métricas usando Dask
    mse = mean_squared_error(y_test_array, y_pred)
    r2 = r2_score(y_test_array, y_pred)

    # Medir el tiempo final
    end_time = time.time()

    # Imprimir los resultados
    print("Valores de predicción: ", y_pred.compute())
    print("Mean Squared Error: ", mse)  # No necesitamos .compute() aquí
    print("R2 Score: ", r2)              # No necesitamos .compute() aquí
    print("Tiempo de ejecución: {:.2f} segundos".format(end_time - start_time))

    # Visualización de los resultados
    plt.figure(figsize=(12, 5))

    # Histograma de los valores predichos y reales
    plt.subplot(1, 2, 1)
    plt.hist(y_pred.compute(), bins=20, alpha=0.7, color='blue', label='Predicciones')
    plt.hist(y_test_array.compute(), bins=20, alpha=0.7, color='green', label='Reales')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de valores predichos y reales')
    plt.legend()

    # Gráfico de dispersión de las predicciones vs valores reales
    plt.subplot(1, 2, 2)
    plt.scatter(y_test_array.compute(), y_pred.compute(), alpha=0.5)
    plt.xlabel('Valores Reales')
    plt.ylabel('Valores Predichos')
    plt.title('Dispersión de valores reales vs predichos')

    plt.tight_layout()
    plt.show()

    # Cerrar el cliente Dask
    client.close()

if __name__ == '__main__':
    # Ejemplo de uso con el dataset proporcionado
    csv_file = 'Transactions Data.csv'
    target_column = 'amount'  # Variable numérica a predecir
    feature_columns = ['oldbalanceOrg', 'newbalanceOrig']  # Variables numéricas como características
    perform_regression_dask(csv_file, target_column, feature_columns)
