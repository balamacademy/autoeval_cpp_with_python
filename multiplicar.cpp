#include <iostream>

int multi(int *arr, int tamano){
    int acumulador = 1;
    for(int i = 0; i < tamano; i++){
        acumulador *= arr[i];
    }
    return acumulador;
}

int main(int argc, char **argv){
    int arr[5];

    for(int i = 0; i < 5; i++){
        std::cin >> arr[i];
    }

    std::cout<<multi(arr, 5);
    return 0;
}