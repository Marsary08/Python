duration = int(input('Введите время в секундах: '))

print(f"{duration // 86400} дн {duration // 3600 % 24} ч {duration // 60 % 60} мин {duration % 60} сек")
