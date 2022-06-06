alph = 'qwertyuiopasdfghjklzxcvbnm_{}1234567890'
text = list('yourflagis{fhke37_kdrjknbmpr_04374j}')
gamma = 'thekey'
for count, i in enumerate(text, start=0):
    text[count] = alph[(alph.index(i) + alph.index(gamma[count % len(gamma)]) + 2) % len(alph)]
print(*text, sep='')