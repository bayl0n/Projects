#include <stdio.h>

int main(int argc, char* argv[]) {

    int digit = 4;
    int *pDigit = &digit;

    printf("%p\n", pDigit);

    return 0;
}
