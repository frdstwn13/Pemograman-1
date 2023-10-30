hari = 0
jam = 0
menit = 0
detik = 0

variabel = int(input())

if variabel >= 86400:
    hari = variabel // 86400
    variabel %= 86400

if variabel >= 3600:
    jam = variabel // 3600
    variabel %= 3600

if variabel >= 60:
    menit = variabel // 60
    variabel %= 60

detik = variabel

if hari > 0:
    print(f"{hari} hari:{jam:02d}:{menit:02d}:{detik:02d}")
else:
    print(f"{jam:02d}:{menit:02d}:{detik:02d}")