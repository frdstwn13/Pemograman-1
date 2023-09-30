import math

alas = int(input("Masukkan Alas: "))
tinggi = int(input("Maukkan Tinggi:"))

sisiA = tinggi
sisiB = int(math.sqrt(alas**2 + tinggi**2))
sisiC = alas

keliling = sisiA + sisiB + sisiC
luas = int(0.5 * alas * tinggi)

print("Diketahui :")
print(f"Alas = {alas} cm")
print(f"Tinggi = {tinggi} cm")

print("Jawab :")
print(f"Sisi A = {sisiA}  cm")
print(f"Sisi b = {sisiB}  cm")
print(f"Sisi c = {sisiC}  cm")
print(f"Keliling = {keliling} cm")
print(f"luas = {luas} cm")