#include <stdio.h>

int main()
{
    int nilai1, nilai2;
    int nilai_batas;

    scanf("%d %d", &nilai1, &nilai2);
    nilai_batas = (nilai1 - nilai2);
    if (nilai_batas < 0)
    {
        nilai_batas = nilai_batas * -1;
        for (int b = 0; b <= nilai_batas; b++)
        {
            int a = 1;

            printf("%d-%d ", nilai1, nilai2);

            nilai1 = nilai1 + a;
            nilai2 = nilai2 - a;
        }
    }
    else
    {
        for (int b = 0; b <= nilai_batas; b++)
        {
            int a = 1;

            printf("%d %d  ", nilai1, nilai2);

            nilai1 = nilai1 - a;
            nilai2 = nilai2 + a;
        }
    }

    return 0;
}