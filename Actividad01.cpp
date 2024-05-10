#include <iostream>
#include <omp.h>
using namespace std;
int main() {
    int nums[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int nums_size = sizeof(nums) / sizeof(nums[0]);
    int sum = 0;
    double start_time = omp_get_wtime();
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < nums_size; ++i) {
        sum += nums[i];
    }
    double end_time = omp_get_wtime();
    cout << "La suma de los elementos es: " << sum << endl;
    cout << "Tiempo de ejecucion: " << end_time - start_time << " segundos" << endl;
    int num_threads = omp_get_max_threads();
    cout << "Numero de hilos utilizados: " << num_threads << endl;
    return 0;
}