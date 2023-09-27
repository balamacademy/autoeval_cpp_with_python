#include <iostream>

int main(int argc, char **argv){
    char nombre[200];

    std::cout << "Dime tu nombre\n";
    std::cin  >> nombre;
    std::cout << "Tu nombre es: "<<nombre<<"\n";

    return 0;
}