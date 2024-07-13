import threading
import time

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            print(f"{self.name} está pensando.")
            time.sleep(1)
            print(f"{self.name} está hambriento.")
            self.dine()

    def dine(self):
        left_fork, right_fork = self.left_fork, self.right_fork

        while True:
            left_fork.acquire(True)
            acquired = right_fork.acquire(False)
            if acquired:
                break
            left_fork.release()
            print(f"{self.name} no pudo conseguir ambos tenedores y suelta el tenedor izquierdo.")
            time.sleep(1)

        print(f"{self.name} tiene ambos tenedores y está comiendo.")
        time.sleep(1)
        left_fork.release()
        right_fork.release()
        print(f"{self.name} ha soltado ambos tenedores y ha terminado de comer.")

def dining_philosophers():
    forks = [threading.Lock() for _ in range(5)]
    philosopher_names = ["Filósofo 1", "Filósofo 2", "Filósofo 3", "Filósofo 4", "Filósofo 5"]

    philosophers = [
        Philosopher(philosopher_names[i], forks[i], forks[(i + 1) % 5])
        for i in range(5)
    ]

    for philosopher in philosophers:
        philosopher.start()

if __name__ == "__main__":
    dining_philosophers()

