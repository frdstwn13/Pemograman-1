banyak_baris = 2
banyak_angka_baris, banyak_angka_baris1 = map(int, input().split())
if banyak_angka_baris == banyak_angka_baris1:
    wadah_array = []
    for i in range(banyak_baris):
        wadah_array.append(list(map(int, input().split())))
    for i in range(banyak_baris - 1):
        for j in range(banyak_angka_baris):
            if i + 1 < banyak_baris:
                wadah_array[i][j] = wadah_array[i][j] * wadah_array[i + 1][j]
    for i in range(banyak_baris - 1):
        for j in range(banyak_angka_baris):
            print(wadah_array[i][j], end=" ")
else:
    print("Jumlah Tidak Sama!")