#include <stdio.h>

    int main(){

    int hrg_a;
    printf("harga sepatu a adalah:");
    scanf("%d", &hrg_a);
    int hrg_b;
    printf("harga sepatu b adalah:");
    scanf("%d", &hrg_b);

    float hrg_adiskon= 0.13;
    float hrg_bdiskon= 0.21;
    printf("Sepatu A mendapat diskon 13%% sehingga harganya menjadi: %.0f\n", hrg_a - (hrg_a * hrg_adiskon));
    printf("Sepatu B mendapat diskon 21%% sehingga harganya menjadi: %.0f\n", hrg_b - (hrg_b * hrg_bdiskon));
    return 0; 
    }