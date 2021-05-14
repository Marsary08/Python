percent = int(input('Введите число от 1 до 20: '))

if percent == 1 or percent == 21:
    print(percent, 'процент')
elif percent >= 2 and percent <= 4:
    print(percent, 'процента')
else:
    print(percent, 'процентов')
