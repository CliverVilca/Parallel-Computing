#include <iostream>
#include <omp.h>
using namespace std;
int main() {
    int nums[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int nums_size = sizeof(nums) / sizeof(nums[0]);
    int sum = 0;

    // Obtener el tiempo de inicio
    double start_time = omp_get_wtime();
    
    // Iniciar la región paralela y reducir la variable sum
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < nums_size; ++i) {
        sum += nums[i];
    }
    // Obtener el tiempo de finalización
    double end_time = omp_get_wtime();
    
    cout << "La suma de los elementos es: " << sum << endl;
    // Imprimir el tiempo de ejecución
    cout << "Tiempo de ejecución: " << end_time - start_time << " segundos" << endl;

    // Obtener el número de hilos utilizados
    int num_threads = omp_get_max_threads();
    
    // Imprimir el número de hilos utilizados
    cout << "Número de hilos utilizados: " << num_threads << endl;

    return 0;
}
