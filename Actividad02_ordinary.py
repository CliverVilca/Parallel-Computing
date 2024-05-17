import random
import time

def worker(a, b):
    c = [a[i] + b[i] for i in range(len(a))]
    return c

if __name__ == "__main__":
    ##random.seed(42)  # Establecer una semilla para la generación de números aleatorios
    n = int(input("Ingrese la cantidad de números que desea sumar: "))
    a = [random.randint(1, 10) for _ in range(n)]  # Generar una lista aleatoria de 'n' elementos entre 1 y 10
    b = [random.randint(1, 10) for _ in range(n)]  # Generar otra lista aleatoria de 'n' elementos entre 1 y 10

    print("Lista a:\n", a)
    print("Lista b:\n", b)
    
    start_time = time.time()  # Registrar el tiempo de inicio de la ejecución

    c = worker(a, b)

    end_time = time.time()  # Registrar el tiempo de finalización de la ejecución
    execution_time = end_time - start_time
    print(f"Resultado de la suma en forma secuencial: {c}\n")
    print(f"Tiempo de ejecución en forma secuencial: {execution_time} segundos")
