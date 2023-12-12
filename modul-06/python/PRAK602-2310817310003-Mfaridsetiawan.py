def hitung(ruangan, jumlah_zetsu):
   for i in range(ruangan):
      print(jumlah_zetsu[i] * (i + 1), end=" ")

ruangan = int(input())

jumlah_zetsu = [int(j) for j in input().split()]

print()
hitung(ruangan, jumlah_zetsu)