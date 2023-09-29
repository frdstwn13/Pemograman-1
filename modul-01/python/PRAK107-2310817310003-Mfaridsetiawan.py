a = int(input("nilai a:"))
b = int(input("nilai b:"))
c = int(input("nilai c:"))

hargaTanahpermeter = 85000
hasil = a + b + c
hasilkeseluruhan = hasil * hargaTanahpermeter

print(f"Diketahui :")
print(f"Panjang sisi segitiga berturut-turut adalah {a}, {b}, dan {c}")
print(f"Keliling Tanah Pak Dengklek adalah {hasil}")
print(f"Harga tanah per meter adalah {hargaTanahpermeter}")
print(f"Jawaban :")
print(f"Biaya yang diperlukan Pak Dengklek adalah: Rp {hasilkeseluruhan}")