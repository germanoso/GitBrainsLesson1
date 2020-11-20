# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс.
# Используйте форматирование строк.

import datetime
total = int(input('Введите секунды: '))

# Решение задачи через вызов библиотеки
print(total, 'секунд:', datetime.timedelta(0, total))

# Второй вариант решения
seconds = total % 60
total = total - seconds
hours = total // 3600
total = total - (hours * 3600)
mins = int(total / 60)
print('Время: {} часов, {} минут и {} секунд'.format(hours, mins, seconds))