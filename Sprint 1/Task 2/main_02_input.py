shifr = list(map(int, input().split('|')))
alph = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for count, i in enumerate(shifr, start=0):
    shifr[count] = alph[i - 1]
print(''.join(shifr))