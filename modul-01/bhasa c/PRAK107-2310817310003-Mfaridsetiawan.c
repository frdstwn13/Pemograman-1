#include <stdio.h>

int main(){

    int x , y , z;

   printf("inputkan nilai sisi segitiga x:");
   scanf("%d", &x);

   printf("inputkan nilai sisi segitiga y:");
   scanf("%d", &y);

   printf("inputkan nilai sisi segitiga z:");
   scanf("%d", &z);

   int hargatanahpermeter = 85000;
   int hasil = x + y + z;
   int hasilkeseluruhan = hasil * hargatanahpermeter;

   printf("Diketahui: \n ");
   printf("Panjang sisi segitiga berturut-turut adalah %d, %d, %d\n", x, y, z);
   printf("Keliling Tanah Pak Dengklek adalah %d\n", hasil);
   printf("Harga tanah per meter adalah %d\n",hargatanahpermeter);
   printf("Jawaban : \n");
   printf("Biaya yang diperlukan Pak Dengklek adalah : Rp %d\n",hasilkeseluruhan);

   return 0;
}