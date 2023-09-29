#include <stdio.h>

    int main(){
    
    int a , b , x , y;

    printf("Variabel a bernilai:");
    scanf("%d", &a);

    printf("Variabel b bernilai:");
    scanf("%d", &b);

    printf("Variabel x bernilai:");
    scanf("%d", &x);

    printf("Variabel y bernilai:");
    scanf("%d", &y);

    int sisabagi_ab= a % b;
    int sisabagi_xy= x % y;
    int hasil= sisabagi_ab + sisabagi_xy;

    printf("Total sisa bagi dari a dibagi b dan x dibagi y adalah %d,\n",hasil);
    return 0;

    }

