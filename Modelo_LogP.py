import math

def logp_model(L, o, g, N, P):
    """
    Calcula el tiempo total de comunicación T según el modelo LogP.
    
    Parámetros:
    L (int): Latencia
    o (int): Overhead
    g (int): Gap
    N (int): Número de mensajes
    P (int): Número de procesadores
    
    Retorna:
    T (int): Tiempo total de comunicación en microsegundos
    """
    T = L + 2 * o + (math.ceil(N / P) - 1) * g
    return T

def main():
    print("Ingrese los parámetros del modelo LogP:")
    
    try:
        L = int(input("Latencia (L) en microsegundos: "))
        o = int(input("Overhead (o) en microsegundos: "))
        g = int(input("Gap (g) en microsegundos: "))
        N = int(input("Número de mensajes (N): "))
        P = int(input("Número de procesadores (P): "))
        
        T = logp_model(L, o, g, N, P)
        print(f"\nTiempo total de comunicación T: {T} microsegundos")
        
    except ValueError:
        print("Por favor, ingrese valores enteros válidos.")

if __name__ == "__main__":
    main()
