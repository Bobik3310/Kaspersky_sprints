alph = 'qwertyuiopasdfghjklzxcvbnm_{}1234567890'
text = list('yourflagis{fhke37_kdrjknbmpr_04374j}')
gamma = 'thekey'
print(*[alph[(alph.index(i) + alph.index(gamma[count % len(gamma)]) + 2) % len(alph)] for count, i in enumerate(text, start=0)], sep='')