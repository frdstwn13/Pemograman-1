HargasepatuA = int(input("Harga Sepatu A adalah: "))
HargasepatuB = int(input("Harga Sepatu B adalah: "))

HargasepatuA_diskon = 0.13
HargasepatuB_diskon = 0.21

print(f"Sepatu A mendapat diskon 13%% sehingga harga menjadi {HargasepatuA - (HargasepatuA * HargasepatuA_diskon):.0f}")
print(f"Sepatu B mendapat diskon 21%% sehingga harga menjadi {HargasepatuB - (HargasepatuB * HargasepatuB_diskon):.0f}")

