import multiprocessing
import random
import time

def worker(tid, a, b, c):
    c[tid] = a[tid] + b[tid]
    print(f"c[{tid}]={c[tid]}")

if __name__ == "__main__":
    ##random.seed(42)  # Establecer una semilla para la generación de números aleatorios
    n = int(input("Ingrese la cantidad de números que desea sumar: "))
    a = [random.randint(1, 10) for _ in range(n)]  # Generar una lista aleatoria de 'n' elementos entre 1 y 10
    b = [random.randint(1, 10) for _ in range(n)]  # Generar otra lista aleatoria de 'n' elementos entre 1 y 10
    c = multiprocessing.Array('i', n)  # Array compartido
    num_cores = multiprocessing.cpu_count()  # Obtener el número de núcleos disponibles

    print(f"Número de núcleos de tu computadora: {num_cores}")
    print(f"Número de hilos de tu computadora: {num_cores * 2}")  # Se asume 2 hilos por núcleo
    print("")

    processes = []
    
    print("Lista a:", a)
    print("Lista b:", b)

    start_time = time.time()  # Registrar el tiempo de inicio de la ejecución

    for tid in range(min(n, num_cores)):  # Crear un proceso por cada núcleo o por cada número, lo que sea menor
        process = multiprocessing.Process(target=worker, args=(tid, a, b, c))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()

    end_time = time.time()  # Registrar el tiempo de finalización de la ejecución
    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")
