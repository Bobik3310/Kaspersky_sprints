hours, malware = map(int, input().split())


def replace(words_replace, words_values):
    for i, j in words_values.items():
        words_replace = words_replace.replace(i, j)
    return words_replace


words = 'small0'
for i in range(hours):
    values = {f'big{i}': ' '.join([f'big{i + 1}'] + [f'small{i + 1}'] * malware), f'small{i}': f'big{i + 1}'}
    words = replace(words, values)
print(words.count(' ') + 1)
