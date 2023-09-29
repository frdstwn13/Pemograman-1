#include <stdio.h>
#include <math.h>

int main(){
 printf("Diketahui : \n");
 int alas , tinggi , sisia, sisib, sisic;
 printf(" Alas = ");
 scanf("%d", &alas);

 printf(" tinggi = ");
 scanf("%d", &tinggi);

 sisia = tinggi;
 sisib = sqrt(pow(alas, 2) + pow(tinggi, 2));
 sisic = alas;

 int keliling = sisia + sisib + sisic;
 int luas = 0.5 * alas * tinggi;

 printf("Sisi A = %d cm \n",sisia);
 printf("Sisi B = %d cm \n",sisib);
 printf("Sisi C = %d cm \n",sisic);
 printf("keliling = %d cm \n",keliling);
 printf("luas = %d cm \n", luas);

 return 0;
    
}