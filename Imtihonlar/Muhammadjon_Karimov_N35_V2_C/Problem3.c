#include <stdio.h>
#include <stdlib.h>

void shiftRight(int *a, int *b, int *c)
{
    printf("%d %d %d", c, b, a);
}
int main()
{
    int a, b, c;
    printf("Songa qiymat bering!\n");
    scanf("%d %d %d", &a, &b, &c);
    shiftRight(a, b, c);
    printf("%d %d %d", c, b, a);
    return 0;
}