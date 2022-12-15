line = input('Введите случайное колличество О и Р: ')
print(max(filter(lambda x:'о' not in x, line.split('о'))))