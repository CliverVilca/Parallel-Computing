import concurrent.futures
import os

def print_thread_info():
    print("\n Numero de hilos sin control y segun dispositivo")

def main():
    print("\n 01 Fuera de la region Paralela ... \n\n")

    # Determine the number of threads to use
    num_threads = os.cpu_count()  # Use the number of CPU cores available

    # Creating threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(print_thread_info) for _ in range(num_threads)]
        # Ensure all threads have completed
        concurrent.futures.wait(futures)

    print("\n\n 02 Fuera de la region Paralela ...\n\n")

if __name__ == "__main__":
    main()
