while True:
    print("Pilih program\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Exit")
    pilihan = float(input("Masukkan Pilihan: "))

    if pilihan == 1 or pilihan == 2 or pilihan == 3 or pilihan == 4:
        nilai_pertama = float(input("Masukkan Nilai Pertama: "))
        nilai_kedua = float(input("Masukkan Nilai Kedua: "))

        if pilihan == 1:
            hasil = nilai_pertama + nilai_kedua
            print(f"Hasil penjumlahan antara {nilai_pertama:.2f} dengan {nilai_kedua:.2f} adalah {hasil:.2f}\n")
        elif pilihan == 2:
            hasil = nilai_pertama - nilai_kedua
            print(f"Hasil pengurangan antara {nilai_pertama:.2f} dengan {nilai_kedua:.2f} adalah {hasil:.2f}\n")
        elif pilihan == 3:
            hasil = nilai_pertama * nilai_kedua
            print(f"Hasil perkalian antara {nilai_pertama:.2f} dengan {nilai_kedua:.2f} adalah {hasil:.2f}\n")
        elif pilihan == 4:
            hasil = nilai_pertama / nilai_kedua
            print(f"Hasil pembagian antara {nilai_pertama:.2f} dengan {nilai_kedua:.2f} adalah {hasil:.2f}\n")
    elif pilihan == 5:
        print("Terimakasih, telah menggunakan kalkulator M.Farid Setiawan")
        break
    else:
        print("Input Anda salah, silahkan coba lagi\n\n")