import concurrent.futures
import os

def hello_world(thread_id, num_threads):
    print(f"\n Hola mundo de un número de hilos {thread_id} de un total {num_threads} \n")

def main():
    print("\n 01 Fuera de la region Paralela ...")

    # Determinar el número de hilos a usar
    num_threads = os.cpu_count()  # Usa el número de núcleos de CPU disponibles

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(hello_world, i, num_threads) for i in range(num_threads)]
        # Asegurarse de que todos los hilos hayan completado
        concurrent.futures.wait(futures)

    print("\n 02 Fuera de la region Paralela ...")

if __name__ == "__main__":
    main()
