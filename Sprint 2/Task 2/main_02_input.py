with open(f'{input("Путь к файлу формата .exe:")}', 'rb') as f:
    symbols = f.read(2).decode('utf-8')
if symbols == 'MZ':
    print('executable, OS Windows')
else:
    print('non-executable')
