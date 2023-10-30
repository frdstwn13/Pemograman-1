#include <stdio.h>

int main()
{
    int detik, hari, jam, menit, detik2;

    printf("input\n");
    scanf("%d", &detik);

    hari = detik / (24 * 3600);
    jam = (detik % (24 * 3600)) / 3600;
    menit = (detik % 3600) / 60;
    detik2 = detik % 60;

    if (hari > 0)
    {
        printf("\nOutput \n%d hari %02d:%02d:%02d", hari, jam, menit, detik2);
    }
    else
    {
        printf("\nOutput \n%02d:%02d:%02d", jam, menit, detik2);
    }

    return 0;
}
