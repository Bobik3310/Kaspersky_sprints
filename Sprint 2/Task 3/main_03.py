import re
with open('Code.txt', 'r') as f:
    func = f.read()
if func == '':
    print('Закиньте вашу функцию в Code.txt')
vars = []
lists = []
vars.append(re.findall(r'[\w][\w\d]+(?=\s*[\,\)])', func[:func.index(':')]))  # аргументы на вход
vars.append(re.findall(r'[\w][\w\d]+(?=\s*\=)', func))  # создаваемые переменные
lists.append(re.findall(r'[\w][\w\d]+(?=\s*\=\[)', func))  # создаваемые списки
count_var = 1
count_list = 1
for i in vars:
    for var in i:
        if var not in str(lists):
            func = str(func).replace(str(var), 'a' + str(count_var))
            count_var += 1
        else:
            func = str(func).replace(str(var), 'R' + str(count_list))
            count_list += 1
print(func)