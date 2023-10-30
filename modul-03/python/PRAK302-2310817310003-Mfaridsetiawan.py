nilai = int(input(' '))
 
hasil = None
if nilai > 80:
    hasil = 'A'
elif nilai <= 79 and nilai > 70:
    hasil = 'B'
elif nilai <= 69 and nilai > 60:
    hasil = 'C'
elif nilai <= 59 and nilai >= 50:
    hasil = 'D'
elif nilai < 50:
    hasil = 'E'


 
print(' {} =  {}'.format(nilai, hasil))