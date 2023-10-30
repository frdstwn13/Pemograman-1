nilai = int(input(' '))
 
hasil = None
if nilai > 1:
    hasil = 'positif'
elif nilai < 0:
    hasil = 'negatif'
elif nilai == 0:
    hasil = 'nol'
 
print(' {} '.format( hasil))