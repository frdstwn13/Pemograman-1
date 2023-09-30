#include <stdio.h>

int main(){

    int a , b , c;

   printf("nilai sisi segitiga a:");
   scanf("%d", &a);

   printf("nilai sisi segitiga b:");
   scanf("%d", &b);

   printf("nilai sisi segitiga c:");
   scanf("%d", &c);

   int hargatanahpermeter = 85000;
   int hasil = a + b + c;
   int hasilkeseluruhan = hasil * hargatanahpermeter;

   printf("Diketahui: \n ");
   printf("Panjang sisi segitiga berturut-turut adalah %d, %d, %d\n", a, b, c);
   printf("Keliling Tanah Pak Dengklek adalah %d\n", hasil);
   printf("Harga tanah per meter adalah %d\n",hargatanahpermeter);
   printf("Jawaban : \n");
   printf("Biaya yang diperlukan Pak Dengklek adalah : Rp %d\n",hasilkeseluruhan);

   return 0;
}