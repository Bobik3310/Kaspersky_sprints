import parsing
with open('shifr.txt', 'rt') as f1, open('words.txt', 'rt') as f2:
    shifr = f1.read()
    words = f2.read()
alph_small = [chr(i) for i in range(ord('a'), ord('z') + 1)]
alph_big = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
text = ''
shifr_list = []
shifr_ind = []
keys = []
n = 0
for ind, i in enumerate(shifr, start=0):
    if i == '.':
        n = ind
    else:
        pass
    if i == '?':
        shifr_ind.append(n)
for i in range(1, len(shifr_ind)):
    shifr_list.append(shifr[shifr_ind[i - 1]:shifr_ind[i]])
    if i == len(shifr_ind) - 1:
        shifr_list.append(shifr[shifr_ind[-1]:])


def ces(list):
    for z in range(1, 27):
        vocab = [''] * len(list)
        for num, i in enumerate(list, start=0):
            for letter in i:
                if letter in alph_small:
                    vocab[num] += alph_small[(alph_small.index(letter) - z) % len(alph_small)]
                if letter in alph_big:
                    vocab[num] += alph_big[(alph_big.index(letter) - z) % len(alph_big)]
        n = 0
        for i in vocab:
            if i.lower() in words:
                n += 1
        if n >= len(list) // 2 + 1:
            return [''.join(vocab), z]
            break


text = ''
new_text = ''
for i in shifr_list[:]:
    i = i.split()
    text += ces(i)[0]
    keys.append(ces(i)[1])
n = 0
for i in shifr:
    if alph_big.count(i) == 1 or alph_small.count(i) == 1:
        new_text += text[n]
        n += 1
    else:
        new_text += i
with open('text.txt', 'w') as f:
    f.write(new_text)
with open('keys.txt', 'w') as f:
    f.write('keys = ' + '{%s}' % (str(keys).strip('[').strip(']')))