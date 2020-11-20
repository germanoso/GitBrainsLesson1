# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


gain_comp = float(input('Введите сумму выручки вашей компании: '))
expenses_comp = float(input('Введите сумму издержек вашей компании: '))

if gain_comp > expenses_comp:                                   # Проверяем условие, работает ли в прибыль
    earn_comp = gain_comp - expenses_comp
    print('Ваша компания работает в прибыль с профицитом ', earn_comp)
    rent_comp = ((earn_comp / gain_comp)*100.00)
    print('Рентабельность = {:.2f} %'.format(rent_comp))
    workers = int(input('Сколько сотрудников у вас работает? '))
    print('Прибыль фирмы в расчете на одного сотрудника составляет: {:.2f}'.format(earn_comp / workers))
elif gain_comp < expenses_comp:                                  # Проверяем условие, работает ли в убыток
    deficit_comp = expenses_comp - gain_comp
    print('Ваша компания работает в убыток с дефицитом ', deficit_comp)
else:
    print('Ваша компания работает в ноль')
