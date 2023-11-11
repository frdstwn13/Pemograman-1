Min = 1
Max = int(input(""))

for a in range(Min , Max +1):
  if a % 2 == 0:
   print('' , end='')
  else :
    print(a,'', end='')

print('')

for a in range(Max,Min, -1):
  if a % 2 == 0:
    print(a,'', end='')