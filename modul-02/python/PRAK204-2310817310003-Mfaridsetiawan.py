nilai = input().split()
if len(nilai) == 1:
    r = float(nilai[0])
    t = float(input())
elif len(nilai) == 2:
    r,t = map(float, nilai)

phi = 3.142857

volume = phi * r ** 2 * t
luas = 2 * phi * r * (r + t)
keliling = 2 * phi * r

print(f"Alas = {volume:.2f}")
print(f"Tinggi = {luas:.2f}")
print(f"Keliling = {keliling:.2f}")