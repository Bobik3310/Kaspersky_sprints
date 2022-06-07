with open(f'{input("Путь к файлу:")}', 'rb') as f:
    symbols = f.read(2)
if hex(symbols[0] * 2 ** 8 + symbols[1])[2:] == '4d5a':
    print(f'{hex(symbols[0] * 2 ** 8 + symbols[1])[2:]} {symbols.decode("utf-8")} - executable, OS Windows')
else:
    print(f'{hex(symbols[0] * 2 ** 8 + symbols[1])[2:]} {symbols.decode("utf-8")}- non-executable')
