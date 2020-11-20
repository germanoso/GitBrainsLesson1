# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = input('Введите число от 1 до 9:')
one_number = int(user_number)
double_number = int(user_number*2)
triple_number = int(user_number*3)
sum_number = one_number + double_number + triple_number
print('{} + {} + {} = {}'.format(one_number, double_number, triple_number, sum_number))