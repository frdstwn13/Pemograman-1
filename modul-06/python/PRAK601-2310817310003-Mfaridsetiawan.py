baris, kolom = map(int, input().split())

matriks = [[0] * kolom for _ in range(baris)]

user = list(map(int, input().split()))
matrix = 0
for i in range(baris):
    for j in range(kolom):
        matriks[i][j] = user[matrix]
        matrix += 1


print()
for i in range(baris):
    for j in range(kolom):
        print(matriks[i][j], end=" ")
    print()