with open(f'{input("Путь к файлу:")}', 'rb') as f:
    symbols = f.read(2).decode('utf-8')
if symbols == 'MZ':
    print(f'{symbols} - executable, OS Windows')
else:
    print(f'{symbols} - non-executable')