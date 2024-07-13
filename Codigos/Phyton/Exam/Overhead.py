import multiprocessing
import random

def monte_carlo_pi_part(num_samples):
    count = 0
    for _ in range(num_samples):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            count += 1
    return count

def parallel_monte_carlo_pi(num_samples, num_processes):
    pool = multiprocessing.Pool(processes=num_processes)
    samples_per_process = [num_samples // num_processes] * num_processes
    results = pool.map(monte_carlo_pi_part, samples_per_process)
    total_count = sum(results)
    pi_estimate = (4.0 * total_count) / num_samples
    return pi_estimate

if __name__ == '__main__':
    num_samples = 10**6
    num_processes = 4
    pi_estimate = parallel_monte_carlo_pi(num_samples, num_processes)
    print(f"Estimacion de Pi: {pi_estimate}")

