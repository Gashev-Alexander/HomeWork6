line = input('Введите случайное колличество О и Р: ')
result = []
while True:
    if 'о' in line:
        start = line.index('о')
    else:
        break
    if 'р' in line[start:]:
        end = line.index('р', start)
        result.append(line[start:end])
    else:
        result.append(line[start:])
        break
    line = line[end + 1:]

print(len(max(result)))