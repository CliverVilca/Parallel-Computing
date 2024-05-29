##Ejercicio 1: 

import multiprocessing

def worker(num, num_threads):
    print(f"HW del número de hilo {num} de un total {num_threads}")

def parallel_region(num_threads):
    threads = []
    for i in range(num_threads):
        thread = multiprocessing.Process(target=worker, args=(i, num_threads))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":

    num_threads = 4
    parallel_region(num_threads)

    num_threads = multiprocessing.cpu_count()
    parallel_region(num_threads)