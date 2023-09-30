#include <stdio.h>

int main(){
    
    int a,b,c;

    printf("Variabel a bernilai:");
    scanf("%d", &a);

    printf("Variabel b bernilai:");
    scanf("%d", &b);

    printf("Variabel c bernilai:");
    scanf("%d", &c);

    int asamadenganb = a == b;
    int blebihbesardaric = b > c;
    int atidaksamadenganc = a != c;

    printf("apakah a sama dengan b ? jawabannya adalah %d\n", asamadenganb);
    printf("apakah b lebih besar dari c ? jawabannya adalah %d\n", blebihbesardaric);
    printf("apakah a tidak sama dengan c ? jawabannya adalah %d\n", atidaksamadenganc);

    return 0;
}