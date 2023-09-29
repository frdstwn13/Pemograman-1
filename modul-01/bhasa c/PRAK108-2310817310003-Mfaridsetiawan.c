#include <stdio.h>

    int main(){
    
    float a , b;

    printf("Diketahui: \n");
    printf("Pak Dengklak mengelilingi taman:");
    scanf("%f", &a);

    printf("Jarak Tempuh Pak Dengklak:");
    scanf("%f", &b);

    float jari_jari= b/a;
    float hasil=jari_jari / (2 * 3.14);

    printf("Jawaban : \n");
    printf("Jari jari taman yang dikelilingi Pak Dengklak adalah %.2f\n",hasil);

    return 0;
    }