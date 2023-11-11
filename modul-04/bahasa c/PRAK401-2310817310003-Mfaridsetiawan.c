#include <stdio.h>

int main()
{
    int a, b;
    char simbol;

    scanf("%d %c", &a, &simbol);

    for (b = 1; b <= 50; b++)
    {
        if (b % a == 0)

        {
            printf("%c ", simbol);
        }
        else
        {
            printf("%d ", b);
        }
    }
    return 0;
}