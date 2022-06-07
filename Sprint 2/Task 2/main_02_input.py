with open(f'{input("Путь к файлу:")}', 'rb') as f:
    text = f.read(2)
print(text)
if symbols == 'MZ':
    print(f'{symbols} - executable, OS Windows')
else:
    print(f'{symbols} - non-executable')