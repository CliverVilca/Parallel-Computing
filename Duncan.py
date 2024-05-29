from concurrent.futures import ThreadPoolExecutor

# Funciones que representan operaciones independientes
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# Datos
values = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

# Ejecutar operaciones en paralelo
with ThreadPoolExecutor() as executor:
    add_results = list(executor.map(lambda p: add(*p), values))
    multiply_results = list(executor.map(lambda p: multiply(*p), values))

print("Resultado MIMD (Suma):", add_results)
print("Resultado MIMD (Multiplicación):", multiply_results)
