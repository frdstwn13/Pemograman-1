input_str = input()
a, simbol = input_str.split()
a = int(a)

for b in range(1, 51):
    if b % a == 0:
        print(simbol, end=' ')
    else:
        print(b, end=' ')