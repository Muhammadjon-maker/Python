#include <stdio.h>
#include <stdlib.h>

int main()
{
    system("cls");
    int arr[5][5];
    int len = sizeof arr[10];
    printf("Songa qiymat bering!\n");
    scanf("%d %d", &arr);
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < len; j++)
        {
            if (j > i)
            {
                printf(j);
            }
            else if (i < j)
            {
                printf(i);
            }
        }
    }
    return 0;
}