#include <stdio.h>
#include <stdlib.h>

int main()
{
    system("cls");
    int son;
    int sum = 0;
    int a;
    int b;
    printf("Songa qiymat bering!\n");
    scanf("%d", &son);
    if (son > 10)
    {
        a = son % 10;
        b = a * a;
        sum += b;
    }
    printf("%d", sum);
    return 0;
}