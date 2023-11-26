def Biodata(tahunlahir, Namaku, Asal):
    tahun_sekarang = 2023
    Umur = tahun_sekarang - tahunlahir

    print("Perkenalkan Nama Saya :", Namaku)
    print("Umur saya             :", Umur)
    print("Saya Adalah Angkatan  :", tahun_sekarang)
    print("Asal Saya dari        :", Asal)

tahunLahir = int(input())
Namaku = input()
Asal = input()

Biodata(tahunLahir, Namaku, Asal)