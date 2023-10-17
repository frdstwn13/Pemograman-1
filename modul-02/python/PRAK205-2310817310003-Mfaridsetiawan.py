import math

a = input().split()

if len(a) == 1:
     a = int(a[0])
     b = int(input())
elif len(a) == 2:
     a, b = map(int,a)

alas = int(math.sqrt(b**2 - a**2))
tinggi = a
keliling = a + b + alas
luas = 0.5 * alas * tinggi

print(f"Alas = {alas} cm")
print(f"Tinggi = {tinggi} cm")
print(f"Keliling = {keliling} cm")
print(f"Luas = {luas:.0f} cm^2")