##Ejercicio 2:

import multiprocessing

def worker(tid, a, b, c):
    c[tid] = a[tid] + b[tid]
    print(f"c[{tid}]={c[tid]}")

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    c = multiprocessing.Array('i', 5)  # Shared array
    
    processes = []
    for tid in range(5):
        process = multiprocessing.Process(target=worker, args=(tid, a, b, c))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()