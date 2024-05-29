import concurrent.futures
import os

def print_thread_info(thread_id, num_threads):
    print(f"HW del numero de hilo {thread_id} de un total {num_threads}")

def main():
    print("\n 01 Fuera de la region Paralela ...\n")

    num_threads = 16  # Setting the number of threads to 8

    # First parallel region
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(print_thread_info, i, num_threads) for i in range(num_threads)]
        concurrent.futures.wait(futures)

    print("\n 02 Fuera de la region Paralela ...\n")

    # Second parallel region
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(print_thread_info, i, num_threads) for i in range(num_threads)]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()
