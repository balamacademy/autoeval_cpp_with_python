#include <iostream>

int sumar(int *arr, int tamano){
    int acumulador = 0;
    for(int i = 0; i < tamano; i++){
        acumulador += arr[i];
    }
    return acumulador;
}

void imprimir(int *arr, int tamano){
    for(int i = 0; i < tamano; i++){
        std::cout << arr[i] << " ";
    }
}

void llenar_arreglo(int a[], int l){
    for(int i = 0; i < l; i++){
        a[i] = i;
    }
}

int main(int argc, char **argv){

    for (int i = 0; i < argc; ++i) {
        std::cout << argv[i] << '\n';
    }

    int arr[4] = {1, 2, 3, 4};

    std::cout<<sumar(arr, 4)<<"\n";


    int arreglo[4];
    llenar_arreglo(arreglo, 4);
    imprimir(arreglo, 4);


    return 0;
}
