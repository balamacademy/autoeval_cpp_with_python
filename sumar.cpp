#include <iostream>

int sumar(int *arr, int tamano){
    int acumulador = 0;
    for(int i = 0; i < tamano; i++){
        acumulador += arr[i];
    }
    return acumulador;
}

int main(int argc, char **argv){
    int arr[4] = {1, 2, 3, 4};

    std::cout<<sumar(arr, 4);
    return 0;
}