#include <iostream>
#include <ctime> // Incluir la librería para medir el tiempo

using namespace std;
int main() {
    // Crear un arreglo de números
    int numeros[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int tamano_numeros = sizeof(numeros) / sizeof(numeros[0]); // Tamaño del arreglo

    // Variable para almacenar la suma
    int suma = 0;

    // Iniciar el temporizador
    clock_t tiempo_inicio = clock();

    // Calcula la suma de los elementos del arreglo de forma secuencial
    for (int i = 0; i < tamano_numeros; ++i) {
        suma += numeros[i];
    }

    // Detener el temporizador
    clock_t tiempo_fin = clock();

    // Calcular la duración en segundos
    double duracion = (double)(tiempo_fin - tiempo_inicio) / CLOCKS_PER_SEC;

    // Imprimir la suma de los elementos
    cout << "La suma de los elementos es: " << suma << endl;

    // Imprimir el tiempo de ejecución en segundos
    cout << "Tiempo de ejecucion: " << duracion << " segundos" << endl;

    return 0;
}
