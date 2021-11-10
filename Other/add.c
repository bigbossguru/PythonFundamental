#include <stdlib.h>
#include <stdio.h>

int add_int(int, int);
float add_float(float, float);

int add_int(int a, int b)
{
    return a+b;
}

float add_float(float a, float b)
{
    return a+b;
}

int * range_(int length)
{
    int* arr = (int*)malloc(length * sizeof(int));
    for(int i=0; i<length; i++)
    {
        arr[i] = i;
    }
    return arr;
}

int main()
{
    int *p;
    p = range_(10);
    for(int i=0; i<10; i++)
    {
        printf("%d ", p[i]);
    }
    return 0;
}