import os

num_threads = os.cpu_count()
for i in range(num_threads):
    print(f"{i+1}.- El numero de hilos (nucleos de CPU) disponibles es: {num_threads}")


import multiprocessing

num_threads = multiprocessing.cpu_count()
print(f"El numero de hilos (nucleos de CPU) disponibles es: {num_threads}")