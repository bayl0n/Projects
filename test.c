#include <stdio.h>

int main(int argc, char* argv[]) {

    // Creating an int and a pointer for it
    int digit = 4;
    int *pDigit = &digit;

    // Printing the memory address of the int to the screen using the pointer
    printf("%p\n", pDigit);

    return 0;
}
