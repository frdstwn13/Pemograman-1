#include <stdio.h>

int main()
{
    int a, b;

    printf("input\n");
    printf("");
    scanf("%d %d", &a, &b);

    if (a > b)
    {
        printf("\nOutput \n%d %d", b, a);
    }
    else
    {
        printf("\nOutput \n%d %d", a, b);
    }

    return 0;
}