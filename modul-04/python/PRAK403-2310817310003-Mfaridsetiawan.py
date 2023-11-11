nilai1, nilai2 = map(int, input().split())
nilai_batas = nilai1 - nilai2

if nilai_batas < 0:
    nilai_batas = abs(nilai_batas)
    for i in range(nilai_batas + 1):
        a = 1

        print(f"{nilai1}-{nilai2} ", end="")

        nilai1 += a
        nilai2 -= a
else:
    for i in range(nilai_batas + 1):
        a = 1

        print(f"{nilai1} {nilai2}  ", end="")

        nilai1 -= a
        nilai2 += a