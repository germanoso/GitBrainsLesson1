# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

str_user = input('Введите целое число: ')
print('Сейчас оно имеет: ', type(str_user), str_user)

# Приводим строку к типу INT
int_user = int(str_user)
print('Приведем к ', type(int_user), 'и его можно возвести, например, в квадрат: ', int_user**2)

# Приводим строку к типу FLOAT
float_user = float(str_user)
print('Теперь это ', type(float_user), float_user)

# Получаем строку 0/1 и переводим к типу BOOL
like_user = input('Вам пока нравится? Ответьте Да - 1, Нет - 0: ')
print('Сейчас это значение имеет ', type(like_user), like_user)
bool_user = bool(int(like_user))
print('А теперь преобразован к ', type(bool_user), bool_user)

# Из всех значений создаем список
list_user = [str_user, int_user, float_user, bool_user]
print('Создаем список: ', type(list_user), list_user)

# Из всех значений создаем словарь
dic_user = {'String': str_user,
            'Integer': int_user,
            'Float': float_user,
            'Bool': bool_user}
print('А теперь это словарь ', type(dic_user))
print(dic_user)
