#include <stdio.h>

int main()
{
    int Min = 1;
    int Max;
    scanf("%d", &Max);

    for (int a = Min; a <= Max; a++)
    {
        if (a % 2 != 0)
        {
            printf("%d ", a);
        }
    }

    printf("\n");

    for (int a = Max; a >= Min; a--)
    {
        if (a % 2 == 0)
        {
            printf("%d ", a);
        }
    }

    printf("\n");
    return 0;
}