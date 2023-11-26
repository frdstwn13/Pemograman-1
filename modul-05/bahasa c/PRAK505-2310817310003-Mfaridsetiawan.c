#include <stdio.h>

void Biodata(int tahunlahir, char *Namaku, char *Asal)
{
    int tahun_sekarang = 2023;
    int umur = tahun_sekarang - tahunlahir;

    printf("Perkenalkan Nama Saya: %s\n", Namaku);
    printf("Umur Saya            : %d\n", umur);
    printf("Saya Adalah Angkatan : %d\n", tahun_sekarang);
    printf("Asal Saya dari       : %s\n", Asal);
}

int main()
{
    int tahunlahir;
    char Namaku[30], Asal[20];

    scanf(" %d", &tahunlahir);
    scanf(" %[^\n]", &Namaku);
    scanf(" %[^\n]", &Asal);

    Biodata(tahunlahir, Namaku, Asal);
    return 0;
}