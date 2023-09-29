#include <stdio.h>

int main(){

    int a , b;

    printf("Jumlah pasukan yang di bawa yu zhong:");
    scanf("%d",&a);

    printf("jumlah pahlawan:");
    scanf("%d",&b);

    int hasil = a/b;

    printf("Jumlah pasukan yang harus dikalahkan setiap pahlawan adalah %d\n",hasil);

    return 0;
}